# Argument-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/06/30                                                             |
| **Submitted by**| polka.dom                                                                        |


## Member details

- Matrix username: @polkadotdom:matrix.org
- Polkadot address: 1L66uQMKFnXKSZx9pCD5o56GvvP1i2Qns7CaS2AaKp9mnwc
- Current rank: Candidate
- Date of initial induction: [2025/05/06](https://collectives.statescan.io/#/extrinsics/6306997-2)
- Date of last report: N/A
- Area(s) of Expertise/Interest: FRAME, System Parachains


## Reporting period

- Start date: 2024/05/10
- End date: 2025/06/30


## Argument

As a candidate seeking promotion to rank 1, I am charged with providing three clear examples of 'modest but substantial' contributions to the protocol. I will delineate these in order of perceived impact.

### RFC 150 - Voting While Delegating
It has long been requested that a user be able to vote simultaneous to their delegating. I first proposed [RFC-150](https://github.com/PolkadotDom/RFCs/blob/dom/voting-while-delegating/text/0150-voting-while-delegating.md), then followed up shortly with the implementation [here](https://github.com/paritytech/polkadot-sdk/pull/9026).

It is my sincere hope that this allows our governance system to more accurately approximate the ground truth voter preferences function.

### AHM Testing Help

As we approached the AHM for Westend, we needed state tests for each of the pallets that we would be migrating. These functioned as a secondary assurance that all data was moving smoothly. I constructed the tests for several of the pallets, a few of which were complicated by state dependencies across pallets. Below are those contributions -

[pallet-bounties](https://github.com/polkadot-fellows/runtimes/pull/669)  
[pallet-referenda](https://github.com/polkadot-fellows/runtimes/pull/672)  
[pallet-scheduler](https://github.com/polkadot-fellows/runtimes/pull/680)  
[pallet-staking/staking-async](https://github.com/polkadot-fellows/runtimes/pull/727)

I'm happy to report that to my knowledge the state piping of these pallets went smoothly. Though there were some overall XCM issues.

### The `Stored` Procedural Macro

The FRAME codebase is littered with derives and attributes intended to mark data items as suitable for runtime storage ([see example](https://github.com/paritytech/polkadot-sdk/blob/master/substrate/frame/conviction-voting/src/vote.rs#L239-L255)). This new attribute allows for consolidating all of those tags into a simpler and more intuitive format. In addition, it significantly lowers boilerplate throughout the codebase. The PR can be found [here](https://github.com/paritytech/polkadot-sdk/pull/8032).

I think this will be a real joy and I hope it makes the Substrate development journey more amenable to beginners.

### Honorable Mentions
[Adjustable Inflation](https://github.com/polkadot-fellows/runtimes/pull/732)  
[RFC 151](https://github.com/polkadot-fellows/RFCs/pull/151)  
and the dozen or so other PRs found across the...  
[polkadot-sdk](https://github.com/paritytech/polkadot-sdk/issues?q=author%3Apolkadotdom)  
[parity-scale-codec](https://github.com/paritytech/parity-scale-codec/pulls?q=author%3Apolkadotdom+)  
[try-runtime-cli](https://github.com/paritytech/try-runtime-cli/pulls?q=author%3Apolkadotdom+)  
[parity-common](https://github.com/paritytech/parity-common/pulls?q=author%3Apolkadotdom+)  
repos.

### On a more personal note

I care very deeply about Polkadot's mission, and I hope this has been made tacit through my actions. The way I see it, our little democratic network state is the only reasonable measure we have against a mounting slide into global autocracy and division. So let's do some good work!

Thank you.