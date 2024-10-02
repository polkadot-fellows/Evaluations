# Evidence-0001: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/10/02                                                                                  |
| **Submitted by**| Michał Kucharczyk                                                                           |


## Member details

- Matrix username: `@michal:parity.io`
- Polkadot address: <a target='_blank' href='https://collectives.statescan.io/#/accounts/14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo'>14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo</a>
- Current rank: 1
- Date of initial induction: `2024/06/02`
- Date of last report: N/A
- Area(s) of Expertise/Interest: `Substrate node` ,`Transaction Pool`, `ChainSpec/GenesisConfig`


## Reporting period

- Start date: 2024/06/02
- End date: 2024/10/02

## Evidence

I am currently focused on refactoring the transaction pool and implementing a fork-aware version to address the issues outlined in [#1202 issue](https://github.com/paritytech/polkadot-sdk/issues/1202). The related [pull request #4369](https://github.com/paritytech/polkadot-sdk/pull/4639) is under review. The design and approach are detailed in this short [top-level design note](https://hackmd.io/@_FY3-hvwQZ6cX_4n8zYUNA/HJqUWj4_s).
Following the knowledge-sharing sessions I conducted within the Node SDK team, I authored a technical [note](https://hackmd.io/@_FY3-hvwQZ6cX_4n8zYUNA/SyT1QuhnA) on the fork-aware transaction pool. Additionally, I have started working on a [transaction test tool](https://github.com/michalkucharczyk/tx-test-tool/) designed to facilitate local and QA tests of the transaction pool. The follow-up work is planned [here](https://github.com/paritytech/polkadot-sdk/issues/5472). This work improves transaction handling under forks, a critical aspect of parachains performance and resilience.

The most important lessons I have learned from this work include:
 - Building a generic transaction graph for efficient transaction pool management,
 - Addressing the challenge of preventing block builder starvation, ensuring smooth non-empty block production.

Additionally, I have minor contributions to Omni-Node, primarily by focusing on chain specifications and genesis configuration across various runtimes through reviews. Some related small PRs include: [#4678](https://github.com/paritytech/polkadot-sdk/pull/4678), [#5813](https://github.com/paritytech/polkadot-sdk/pull/5813), and [#4739](https://github.com/paritytech/polkadot-sdk/pull/4739).

## Voting record

None. I'll try to improve it.

