# Argument-0010: Retention at Rank 2

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2026/10/08) |
| **Submitted by**| Christian Langenbacher          |
| **Sponsored by**| N/A (inactive, not claiming a salary)            |


## Member details

- Matrix username: `@clang:matrix.org`
- Polkadot address: `16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3`
- Current rank: `2`
- Date of initial induction: `2024/03/27`
- Date of last report: `2026/06/25`
- Link to last report: [0009 Retention at Rank II](https://collectives.subsquare.io/fellowship/members/16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3/evidences/9187922-3)
- [Subsystems](../../subsystems.md) developed/maintained: `Runtimes (Engineering, Security, Benchmarking)` (primary), `Runtimes (FRAME, APIs, integrations)`


## Reporting period

- Start date: 2026/06/25
- End date: 2026/10/08


## Argument

Up until now, I have been an active Member. However, with the new
[accountability](../../README.md#accountability) requirements, I am unsure in this moment of transition
how sponsorship and the restrictions on other full-time employment apply to me. Hence, I have set myself to
inactive and will not draw a salary for the time being, which is why this report does not name a sponsor.
Nevertheless, it is my interest to stay active in the ecosystem, and I will revisit my status once the
requirements are settled.

My argument primarily revolves around PRs and issues that I filed in the Polkadot SDK and
Runtimes repositories.

My work falls primarily into the Runtimes (Engineering, Security) subsystem: the safety of runtime
upgrades, state hygiene on the relay chains, and keeping the Runtimes repository and its integration tests
maintainable. The multi-block migration work also extends upstream into FRAME.

### A safety net for stuck multi-block migrations

As part of the TODO cleanup from my last report, I switched the Polkadot Hub runtimes to the upstream
`ForceUnstuckOnFailedMigration` ([runtimes#1217](https://github.com/polkadot-fellows/runtimes/pull/1217)).
During the review, ggwpez [pointed out](https://github.com/polkadot-fellows/runtimes/pull/1217#pullrequestreview-4592477489)
that the `max_blocks` of the aggregated MBM is just the sum of the individual migrations' limits. If a single
migration does not set one, there is no fallback, and a buggy migration that does not make progress would
keep the chain stuck indefinitely.

I took up the suggested follow-up and [capped](https://github.com/polkadot-fellows/runtimes/pull/1238)
individual MBMs to one day in the runtimes. After hitting the cap, the migration is considered failed, and
the `FailedMigrationHandler` is triggered. As this is useful for every chain using the migrations pallet, I
also drafted the [upstream version](https://github.com/paritytech/polkadot-sdk/pull/12841), which
integrates a configurable cap directly into `pallet-migrations`. Following bkchr's proposal, we closed the
runtimes PR in favour of the upstream one: the issue is rather unlikely to happen, and we have been rolling
without the cap for quite a while already.

Exceeding the limit only helps if the failure handler leaves the chain recoverable. Hence, the upstream PR
also switches the default from `FreezeChainOnFailedMigration` to `ForceUnstuckOnFailedMigration`.
`EnterSafeModeOnFailedMigration` would be the better middle ground, but while looking into it I noticed
that it returns `KeepStuck` even after successfully entering safe mode, which would block any manual
intervention. I have [raised this](https://github.com/paritytech/polkadot-sdk/issues/12921) as a
separate question upstream and deferred that change until it is clarified.

### Removing stale downward message queues

Before [polkadot-sdk#6604](https://github.com/paritytech/polkadot-sdk/pull/6604), DMP queued messages
for paras without a head. The leftover queues have been waiting for a cleanup on Polkadot and Kusama since
[December 2024](https://github.com/polkadot-fellows/runtimes/issues/513).

I diagnosed the affected para IDs on both relay chains with a
[script](https://github.com/encointer/runtimes/blob/20a803f067e9d5f3fa80b42b2a8bcad64aa476f0/stale-dmp-queues.py)
(8 paras per relay) and [wrote a migration](https://github.com/polkadot-fellows/runtimes/pull/1302)
that removes their queues and queue heads. I chose to target those paras explicitly instead of iterating
through all storage keys, as the bug has been fixed upstream and no new stale queues should appear. Some of
these paras could have been re-registered by the time of the upgrade, so the migration skips any para
that has a head by then. The PR is still pending review.

### Continuing to reduce the Runtimes TODO backlog

In my last report I described the [triage](https://github.com/polkadot-fellows/runtimes/issues/696#issuecomment-4787936619)
of all `TODO`/`FIXME` markers in the Runtimes repository. The PRs I mentioned there as pending have all been
merged in this period ([#1213](https://github.com/polkadot-fellows/runtimes/pull/1213),
[#1214](https://github.com/polkadot-fellows/runtimes/pull/1214),
[#1216](https://github.com/polkadot-fellows/runtimes/pull/1216),
[#1217](https://github.com/polkadot-fellows/runtimes/pull/1217)), and I continued the work with
a few more:

- [#1293](https://github.com/polkadot-fellows/runtimes/pull/1293) (merged): Bridge Hub Polkadot now uses
  the upstream `ethereum_extrinsic` test, removing the local copy and the now-unused fixtures dev-dependency.
- [#1300](https://github.com/polkadot-fellows/runtimes/pull/1300) (merged), [#1294](https://github.com/polkadot-fellows/runtimes/pull/1294):
  dropping TODOs that had silently been resolved long ago.
- [#1295](https://github.com/polkadot-fellows/runtimes/pull/1295): replacing the archived
  `actions/create-release` and `actions/upload-release-asset` actions in the release workflow, keeping
  the published asset names unchanged.

I posted a [status update](https://github.com/polkadot-fellows/runtimes/issues/696#issuecomment-5701815620)
on the tracking issue: of the 27 actionable TODOs from the original triage, 13 are gone from `main` and 4 more
are addressed by open PRs. In the meantime, 7 new ones appeared, so 17 remain open. These are
categorized into those that can be removed with the next SDK bump and those that still need an issue or work.
I also used the occasion to close out stale issues whose work had already been done
([#382](https://github.com/polkadot-fellows/runtimes/issues/382#issuecomment-5702998892),
[#1061](https://github.com/polkadot-fellows/runtimes/issues/1061#issuecomment-5703247349)).

### Consolidating the emulated integration test helpers

The Runtimes repository's `integration-tests-helpers` crate had become a re-export facade of the
upstream `emulated-integration-tests-common` crate: the macros it existed for had been backported, but
the `pub use emulated_integration_tests_common::*` was kept for compatibility. This resulted in a mixed
import pattern, where test crates imported the same items from both places.

I [removed the facade](https://github.com/polkadot-fellows/runtimes/pull/1299) so that almost all
crates now depend only on the upstream version, re-exported the Snowbridge helpers instead of redefining
them, and replaced the remaining test macro with a generic test function for better type checks, mirroring
the more recent pattern in the codebase. This touches 47 files and closes a
[TODO open since June 2024](https://github.com/polkadot-fellows/runtimes/issues/363). Along the way, I
noticed that `.gitignore`'s `**/chains/` pattern also matches `integration-tests/emulated/chains/`, so files
added to the emulated chain crates were silently untracked. The PR is still pending review.

### Additional contributions

I upstreamed a minor convenience change to derive `Debug`, `Clone`, `PartialEq` and `Eq` for
`EraPayoutParams` ([polkadot-sdk#12449](https://github.com/paritytech/polkadot-sdk/pull/12449)), which I
noticed was missing during the cleanup in the runtimes repository.

I remained involved in
[3 Polkadot SDK issues](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue%20involves%3Aclangenb%20updated%3A2026-06-25..2026-10-08)
and [3 Runtimes issues](https://github.com/polkadot-fellows/runtimes/issues?q=is%3Aissue%20involves%3Aclangenb%20updated%3A2026-06-25..2026-10-08)
over the period, and continued to assist community members with technical questions in the
Fellowship and ecosystem Element channels.

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|------|----------------------|----------------------|----------------------------|----------|
| I    | 90%                  | N/A                  |                            |          |
| II   | 80%                  | N/A                  | No eligible referenda      |          |
| III  | 70%                  | 100%                 |                            |          |
| IV   | 60%                  | 90%                  |                            |          |
| V    | 50%                  | 80%                  |                            |          |
| VI   | 40%                  | 70%                  |                            |          |


## Misc

- [ ] Question(s):
- [ ] Concern(s):
- [ ] Comment(s):
