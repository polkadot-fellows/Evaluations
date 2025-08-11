# Argument-0006: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/07/09)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: II
- Date of initial induction: 2024-04-26
- Date of last report:  2025/04/16
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling, Availability, Collator Protocol


## Reporting period

- Start date: 2025/04/16
- End date: 2025/07/09


## Argument

Over the past few months, I’ve been fully focused on designing and implementing the new collator protocol—the interface that enables communication between backing validators and collators.

I am leading this critical protocol upgrade aimed at improving the reliability and resilience of the parachain backing process. It ensures that parachain liveness is maintained at all times, a key requirement as we prepare for the migration to Asset Hub (which makes parachain liveness even more important).
The main feature of the protocol is that it adds a persistent reputation-based system for collators, which are used for prioritising connections and collation fetches.

With major foundational pieces (mostly authored in the last reporting period) already merged—such as [the UMP primitives](https://github.com/paritytech/polkadot-sdk/pull/7955) and the [reputation-based peer manager](https://github.com/paritytech/polkadot-sdk/pull/8191)—I’ve shifted my focus to implementing the final core components needed to kick off the testing phase.

The ongoing work is centered on [this PR](https://github.com/paritytech/polkadot-sdk/pull/8541), which introduces the `CollationManager` (the component that keeps track of advertisements & collations, tracks their statuses and launches work - fetching or seconding) and implements the main subsystem logic (the code that glues together all components).
The PR is pending review, some small enhancements, final touch-ups and some more testing. The finish line is in sight, and the implementation will ship with comprehensive unit tests to ensure robustness, aiming to be tested in a live testnet by the end of Q3.

I have also authored a [temporary in-memory implementation of the reputation database](https://github.com/paritytech/polkadot-sdk/pull/8242), to unblock testing until the persistent, production-ready
DB implementation is done.

Besides my engineering work, I have been delegating and providing support to other engineers contributing to the collator protocol.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II  |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referendums available for my rank to vote on. |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

