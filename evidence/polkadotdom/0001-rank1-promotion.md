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

- Start date: 2024/04/11
- End date: 2025/06/30


## Argument

Hello, all! My name is Dom. I've been actively contributing to the Polkadot ecosystem since [April 11th, 2024](https://github.com/paritytech/polkadot-sdk/pull/4091) and I believe it's now time for me to take the next step.

As a candidate seeking promotion to rank 1, I am charged with providing three clear examples of 'modest but substantial' contributions to the protocol. I will delineate these in order of perceived impact.

### RFC 150 - Voting While Delegating
It has long been [requested](https://github.com/polkadot-fellows/RFCs/pull/35) that a user be able to vote simultaneous to their delegating. I first proposed [RFC-150](https://github.com/PolkadotDom/RFCs/blob/dom/voting-while-delegating/text/0150-voting-while-delegating.md), then followed up shortly with the implementation [here](https://github.com/paritytech/polkadot-sdk/pull/9026).

I chose to work on this because I believe it will allow our governance system to more accurately approximate the ground truth voter preferences function. By increasing delegations and therefore voter turnout, it will ensure everyone is more accurately represented when decisions are made - the foundation of any democracy. I am hopeful it will meaningfully increase delegation rate within OpenGov.

### AHM Testing Help

As the ecosystem approached the AHM for Westend, the Parity team [needed state tests](https://github.com/polkadot-fellows/runtimes/issues/644) for each of the pallets that would be migrating from relay to AH. These were to function as a secondary assurance that all data was moving smoothly through XCM. I constructed the tests for the [pallet-bounties](https://github.com/polkadot-fellows/runtimes/pull/669), [pallet-referenda](https://github.com/polkadot-fellows/runtimes/pull/672), [pallet-scheduler](https://github.com/polkadot-fellows/runtimes/pull/680), and [pallet-staking/staking-async](https://github.com/polkadot-fellows/runtimes/pull/727) pallets, a few of which were complicated by cross pallet state dependencies.

I felt this was an important use of time due to the immutability and difficult to amend nature of a finalized blockchain. It struck me very much as a 'measure twice, cut once' situation.. I am happy to report that the state piping of these pallets went smoothly.

### The `Stored` Procedural Macro

The FRAME codebase is littered with derives and attributes intended to [mark data items as suitable for runtime storage](https://github.com/paritytech/polkadot-sdk/blob/master/substrate/frame/conviction-voting/src/vote.rs#L239-L255). I personally recall being confused by these as a beginner and was subsequently stalled when my own storage items didn't work as expected.

The [new stored macro](https://github.com/paritytech/polkadot-sdk/pull/8032) allows for consolidating those tags into a simpler and more intuitive format. This will make FRAME much more amenable to beginners, and the immense reduction to boilerplate will serve us nicely.

### Honorable Mentions

I will speak on the following lightly, though each substantial in their own right.

I set up the parameterization of yearly DOT emission in [Adjustable Inflation](https://github.com/polkadot-fellows/runtimes/pull/732) and engaged in [promulgating security measures](https://github.com/paritytech/polkadot-sdk/issues/8557). It is my belief that giving the people a voice in economic parameters is an important endeavor.

I identified a signaling issue with our referenda system in [RFC 151, Crowdsourcing Decision Deposits](https://github.com/polkadot-fellows/RFCs/pull/151). I hope that this will lower the barrier to entry for ecosystem agents looking to enact change.

I [added serialization to the BoundedBTreeMap](https://github.com/paritytech/parity-common/pull/870) data structure to enable its use in genesis storage. I hope that this will save time for those seeking the same functionality.

### On a more personal note

I care very deeply about Polkadot's mission, and I hope this has been made tacit through my actions. The way I see it, our little democratic network state is the only reasonable measure we have against a mounting slide into global autocracy and division. So let's do some good work!

Thank you.