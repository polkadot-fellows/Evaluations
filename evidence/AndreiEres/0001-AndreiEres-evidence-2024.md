# Evidence-0001: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/10/20                                                             |
| **Submitted by**| Andrei Eres                                                                        |


## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 1
- Date of initial induction: 2024/07/19
- Date of last report: N/A
- Area(s) of Expertise/Interest: Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking


## Reporting period

- Start date: 2024/08/14
- End date: 2024/10/20



## Evidence
During the reporting period, I primarily focused on the scalability and observability of Polkadot:

- Optimized PVF execution:
    - Validators prepare the PVF in advance for a session where they are authority: [#4791](https://github.com/paritytech/polkadot-sdk/pull/4791), [#5606](https://github.com/paritytech/polkadot-sdk/pull/5606).
    - Added PVF execution priority to maintain finality when nodes are overloaded: [#4837](https://github.com/paritytech/polkadot-sdk/pull/4837).
    - Drop execution of postponed backing jobs that are no longer viable: [#5616](https://github.com/paritytech/polkadot-sdk/pull/5616).
- Started working on benchmarking the networking stack.
    - Added understanding of the task (work consist of protocol and subsystem benchmarks): [HackMD](https://hackmd.io/IPtg6eGgS6yFkDND6UDscA)
    - Added protocol benchmarks for libp2p based network backends: [#6077](https://github.com/paritytech/polkadot-sdk/pull/6077)
- Also:
    - Prepared for the increase `max_pov_size` to 10MB: [#5753](https://github.com/paritytech/polkadot-sdk/pull/5753), [#5924](https://github.com/paritytech/polkadot-sdk/pull/5924).
    - Refactored Polkadot code: [5707](https://github.com/paritytech/polkadot-sdk/pull/5707), [6015](https://github.com/paritytech/polkadot-sdk/pull/6015).
    - Updated Rust version in Fellowship Runtimes: [473](https://github.com/polkadot-fellows/runtimes/pull/473).
    - Improved stability of the polkadot-introspector, which we use to monitor parachain consensus on Polkadot, Kusama, and testnets.: e.g. [#770](https://github.com/paritytech/polkadot-introspector/pull/770), [#796](https://github.com/paritytech/polkadot-introspector/pull/796).

In the upcoming period, I will continue working on the scalability and observability of Polkadot, focusing on the performance of the networking stack.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity). | There were no referenda during the current period in which I was allowed to vote. I target to raise it to 90% at least for the next reporting period |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
