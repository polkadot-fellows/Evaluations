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
During the reporting period, I primarily focused on the scalability and observability of Polkadot. There are the most impactful directions:

- **Backing back pressure.** In cases of high load, we decided to prioritize PVF execution for disputes and approvals over backing to maintain finality. Splitting the queues by job kind revealed a problem where we executed backing jobs even when the candidate was no longer viable. We resolved this issue by dropping stale jobs. See: [#4837](https://github.com/paritytech/polkadot-sdk/pull/4837), [#5616](https://github.com/paritytech/polkadot-sdk/pull/5616).
- **Finality lag stabilization.** We experienced increased finality lag at session boundaries because new validators began preparing the PVF artifacts only after the session started. Now, they should prepare them one session in advance. See: [#4791](https://github.com/paritytech/polkadot-sdk/pull/4791), [#5606](https://github.com/paritytech/polkadot-sdk/pull/5606).
- **Benchmarking the networking stack.** Work on replacing the high-consuming libp2p with litep2p is in progress. To make this project efficient, we need to measure improvements and regressions using protocol and subsystem benchmarks. As a first step, we have added protocol benchmarks for libp2p-based network backends. See: [understanding of the task](https://hackmd.io/IPtg6eGgS6yFkDND6UDscA), [#6077](https://github.com/paritytech/polkadot-sdk/pull/6077)


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
