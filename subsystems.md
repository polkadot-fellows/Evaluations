# Subsystems

The subsystem list is machine-readable: **[subsystems.yml](subsystems.yml)**
is the source of truth, with assignees (Rank 3+) and delegates (Rank 2 and
Rank 1, listed separately) as GitHub handles so tooling can route reviews.

Members filing a retention or promotion argument add their handle under their
subsystem in the YAML, one entry per subsystem they work in. CI pings each
placement's assignees, whose approval on the PR marks sponsorship. Follow-up
arguments are plain markdown and need no YAML change: CI routes them by the
`argument/<handle>/` directory, narrowed to the subsystems the argument
declares for the period in its "developed/maintained" field (separate several
with ";"). Directories that differ from the member's handle are covered by
the `aliases` map.

Subsystems are created, renamed or removed through the regular PR process.
