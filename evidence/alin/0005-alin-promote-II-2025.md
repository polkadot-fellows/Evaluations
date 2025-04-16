# Argument-0005: Promotion to rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/04/16)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: I
- Date of initial induction: 2024-04-26
- Date of last report:  2025/03/24
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling, Availability, Collator Protocol


## Reporting period

- Start date: 2024-04-26
- End date: 2025/04/16


## Argument

This letter details my work for the past year and 10 months (since I've started contributing to polkadot full-time),
which are indicative of my promotion to rank II.

My contributions throughout the reporting period are centered around the following large projects:

### Data availability

Data availability recovery is a large CPU consumer for Polkadot validator nodes, due to the expensive reed-solomon erasure coding.
This is one of the limiting factors of scaling up the number of cores Polkadot and Kusama can offer.
I lead the endeavour of optimising this process, via two main avenues:

1. implementing systematic recovery (which effectively brings down the cpu cost of decoding data to 0, by leveraging the nice property that the first n/3 chunks are an exact copy of the initial data). This is a protocol addition.
2. optimising the underlying reed-solomon implementation

These two work streams delivered a combined CPU consumption reduction of ~60% for large PoVs (as measured by my [tests on private testnets](https://github.com/paritytech/polkadot-sdk/pull/1644#issuecomment-2129246105)).

The systematic recovery implementation was a complex multistep process, which solidifed me as one of the domain experts on these subsystems:
- [Refactoring the availability-recovery subsystem to follow a strategy pattern](https://github.com/paritytech/polkadot-sdk/pull/1457), for increased extensibility and adding fail-over mechanisms
- Authoring [RFC47](https://github.com/polkadot-fellows/RFCs/blob/main/text/0047-assignment-of-availability-chunks.md), which proposes a canonical shuffling of chunk indices to ensure fair distribution of network bandwidth usage for availability recovery. This also formalizes the new network protocol and the upgrade path. The RFC was accepted by the fellowship.
- [Adding support for fallback requests to substrate networking](https://github.com/paritytech/polkadot-sdk/pull/2771), required in order to achieve backwards-compatibility between the old and new protocol versions.
- [Adding a NodeFeatures runtime primitive for coordinating enablement of features on validators](https://github.com/paritytech/polkadot-sdk/pull/2177), in order to achieve consensus on when the new canonical chunk index shuffling can be atomically enacted. This primitive later ended up being used by multiple features, like elastic scaling just to name one.
- [Main subsystem implementation](https://github.com/paritytech/polkadot-sdk/pull/1644), which adds the new recovery strategy, together with the new network protocol and comprehensive tests.
- Testing extensively and benchmarking performance on private testnets.
- [I optimised the cumulus recovery procedure to skip re-encoding](https://github.com/paritytech/polkadot-sdk/pull/2287), which was not required for protocol correctness and was consuming valuable CPU time.

The work has been security-audited with no findings logged.

The work on optimising the reed-solomon implementation involved:
- extensive benchmarking agains other implementations (our rust SIMD implementation and kagome's C++ port).
- root-causing and fixing the large CPU consumption difference between the rust and C++ implementations: https://github.com/paritytech/reed-solomon-novelpoly/issues/14#issuecomment-1857666824. This involved diving deep up to assembly code, using different profilers and monitoring hardware performance counters.
- discovering and applying micro-optimisations that improved the performance of the library: https://github.com/paritytech/reed-solomon-novelpoly/pull/34, https://github.com/paritytech/reed-solomon-novelpoly/pull/31, https://github.com/paritytech/reed-solomon-novelpoly/pull/24

### Elastic scaling

I was one of the main developers responsible for implementing elastic scaling (together with fellows @sandreim and @skunert, with whom I closely collaborated and exchanged reviews). This was a complex project that spanned multiple subsystems, crucial to the scaling strategy of Polkadot for parachains like Mythos and Asset hub.

I owned and delivered multiple complex components of the implementation:
- [Runtime implementation on the relay chain](https://github.com/paritytech/polkadot-sdk/pull/3479). This effectively lifts the limitation that a parachain can have only one backed candidate at a time. It brings support for backing candidate chains, increasing throughput.
- Support for candidate chains in the provisioner subsystem: https://github.com/paritytech/polkadot-sdk/pull/3233 and https://github.com/paritytech/polkadot-sdk/pull/3778. Needed so that the relay chain runtime is able to request multiple backable candidates per para from the node.
- Rewriting the prospective-parachains subsystem, a critical component of the backing pipeline. This was needed in order to allow backing candidates out of order, a key aspect of elastic scaling. PRs: https://github.com/paritytech/polkadot-sdk/pull/4035 and https://github.com/paritytech/polkadot-sdk/pull/4937.
- Adding support for elastic scaling to cumulus pov-recovery component: https://github.com/paritytech/polkadot-sdk/pull/4733.
- [Writing a documentation guide for enabling elastic scaling on parachains](https://github.com/paritytech/polkadot-sdk/pull/4663).
- Implementing multiple parts of [RFC103](https://github.com/polkadot-fellows/RFCs/pull/103), which effectively lifts the MVP status of elastic scaling, bringing resilience against one collator distributing the same collation to all backing groups.
    - v2 receipt checks in different subsystems: https://github.com/paritytech/polkadot-sdk/pull/6011, https://github.com/paritytech/polkadot-sdk/pull/5908.
    - support for v2 receipts in cumulus: https://github.com/paritytech/polkadot-sdk/pull/5372, https://github.com/paritytech/polkadot-sdk/pull/5888.
- [Removing support for the scheduling TTL from the coretime assignment pallet](https://github.com/paritytech/polkadot-sdk/pull/5461), which prevented parachains from sharing a core with interlaced assignments.
- [Deprecating AsyncBackingParams](https://github.com/paritytech/polkadot-sdk/pull/7254), which were initially introduced for enabling and configuring async backing. This is one of the main blockers for enabling elastic scaling on Polkadot. The PR also removes and refactors a lot of code which used to handle
the potential of async backing not being enabled, which is no longer possible on production networks. The reason for removing the static params is twofold:
    - they have been made obsolete by the claim queue concept which was introduced for agile coretime.
    - enabling elastic scaling on polkadot would have meant bumping the static max_candidate_depth value to at least 6 to allow for a parachain using 3 cores. This is not ideal, since being a static parameter, it would apply to all parachains regardless of their assigned coretime, leading
    to increased resource usage on validators and less than ideal spam protection.
- Another notable contribution was my involvement in the design discussions around [streamlined block production](https://github.com/paritytech/polkadot-sdk/issues/5190#issuecomment-2505949587)
I researched and proposed an alternative implementation idea which would achieve the desired result in a much shorter time
(thanks to the simpler design, despite it being less efficient). I successfully developed a PoC and tested it with gluttons and spammening parachains.
The code is available here: https://github.com/paritytech/polkadot-sdk/tree/alindima/post-state-poc. We've so far chosen not to follow this route, as the current throughput requirements of parachains don't require such a quick solution.
- Conducting extensive testing on private testnets, adding automated tests.

### Collator protocol revamp

This is an on-going project that I'm leading, which will improve the resilience of backing validators through a persisted reputation system for collators.
I've conducted research on the topic based on [previous issues](https://github.com/paritytech/polkadot-sdk/issues/616) and discussions with other fellows. I've created a document which has been so far privately reviewed by other fellows and will be later turned into an RFC. I have created a development plan for this project, which can be viewed [here](https://github.com/orgs/paritytech/projects/119/views/2).

Implementation is on-going, some of the key components already merged or in the review process:
- [PR](https://github.com/paritytech/polkadot-sdk/pull/7955) which adds and handles a new UMP signal. This is a mechanism for parachain runtimes to assign the merit of building a valid block to a particular network key (PeerId). This is a key attribute of the revamp.
- [Adding a reputation-based peer manager component](https://github.com/paritytech/polkadot-sdk/pull/8191): the component which maintains connections to peers and stores their reputations.

### Other notable contributions

I've done many various refactors, bugfixes and small improvements.
I regularly provide reviews in my areas of expertise and help other developers with technical issues.

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
