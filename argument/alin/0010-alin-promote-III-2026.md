# Argument-0010: Promotion to Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/06/08                                                                                  |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: II
- Date of initial induction: 2024-04-26
- Date of last report: 2026/04/15
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling, Availability, Collator Protocol, Low-Latency


## Reporting period

- Start date: 2024/04/26
- End date: 2026/06/08

## Argument

Since joining the Polkadot Fellowship in April 2024, I have spent two years within the Fellowship (and three years overall as a full-time Polkadot contributor) working across and leading critical areas of the stack, from planning and research, to development, team coordination, testing, deployment and monitoring/debugging.

My main area of expertise is the Polkadot relay chain protocol, node and runtime implementation.
I have led teams, coordinated, delegated and reviewed work for complex protocol components, as well as designed improvements and implemented large components and improvements of the parachains protocol in Polkadot.

Besides my main area of expertise, I also contributed significantly across different areas of the stack, going into substrate node internals, collator implementation and smart contract execution environment and tooling.
I have also supported the overall network functioning by debugging and fixing live issues on several occasions.

My most significant contributions are organised below against the Rank III requirements from Section 6.4 of the Manifesto: autonomous ownership of substantial protocol components from design through deployment, security-conscious and game-theoretic thinking, the ability to make system-level tradeoff decisions, willingness to support what I have built on a live public network, and active engagement with the broader ecosystem.

Please note that I have included only the most significant and complex work I have done over the past three years. 

### Collator protocol revamp

This is the second generation of the collator protocol implementation within Polkadot, the communication interface between collators and validator nodes in the network.

The existing collator protocol had known weaknesses that left the parachain backing process vulnerable to denial-of-service attacks and unreliable under adversarial conditions, issues previously raised and explored by fellow @eskimor ([issue #616](https://github.com/paritytech/polkadot-sdk/issues/616)).

I am the primary author of the formalisation and implementation of the new collator protocol, which is based on the original idea proposed by @eskimor.
I enhanced and formalised the design into a document, that was reviewed and approved by numerous fellows as well as security auditors. The design document remains private for the time being, due to the sensitive nature of the topic, until the protocol is fully enabled on all production networks.

I showcased great security-conscious and game-theoretic thinking, balancing multiple conflicting factors:
- resilience in the face of malicious collators or even malicious random peers on the internet
- performance
- limiting complexity
- not trading off parachain generality (not making unreasonable assumptions on the inner parachain workings and protocols)

The novelty of the solution involved introducing a persistent reputation-based system for collators used for prioritising connections and collation fetches. The design fundamentally hardens the parachain backing pipeline against adversarial behaviour.

In terms of implementation, it involved a complete redesign and rewrite of the subsystem, with modularity, simplicity and security as main goals. Compared to the previous implementation, the code is better architected, separating the two key behaviours of the subsystem: managing peer connections and managing the collations lifecycle.

I authored a large majority of the implementation, showcased by:

1. The necessary `CandidateDescriptor` primitive modifications in [PR #7955](https://github.com/paritytech/polkadot-sdk/pull/7955), introducing a new UMP signal that allows parachains to attribute block-building merit to specific `PeerId`s — the key mechanism enabling collator accountability. A key aspect of this PR was investigating and mitigating the risk of introducing accidental disputes raised by un-upgraded validators.
2. [PR #8191](https://github.com/paritytech/polkadot-sdk/pull/8191) — the reputation-based peer manager, managing peer connections based on historical behaviour.
3. [PR #8541](https://github.com/paritytech/polkadot-sdk/pull/8541) — the `CollationManager` and main subsystem logic, the final substantial component tying together all parts of the new protocol.
4. [PR #8242](https://github.com/paritytech/polkadot-sdk/pull/8242) — a temporary in-memory reputation database to unblock end-to-end testing while the persistent backend was being completed.

I also led and coordinated this project within Parity for the most part, until it was handed over to fellow @tdimitrov (due to reprioritisation). I remain an occasional reviewer and advisor on the project.

The protocol is now approaching mainnet deployment, with a temporary mitigation already deployed for Asset Hub on Polkadot. Final testing is being conducted on private test networks under adversarial scenarios.
The code has been released but is still gated by a CLI flag, until testing concludes.

This project satisfies the formal rank III requirement from the manifesto:

I played a supporting role in the ideation (the original idea is @eskimor's) and **the primary role in both** the formalisation and the implementation of the component. Each PR went through expert code-review, and the protocol is a functional implementation being readied for production.

Most importantly, the entire revamp is a direct expression of the security mindset the Manifesto places at the heart of the rank: the individual *"should by now be thinking ... in a very much ... security-conscious, game-theoretic way, understanding that the systems whose design they are increasingly a part of must function adequately even with a modest minority of malicious users."* The protocol exists precisely to keep parachain backing live against adversarial collators and arbitrary malicious internet peers, while balancing performance, complexity, and parachain generality.

### Elastic scaling

Elastic scaling allows parachains to occupy more than one core at a time, to scale up or down according to demand. I was one of the core engineers driving this effort alongside @sandreim and @skunert, contributing deep work across the runtime, node subsystems, and Cumulus.

On the relay chain, I authored the majority of the code for the elastic scaling MVP:

- [PR #3479](https://github.com/paritytech/polkadot-sdk/pull/3479) — the runtime changes necessary to support multiple backed candidates per parachain. This PR lifts the longstanding assumption of 1 para-1 core that was baked in the runtime.
- [PR #3233](https://github.com/paritytech/polkadot-sdk/pull/3233) and [PR #3778](https://github.com/paritytech/polkadot-sdk/pull/3778) — provisioner subsystem support for multiple candidates per para.
- [PR #4035](https://github.com/paritytech/polkadot-sdk/pull/4035) and [PR #4937](https://github.com/paritytech/polkadot-sdk/pull/4937) — a rewrite of the prospective-parachains subsystem to support out-of-order backing, a complex endeavour I owned and that removed a critical bottleneck. This rewrite enabled truly parallel execution of linked candidates across different backing groups, achieving elastic scaling's true parallelisation potential.

On the Cumulus side, I authored [PR #4733](https://github.com/paritytech/polkadot-sdk/pull/4733) (PoV recovery support) and a [comprehensive guide for parachain teams enabling elastic scaling](https://paritytech.github.io/polkadot-sdk/master/polkadot_sdk_docs/guides/enable_elastic_scaling_mvp/index.html).

Getting elastic scaling from MVP to production required two additional threads. I owned the RFC103 Cumulus-side implementation in [PR #5372](https://github.com/paritytech/polkadot-sdk/pull/5372) and [PR #5888](https://github.com/paritytech/polkadot-sdk/pull/5888), and authored the node-side support in [PR #5908](https://github.com/paritytech/polkadot-sdk/pull/5908) (v2 receipts on collation generation) and [PR #6011](https://github.com/paritytech/polkadot-sdk/pull/6011) (receipt version validation when fetching collations). I also authored [PR #7254](https://github.com/paritytech/polkadot-sdk/pull/7254) to deprecate `AsyncBackingParams` and [PR #5461](https://github.com/paritytech/polkadot-sdk/pull/5461) to remove scheduling TTL, enabling dynamic resource allocation and reducing validator overhead.

Elastic scaling is now deployed to production on Polkadot and Kusama and actively being used by parachains (such as Asset Hub, People chain), enabling higher throughput and lower latency, showcasing the truly scalable nature of the polkadot network.

To summarise, I played a supporting role in the ideation phase and one of the primary roles in the implementation of the relay chain side of the MVP.

### Optimizing data availability

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
roadmap for protocol upgrade and deployment. The Fellowship accepted this RFC through governance voting.

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

I played the primary role in the ideation and implementation of the availability recovery improvements,
which culminated with the rearchitecture of the subsystem.

### Low latency

My most recent focus has been on achieving low-latency block confidence for parachains, based on a [design proposed by @eskimor](https://github.com/paritytech/polkadot-sdk/pull/11413).
I have been a contributor to the project and am now leading the team working on low-latency within Parity.

The core novelty of the design is decoupling the relay parent (execution context) from the scheduling parent (backing context) via v3 candidate descriptors.

I owned and implemented the relay chain support for allowing older relay parents (that can even be multiple sessions old).
Work is captured in the following PRs: [PR #11231](https://github.com/paritytech/polkadot-sdk/pull/11231), which adds a runtime API and configuration item for the max session age, [PR #11328](https://github.com/paritytech/polkadot-sdk/pull/11328) which implements full runtime support for allowing older relay parents as well as the prospective-parachains support, added in [PR #11772](https://github.com/paritytech/polkadot-sdk/pull/11772).

On the research side, I authored two design proposals for cross-session continuity: [cross-session availability](https://hackmd.io/NKUWBZC7Q8ipvg1FYibRzQ) and [cross-session backing](https://hackmd.io/IIpnCvYXRtOhmcz-8luNhg), reviewed within the low-latency working group. While we ultimately converged on resubmissions as the preferred solution, the research informed key planning and prioritisation decisions for the block-confidence roadmap, exemplifying the Rank III qualifier of *making system-level tradeoff decisions* and *comprehensive knowledge of overall priorities and tradeoffs*.

### Operational availability and live incident response

> *They should be able and willing to support that which they built given that it is running 24/7 on a public network.* (Manifesto §6.4)

On 2026-03-23, immediately following the 2.1.1 runtime upgrade, 5 of 37 active parachains stalled block production. I led the full incident response: investigation, root-cause analysis, coordination with affected parachain teams, and the [public postmortem](https://forum.polkadot.network/t/partial-polkadot-parachains-stall-on-runtime-upgrade-2-1-1-postmortem/17387). Root cause was a SCALE codec compatibility violation in the deprecated `backing_state` runtime API (was identified in ~2.5 hours, and recovery was underway within 7 hours).

This is part of a broader pattern of supporting the production systems I have authored or own.

### Ecosystem engagement and knowledge sharing

Authored several long-form semi-technical articles (either for public or private review):

- [RFC47: Assignment of availability chunks](https://github.com/polkadot-fellows/RFCs/blob/main/text/0047-assignment-of-availability-chunks.md) — accepted by the Fellowship.
- [Elastic scaling enablement guide](https://github.com/paritytech/polkadot-sdk/pull/4663) — documentation for parachain teams.
- [2.1.1 runtime upgrade postmortem](https://forum.polkadot.network/t/partial-polkadot-parachains-stall-on-runtime-upgrade-2-1-1-postmortem/17387)
- Collator protocol revamp design (still private for security reasons, will be published soon).

I also participated in several OpenDev calls, presenting on elastic scaling progress, collator protocol design, and low-latency work.
I have led teams comprised of engineers within and outside Parity, showcasing good knowledge sharing and mentorship capabilities. In particular, I led a cross-organizational team of six engineers (four from Parity, two from Chainsafe) for the anvil-polkadot project (see below).

I also provided support to ecosystem teams looking to experiment with elastic scaling (for example Peaq).

I am also an [active reviewer](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aalindima) across polkadot-sdk on my areas of expertise.

### Other contributions

#### Anvil-polkadot
For the second half of 2025, I led a cross-organizational team of six engineers (four from Parity, two from Chainsafe) to deliver [anvil-polkadot](https://github.com/paritytech/foundry-polkadot/tree/master/crates/anvil-polkadot), an EVM-compatible test node critical for the launch of smart contracts on Polkadot Hub. I authored the [design and development plan (issue #209)](https://github.com/paritytech/foundry-polkadot/issues/209), wrote the [initial prototype (PR #220)](https://github.com/paritytech/foundry-polkadot/pull/220) and the [arbitrary state injection feature (PR #296)](https://github.com/paritytech/foundry-polkadot/pull/296), and contributed fixes to [pallet-revive (PR #10175)](https://github.com/paritytech/polkadot-sdk/pull/10175) and [pallet-revive EIP-3607 bypass (PR #10387)](https://github.com/paritytech/polkadot-sdk/pull/10387). The project is now in maintenance mode, having completed the features critical for launch. This project enables a seamless onboarding experience for EVM developers onto Polkadot's revive smart contracts, by offering them a familiar test tooling experience and lowering the barriers to entry.

#### Streamlined block production — design and prototype

I participated in the design of [streamlined block production](https://github.com/paritytech/polkadot-sdk/issues/5190#issuecomment-2505949587), proposing a simplified post-state-based approach that would achieve the same result as transaction-streaming on a much shorter timeline (at the cost of being less efficient than the long-term design). I developed a [working proof of concept](https://github.com/paritytech/polkadot-sdk/tree/alindima/post-state-poc) and tested it with gluttons and spammening parachains. While the production need for this implementation has not yet materialised, the groundwork remains valuable for future scaling needs and demonstrates the kind of independent ideation and prototyping the Rank III bar expects — *occasionally innovative in API & code design, adapting/importing/inventing ideas that lead to effective solutions* (Manifesto §4.5.1, Level 3).

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II  |80%   |N/A   | N/A | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e. 100% voting activity) — there were no referenda on the Members or Proficient Members tracks during this period |
|III|70%   |100%  |   | Seeking promotion to this rank. |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
