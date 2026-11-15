#!/usr/bin/env python3
"""Sponsorship routing for retention/promotion PRs.

Two triggers:
- subsystems.yml membership diff: a handle newly placed under a subsystem
  pings its assignees (initial placement).
- argument/<member>/ files: route the PR to the assignees of the subsystems
  the argument declares for the period (the template's
  "developed/maintained" field), intersected with the member's placements.
  Declared-but-not-placed subsystems get flagged in the comment. If the field
  is absent or matches nothing, fall back to pinging every placement. The
  `aliases` map covers directories that differ from the member's handle. A
  member missing from subsystems.yml gets told to add themselves, which then
  pings via the first trigger.

One marker-tagged comment per PR, updated as the diff changes.
"""
import os
import subprocess
import sys
import urllib.request

import yaml

MARKER = "<!-- sponsor-ping -->"


def load_subsystems(text):
    """(subsystem name -> (assignees, all member handles), dir -> handle aliases)"""
    doc = yaml.safe_load(text)
    out = {}
    for s in (doc or {}).get("subsystems", []):
        assignees = list(s.get("assignees") or [])
        delegates = s.get("delegates") or {}
        members = set(assignees)
        for rank in ("rank2", "rank1"):
            members |= set(delegates.get(rank) or [])
        out[s["name"]] = (assignees, members)
    aliases = {}
    for handle, dirs in (doc or {}).get("aliases", {}).items():
        for d in dirs:
            aliases[d] = handle
    return out, aliases


def api(method, path, token, payload=None):
    import json

    req = urllib.request.Request(
        f"https://api.github.com{path}",
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
    )
    if payload is not None:
        req.data = json.dumps(payload).encode()
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def declared_subsystems(text):
    """Names from the template's 'developed/maintained:' field; [] if absent.

    Names are separated by ';' because commas appear inside names themselves
    ("Runtimes (FRAME, APIs, integrations)").
    """
    for line in text.splitlines():
        if "developed/maintained:" in line:
            _, _, rest = line.partition("developed/maintained:")
            return [s.strip() for s in rest.split(";") if s.strip()]
    return []


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    pr = os.environ["PR_NUMBER"]
    base_ref = os.environ["BASE_REF"]
    token = os.environ["GITHUB_TOKEN"]

    # Under pull_request_target the checkout is the base repo; the PR head is
    # fetched (not checked out) so its content is only ever read as data.
    fetch = git("fetch", "origin", f"pull/{pr}/head")
    if fetch.returncode != 0:
        raise SystemExit(f"cannot fetch PR head: {fetch.stderr.strip()}")
    head_yaml = git("show", "FETCH_HEAD:subsystems.yml")
    if head_yaml.returncode != 0:
        # Stale fork without the file: an argument-only PR still routes by
        # the base version.
        head_yaml = git("show", f"origin/{base_ref}:subsystems.yml")
    if head_yaml.returncode != 0:
        raise SystemExit("subsystems.yml missing on both sides")
    head, head_aliases = load_subsystems(head_yaml.stdout)

    asks = []
    announced = set()

    # Trigger 1: membership diff in subsystems.yml. The file being new in the
    # PR means there is no base to diff and nobody to ping yet.
    base = git("show", f"origin/{base_ref}:subsystems.yml")
    if base.returncode == 0:
        base, _ = load_subsystems(base.stdout)
        for name, (assignees, members) in head.items():
            added = members - base.get(name, ([], set()))[1]
            if not added:
                continue
            pings = " ".join(f"@{a}" for a in assignees) if assignees else "Fellows"
            joined = ", ".join(f"`{h}`" for h in sorted(added))
            asks.append(
                f"- {joined} placed under **{name}**: {pings}, your review here marks sponsorship."
            )
            announced |= {(h, name) for h in added}

    # Trigger 2: argument files route by directory name, narrowed to the
    # subsystems the argument declares for the period. New files only, so
    # editing an old argument does not re-route.
    changed = git("diff", "--name-only", "--diff-filter=A", f"origin/{base_ref}...FETCH_HEAD")
    arg_files = [
        p
        for p in changed.stdout.splitlines()
        if p.startswith("argument/") and len(p.split("/")) > 2
    ]
    canonical = {name.lower(): name for name in head}
    for member in sorted({p.split("/")[1] for p in arg_files}):
        member = head_aliases.get(member, member)
        placed = [name for name, (_, m) in head.items() if member in m]
        declared = set()
        for p in arg_files:
            if head_aliases.get(p.split("/")[1], p.split("/")[1]) != member:
                continue
            content = git("show", f"FETCH_HEAD:{p}")
            if content.returncode != 0:
                continue
            for raw in declared_subsystems(content.stdout):
                if raw.lower() in canonical:
                    declared.add(canonical[raw.lower()])
                else:
                    asks.append(
                        f"- `{member}` declares work in \"{raw}\", which matches no "
                        "subsystem in subsystems.yml. Fix the name or the YAML."
                    )
        not_placed = declared - set(placed)
        for name in sorted(not_placed):
            asks.append(
                f"- `{member}` declares work in **{name}** but is not placed under it "
                "in subsystems.yml. Add the placement or correct the argument."
            )
        subs = sorted(declared & set(placed)) or placed
        if not subs:
            asks.append(
                f"- `{member}` files an argument but is not in subsystems.yml. "
                "Add your handle under your subsystem in this PR so review routes to the assignees."
            )
            continue
        for name in subs:
            if (member, name) in announced:
                continue
            assignees = [a for a in head[name][0] if a != member]
            pings = " ".join(f"@{a}" for a in assignees) if assignees else "Fellows"
            asks.append(
                f"- `{member}` under **{name}**: {pings}, your review here marks sponsorship."
            )

    if not asks:
        print("nothing to route")
        return

    body = (
        f"{MARKER}\n**Subsystem sponsorship**\n\n"
        + "\n".join(asks)
        + "\n\nAssignees, please review; your approval on this PR marks sponsorship "
        "per the retention and salary requirements."
    )

    comments = api("GET", f"/repos/{repo}/issues/{pr}/comments?per_page=100", token)
    existing = next((c for c in comments if c["body"].startswith(MARKER)), None)
    if existing:
        if existing["body"] == body:
            print("comment already up to date")
            return
        api("PATCH", f"/repos/{repo}/issues/comments/{existing['id']}", token, {"body": body})
        print("updated sponsorship comment")
    else:
        api("POST", f"/repos/{repo}/issues/{pr}/comments", token, {"body": body})
        print("posted sponsorship comment")


if __name__ == "__main__":
    sys.exit(main())
