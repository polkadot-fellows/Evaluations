# Argument-0004: Retain at Rank IV

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/01/07                                                                                  |
| **Submitted by**| eskimor                                                                             |


## Member details

- Polkadot address: `12pRzYaysQz6Tr1e78sRmu9FGB8gu8yTek9x6xwVFFAwXTM8`
- Current rank: 4
- Date of initial induction: 2023/07/16
- Date of last report: 2025/06/24
- Area(s) of Expertise/Interest: `Parachains Consensus`


## Reporting period

- Start date: 2025/06/24
- End date: 2026/01/07


## Argument

This period focused on designing low-latency block confirmations and cross-chain messaging for Polkadot, and ended with implementation work and looking into scalable Web3 storage.

### Low-Latency Design

The [Low-Latency Parachains design](https://github.com/paritytech/polkadot-sdk/blob/0fc95188b57db6f50f1503ebcc3d78e9a161c1b4/docs/low-latency-v2-design.md) introduces:

1. **Acknowledgement-based block finality** - collators sign commitments to a canonical chain; equivocation is provable and slashable, enabling ~100ms confirmations
2. **Scheduling parent concept** - decouples parachain blocks from relay chain blocks, allowing parachain blocks to remain valid during relay chain reorgs and enabling resubmission

Alternative approaches were considered and rejected:

- **Inclusion lists (FOCIL-style)**: FOCIL works for Ethereum because the beacon chain enforces inclusion via fork choice. Polkadot's relay chain decides forks independently of parachain promises, and punishment is limited to block rewards (collators can avoid promises by not producing blocks).

- **Ethereum L2 preconfirmations**: L1 validators commit to including L2 transactions because they understand Ethereum transactions. Polkadot parachains are heterogeneous - validators cannot build parachain blocks to uphold promises if collators fail.

### Speculative Messaging

The [Speculative Messaging design](https://github.com/paritytech/polkadot-sdk/blob/0fc95188b57db6f50f1503ebcc3d78e9a161c1b4/docs/speculative-messaging-design.md) replaces HRMP with a variant of off-chain XCMP that enables low-latency messaging. Messaging latencies can be made as low as parachain block times, for certain scenarios even intra-block messaging should be feasible (super chains).

### Scalable Web3 Storage Design

The [Scalable Web3 Storage design](https://github.com/paritytech/polkadot-sdk/pull/10731) proposes a decentralized storage protocol where:

- **Buckets** are the fundamental unit - defining what data belongs together, who can access it (members with roles), and which providers store it (via storage agreements with locked stake) and most importantly serve as provider independent reference to data
- **The chain exists as a credible threat, not the hot path** - writes and reads happen off-chain directly with providers; the chain is only touched for bucket creation, storage agreement setup, optional checkpoints, and dispute resolution
- **Game-theoretic enforcement** replaces continuous cryptographic proofs - providers commit Merkle roots and lock stake; clients can challenge at any time, forcing proof of data availability or full stake slash

This differs fundamentally from existing systems:

| Aspect | This Design | Filecoin | IPFS |
|--------|-------------|----------|------|
| **Write latency** | Sub-second | Minutes-hours (sealing) | Fast but no persistence |
| **Chain load** | Minimal | Heavy (continuous proofs) | N/A |
| **Read incentives** | Proof-of-DOT priority | Separate retrieval market | None |
| **Proof mechanism** | On-demand challenges | Continuous PoRep/PoSt | None |

The design builds on **Proof-of-DOT** for sybil resistance: clients lock DOT against a PeerID, enabling reputation tracking and spam prevention on the network layer (different to Proof of Personhood which is on the blockchain/transaction layer). Providers prioritize clients based on payment history, creating a market for read performance.

### Low-Latency Implementation Progress

Implementation of the low-latency design is underway:

1. **[Candidate Descriptor V3](https://github.com/paritytech/polkadot-sdk/pull/10742)** - Node feature enabling new candidate protocol versions. First e2e tests are already passing.

2. **[Prospective Parachains Cleanup](https://github.com/paritytech/polkadot-sdk/pull/10650)** - Architectural refactoring that:
   - Separates `RelayChainScope` from `Scope` for cleaner abstraction
   - Removes redundant data tracking between prospective-parachains and backing implicit view
   - Prepares the codebase for the scheduling_parent design where execution and scheduling contexts diverge

### Instant On-Demand Coretime

The [Fix coretime partitioning + super low latency on-demand](https://github.com/paritytech/polkadot-sdk/pull/10184) PR fixes coretime issues and improves on-demand latency:

- **Fixed coretime partitioning** - the claim queue builder was broken, missing assignments from upcoming blocks
- **On-demand orders are now instant** - they appear in the claim queue in the same block the order is placed, reducing latency from ~6 seconds to same-block

### Architect Role Fulfillment

Per the Manifesto's requirements for Rank IV (Architect):

**"Primary role in ideation and formalisation of a major protocol component"**: Three designs addressing fundamental limitations - block confirmation latency, cross-chain messaging latency, and decentralized storage.

**"Primary role in code-design and implementation"**: Candidate descriptor v3 implementation underway with first e2e test passing.


## Voting record

According to subsquare I voted on 246 of 388 referenda (63.4%).
