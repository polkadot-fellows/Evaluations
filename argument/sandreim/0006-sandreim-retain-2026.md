# Argument-0006 Retention at Rank 3

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/06/04)                                                             |
| **Submitted by**| Andrei Sandu                                                                        |

## Member details

- Matrix username: @sandreim:parity.io
- Polkadot address: 13QdJvnJgfoitjrxESwrCWTaLMN8KvXxufDUucXM6EWGuxqh
- Current rank: 3
- Date of initial induction: 2023/07/18
- Date of last report: 2025/12/08
- Area(s) of Expertise/Interest: Parachain Consensus, Node Performance Engineering, Observability,
Stress and integration testing

## Reporting period

- **Start date:** 2025/12/09
- **End date:** 2026/06/04

## Argument

This period continued my multi-quarter effort to improve parachain block production reliability. My
central focus was **block confidence work** — diagnosing the root causes of low block confidence
and mitigating them by enabling longer AURA slots and faster block propagation. I also supported the
Bulletin Chain launch with integration and stress testing of 6s, 2s and 1s block configurations and
authored a high-level proposal for Polkadot SDK release QA automation. I started the
cleanup of legacy collation/validation protocol code, and acted as a reviewer and design
consultant for the low-latency parachain work. Beyond that, I delivered a small protocol
improvement raising the code-size limits required to support larger parachain code upgrades.

### Block confidence work

I drove the diagnosis and resolution of the issues affecting block confidence in production chains
AH and PC.

**Investigation and root-cause analysis.** I drafted the plan to deploy the YAP canary parachain on
Polkadot
([#10933](https://github.com/paritytech/polkadot-sdk/issues/10933), runtime in
[#10165](https://github.com/paritytech/polkadot-sdk/pull/10165)) running 12 cores and 500ms blocks.
From this I identified and documented the dominant causes
([#10860](https://github.com/paritytech/polkadot-sdk/issues/10860)), the gap between Polkadot Asset
Hub and YAP/Kusama confidence ([#11827](https://github.com/paritytech/polkadot-sdk/issues/11827)), and
slow availability where the block producer does not see 2/3 of bitfields in time
([#11582](https://github.com/paritytech/polkadot-sdk/issues/11582)).

**Longer AURA slots.** I migrated parachains to 24s AURA slots — across all testnet parachains
([#11778](https://github.com/paritytech/polkadot-sdk/pull/11778)), the Bulletin Chain
([runtimes#1149](https://github.com/polkadot-fellows/runtimes/pull/1149)), and Kusama/Polkadot Asset
Hub and People Chain ([runtimes#1174](https://github.com/polkadot-fellows/runtimes/pull/1174)). With a
longer slot a single collator authors several consecutive blocks, which reduces slot-boundary fork
contention between collators (improving confidence) and improving Elastic Scaling throughput.

**Block propagation** I investigated AH and concluded that freshly built block traverses multiple
network hops to reach the next author, and each hop costs roughly 3x the inter-peer
latency (announce, request, response). Late blocks force authors to build on stale parents
resulting in forks.

I took the following actions to tackle this issue:

- Implemented workaround (increase sync peers) via CLI by coordinating with the System Parachain
  collators
- Implemented long term fix: authority discovery for parachains in Cumulus
  ([#11954](https://github.com/paritytech/polkadot-sdk/pull/11954)), aimed at eliminating multi-hop
  propagation delay on large parachain networks by ensuring 1-hop block announces between
  block authors
- Future proofing for large networks: proposed prioritized reserved peers bandwidth for sync
  protocols ([#11978](https://github.com/paritytech/polkadot-sdk/issues/11978)).

### Protocol improvement

I raised the RC block-size and code-size limits required to support larger parachain code upgrades,
enabling parachain code size up to 5MiB
([#11894](https://github.com/paritytech/polkadot-sdk/pull/11894),
[#11893](https://github.com/paritytech/polkadot-sdk/pull/11893)), with the corresponding production
runtime change in [runtimes#1157](https://github.com/polkadot-fellows/runtimes/pull/1157).

### Integration and stress testing

I fixed Fellowship zombienet test flakiness, extended the automated test coverage for Elastic
Scaling, and supported the Bulletin Chain launch (stress testing, stress test tool improvements
and investigating node issues).

- Added Elastic Scaling zombienet tests for Polkadot Asset Hub and People Chain
  ([runtimes#1155](https://github.com/polkadot-fellows/runtimes/pull/1155), [#12001](https://github.com/paritytech/polkadot-sdk/pull/12001)).
- Improved the Bulletin Chain stress-test tooling to support long-duration runs, mixed payload sizes,
  and resilient RPC reconnection ([#392](https://github.com/paritytech/polkadot-bulletin-chain/pull/392),
  [#398](https://github.com/paritytech/polkadot-bulletin-chain/pull/398),
  [#416](https://github.com/paritytech/polkadot-bulletin-chain/pull/416),
  [#422](https://github.com/paritytech/polkadot-bulletin-chain/pull/422)).

### Polkadot SDK release QA automation

I authored a high-level design for automating Polkadot SDK release QA
([#12054](https://github.com/paritytech/polkadot-sdk/issues/12054)). I identified the gaps in our
current release process. Release candidates are validated manually with no real
application load, no long-duration runs, no mixed-version (matrix) testing, no negative scenarios,
and no verification against production runtimes. I proposed a dedicated, scalable test environment
created by forking test/prod networks with `zombie-bite`, triggered by SDK release and Fellowship
runtime releases. The goal is to mimic real-world conditions (multiple node versions, simulated
latencies and faults, malicious actors, simulated user load) and runs continuously for days at a
time, with results and individual failures aggregated and reported automatically. The proposal
defines an MVP focused on block production, block confidence, and finality for SDK releases.

### Protocol cleanup

I scoped and drafted the retirement of legacy code paths to reduce maintenance burden and attack
surface: removing v1 `CandidateDescriptor` support
([#11373](https://github.com/paritytech/polkadot-sdk/issues/11373))
and simplifying the upgrade path of the validation and collation protocols
([#11412](https://github.com/paritytech/polkadot-sdk/issues/11412)). The implementation work —
disabling v1 candidate receipts ([#11397](https://github.com/paritytech/polkadot-sdk/pull/11397)) and
removing v1 support from the collator protocol ([#11414](https://github.com/paritytech/polkadot-sdk/pull/11414))
 — is drafted but currently parked, since I must sync with parachain teams that might still use old
versions.

### Design consultation and code review

I acted as a consultant and reviewer for the low-latency parachain design and its implementation,
contributing to the design discussions and reviewing the PRs that build it — notably the support
for older relay parents, relay-parent advertisement in v3, v3-descriptor scheduling and v3 Cumulus
support.
I also reviewed the ongoing collator-protocol revamp
([#8541](https://github.com/paritytech/polkadot-sdk/pull/8541),
[#11046](https://github.com/paritytech/polkadot-sdk/pull/11046),
[#10917](https://github.com/paritytech/polkadot-sdk/pull/10917) and related PRs). In total I reviewed
70 merged PRs in `polkadot-sdk` during the reporting period.

A full list of merged contributions in `polkadot-sdk` for the period is available
[here](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Asandreim+is%3Amerged+merged%3A2025-12-09..2026-06-04).

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|III|70%   |100%  | 100% | 47 out of the 47 |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
