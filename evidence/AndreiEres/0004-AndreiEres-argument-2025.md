# Argument-0000: Retention at/Promotion to Rank ____

|                 |                               |
| --------------- | ----------------------------- |
| **Report Date** | 2025/07/07                    |
| **Submitted by**| Andrei Eres                   |


## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 1
- Date of initial induction: 2024/07/19
- Date of last report: 2025/04/02
- Area(s) of Expertise/Interest: Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking


## Reporting period

- Start date: 2025/04/02
- End date: 2025/07/07


## Argument

During this reporting period, my primary focus was on the performance and stability of Polkadot. The most impactful areas were:

**Dispute Resilience:**
- In May 2025, both Polkadot and Kusama experienced dispute storms. This highlighted the need for better spam prevention, monitoring, and alerting.
- The investigation revealed that the disputes on Polkadot originated from a single validator suffering from disk corruption. To mitigate this, I implemented integrity checks for PVF artifacts before execution. See [PR #8833](https://github.com/paritytech/polkadot-sdk/pull/8833) and follow-up  [PR #8908](https://github.com/paritytech/polkadot-sdk/pull/8908).
- We observed high CPU usage in the dispute subsystems during finality lag. To tackle this, I created a subsystem benchmark for dispute participation, and I’m expanding it to include more scenarios. See [PR #8828](https://github.com/paritytech/polkadot-sdk/pull/8828).
- We maintain a tool called polkadot-introspector to collect on-chain metrics about Polkadot performance. For this issue, I added tracking for dispute initiators and set up dispute alerts for our on-call rotation. For example, see [PR #887](https://github.com/paritytech/polkadot-introspector/pull/887).

**Block confidence:**
- We want to make the network more reliable for collators and ensure that every produced candidate gets to finalization. To improve parachain throughput and latency, we need thorough measurements. Some required metrics exist but lack dashboards; others need to be implemented.
- I started analyzing current metrics and preparing monitoring dashboards. As first results, I discovered that existing metrics about collators’ connection to backing groups are noisy and insufficient. I added a new metric for better visibility. See [PR #8973](https://github.com/paritytech/polkadot-sdk/pull/8973).
- I also added additional parachain performance metrics to the aforementioned polkadot-introspector. For example, see [PR #853](https://github.com/paritytech/polkadot-introspector/pull/853).

**Trie database optimization:**
- As part of launching Solidity smart contracts on AssetHub, I worked on optimizing the Trie database. See [parent issue #6131](https://github.com/paritytech/polkadot-sdk/issues/6131).
- To help collators perform optimally immediately after restart, I added an option to warm up the Trie Cache on node start. See [PR #7556](https://github.com/paritytech/polkadot-sdk/pull/7556).
- Improving the collators' throughput, we still face a bottleneck on the validators' side during block validation. I prepared a new benchmark to determine the weights involved in block validation. See [PR #8069](https://github.com/paritytech/polkadot-sdk/pull/8069).
- To confirm gains from keeping the entire state in the Trie Cache, I prepared a high-level benchmark based on ERC20 transfers: See [PR #7979](https://github.com/paritytech/polkadot-sdk/pull/7979) and results in [Issue #7540](https://github.com/paritytech/polkadot-sdk/issues/7540#issuecomment-3009015002).

In the upcoming period, I will continue to work on the performance and stability of Polkadot, focusing on dispute resilience and parachain performance optimization.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity). | There were no referenda during the current period in which I was allowed to vote. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

