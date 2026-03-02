# Argument-0005: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/12/03
| **Submitted by**| Michał Kucharczyk                                                                           |


## Member details

- Matrix username: `@michal:parity.io`
- Polkadot address: [14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo](https://collectives.statescan.io/#/accounts/14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo)
- Current rank: 1
- Date of initial induction: `2024/06/02`
- Date of last report: `2025/09/05`
- Area(s) of Expertise/Interest: `Substrate node` ,`Transaction Pool`, `ChainSpec/GenesisConfig`


## Reporting period

- Start date: 2025/09/05
- End date: 2025/12/03

## Argument

My main focus during this reporting period was completing the [PoV storage size reclaim fix](https://github.com/paritytech/polkadot-sdk/pull/10215). This addresses the long-standing [issue #6020](https://github.com/paritytech/polkadot-sdk/issues/6020) where storage root calculation could cause blocks to exceed PoV budgets. I implemented incremental storage root estimation spanning runtime, state machine, and trie layers. The main challenge was performance optimization - the naive approach reduced throughput to 2% of the original. Through iterative profiling and optimization, I brought the overhead down to 2-10%. The PR is now ready for review. I documented the "full stack" profiling methodology in [Reliable Flamegraphs for Substrate-Based Binaries](https://hackmd.io/QxHZRIzCRHavLHjURR634g).

The fork-aware transaction pool remains in maintenance mode. I continued with small fixes and supporting external teams encountering txpool issues: documented an [instant-seal transaction inclusion race](https://github.com/paritytech/polkadot-sdk/issues/10104), diagnosed [delayed ready events for manual-seal](https://github.com/paritytech/polkadot-sdk/issues/10332), and helped resolve a chain reverting issue for Anvil Node.

Additionally, I made tiny contributions to tooling and observability: [wasmtime perfmap profiling support](https://github.com/paritytech/polkadot-sdk/pull/9821) enabling proper flamegraph generation, and a [new timing histogram](https://github.com/paritytech/polkadot-sdk/pull/10312) for unfiltered InBlock events on the reliability dashboard.  


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

