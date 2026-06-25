# Argument-0007: Promotion to Rank III (Fellow)

|                  |                                              |
| ---------------- | -------------------------------------------- |
| **Report Date**  | 2026/06/24                                   |
| **Submitted by** | Alexandru Vasile                             |


## Member details

- Matrix username: @lexnv:parity.io
- Polkadot address: 14Mjra9hNggCSLyVv3AmtvpjeyBhUMwiEEBXGFidu3ZWTEQN
- Current rank: I
- Date of initial induction: 2025/02/12
- Date of last report: 2026/05/06
- Area(s) of Expertise/Interest: `Substrate Networking`, `Substrate Node`, `Substrate RPC`, `FRAME`


## Reporting period

- Start date: 2025/02/12
- End date: 2026/06/23


## Argument

I have been a member of the Fellowship since February 2025 and have been working on Polkadot
core development continuously since January 2022. My primary area of expertise is the Polkadot
p2p networking stack and the node implementation, where I have designed, implemented and
now maintain core components needed by the relay chain to operate.

This is a request for an accelerated promotion to **Rank III**. While I have served around 16 months at Rank I,
I have contributed to the ecosystem for four contiguous years, being primarily responsible for Polkadot's core litep2p
networking stack, RPC-V2 specification, chain Metadata v15&16, the `revive` block builder. In the following
sections I have included my most complex and significant work as evidence.

Besides my primary area of expertise, I have contributed significantly to multiple layers of our stack,
spanning into substrate node, chain synchronization, grandpa fixes, collator protocol, the `revive` block builder,
and user facing tooling (including subxt, jsonrpsee and [subp2p-explorer](https://github.com/lexnv/subp2p-explorer)).

### Litep2p: Leading a major protocol component to production

I led the productivization and the gradual rollout of [litep2p](https://github.com/paritytech/litep2p), a high-performance
networking crate design to replace **libp2p**. Operating on a flat architectural model where data is routed to the
components that need it, litep2p acts as a highly resource efficient upgrade for the ecosystem. The project
touched the entire networking stack of polkadot nodes: implementing transport layers (TCP, WebSocket),
multiplexing the connections into substreams, reimplementing fully compatible Polkadot protocols (Kademlia, Identify, Ping),
and exposing robust API notifications.

I drove the project from a proof-of-concept to a production-ready solution, initiating and tracking progress via the robustness
milestone ([litep2p#140](https://github.com/paritytech/litep2p/issues/140)). I rearchitected, modularized, and refactored several
core components to balance performance with network resilience:

* **Transport Manager Modularization & Connection Handling:** I redesigned the main state transition for dialing peer management,
 resolving multiple inconsistencies and race conditions ([#251](https://github.com/paritytech/litep2p/pull/251)).
 I introduced the ability to accept or reject inbound connections before protocol negotiation ([#186](https://github.com/paritytech/litep2p/issues/186)),
 prevented invalid secondary connections ([#176](https://github.com/paritytech/litep2p/pull/176)), and resolved double-lock
 overwrites on disconnected peers ([#179](https://github.com/paritytech/litep2p/pull/179)).

* **Reputation-Based Address Store:** I reworked the address store to expand dial candidate tracking ([#180](https://github.com/paritytech/litep2p/issues/180)).
 I implemented a reputation-based tracking and eviction algorithm that prioritizes publicly reachable addresses,
 resulting in a significantly healthier DHT over time ([#250](https://github.com/paritytech/litep2p/pull/250)).

* **Kademlia DHT Optimization:** I refactored the `FindNode` and `GetRecord` Kademlia queries to improve correctness by
 strictly tracking the best *K* results ([#114](https://github.com/paritytech/litep2p/issues/114), [#97](https://github.com/paritytech/litep2p/issues/97)).
 I also implemented partial result returns to accelerate authority discovery within Substrate ([#315](https://github.com/paritytech/litep2p/pull/315)).

* **Eliminating Panics and Memory Leaks:** I eliminated critical memory leaks threatening validator stability, specifically
 targeting pending substreams in request-response and notification protocols ([#297](https://github.com/paritytech/litep2p/pull/297),
 [#296](https://github.com/paritytech/litep2p/pull/296)), cancel-path leaks across TCP/WebSocket/QUIC ([#272](https://github.com/paritytech/litep2p/pull/272)),
 and aborted dial attempts ([#255](https://github.com/paritytech/litep2p/pull/255)). I also removed crash-inducing panics on missing peer states
 ([#143](https://github.com/paritytech/litep2p/pull/143)) and mid-substream connection closures ([#291](https://github.com/paritytech/litep2p/pull/291)).

* **Cryptographic Peer Integrity:** I hardened the stack against identity spoofing by extending the Noise handshake to cryptographically
 verify remote peer signature payloads ([#278](https://github.com/paritytech/litep2p/pull/278)).

Following the [stabilization announcement](https://forum.polkadot.network/t/announcing-the-stabilization-of-the-litep2p-network-backend/13712),
litep2p became the default network backend in the Polkadot SDK release 2503-7 ([PR #8461](https://github.com/paritytech/polkadot-sdk/pull/8461)).

The project was rigorously tested as part of the gradual rollout and vetted by security reviewers, resulting in a highly stable release.
Since becoming the default, it has operated seamlessly with no exposed vulnerabilities or major issues.

Key performance optimizations achieved include: **~40-50% reduction in CPU usage** for validators compared to libp2p;
**5x faster authority discovery**, reducing the time to find 1,000 authority records from ~10 minutes to ~2 minutes.
**35% faster chain sync times** to the tip of the chain; and **~24% higher throughput** for request-response protocols.

This body of work directly fulfills the requirement established in Section 6.4.1: taking a
*primary role in the implementation of a major protocol component ... subject to expert code-review
and included in a functional implementation of the protocol*. The component is actively running 24/7 on all Substrate chains (Polkadot, Kusama, relay, and parachains).
While the underlying flat architecture provided the foundation, my work to rearchitect, modularize, and secure the core components turned the PoC into
a performant reality. This component decomposition and robust state management represent an *innovative API & code design ... that lead to effective solutions*
which the Manifesto places at Level 3 under Section 4.5.1.

### Elastic Scaling & Async Backing Rollout on Asset Hub

Reusing the rollout procedure established for the litep2p project, I led the enablement and rollout of async backing
and elastic scaling on Asset Hub. While async backing successfully targets 6s parachain blocks, elastic scaling
pushes the system further to **~2s blocks on 3 cores, and ~600ms on 12 cores**. The overarching effort is scoped in
[polkadot-sdk#10425](https://github.com/paritytech/polkadot-sdk/issues/10425).

I authored the Kusama Asset Hub rollout checklist ([polkadot-sdk#10637](https://github.com/paritytech/polkadot-sdk/issues/10637)) and published the
detailed post-launch write-up on the [Polkadot Forum](https://forum.polkadot.network/t/elastic-scaling-rollout-asset-hub-kusama-asset-hub-polkadot/16133).

As block times shrink, collators require sufficient headroom to propagate a block before its slot ends. To address this, I authored
[PR #10154](https://github.com/paritytech/polkadot-sdk/pull/10154), which reduces the authoring duration of the last block produced in a slot.
This created the crucial propagation window required to maintain stability under elastic scaling conditions.

**Networking Stack Hardening**

After enabling elastic scaling, I dedicated a significant amount of time to stabilizing parachain **block confidence**.
To reproduce and isolate these instabilities, I deployed a dedicated test parachain (YAP) across Versi, Westend, Paseo, Kusama, and Polkadot.
My root-cause analysis ([polkadot-sdk#11377](https://github.com/paritytech/polkadot-sdk/issues/11377)) identified several bottlenecks, which
led to multiple improvements and optimizations across the collator protocol and networking stack.

* **Connection Stability & Dialing Robustness:** I bounded dial concurrency and total dialing time to make connections more resilient
 ([PR #538](https://github.com/paritytech/litep2p/pull/538)), optimized substream opening for `SetReservedPeers` to reduce dialing delays
 ([PR #10362](https://github.com/paritytech/polkadot-sdk/pull/10362)), fixed premature connection terminations on fragmented reads
 ([#489](https://github.com/paritytech/litep2p/issues/489)), and corrected bandwidth metering that was over-reporting usage ([#490](https://github.com/paritytech/litep2p/issues/490)).

* **Address Store Health:** I improved network routing by preventing localhost addresses from polluting the store ([PR #480](https://github.com/paritytech/litep2p/pull/480)),
 prioritizing public addresses for dialing ([#527](https://github.com/paritytech/litep2p/issues/527)), and leveraging successful connections to report failed addresses back
 for a healthier store ([#526](https://github.com/paritytech/litep2p/issues/526)). Additionally, I fixed DHT bugs where authority-discovery records lacked ports
 ([#10466](https://github.com/paritytech/polkadot-sdk/issues/10466)), corrected address-score updates on `PeerIdMismatch` errors ([#492](https://github.com/paritytech/litep2p/issues/492)),
 and resolved prefix string bugs for reserved peers ([PR #11078](https://github.com/paritytech/polkadot-sdk/pull/11078)).

* **Collation Protocol:** To maintain accurate network state, I ensured collations are automatically re-advertised whenever a peer's authority IDs change
 ([PR #10891](https://github.com/paritytech/polkadot-sdk/pull/10891)) and optimized memory by aggressively removing stale pending collations from the waiting queue
 ([PR #10906](https://github.com/paritytech/polkadot-sdk/pull/10906)).

During this process, I also built observability tools to enhance our debugging capabilities, mainly to observe validators behind NAT which caused
collations to drop due to a lack of connectivity on the p2p layer ([validators-monitoring](https://github.com/lexnv/validators-monitorig)) and
block confidence monitoring tools for faster incident response by analyzing substrate logs ([block-confidence-monitor](https://github.com/lexnv/block-confidence-monitor)).

Owning the rollout end-to-end, weighing block time against block confidence and coordinating a deployment across testnets, Kusama and
Polkadot reflects the *comprehensive knowledge of the overall priorities and tradeoffs in the development and design of a global, decentralised and
unstoppable network* the Manifesto Section 6.4 expects of a Fellow and the willingness to support the live public network.

### RPC Spec V2

I contributed to the RPC-v2 specification, a new class of fully scoped and documented RPC methods that aligns the
ecosystem on a concrete set of methods with strong guarantees, improving developer experience, API robustness and reliability,
and bringing Polkadot full nodes into alignment with light clients. I act as a reviewer and gatekeeper across all RPC-v2 methods,
and was the primary designer of the **`archive` methods** while also contributing to the `chainHead` and `transaction` API designs.

The archive API exposes historical chain state to indexers and analysis tools. As described in the
[RPC-V2 forum post](https://forum.polkadot.network/t/archive-rpc-v2-methods/11121), I designed `archive_storageDiff`
(a subscription reporting storage additions/removals/modifications between two blocks, with prefix filtering and child-trie support)
and `archive_storage` (storage snapshots with value/hash retrieval, prefix iteration and merkle-value queries).

Designing a clean, fully-specified API and acting as its gatekeeper is the *innovative API & code design ... that lead to effective solutions*
the Manifesto expects at Section 4.5.1, and demonstrates the ability to *effectively review output and make insightful suggestions* on the
work of peers of the same or higher rank.

### Metadata V15 and V16

For **Metadata V15** ([#12939](https://github.com/paritytech/substrate/issues/12939)), my most
significant contribution was embedding runtime-API type information into the metadata, so tools (subxt / PAPI) can generate
strongly-typed runtime-API clients and move off ad-hoc `state_call` usage toward `chainHead`-based calls.

I then led Metadata V16 ([polkadot-sdk#4520](https://github.com/paritytech/polkadot-sdk/issues/4520)) to remove hard-coded
per-chain configuration, introducing deprecation information, a new transaction-extension type, and
associated types for runtime-configuration traits, staged behind unstable versioning (`u32::MAX`)
before stabilisation ([PR #5732](https://github.com/paritytech/polkadot-sdk/pull/5732)) and coordinated with the Subxt team. Progress is documented on the Forum in
[Upcoming Metadata V16](https://forum.polkadot.network/t/upcoming-metadata-v16-features-to-include-in-v16/8153)
and [Metadata V16 updates](https://forum.polkadot.network/t/metadata-v16-updates/9557). This is a
clear instance of *primary responsibility for the formalisation of a protocol component* whose
longevity is visible in its ecosystem-wide adoption.

### Operational availability and ownership

The Manifesto requires that a Fellow be *"able and willing to support that which they built given that
it is running 24/7 on a public network."*
After the litep2p stabilization I remained the main owner of the project, watching for production
incidents and continuing to harden the project.

**Live debugging across the stack:** Beyond litep2p, I have investigated and fixed a range of
production issues: collators persistently stuck in the "Block history" state
([#8416](https://github.com/paritytech/polkadot-sdk/issues/8416)); a hot path where litep2p lagged
behind libp2p ([#7183](https://github.com/paritytech/polkadot-sdk/issues/7183)); and `chainHead`
RPC correctness — `newBlock` events emitting unannounced parent hashes
([#5761](https://github.com/paritytech/polkadot-sdk/issues/5761)) and out-of-order JSON-RPC delivery
([#5512](https://github.com/paritytech/polkadot-sdk/issues/5512)). I also hardened the node against
failure modes that only surface at scale: running the network backend as an essential task so a
backend failure can no longer be silently swallowed
([PR #10847](https://github.com/paritytech/polkadot-sdk/pull/10847)), closing missing body gaps for
non-archive nodes ([PR #11332](https://github.com/paritytech/polkadot-sdk/pull/11332)), and skipping
block execution when collators have no parent-block state
([PR #11330](https://github.com/paritytech/polkadot-sdk/pull/11330)).

**Observability for live operators:** I have systematically added the metrics operators need to
diagnose the network from dashboards rather than logs: inbound/outbound network traffic
([PR #10846](https://github.com/paritytech/polkadot-sdk/pull/10846)), peerset notification-layer
metrics for per-peer connection states
([PR #11574](https://github.com/paritytech/polkadot-sdk/pull/11574)), collation-fetch latency metrics
that closed a visibility blindspot
([PR #11600](https://github.com/paritytech/polkadot-sdk/pull/11600)) together with the para-id of
collations that fail to fetch ([PR #11629](https://github.com/paritytech/polkadot-sdk/pull/11629)),
and RPC-v2 `transactionWatch_v1_submitAndWatch` counters and latency histograms across transaction
state transitions that surface `inblock/retracted` oscillations
([PR #8345](https://github.com/paritytech/polkadot-sdk/pull/8345)).

**Supporting contributors and ongoing maintenance:** I offer review and guidance in my area of
expertise to external contributors extending the API. For example, I've provided feedback to `archive_v1_storage`
pagination addition into Substrate ([#10185](https://github.com/paritytech/polkadot-sdk/issues/10185)).
I also keep production on a vetted networking stack by bringing litep2p releases into the SDK, most
recently the bumps to v0.14.3 ([PR #12432](https://github.com/paritytech/polkadot-sdk/pull/12432)),
v0.14.0 ([PR #12049](https://github.com/paritytech/polkadot-sdk/pull/12049)),
v0.13.3 ([PR #11316](https://github.com/paritytech/polkadot-sdk/pull/11316)) and more.

Sustaining this ownership long after release and triaging production incidents are part of the
*commitment to availability even when it may be inconvenient* that the Manifesto Section 6.4 asks of a Fellow.

### Mentoring, reviews and knowledge sharing

For knowledge sharing within the ecosystem (section 6.4.1), I have written multiple Forum posts (see
[Publications](#publications)), presented litep2p and the RPC-v2 spec at team retreats, and onboarded
new joiners to the networking stack.

I have mentored and reviewed across several projects, most recently **WebRTC** in my networking area
of expertise, scoped in [litep2p milestone #4](https://github.com/paritytech/litep2p/milestone/4)
(WebRTC as a lightweight light-client transport alongside WebSocket, with smoldot compatibility,
backpressure, panic-hardening and metrics).

The project began with my review support for the ChainSafe team (up to three full-time developers)
and then migrated in-house, where my teammate Gabriele is tackling the low-level implementation.
My own contributions include memory-leak fixes and a long-running stress-testing harness on the WebRTC
substream layer ([litep2p-perf PR #4](https://github.com/lexnv/litep2p-perf/pull/4)): a Go (`libp2p-go`)
interoperability client that drives bidirectional throughput tests and acts as a spec-compliance
check, which uncovered and drove fixes for SCTP message fragmentation across packets, ICE/substream
shutdown handling and producer backpressure.

I also led the design and implementation of the **`revive` Ethereum block-storage** initiative ([PR #9418](https://github.com/paritytech/polkadot-sdk/pull/9418)),
a core dependency for the company-wide Ethereum-compatible smart-contract effort. By incrementally building the trie in memory through low-level APIs
([PR #9554](https://github.com/paritytech/polkadot-sdk/pull/9554)) I reduced pallet storage usage by roughly **90%**, and provided guidance and
review for Lukasz's work on the associated RPC layer ([PR #9512](https://github.com/paritytech/polkadot-sdk/pull/9512)) and benchmarks.

Mentoring cross-organisation teams, onboarding new joiners and independently delivering a component like the `revive` block builder
together meet the Manifesto's *demonstrable presence of knowledge sharing within the ecosystem* (Section 6.4.1).

### Security-conscious and game-theoretic thinking

The Manifesto requires that, by this rank, the individual is *"thinking ... very much in a security-conscious, game-theoretic way, understanding
that the systems whose design they are increasingly a part of must function adequately even with a modest minority of malicious users"*. The
networking work above is shaped end-to-end by this.

Litep2p's connection limits, per-layer resource bounding, reputation-based address store, and Noise
peer-integrity checks exist specifically to keep the network live against adversarial peers
and to shrink the attack surface for **DoS and eclipse** attacks, while delivering a more performant backend.

The elastic-scaling block-confidence investigation is fundamentally reasoning about how the system behaves under
partial connectivity, re-orgs, and adversarial and failure conditions — not only the happy path.

### Publications

The following long-form, semi-technical Forum articles satisfy the sections 6.4.1 requirement for advocacy
and knowledge sharing:

- [Litep2p Network Backend updates](https://forum.polkadot.network/t/litep2p-network-backend-updates/9973)
- [Announcing the stabilization of the Litep2p Network Backend](https://forum.polkadot.network/t/announcing-the-stabilization-of-the-litep2p-network-backend/13712)
- [Elastic Scaling Rollout: Asset Hub Kusama / Asset Hub Polkadot](https://forum.polkadot.network/t/elastic-scaling-rollout-asset-hub-kusama-asset-hub-polkadot/16133)
- [Archive RPC-V2 Methods](https://forum.polkadot.network/t/archive-rpc-v2-methods/11121)
- [Upcoming Metadata V16](https://forum.polkadot.network/t/upcoming-metadata-v16-features-to-include-in-v16/8153)
- [Metadata V16 updates](https://forum.polkadot.network/t/metadata-v16-updates/9557)

### Considerations regarding my argument

I have contributed to core Polkadot protocols and components for more than four years and joined the
Fellowship comparatively late relative to that work, which is why I am requesting an accelerated
promotion to Rank III. As a Fellow I wish to extend my responsibilities as a core protocol owner of
the Polkadot networking stack and to continue offering support and expertise to the ecosystem. I hope
the evidence presented stands well alongside that of fellow members.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e. 100% voting activity). | No referenda were open to my rank during the period. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
