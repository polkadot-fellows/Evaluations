# Argument-0009: Retention at Rank II

|                  |             |
| ---------------- | ----------- |
| **Report Date**  | 2026/08/28  |
| **Submitted by** | Andrei Eres |

## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 2
- Date of initial induction: 2024/07/19
- Date of last report: 2026/06/03
- Area(s) of Expertise/Interest: Statement Store, Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking


## Reporting period

- Start date: 2026/06/03
- End date: 2026/08/28


## Argument

During this reporting period, my main focus was scaling the statement-store for large networks: together with the team we designed the DHT-affinity distribution, and brought it to a working proof of concept. I also hardened the gossip protocol's memory behavior and continued developing statement-store support in smoldot.

### Statement Store DHT-affinity distribution

The statement-store is a substrate component that lets web3 applications exchange signed statements across the network. Its current design, where every node stores all statements, cannot scale to large networks. After last period's research, we designed a DHT-affinity distribution and started its implementation (see [the tracking issue with implementation details](https://github.com/paritytech/polkadot-sdk/issues/11932)).

On the feature branch we built the proof of concept end to end. The explicit-affinity module collects the topics a node is interested in, from its configuration and live RPC subscriptions. Peers share these filters with each other, and the peer steering module connects the node to peers with matching interests. Testing with zombienet scenarios caught real bugs, for example peer steering could drop all connected peers at once. The work is ongoing: the gated v2 DHT-affinity path and behaviour-based peer scoring are prepared for review and merge to master.


### Statement Gossip Hardening

While preparing the protocol for large networks, I removed the unbounded memory in the gossip layer on master. Initial sync used to snapshot every statement hash for each connecting peer, a full store scan and up to 2 MiB per peer. I replaced it with [a resumable cursor over the admission journal](https://github.com/paritytech/polkadot-sdk/pull/12890). I also [removed the per-peer known-statement cache](https://github.com/paritytech/polkadot-sdk/pull/12873), which a peer could inflate to 320 MiB, [bounded outbound sends with a per-peer outbox](https://github.com/paritytech/polkadot-sdk/pull/12878), made the validation queue allocate lazily, and prepared [bounding of the inbound batch size](https://github.com/paritytech/polkadot-sdk/pull/12991) against decode-amplification attacks. Together these changes make the gossip layer run in bounded memory regardless of peer behavior.

### Statement Store Light Node

In smoldot, I continued improving the statement-store support landed last period: [indexed subscriptions by topic](https://github.com/paritytech/smoldot/pull/3281) to narrow statement matching from a scan over all subscriptions to only the relevant ones, [moved notifications to a dedicated channel](https://github.com/paritytech/smoldot/pull/3316), [fixed a panic on affinity updates](https://github.com/paritytech/smoldot/pull/3334) when the statement protocol is disabled, and closed the remaining follow-ups from the initial implementation. I also made [statement submission validate like on a full node](https://github.com/paritytech/smoldot/pull/3344), so clients get the same responses whether they submit through smoldot or a polkadot-sdk node, with a zombienet test that checks the parity between the two.

### Further development

In the next period, I'll continue the rollout of statement-store distribution for large networks.


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
