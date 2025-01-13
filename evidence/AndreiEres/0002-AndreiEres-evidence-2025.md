# Evidence-0002: Retention at Rank I

| **Report Date**  | 2025/01/07  |
|------------------|-------------|
| **Submitted by** | Andrei Eres |

## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 1
- Date of initial induction: 2024/07/19
- Date of last report: 2024/10/20
- Area(s) of Expertise/Interest: Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking

## Reporting period
- Start date: 2024/10/20
- End date: 2025/01/07

## Evidence

During the reporting period, I primarily focused on the scalability of Polkadot. There are the most impactful directions:
- **Backing back pressure.** Completed the fork tracking and removing non-viable backing jobs in [#5616](https://github.com/paritytech/polkadot-sdk/pull/5616). A possible follow-up is to investigate the impact of dropping approval jobs as well; see [issue \#6401](https://github.com/paritytech/polkadot-sdk/issues/6401)
- **Networking backend benchmarking**. To support the ongoing transition from libp2p to litep2p, implemented and released benchmarks to compare the performance of network backends based on both libraries.. See [\#6077](https://github.com/paritytech/polkadot-sdk/pull/6077), [\#6455](https://github.com/paritytech/polkadot-sdk/pull/6455), [#6636](https://github.com/paritytech/polkadot-sdk/pull/6636). Charts over commits to master branch: [notifications_protocol](https://paritytech.github.io/polkadot-sdk/bench/notifications_protocol/), [request_response_protocol](https://paritytech.github.io/polkadot-sdk/bench/request_response_protocol/).
- **Subsystem benchmarking with real networking stack**. While networking backend benchmarks allow us to compare the performance of p2p libraries, we need to use a real network in our subsystem benchmarks to see the bigger picture. Attempted a straightforward approach by spawning real peers, but it was unsuccessful: [\#6845](https://github.com/paritytech/polkadot-sdk/pull/6845). Started working on a more efficient approach: [\#7125](https://github.com/paritytech/polkadot-sdk/pull/7125).

In the upcoming period, I will continue working on the scalability of Polkadot, focusing on the performance of the networking stack.

## Voting record
|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity). | There were no referenda during the current period in which I was allowed to vote. I target to raise it to 90% at least for the next reporting period |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
