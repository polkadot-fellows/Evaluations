# Argument-0004: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/03/24)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: I
- Date of initial induction: 2024-04-26
- Date of last report:  2024/12/19
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling, Availability


## Reporting period

- Start date: 2024/12/19
- End date: 2025/03/24


## Argument

My contributions throughout the reporting period are centered around the following topics:

1. Elastic scaling

During this period I've worked on the deprecation of the static async backing parameters which were initially introduced
for enabling and configuring async backing. The reason for removing the static params is twofold:
- they have been made obsolete by the claim queue concept which was introduced for agile coretime.
- enabling elastic scaling on polkadot would have meant bumping the static max_candidate_depth value to at least 6 to allow for a parachain
using 3 cores. This is not ideal, since being a static parameter, it would apply to all parachains regardless of their assigned coretime, leading
to increased resource usage on validators and less than ideal spam protection.

This is one of the main blockers for enabling elastic scaling on polkadot. The PR also removes and refactors a lot of code which used to handle
the potential of async backing not being enabled, which is no longer possible on production networks. Link to the PR: https://github.com/paritytech/polkadot-sdk/pull/7254.

2. Collator protocol revamp

This is a project that will improve the resilience of backing validators through a persisted reputation system for collators.
During the reporting period, I've researched the topic based on [previous issues](https://github.com/paritytech/polkadot-sdk/issues/616) and discussions with other fellows. I've created a document which has been so far privately reviewed by other fellows and will be later turned into an RFC.
I am leading this project and I'm the main developer responsible for it at present. So far I've been in the research, planning and prototyping phase, the WIP code can be seen on [this branch](https://github.com/paritytech/polkadot-sdk/tree/alindima/collator-protocol-revamp).
A first PR which adds a new UMP signal is also open for review: https://github.com/paritytech/polkadot-sdk/pull/7955, adding a mechanism for parachain runtimes to assign the merit of building a valid block to a particular network key (PeerId). This is a key attribute of the revamp.

### Other work:

Besides the mentioned topics, I'm providing reviews for my area of expertise in polkadot-sdk and RFCs, as well as technically mentoring someone from the Parachains core team at Parity (which I'm a part of).


## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referendums available for my rank to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
    I plan on submitting an evidence for promotion to rank II in a couple of months

