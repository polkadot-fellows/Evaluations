# Argument-0005: Retain at Rank IV

|                 |                  |
| --------------- | ---------------- |
| **Report Date** | 2026/07/16       |
| **Submitted by**| eskimor          |


## Member details

- Polkadot address: `12pRzYaysQz6Tr1e78sRmu9FGB8gu8yTek9x6xwVFFAwXTM8`
- Current rank: 4
- Date of initial induction: 2023/07/16
- Date of last report: 2026/01/07
- Link to last report: https://github.com/polkadot-fellows/Evaluations/pull/239
- Area(s) of Expertise/Interest: `Parachains Consensus`


## Reporting period

- Start date: 2026/01/07
- End date: 2026/07/16


## Argument

The designs of the previous period moved into implementation this period - partly by me,
increasingly by colleagues building on those designs. My role has shifted accordingly:
driving the designs forward, implementing core pieces and reviewing/guiding the
implementation work of others.

### Low-Latency Parachains: Implementation

The [low-latency v2 design](https://github.com/paritytech/polkadot-sdk/pull/11413) is now
being implemented by a group of engineers, coordinated via tracking issues I authored:
[low-latency relay chain](https://github.com/paritytech/polkadot-sdk/issues/10883),
[low-latency cumulus changes](https://github.com/paritytech/polkadot-sdk/issues/11170) and
[collator protocol V4](https://github.com/paritytech/polkadot-sdk/issues/11903).

Core PRs by myself here:

- **[V3 Candidate Descriptor with explicit scheduling parent](https://github.com/paritytech/polkadot-sdk/pull/10472)** (merged) -
  the central relay chain change: decouples parachain block validity from a specific relay
  chain block, making parachain blocks survive relay chain forks and enabling resubmission.
- **[Candidate descriptor v3 cumulus changes](https://github.com/paritytech/polkadot-sdk/pull/10742)** (merged) -
  parachain side: scheduling proofs, PVF validation, block builder, including e2e test.
- **[Prospective parachains cleanup](https://github.com/paritytech/polkadot-sdk/pull/10650)** (merged) -
  architectural refactoring preparing the code base for diverging execution and scheduling
  contexts. [Follow-up](https://github.com/paritytech/polkadot-sdk/pull/11870) in review.

Implementation work building directly on this design (selection, all merged):
@iulianbarbu - [scheduling info PVF verification](https://github.com/paritytech/polkadot-sdk/pull/12097) and
[scheduling signature verification](https://github.com/paritytech/polkadot-sdk/pull/12185),
@alindima - [older relay parents in prospective-parachains](https://github.com/paritytech/polkadot-sdk/pull/11772) and
[v3 descriptor support in the runtime](https://github.com/paritytech/polkadot-sdk/pull/11328),
@mchristou - [cumulus resubmission store](https://github.com/paritytech/polkadot-sdk/pull/12091),
@serban300 - [v3 find_parent() adjustments](https://github.com/paritytech/polkadot-sdk/pull/12296),
@AlexandruCihodaru - [v3 descriptor support in the experimental validator](https://github.com/paritytech/polkadot-sdk/pull/11306).
I reviewed most of these.

### Speculative Messaging: Design Iterations & PoC

The [speculative messaging design](https://github.com/paritytech/polkadot-sdk/pull/10449)
went through three major revisions this period, and is now being implemented:
[v0.3 - flat per-destination commitments](https://github.com/paritytech/polkadot-sdk/pull/12579),
[v0.4 - factoring out off-chain block verification](https://github.com/paritytech/polkadot-sdk/pull/12588) and
[v0.5 - streams and PoV lifts](https://github.com/paritytech/polkadot-sdk/pull/12659).

The off-chain block verification design that fell out of v0.4 is a component in its own
right, with applications beyond messaging.

Implementation has started, based on my design:
@lexnv is working on a [PoC](https://github.com/paritytech/polkadot-sdk/pull/12095),
@naijauser on the [primitives](https://github.com/paritytech/polkadot-sdk/pull/12368).

### Scalable Web3 Storage: From Design to Project

The [storage design](https://github.com/paritytech/polkadot-sdk/pull/10731) of the last
report got merged and subsequently
[moved](https://github.com/paritytech/polkadot-sdk/pull/12355) into its own repository:
[paritytech/web3-storage](https://github.com/paritytech/web3-storage). It is now an active
implementation project with roughly ten contributors - among them @bkontur,
@franciscoaguirre, @ilchu and @danielbui12 - covering the storage provider pallet,
challenge protocol, provider node and S3 compatible interface. I keep refining the design
as implementation questions come up, e.g.
[challenge clarifications](https://github.com/paritytech/web3-storage/pull/231).

### Instant On-Demand Coretime

[Fix coretime partitioning + super low latency on-demand](https://github.com/paritytech/polkadot-sdk/pull/10184)
got merged: on-demand orders now appear in the claim queue in the very same block the order
is placed, down from ~6 seconds. This also fixed the broken claim queue builder for
partitioned coretime.

### Quality Assurance: Deterministic Simulation Testing

Following up on the QA learnings from previous periods, I built
[deterministic simulation based testing for subsystems](https://github.com/paritytech/polkadot-sdk/pull/12007)
together with the required
[clock abstraction](https://github.com/paritytech/polkadot-sdk/pull/12212). Tests declare
the chain as facts and assert only on the observable contract of the subsystem. This makes
them:

- **implementation independent** - a subsystem may issue different queries or in different
  order without breaking a single test; you assert the behavior of interest, nothing else,
- **deterministic** - time is driven via a mock clock, no flaky timeouts, and failures
  report the effect timeline instead of hanging,
- **differential** - one scenario runs against both collator protocol implementations
  (legacy and experimental), any divergence in observable behavior locates a bug for free,
- **roughly 10× smaller** than the equivalent mock-overseer tests.

The framework also supports known-bug tests, enabling a test-first workflow: expected
behavior gets merged and pinned before the fix exists. Writing edge-case scenarios became
cheap enough that the pilot alone surfaced several production bugs (e.g. claim queue
handling at [session boundaries](https://github.com/paritytech/polkadot-sdk/pull/12255)).
This matters increasingly as AI contributes more code: the contract is pinned by tests that
don't change with the implementation.

### Maintenance & Fixes

Resilience and correctness fixes, mostly found while working on the above (all merged,
several backported to stable releases):
[statement distribution pruning bug](https://github.com/paritytech/polkadot-sdk/pull/11820),
[rotation bug fix + simplification](https://github.com/paritytech/polkadot-sdk/pull/11967),
[enforce current relay parent to be available](https://github.com/paritytech/polkadot-sdk/pull/11621),
[report back when candidate is rejected](https://github.com/paritytech/polkadot-sdk/pull/11463),
[UMP signal handling cleanup](https://github.com/paritytech/polkadot-sdk/pull/12240).

### Architect Role Fulfillment

Per the Manifesto's requirements for Rank IV (Architect):

**"Primary role in ideation and subsequent formalisation of a major protocol component"**:
Low-latency parachains, speculative messaging and Web3 storage - all three designs are
formalised in design documents and are in active implementation.

**"Primary role in code-design and implementation"**: V3 candidate descriptor
(relay chain and cumulus side) merged and deployed as node feature; deterministic
simulation testing framework merged.


## Voting record

| Rank | Activity threshold | Agreement threshold | My record |
|------|-------------------|---------------------|-----------|
| IV   | 60%               | 90%                 | I voted on 60 of 106 referenda I was eligible to vote on in this reporting period (56.6%). I voted against two: [#512](https://collectives.subsquare.io/fellowship/referenda/512), which ended up rejected (i.e. in line with the consensus), and [#565](https://collectives.subsquare.io/fellowship/referenda/565), which is still being decided. |

Lifetime: [307 votes according to subsquare](https://collectives.subsquare.io/user/12pRzYaysQz6Tr1e78sRmu9FGB8gu8yTek9x6xwVFFAwXTM8/votes).
