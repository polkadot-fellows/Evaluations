# Argument-0008: Retention at Rank II

|                  |             |
| ---------------- | ----------- |
| **Report Date**  | 2026/06/03  |
| **Submitted by** | Andrei Eres |

## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 2
- Date of initial induction: 2024/07/19
- Date of last report: 2026/03/04
- Area(s) of Expertise/Interest: Statement Store, Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking


## Reporting period

- Start date: 2026/03/04
- End date: 2026/06/03


## Argument

During this reporting period, my main focus remained the statement-store: hardening it with a complete testing strategy and scaling for large networks through affinity-based distribution, and implementing its light-node support in smoldot. I also worked on node scalability and continued maintaining network observability.

### Statement Store

The statement-store is a substrate component that lets web3 applications exchange signed statements across the network. In this period we finished a production-ready solution for small networks and began work on scalability for large networks.

The statement-store is an old component that we only recently began actively developing, so we put extra effort into preparing it for reliable operation: validating propagation correctness, resilience under load, and fault tolerance. We started with a testing strategy that defined not only the testing gaps but also the monitoring approach (see [the tracking issue with implementation details](https://github.com/paritytech/polkadot-sdk/issues/11472)).

While implementing the testing strategy, I added unit and integration tests that caught several bugs and deepened our understanding of the component. For example, we fixed a double state cleanup on flooding, and found that asynchronous DB flushes can lose a freshly submitted statement on SIGKILL — which I documented as acceptable for a best-effort protocol. In the final stage I prepared an on-call dashboard with key signals, wrote a runbook, and set up recurring load tests for new binary releases.

For real scalability, the current approach — where every node stores all statements — cannot scale, so we started working on DHT-based distribution (see [the tracking issue](https://github.com/paritytech/polkadot-sdk/issues/11932)). The work is ongoing; I'm currently researching peer-topology mechanisms.


### Statement Store Light Node

To bring the statement-store to devices like browsers and mobile apps, we decided to reuse smoldot — an existing light client implementation.

I landed [basic statement-store support](https://github.com/paritytech/smoldot/pull/3127), and on top of that implemented [explicit affinity](https://github.com/paritytech/smoldot/pull/3151). Some issues from these PRs moved to follow-ups, so I'm continuing to improve the support.

Testing the light node was also part of the testing strategy mentioned above. Beyond unit tests, I added the repository's first [browser-based integration tests](https://github.com/paritytech/smoldot/pull/3244) and [zombienet tests](https://github.com/paritytech/smoldot/pull/3191), together with the CI infrastructure to run them. The main smoldot team now actively uses these tests.

I also added a performance-benchmark case that [uses light nodes as load clients](https://github.com/paritytech/smoldot/pull/3239). It revealed several long-session stability problems in smoldot, which I [documented](https://github.com/paritytech/smoldot/issues/3255) for the main smoldot team.


### Node Scalability and Observability

As part of my on-call rotations, I worked on making metrics more robust across runtime upgrades. In polkadot-introspector (our tool for collecting on-chain metrics), I switched to [dynamic decoding of inherent data](https://github.com/paritytech/polkadot-introspector/pull/944), which prevented the metadata-mismatch breakage that was about to hit Kusama and Polkadot and also improved the tool's stability.

On the scalability side, I finished [enabling trie cache warm-ups on Westend, Kusama, and Polkadot](https://github.com/paritytech/polkadot-sdk/issues/8810), reducing cold-cache state-access latency on freshly started nodes across the production networks.

### Further development

In the next period, I'll continue scaling the statement-store for large networks. I'll also continue maintaining network observability.


## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
| ----- | ------------------- | -------------------- | -------------------------- | -------- |
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
