# Argument-0006: Retention at Rank II

|                  |             |
| ---------------- | ----------- |
| **Report Date**  | 2025/12/03  |
| **Submitted by** | Andrei Eres |

## Member details

- Matrix username: @andrei:parity.io
- Polkadot address: 1436xp47dm3w1yTvSncsf4cgVLH5dVsgBzMqtHkSx1XjG1Wb
- Current rank: 2
- Date of initial induction: 2024/07/19
- Date of last report: 2025/08/25
- Area(s) of Expertise/Interest: Parachain Consensus, Nodes Scalability and Observability, Subsystem Benchmarking


## Reporting period

- Start date: 2025/08/25
- End date: 2025/12/03


## Argument

During this reporting period, I focused on making the statement-store production-ready, supporting the Ethereum-compatible smart contract launch, and improving parachains block confidence.

### Statement Store Scalability
The statement-store is a substrate component that can be used by web3 applications to exchange signed statements across the network. Although it's been around for a while, it hasn't been used in production yet.

To evaluate the performance of statement-store, I implemented [the full scenario benchmarks](https://github.com/paritytech/polkadot-sdk/pull/9763) and [isolated tests](https://github.com/paritytech/polkadot-sdk/pull/9884). Initial results showed that nodes could not handle more than 300 clients before hitting bottlenecks.

I found and fixed [a deadlock in statement gossiping](https://github.com/paritytech/polkadot-sdk/pull/9868), and [optimized the propagation protocol](https://github.com/paritytech/polkadot-sdk/pull/9912) to reduce network overhead. After these changes, nodes can now handle statement exchange among 50K clients within one minute.

The work is ongoing. We're making the statement-store a convenient tool for web3 developers by [updating the RPC interface](https://github.com/paritytech/polkadot-sdk/pull/10421) and improving scalability.

### Smart Contract Launch Support
As part of launching Solidity smart contracts on AssetHub, I worked on [embedding EVM in foundry-polkadot](https://github.com/paritytech/foundry-polkadot/issues/211) and [optimizing the Trie database](https://github.com/paritytech/polkadot-sdk/issues/6131).

In pallet-revive, I added testing helpers that let developers set up specific scenarios like [pre-funding accounts](https://github.com/paritytech/polkadot-sdk/pull/9617) or [modifying contract storage](https://github.com/paritytech/polkadot-sdk/pull/9606). For foundry-polkadot, I worked on [translating state changes between REVM and PVM](https://github.com/paritytech/foundry-polkadot/pull/246) to keep execution consistent, and [implemented the CREATE opcode](https://github.com/paritytech/foundry-polkadot/pull/254).

I also finished [the Trie Cache benchmarks](https://github.com/paritytech/polkadot-sdk/pull/7979) that measure smart contract throughput on Asset Hub.

### Block Confidence
To improve Polkadot chains reliability, we started a block confidence initiative. During the reporting period, I improved the collation metrics [to separate expected fork-based drops from actual problems](https://github.com/paritytech/polkadot-sdk/pull/9319).

I kept maintaining polkadot-introspector, our monitoring tool that tracks on-chain data about parachain performance and network health.

### Further development
In the next period, I'll keep working on network scalability and performance, focusing on statement-store production readiness and parachain throughput.


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
