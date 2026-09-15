# Argument-0006: Promotion to Rank V

|                 |                  |
| --------------- | ---------------- |
| **Report Date** | 2026/07/16       |
| **Submitted by**| eskimor          |


## Member details

- Polkadot address: `12pRzYaysQz6Tr1e78sRmu9FGB8gu8yTek9x6xwVFFAwXTM8`
- Current rank: 4 (since 2024, promotion via [Argument-0001](https://github.com/polkadot-fellows/Evaluations/blob/main/argument/eskimor/0001-eskimor-promote-IV-2024.md))
- Date of initial induction: 2023/07/16
- Date of last report: 2026/07/16
- Link to last report: [Argument-0005 (retention)](0005-eskimor-retain-IV-2026-2.md)
- Area(s) of Expertise/Interest: `Parachains Consensus`


## Reporting period

This argument covers my time at Rank IV (2024/06 - present). For the most recent
period in detail, see my parallel [retention argument](0005-eskimor-retain-IV-2026-2.md).


## Argument

I have been at Rank IV for two years. In that time my role has shifted from implementing
major components to originating them: I am the author of three protocol designs - low
latency parachains, speculative messaging and scalable Web3 storage - all three of which
are currently being implemented, two of them primarily by colleagues building on my
designs and under my review. Below I address the Rank V requirements individually.

### "Play a primary role in ideating, designing and formalising or prototyping a major component."

I am the sole originator and author of three major designs, each formalised in a design
document and in active implementation:

1. **[Low-latency parachains](https://github.com/paritytech/polkadot-sdk/pull/11413)** -
   acknowledgement-based block confirmations (~100ms) via slashable collator commitments,
   plus the scheduling parent concept decoupling parachain block validity from relay chain
   forks. I formalised the design, implemented the core relay chain and cumulus changes
   myself ([#10472](https://github.com/paritytech/polkadot-sdk/pull/10472),
   [#10742](https://github.com/paritytech/polkadot-sdk/pull/10742), both merged) and
   coordinate the implementation effort via tracking issues
   ([relay chain](https://github.com/paritytech/polkadot-sdk/issues/10883),
   [cumulus](https://github.com/paritytech/polkadot-sdk/issues/11170),
   [collator protocol V4](https://github.com/paritytech/polkadot-sdk/issues/11903)).
   Six engineers have merged implementation PRs against these issues to date, among them
   @iulianbarbu, @alindima, @mchristou, @serban300 and @AlexandruCihodaru.

2. **[Speculative messaging](https://github.com/paritytech/polkadot-sdk/pull/10449)** -
   HRMP replacement enabling messaging latencies down to parachain block times, with
   intra-block messaging feasible for super chains. Iterated through five design revisions
   based on implementation feedback; the
   [off-chain block verification](https://github.com/paritytech/polkadot-sdk/pull/12588)
   component was factored out as a building block in its own right.
   [PoC](https://github.com/paritytech/polkadot-sdk/pull/12095) (@lexnv) and
   [primitives](https://github.com/paritytech/polkadot-sdk/pull/12368) (@naijauser) are in
   progress.

3. **[Scalable Web3 storage](https://github.com/paritytech/polkadot-sdk/pull/10731)** -
   bucket-based decentralized storage with game-theoretic enforcement (challenge protocol
   with staked providers) instead of continuous cryptographic proofs, keeping the chain off
   the hot path. Now its own project at
   [paritytech/web3-storage](https://github.com/paritytech/web3-storage) @mudigal's team
   implementing it, among them @bkontur, @franciscoaguirre, @ilchu and
   @danielbui12.

### "Usefully assisted in devising three more major components."

Beyond the components above, over my time in the ecosystem:

- **Dispute handling** - authored the
  [dispute-distribution subsystem](https://github.com/paritytech/polkadot/pull/3282) and
  contributed substantially to dispute resilience over the years
  (spam protection, load reduction, [disabling strategy](https://github.com/paritytech/polkadot-sdk/issues/784#issuecomment-1691886382)).
- **Availability distribution** - authored the
  [request-based availability distribution](https://github.com/paritytech/polkadot/pull/2423)
  and the underlying
  [generic request/response networking infrastructure](https://github.com/paritytech/polkadot/pull/2352)
  still in use today.
- **Agile Coretime & on-demand** - led node-side implementation of
  [on-demand parachains](https://github.com/paritytech/polkadot/pull/6969) and
  [Coretime](https://github.com/paritytech/polkadot-sdk/pull/1694), designed the
  [price controller](https://github.com/paritytech/polkadot-sdk/pull/4521), authored
  [RFC-149](https://polkadot-fellows.github.io/RFCs/approved/0149-rfc-1-renewal-adjustment.html),
  co-led the Polkadot launch, and reduced on-demand latency to same-block
  ([#10184](https://github.com/paritytech/polkadot-sdk/pull/10184)).
- **Elastic scaling** - played a major role in devising the approach of
  [RFC-103](https://github.com/polkadot-fellows/RFCs/pull/103) (formalised and authored by
  @sandreim): constraining candidate validity to a specific core via UMP signals. The UMP
  signal mechanism proved to be broadly enabling - it also underpins speculative messaging,
  the collator protocol resilience improvements and
  [offchain parachain runtime upgrades (RFC-102)](https://github.com/polkadot-fellows/RFCs/pull/102).
- **Collator protocol** - from [DoS protection](https://github.com/paritytech/polkadot/pull/3446)
  to devising the [revamp](https://github.com/paritytech/polkadot-sdk/issues/616) currently
  being implemented.
- **[Proof of DOT](https://github.com/paritytech/polkadot-sdk/issues/6173)** - generic
  sybil resilience for p2p networks, foundational for the storage design above.
- **Deterministic simulation testing** -
  [introduced](https://github.com/paritytech/polkadot-sdk/pull/12007) for node subsystems:
  implementation independent, deterministic, differential subsystem tests; the pilot alone
  surfaced several production bugs.

### "Usefully assisted (through advocation, research or rationalisation) in determining the long-term technical roadmap."

I initiated and led the strategic shift of Polkadot core development towards low latency
and block confidence, which is now a major workstream (see above). The reasoning: Polkadot
has world-class scalability and resilience, but user-perceived latency is what wins
adoption. Speculative messaging and the storage initiative extend this: rounding out
Polkadot as a full Web3 cloud - compute, messaging, storage. The "Spammening" load tests
on Kusama, which I co-initiated, established that we validate our scalability claims
publicly; the weaknesses they surface
([example](https://forum.polkadot.network/t/2025-11-25-kusama-parachains-spammening-aftermath/11108))
feed directly into the QA investments (deterministic simulation testing) above.

### Speaking with technical authority on all levels of the protocol

My designs routinely survive review by the highest ranks. Where they were challenged, the
challenges were resolved on technical grounds - e.g. the low-latency design documents the
considered-and-rejected alternatives (FOCIL-style inclusion lists, Ethereum L2
preconfirmations) with the arguments why they don't transfer to Polkadot's heterogeneous
sharding model. The design documents themselves are written to be that argument.

## Voting record

| Rank | Activity threshold | Agreement threshold | My record |
|------|-------------------|---------------------|-----------|
| IV   | 60%               | 90%                 | I voted on 60 of 106 referenda I was eligible to vote on in this reporting period (56.6%). I voted against two: [#512](https://collectives.subsquare.io/fellowship/referenda/512), which ended up rejected (i.e. in line with the consensus), and [#565](https://collectives.subsquare.io/fellowship/referenda/565), which is still being decided. |

Lifetime: [307 votes according to subsquare](https://collectives.subsquare.io/user/12pRzYaysQz6Tr1e78sRmu9FGB8gu8yTek9x6xwVFFAwXTM8/votes).
