# Argument-0004: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/09/05
| **Submitted by**| Michał Kucharczyk                                                                           |


## Member details

- Matrix username: `@michal:parity.io`
- Polkadot address: [14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo](https://collectives.statescan.io/#/accounts/14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo)
- Current rank: 1
- Date of initial induction: `2024/06/02`
- Date of last report: `2025/06/13`
- Area(s) of Expertise/Interest: `Substrate node` ,`Transaction Pool`, `ChainSpec/GenesisConfig`


## Reporting period

- Start date: 2025/06/13
- End date: 2025/09/05

## Argument

The fork-aware transaction pool became the default starting with the `2506-01` release. The new transaction pool is now in maintenance mode, and no active development is planned for it.  

Over the last three months, I made a few small improvements and bug fixes in the `txpool`. These include adjusted [metrics buckets](https://github.com/paritytech/polkadot-sdk/pull/9495) for the reliability dashboard, a [fix](https://github.com/paritytech/polkadot-sdk/pull/9338) for instant-seal nodes, and relaxed re-validation for [implicitly](https://github.com/paritytech/polkadot-sdk/pull/9189) dependent transactions, which should make it easier to transact from newly funded accounts. I also started some work on throughput testing on the versi network, which was not concluded yet.

My main focus during reporting period was improving the [PoV storage size reclaim mechanism](https://github.com/paritytech/polkadot-sdk/issues/6020). The current issue is that storage root calculation, done in the final step of block building, may include nodes that were not counted during extrinsic execution. This can cause the storage size limit to be exceeded. I evaluated and optimized the performance of several approaches and, based on brainstorming sessions with teammates, was able to find an acceptable solution. The details are described in this [write-up](https://hackmd.io/o_Ghc86OT4KzCE4x04MeOg?view), this undertaking is still proof of concept stage.  

As part of this work, I also explored the details of how the Substrate state trie is implemented.  


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | None. |   |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

