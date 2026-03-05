# Argument-0006: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/03/05
| **Submitted by**| Michał Kucharczyk                                                                           |


## Member details

- Matrix username: `@michal:parity.io`
- Polkadot address: [14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo](https://collectives.statescan.io/#/accounts/14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo)
- Current rank: 1
- Date of initial induction: `2024/06/02`
- Date of last report: `2025/12/03`
- Area(s) of Expertise/Interest: `Substrate node` ,`Transaction Pool`, `ChainSpec/GenesisConfig`


## Reporting period

- Start date: 2025/12/03
- End date: 2026/03/05

## Argument

During this period I continued to deepen my expertise in Substrate node internals, specifically around block production, storage proofs, and the transaction pool.

The [PoV size reclaim fix](https://github.com/paritytech/polkadot-sdk/pull/10215) for [issue #6020](https://github.com/paritytech/polkadot-sdk/issues/6020) remains under review. This work spans runtime, state machine, and trie layers — requiring cross-cutting understanding of how storage proofs flow through the stack and how they impact performance. To formalize the interface changes it introduces, I submitted [RFC-158: Introduce v2 of `storage_proof_size` Host Function](https://github.com/polkadot-fellows/RFCs/pull/158).

I performed a thorough review of the [Block Bundling Node Side](https://github.com/paritytech/polkadot-sdk/pull/10477) PR, which is a substantial change to block production mechanics. The review surfaced minor code maintainability improvements that I explored on my fork: [BlockProductionSchedule](https://github.com/michalkucharczyk/polkadot-sdk/pull/5) and [BlockImportAuxiliaryData removal](https://github.com/michalkucharczyk/polkadot-sdk/pull/6).

As part of on-boarding to the PolkaJam implementation, I have been building familiarity with the JAM protocol through hands-on work on [jamtart](https://github.com/paritytech/jamtart) — a testing and benchmarking tool for JAM nodes. My main focus has been observability: the JAM toaster had limited tooling for protocol-level metrics, making debugging difficult. To address this I worked on [events streaming](https://github.com/paritytech/jamtart/pull/14), [preliminary Grafana dashboards](https://github.com/paritytech/jamtart/pull/12), [database layer performance](https://github.com/paritytech/jamtart/pull/7), and a [JIP-3 telemetry stress testing tool](https://github.com/michalkucharczyk/jip-3-spammer) for validating telemetry server capacity. As a side project, I also built [jam-orbit](https://github.com/michalkucharczyk/jam-orbit) ([demo](https://michalkucharczyk.github.io/files/30-jam-orbit-poc/0/index.html)), an educational toy for visualising JAM validator activity.

The fork-aware transaction pool continues in maintenance mode. I investigated and filed [Stuck transactions on Paseo Asset Hub](https://github.com/paritytech/polkadot-sdk/issues/11034), uncovering interesting edge cases around ETH transaction handling. I also participated in DevOps alert triage for asset-hub-polkadot reliability.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | None. |   |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
