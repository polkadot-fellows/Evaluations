# Argument-0005: Promotion to Rank II

|                  |             |
| ---------------- | ----------- |
| **Report Date**  | 2025/08/25  |
| **Submitted by** | Andrei Eres |


## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 1
- Date of initial induction: 2024/07/19
- Date of last report: 2025/07/07
- Area(s) of Expertise/Interest: Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking


## Reporting period

- Start date: 2024/07/19
- End date: 2025/08/25


## Argument

Since I started working on Polkadot, my primary focus has been on validator node scalability and observability. Through this work, I have developed familiarity with the Parachain Protocol while contributing to network maintenance through on-call rotations and incident response. The contributions below reflect my growing understanding of the protocol and readiness to take on the responsibilities of a Rank II member.

### PVF execution
One of the important parts of the candidate validation pipeline is PVF execution. Improving execution speed directly reduces latency and enhances the scalability of the Polkadot network.

I stabilized finality lag at session boundaries by having new validators prepare PVF artifacts [one session in advance](https://github.com/paritytech/polkadot-sdk/pull/4791), rather than only after the session starts.

To maintain finality under high load, I added prioritization of PVF execution [for disputes and approvals over backing](https://github.com/paritytech/polkadot-sdk/pull/4837). Splitting the queues by job type revealed that we sometimes executed backing jobs even when the candidate was no longer viable. I resolved this issue [by dropping stale jobs](https://github.com/paritytech/polkadot-sdk/pull/5616).

[The investigation](https://forum.polkadot.network/t/2025-05-03-polkadot-parachain-block-time-degradation/12963) of a recent Polkadot incident revealed that the disputes originated from a single validator suffering from disk corruption. To mitigate this, I implemented [integrity checks for PVF artifacts](https://github.com/paritytech/polkadot-sdk/pull/8833).

### Smart Contracts Launch
As part of launching Solidity smart contracts on AssetHub, I worked [on optimizing the Trie database](https://github.com/paritytech/polkadot-sdk/issues/6131) and recently started working [on embedded EVM in foundry-polkadot](https://github.com/paritytech/foundry-polkadot/issues/211).

To help collators perform optimally immediately after restart, I added an option [to warm up the Trie Cache on node start](https://github.com/paritytech/polkadot-sdk/pull/7556). I'm in the process of enabling it [for all AssetHub parachains](https://github.com/paritytech/polkadot-sdk/issues/8810).

While improving the collators' throughput, we still face a bottleneck on the validators' side during block validation. I prepared a new benchmark to determine the weights involved [in block validation](https://github.com/paritytech/polkadot-sdk/pull/8069).

I prepared a benchmark to determine how many smart contract calls we can [include in one block](https://github.com/paritytech/polkadot-sdk/pull/7979). This was the first time we interacted with smart contracts directly, rather than through the ETH proxy node. As a result, we discovered a few issues, such as [a wrong generated address](https://github.com/paritytech/contract-issues/issues/37) and [unexpected compile error](https://github.com/paritytech/polkadot-sdk/pull/7756). The benchmark setup can also be used in the next Spammening event [with smart contract calls](https://github.com/paritytech/polkadot-sdk/issues/8027).

### Subsystem Benchmarks
On our road to 1k validators, we used to test node performance on testnets, but then we came up with a different approach. The logic of the Parachain Protocol is spread over many subsystems, but most of the load is localized in just a few of them. To test the most loaded subsystems with different parameters for many test cases without running large testnets, we introduced subsystem benchmarks.

I wrote benchmarks for [statement-distribution](https://github.com/paritytech/polkadot-sdk/pull/3863), [dispute-coordinator and dispute-distribution](https://github.com/paritytech/polkadot-sdk/pull/8828) subsystems, added CPU and memory profiling to the framework, and set up publishing of the results for commits to the master branch [to the public charts](https://paritytech.github.io/polkadot-sdk/bench/). Contrary to our hypothesis, the statement-distribution benchmark didn't show significant CPU usage, so the impact of optimizing the subsystem on node performance is minimal. The dispute subsystems benchmark confirmed the recent fix [of key derivation overusage](https://github.com/paritytech/polkadot-sdk/pull/8837) made by [tdimitrov](https://github.com/tdimitrov).

Currently, benchmarks use an emulated network. We had an idea of using a real networking stack to better understand the networking load. I made a few attempts and received initial results for the availability-recovery and statement-distribution subsystems. However, [the work is still ongoing](https://github.com/paritytech/polkadot-sdk/pull/7125).

### Networking Benchmarks
Work on replacing the resource-intensive libp2p with litep2p is still in progress. To make this project efficient, we needed to measure improvements and regressions using protocol benchmarks.

I implemented and released benchmarks to compare the performance of network backends based [on libp2p](https://github.com/paritytech/polkadot-sdk/pull/6077), [and litep2p](https://github.com/paritytech/polkadot-sdk/pull/6455). Then optimized the benchmarks [for CI execution](https://github.com/paritytech/polkadot-sdk/pull/6636). The benchmark results over commits to the master branch are presented [in the charts](https://paritytech.github.io/polkadot-sdk/bench/).

It's worth mentioning that the benchmarks have already paid off. In the charts, we found that in some cases, libp2p is faster than litep2p. The networking team then improved the speed for [the most common payload sizes](https://github.com/paritytech/polkadot-sdk/issues/7183).

### Monitoring
To improve parachain throughput and latency, and to ensure the network is reliable, we need thorough measurements. We use multiple dashboards and alerting, constantly adding new metrics.

Recently, I started working on collator performance. Some required metrics exist but lack dashboards; others need to be implemented. As initial results, I added metrics about [connectivity to backing groups](https://github.com/paritytech/polkadot-sdk/pull/8973) and improved the accuracy of [collation drops](https://github.com/paritytech/polkadot-sdk/pull/9319).

I maintain a tool called polkadot-introspector to collect on-chain metrics about Polkadot performance and stability, e.g., tracking [dispute initiators](https://github.com/paritytech/polkadot-introspector/pull/887) and [candidate status](https://github.com/paritytech/polkadot-introspector/pull/853). We use these metrics to track the current state of Polkadot and Kusama and set up alerts for our on-call rotation.

I also regularly go on-call, e.g., I was on duty during [the last Polkadot incident](https://github.com/paritytech/polkadot-sdk/issues/8414), communicating with the community in GitHub and Matrix chats.


### Publications
- [Introduction to subsystem benchmarks](https://forum.polkadot.network/t/what-are-subsystem-benchmarks/8212/) in the Polkadot Forum.


## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                      | Comments                                                                          |
| ----- | ------------------- | -------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| I     | 90%                 | N/A                  | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity). | There were no referenda during the current period in which I was allowed to vote. |
| II    | 80%                 | N/A                  |                                                                                                 |                                                                                   |
| III   | 70%                 | 100%                 |                                                                                                 |                                                                                   |
| IV    | 60%                 | 90%                  |                                                                                                 |                                                                                   |
| V     | 50%                 | 80%                  |                                                                                                 |                                                                                   |
| VI    | 40%                 | 70%                  |                                                                                                 |                                                                                   |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
