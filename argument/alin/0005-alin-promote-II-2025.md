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

Since joining the Polkadot Fellowship on April 26, 2024, I’ve spent the past year—and nearly two years overall as a
full-time contributor—working deeply across critical areas of the Polkadot stack.
My focus spans parachain consensus, elastic scaling, availability, and the collator protocol.
The contributions I’ve made during this time reflect a high level of technical
competency, autonomy, leadership and commitment, which I believe justifies my promotion from Rank I to Rank II.

My most notable contributions are centered around the following large protocol-level enhancements:

### Optimizing Data Availability

Data availability recovery has long been a bottleneck for Polkadot validator nodes, due in large part to the computational cost of Reed-Solomon erasure coding.
Recognizing this as a core obstacle to scaling the number of parachain cores on Polkadot and Kusama, I led the initiative to optimize this subsystem both at the protocol and implementation level.

The most significant improvement came through implementing [systematic 
recovery](https://github.com/paritytech/polkadot-sdk/pull/1644), a protocol upgrade that eliminates 
the decoding overhead in most cases by leveraging the property that the first third of the encoded 
chunks are unaltered copies of the original data. In tandem with this, I also optimized the 
underlying Reed-Solomon implementation itself, resulting in a combined reduction of approximately 
**60% in CPU usage** for large PoVs, validated by [benchmarks on private 
testnets](https://github.com/paritytech/polkadot-sdk/pull/1644#issuecomment-2129246105).

To enable these changes, I undertook several foundational updates. First, I [refactored the 
availability-recovery subsystem](https://github.com/paritytech/polkadot-sdk/pull/1457) to follow a 
strategy pattern, improving extensibility and allowing graceful failovers. I authored 
[RFC47](https://github.com/polkadot-fellows/RFCs/blob/main/text/0047-assignment-of-availability-chunks.md),
which introduced a canonical shuffling of chunk indices to balance bandwidth usage and provided a 
roadmap for protocol upgrade and deployment. The Fellowship accepted this RFC.

Ensuring compatibility between protocol versions, I [added fallback support to Substrate 
networking](https://github.com/paritytech/polkadot-sdk/pull/2771) and implemented a 
[NodeFeatures runtime primitive](https://github.com/paritytech/polkadot-sdk/pull/2177) to coordinate 
feature enablement across validators. This primitive has since been adopted by other key subsystems, 
such as elastic scaling.

The systematic recovery strategy and new protocol were delivered via the [main subsystem 
implementation](https://github.com/paritytech/polkadot-sdk/pull/1644), with extensive integration 
tests. Additionally, I [optimized the Cumulus recovery 
procedure](https://github.com/paritytech/polkadot-sdk/pull/2287) to avoid unnecessary re-encoding, 
further reducing CPU consumption.

In parallel, I investigated the performance disparity between our Rust implementation of 
Reed-Solomon and Kagome’s C++ version. After deep profiling—including analysis at the assembly 
level—I identified key inefficiencies and proposed solutions ([analysis 
here](https://github.com/paritytech/reed-solomon-novelpoly/issues/14#issuecomment-1857666824)). This 
led to a series of [micro-optimizations](https://github.com/paritytech/reed-solomon-novelpoly/pull/34),
[performance fixes](https://github.com/paritytech/reed-solomon-novelpoly/pull/31), and [code 
improvements](https://github.com/paritytech/reed-solomon-novelpoly/pull/24) that significantly 
improved the performance of the Rust implementation.

All of this work has been successfully audited, with no security findings logged.

### Implementing Elastic Scaling

Elastic scaling is one of Polkadot’s most ambitious recent upgrades, allowing parachains to scale 
up by occupying more than one core. I was one of the core engineers driving this effort, 
collaborating closely with @sandreim and @skunert. My role involved deep work across the runtime, 
and different node subsystems.
This was a complex protocol-level project which is crucial for the scaling strategy of parachains
like Mythos and Asset hub.

On the relay chain, I implemented the [runtime 
changes](https://github.com/paritytech/polkadot-sdk/pull/3479) necessary to support multiple backed 
candidates per parachain. This lifted a core limitation and enabled parallel backing. I extended 
these capabilities to the provisioner subsystem via 
[PR 3233](https://github.com/paritytech/polkadot-sdk/pull/3233) and 
[PR 3778](https://github.com/paritytech/polkadot-sdk/pull/3778), enabling nodes to handle multiple 
candidates per para.

To support out-of-order backing, I rewrote the prospective-parachains subsystem, 
which was a critical bottleneck. This was a very complex endeavour that I owned.
The resulting updates are captured in 
[PR 4035](https://github.com/paritytech/polkadot-sdk/pull/4035) and 
[PR 4937](https://github.com/paritytech/polkadot-sdk/pull/4937).

Elastic scaling also required updates to Cumulus, including support in the PoV recovery component, 
which I delivered in [PR 4733](https://github.com/paritytech/polkadot-sdk/pull/4733). To support 
adoption, I authored a [comprehensive documentation 
guide](https://github.com/paritytech/polkadot-sdk/pull/4663) for parachain teams.

Getting the elastic scaling feature from the MVP to the production status involved two threads of work: RFC103 and
deprecating AsyncBackingParams.

[RFC103](https://github.com/polkadot-fellows/RFCs/pull/103) addresses a potential vulnerability 
where a collator could distribute the same collation to all backing groups. I contributed
numerous times to the node-side implementation (https://github.com/paritytech/polkadot-sdk/pull/6011, https://github.com/paritytech/polkadot-sdk/pull/5908)
and owned the Cumulus-side support: https://github.com/paritytech/polkadot-sdk/pull/5372, https://github.com/paritytech/polkadot-sdk/pull/5888.

To enable dynamic resource allocation, I [removed support for scheduling 
TTL](https://github.com/paritytech/polkadot-sdk/pull/5461) from the coretime assignment pallet and 
[deprecated `AsyncBackingParams`](https://github.com/paritytech/polkadot-sdk/pull/7254), which had 
become obsolete with the introduction of the claim queue concept. Removing these static parameters 
reduced validator overhead and improved spam resistance.

In parallel, I participated in the design of [streamlined block 
production](https://github.com/paritytech/polkadot-sdk/issues/5190#issuecomment-2505949587), proposing 
a simplified post-state-based approach. I developed a [proof of 
concept](https://github.com/paritytech/polkadot-sdk/tree/alindima/post-state-poc) and tested it using 
gluttons and spammening parachains. While the need for this implementation hasn’t yet materialized, 
the groundwork remains valuable for future scaling needs and showcases my ability to innovate and meaningfully
contribute to areas outside of my previous expertise.

The remaining work needed for the elastic scaling production launch is tracked [here](https://github.com/paritytech/polkadot-sdk/issues/5051).

### Collator protocol revamp

In an effort to enhance the reliability of the parachain backing process, I started leading a 
comprehensive revamp of the collator protocol, introducing a persistent reputation system for collators.
This project builds on previous issues raised in the 
ecosystem ([reference](https://github.com/paritytech/polkadot-sdk/issues/616)) and collaborative 
discussions with other fellows.

I created a detailed proposal, currently under private review (which will soon make it to an RFC),
and outlined the development process (which I'm managing) in 
an open [project plan](https://github.com/orgs/paritytech/projects/119/views/2).

Early implementation work has already been merged or is in review. This includes a [new UMP 
signal](https://github.com/paritytech/polkadot-sdk/pull/7955) that allows parachains to attribute 
block-building merit to specific `PeerId`s—a key mechanism for enabling collator accountability. 
Additionally, I authored the [reputation-based peer 
manager](https://github.com/paritytech/polkadot-sdk/pull/8191), which will manage peer connections 
based on historical behavior.

### Other notable contributions

Beyond these major initiatives, I’ve continued to contribute across the codebase with bug fixes, 
refactors, and performance enhancements. I actively review work in the areas of availability, 
consensus, and collator protocol, and regularly provide technical support to other contributors.

### Reference of published write-ups

- [RFC47](https://github.com/polkadot-fellows/RFCs/blob/main/text/0047-assignment-of-availability-chunks.md)
- [Elastic Scaling update guide](https://paritytech.github.io/polkadot-sdk/master/polkadot_sdk_docs/guides/enable_elastic_scaling_mvp/index.html)

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
