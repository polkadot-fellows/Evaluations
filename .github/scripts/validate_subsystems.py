#!/usr/bin/env python3
"""Validate subsystems.yml: schema, unique names, GitHub handle shape.

A subsystem needs at least one assignee/delegate, or a `note` saying who
covers it for now (e.g. the JAM Prize rows).
"""
import re
import sys

import yaml

HANDLE = re.compile(r"^[A-Za-z0-9](?:-?[A-Za-z0-9]){0,38}$")
DIRNAME = re.compile(r"^[A-Za-z0-9._-]+$")
KNOWN_KEYS = {"name", "assignees", "delegates", "note"}


def fail(msg):
    print(f"subsystems.yml: {msg}", file=sys.stderr)
    sys.exit(1)


def main(path):
    with open(path) as f:
        doc = yaml.safe_load(f)
    if not isinstance(doc, dict) or not isinstance(doc.get("subsystems"), list):
        fail("top level must be a mapping with a 'subsystems' list")

    aliases = doc.get("aliases") or {}
    if not isinstance(aliases, dict):
        fail("'aliases' must be a mapping of handle -> [directory names]")
    for handle, dirs in aliases.items():
        if not isinstance(handle, str) or not HANDLE.match(handle):
            fail(f"aliases: {handle!r} is not a valid GitHub handle")
        if not isinstance(dirs, list) or not dirs:
            fail(f"aliases: {handle!r} needs a non-empty list of directory names")
        for d in dirs:
            if not isinstance(d, str) or not DIRNAME.match(d):
                fail(f"aliases: {d!r} is not a valid directory name")

    seen = set()
    for i, s in enumerate(doc["subsystems"]):
        where = f"entry {i + 1}"
        if not isinstance(s, dict):
            fail(f"{where} is not a mapping")
        unknown = set(s) - KNOWN_KEYS
        if unknown:
            fail(f"{where} ({s.get('name', '?')}): unknown keys {sorted(unknown)}")

        name = s.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(f"{where}: missing 'name'")
        if name in seen:
            fail(f"duplicate subsystem name {name!r}")
        seen.add(name)
        where = repr(name)

        assignees = s.get("assignees")
        if not isinstance(assignees, list):
            fail(f"{where}: 'assignees' must be a list (use [] when empty)")
        for handle in assignees:
            if not isinstance(handle, str) or not HANDLE.match(handle):
                fail(f"{where}: {handle!r} is not a valid GitHub handle")

        delegates = s.get("delegates")
        if not isinstance(delegates, dict) or set(delegates) != {"rank1", "rank2"}:
            fail(f"{where}: 'delegates' must be a mapping with rank1 and rank2 lists")
        member_handles = list(assignees)
        for rank in ("rank2", "rank1"):
            value = delegates[rank]
            if not isinstance(value, list):
                fail(f"{where}: delegates.{rank} must be a list (use [] when empty)")
            for handle in value:
                if not isinstance(handle, str) or not HANDLE.match(handle):
                    fail(f"{where}: {handle!r} is not a valid GitHub handle")
            member_handles += value
        if len(member_handles) != len(set(member_handles)):
            dupes = sorted({h for h in member_handles if member_handles.count(h) > 1})
            fail(f"{where}: {dupes} listed more than once")
        if not member_handles and not s.get("note"):
            fail(f"{where}: no assignees, delegates or note")

    print(f"ok: {len(seen)} subsystems")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "subsystems.yml")
