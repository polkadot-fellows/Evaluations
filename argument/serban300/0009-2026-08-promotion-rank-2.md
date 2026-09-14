# Argument-0009: Promotion to Rank II

|                 |              |
| --------------- |--------------|
| **Report Date** | 2026/08/20   |
| **Submitted by**| Serban Iorga |


## Member details

- Matrix username: `@serban.iorga:parity.io`
- Polkadot address: `14oHMAJ5btnDCusHrTWraw1wTsLJwZeqPDLxusm1R1Zh3Vxa`
- Current rank: `1`
- Date of initial induction: `2024/04/22`
- Date of last report: `2026/06/30`
- Link to last report: https://github.com/polkadot-fellows/Evaluations/pull/317
- Area(s) of Expertise/Interest:
    - `Bridges`
    - `BEEFY`
    - `MMR`
    - `XCMP/HRMP/DMP`
    - `Omni-Node`
    - `Cumulus Node`
    - `Parachain Authoring`


## Reporting period

- Start date: `2025/03/28`
- End date: `2026/08/20`


## Argument

I have been contributing to Polkadot full-time since June 2022 and have held Rank I for the most part of the time since 
April 2024. The exception is the period 2024/10/03 - 2025/03/28, during which I failed to submit a retention argument 
and consequently lost the rank; I argued for it again in March 2025 and have held it continuously since.

Below are the projects I consider worth putting forward:

### Message passing: XCMP/HRMP

A parachain could enqueue only around 300 inbound messages per block, which put a hard ceiling on how much
cross-consensus traffic it could accept. I identified that the constraint was not bandwidth, as had been
assumed, but the accuracy of the weight metering around enqueueing. Improving that metering
([#7963](https://github.com/paritytech/polkadot-sdk/pull/7963)) and introducing batching
([#8021](https://github.com/paritytech/polkadot-sdk/pull/8021)) raised the ceiling to over 20,000 messages per
block — roughly a 60x increase.

The next bottleneck was structural rather than a matter of tuning. Parachains exchange XCMP pages in the
`XcmpMessageFormat::ConcatenatedVersionedXcm` format: a page is a concatenation of encoded `VersionedXcm`s, so
to split a page into individual messages the receiver must fully decode each one and then re-encode it before
forwarding to `pallet-message-queue`. That is around 2.5 microseconds plus a per-byte cost paid on every
message, purely to find its boundaries. I implemented a new format,
`XcmpMessageFormat::ConcatenatedOpaqueVersionedXcm`, carrying double-encoded XCMs so that splitting a page
becomes almost free ([#9588](https://github.com/paritytech/polkadot-sdk/pull/9588)).

A new wire format between parachains is only useful if it can actually be adopted, and at the time there was
no way for a sender to know whether a receiver understood it. I therefore designed and implemented a
negotiation strategy that lets a pair of parachains discover support and switch over safely
([#11263](https://github.com/paritytech/polkadot-sdk/pull/11263)).

The last remaining piece is retrying pages rather than dropping messages when a receiving parachain does not
have the bandwidth to take them ([#12638](https://github.com/paritytech/polkadot-sdk/pull/12638)), which has
been approved and will be merged shortly.

### Bounding heap memory usage during decoding

Decoding is where a runtime spends much of its memory: every block, every extrinsic and every message passes
through it, and until this work none of that consumption was measured. Making it measurable and then reducing
it lowers the memory a node has to keep available to execute a block. I have owned this from the primitives
upward.

I added heap usage tracking and limiting to `parity-scale-codec` itself
([#616](https://github.com/paritytech/parity-scale-codec/pull/616)), then integrated those primitives into
`polkadot-sdk`, first bounding the decoded size of an `UncheckedExtrinsic` call
([#8234](https://github.com/paritytech/polkadot-sdk/pull/8234)).

The two most important parts came after that. Lazily decoding the extrinsics in a block
([#9480](https://github.com/paritytech/polkadot-sdk/pull/9480)) removed the need to decode a block's
extrinsics up front: they are now decoded one at a time, as each is executed, rather than the whole block
being held in decoded form at once. Tracking and limiting the nested memory used by XCM `Transact` instructions
([#11147](https://github.com/paritytech/polkadot-sdk/pull/11147)) extended the accounting to the nested,
double-encoded structures carried inside messages, which were not previously accounted for.

### Omni-Node

The goal of the Omni-Node effort was that a parachain team should not need to maintain its own node binary at all.

The first significant piece was a large refactoring of `polkadot-parachain-bin`
([#4916](https://github.com/paritytech/polkadot-sdk/pull/4916)), deduplicating and simplifying the per-runtime
code paths the binary had accumulated. Together with the `Runtime::OmniNode` variant
([#4805](https://github.com/paritytech/polkadot-sdk/pull/4805)) and smaller cleanups
([#4666](https://github.com/paritytech/polkadot-sdk/pull/4666)), this left a clean separation between the
generic and the runtime-specific logic.

That generic half then became a library, `polkadot-parachain-lib`
([#5288](https://github.com/paritytech/polkadot-sdk/pull/5288)), so that a team needing a slightly customised
node can build one on top of it instead of copying the binary and diverging from upstream.

I also extended the library beyond what the binary had supported: `u64` block numbers
([#5269](https://github.com/paritytech/polkadot-sdk/pull/5269)), which unblocked a parachain use case
([#4787](https://github.com/paritytech/polkadot-sdk/issues/4787)) it could not otherwise serve, and manual
seal ([#5586](https://github.com/paritytech/polkadot-sdk/pull/5586)), which shortens the development and
debugging loop for parachain teams.

Alongside the code, I took part in the public discussion where the Omni-Node direction was shaped with
parachain teams, on the
[forum thread gathering ideas and feedback](https://forum.polkadot.network/t/polkadot-parachain-omni-node-gathering-ideas-and-feedback/7823).

### BEEFY fork equivocation reporting

I implemented fork equivocation reporting end to end: the runtime support for reporting fork voting 
([#4522](https://github.com/paritytech/polkadot-sdk/pull/4522)), the generation and verification logic for ancestry 
proofs ([#4430](https://github.com/paritytech/polkadot-sdk/pull/4430)), benchmarks for the
equivocation logic ([#5188](https://github.com/paritytech/polkadot-sdk/pull/5188)), a check that key ownership
proofs are optimal ([#4699](https://github.com/paritytech/polkadot-sdk/pull/4699)), and finally enabling the
equivocation reporting extrinsic itself
([#6856](https://github.com/paritytech/polkadot-sdk/pull/6856)). More recently I refactored BEEFY to
accommodate other crypto types and hashing algorithms
([#10763](https://github.com/paritytech/polkadot-sdk/pull/10763)), unblocking an open-source user outside
Parity.

### Conclusion

My work over this period spans the receiving side of cross-consensus message passing, which I took from around
300 to over 20,000 messages per block and then gave a cheaper wire format; the decoding primitives that the
whole of `polkadot-sdk` depends on; BEEFY fork equivocation reporting, delivered end to end; and the Omni-Node,
which removed the need for parachain teams to maintain their own copy of the parachain node code. All of it has
been subject to expert code review and is part of the production implementation of the protocol. 

I believe these contributions align with the responsibilities of Rank II, 
and I respectfully request your consideration for promotion.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                            | Comments |
|---|---------------------|---|-----------------------------------------------------------------------|----------|
|I  | 90%                 |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote. | -        |                                                                                                                                                                                                                                                            |          |
|II | 80%                 |N/A   |                                                                       |          |
|III| 70%                 |100%  |                                                                       |          |
|IV | 60%                 |90%   |                                                                       |          |
|V  | 50%                 |80%   |                                                                       |          |
|VI | 40%                 |70%   |                                                                       |          |


