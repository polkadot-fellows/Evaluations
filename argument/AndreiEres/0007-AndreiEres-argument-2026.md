# Argument-0007: Retention at Rank II

|                  |             |
| ---------------- | ----------- |
| **Report Date**  | 2026/03/04  |
| **Submitted by** | Andrei Eres |

## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 2
- Date of initial induction: 2024/07/19
- Date of last report: 2025/12/03
- Area(s) of Expertise/Interest: Statement Store, Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking


## Reporting period

- Start date: 2025/12/03
- End date: 2026/03/04


## Argument

During this reporting period, my main focus was bringing the statement-store to production readiness. I also continued improving network observability.

### Statement Store

The statement-store is a substrate component that allows web3 applications to exchange signed statements across the network. After defining its current performance in the previous period, we started preparing a production-ready solution for small networks.

On the performance side, I [removed the runtime dependency from statement validation](https://github.com/paritytech/polkadot-sdk/pull/10787) and [parallelized network statement processing](https://github.com/paritytech/polkadot-sdk/pull/10617) across many workers, significantly improving throughput. To validate these improvements objectively, I continued building the benchmarking infrastructure — e.g. [networking](https://github.com/paritytech/polkadot-sdk/pull/10661) and [latency](https://github.com/paritytech/polkadot-sdk/pull/10542) benchmarks — and set up end-to-end scale tests in k8s using a [CLI tool](https://github.com/paritytech/polkadot-sdk/pull/11234). I also implemented [rate-limiting for statement networking](https://github.com/paritytech/polkadot-sdk/pull/11051) to prevent peers from bypassing the in-memory cache.

To bring the statement-store to devices like browsers and mobile apps, we decided to reuse smoldot — an existing light client implementation. I'm currently working on a [prototype](https://github.com/AndreiEres/smoldot/pull/2) of the light statement store for non-production use.

### Network Observability

As part of my on-call rotations, I worked on making metrics more accurate: [improved the bitfields metrics](https://github.com/paritytech/polkadot-sdk/pull/10827) in polkadot-sdk and [fixed dispute duplication metrics](https://github.com/paritytech/polkadot-introspector/pull/921) in polkadot-introspector. Using data from regression benchmarks I set up in previous periods, I also found a [possible regression in litep2p-based notification_protocol](https://github.com/paritytech/devops/issues/4867).

### Further development

In the next period, I'll continue developing the next version of the statement-store, focusing on scalability for large networks and the light statement store implementation. I'll also continue maintaining network observability.


## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                      | Comments                                                                          |
| ----- | ------------------- | -------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| I     | 90%                 | N/A                  |                                                                                                 |                                                                                   |
| II    | 80%                 | N/A                  | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity). | There were no referenda during the current period in which I was allowed to vote. |
| III   | 70%                 | 100%                 |                                                                                                 |                                                                                   |
| IV    | 60%                 | 90%                  |                                                                                                 |                                                                                   |
| V     | 50%                 | 80%                  |                                                                                                 |                                                                                   |
| VI    | 40%                 | 70%                  |                                                                                                 |                                                                                   |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
