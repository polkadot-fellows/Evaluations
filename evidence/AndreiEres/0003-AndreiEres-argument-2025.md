# Argument-0003: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/04/02                                                             |
| **Submitted by**| Andrei Eres                                                                        |


## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 1
- Date of initial induction: 2024/07/19
- Date of last report: 2025/01/07
- Area(s) of Expertise/Interest: Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking


## Reporting period

- Start date: 2025/01/07
- End date: 2025/04/02


## Argument

During this reporting period, I primarily focused on the scalability and performance of Polkadot. The most impactful directions are:
- **Trie database optimization.**
  - As part of launching Solidity smart contracts on AssetHub, I worked on optimizing the Trie database. See [parent issue \#6131](https://github.com/paritytech/polkadot-sdk/issues/6131).
  - We considered setting a maximum size for the Trie cache based on runtime to fit the entire state into memory. However, we decided it should be up to the collator to determine the setup for running nodes. Therefore, we abandoned the initial plan to simply warm up the cache. Collators who want better performance can adjust the cache size as needed using an existing CLI flag. See [PR \#7556](https://github.com/paritytech/polkadot-sdk/pull/7556).
  - Improving the collators' throughput, we still face a bottleneck on the validators' side during block validation. We are currently preparing a new benchmark to determine the weights involved in block validation. See [PR \#8069](https://github.com/paritytech/polkadot-sdk/pull/8069).
  - I prepared a benchmark to determine how many smart contract calls we can include in one block. See [PR \#7979](https://github.com/paritytech/polkadot-sdk/pull/7979). This was the first time we interacted with smart contracts directly, rather than through the ETH proxy node. As a result, we discovered a few issues, such as [issue \#37](https://github.com/paritytech/contract-issues/issues/37) and [PR \#7756](https://github.com/paritytech/polkadot-sdk/pull/7756). The benchmark setup can also be used in the next Spammening event with smart contract calls. See [issue \#8027](https://github.com/paritytech/polkadot-sdk/issues/8027).
- **Networking backend benchmarking.**
  - To support the ongoing transition from libp2p to litep2p, we recently implemented benchmarks to compare the performance of network backends using both libraries. The benchmark results for commits to the master branch are presented in the following charts: [notifications protocol](https://paritytech.github.io/polkadot-sdk/bench/notifications_protocol/), [request-response protocol](https://paritytech.github.io/polkadot-sdk/bench/request_response_protocol/).
  - At this stage, I primarily focused on optimizing execution time in CI and improving data representation in charts. For example, see [PR \#7056](https://github.com/paritytech/polkadot-sdk/pull/7056) and [PR \#7185](https://github.com/paritytech/polkadot-sdk/pull/7185).
  - It's worth mentioning that the benchmarks have already paid out. In the charts, we found that in some cases, llibp2p is faster than litep2p. The networking team then improved the speed for the most common payload sizes. See [issue \#7183](https://github.com/paritytech/polkadot-sdk/issues/7183)
- **Subsystem benchmarking with real networking stack.**
  - While networking backend benchmarks allow us to compare the performance of p2p libraries, we need to use a real network in our subsystem benchmarks to see the bigger picture. Currently, benchmarks use a simulated network. The benchmark results for commits to the master branch are presented in the following charts: [approval-voting](https://paritytech.github.io/polkadot-sdk/bench/approval-voting-regression-bench/), [availability-distribution](https://paritytech.github.io/polkadot-sdk/bench/availability-distribution-regression-bench/), [availability-recovery](https://paritytech.github.io/polkadot-sdk/bench/availability-recovery-regression-bench/), [statement-distribution](https://paritytech.github.io/polkadot-sdk/bench/statement-distribution-regression-bench/).
  - I continued to work on adding a real networking stack to our subsystem benchmarks and received initial results for the availability-recovery and statement-distribution subsystems. However, the work is still ongoing. See [PR \#7125](https://github.com/paritytech/polkadot-sdk/pull/7125).
* **Tests stability.**
  * I worked on improving the stability of flaky tests in the Polkadot repo. See [PR \#7657](https://github.com/paritytech/polkadot-sdk/pull/7657).

In the upcoming period, I will continue to work on the scalability of Polkadot, focusing on the performance of the Trie database and the networking stack.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity). | There were no referenda during the current period in which I was allowed to vote. I didn't count [one wrong track](https://collectives.subsquare.io/fellowship/referenda/301). |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
