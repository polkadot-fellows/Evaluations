# Argument-0008: Retention at Rank I

|                 |                   |
| --------------- |-------------------|
| **Report Date** | 2026/04/25        |
| **Submitted by**| Damilare Akinlose |

---

## Member details

- **Matrix username**: `@dharjeezy/:matrix.org`
- **Polkadot address**: `12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW`
- **Current rank**: `1`
- **Date of initial induction**: `2024-04-29`
- **Date of last report**: `2026/01/18`
- **Area(s) of Expertise/Interest**: `FRAME/Runtime & Node`

---

## Reporting period

- **Start date**: 2026/01/19
- **End date**: 2026/04/25

---

## Argument

I am applying for Rank I retention.

In this cycle, my work focused on three areas. I added new `try_state` invariant checks to several consensus and reward related pallets. I landed a long-running overhaul of the `litep2p` ping protocol along with the connection keep-alive redesign that it required. I also continued progressing developer-facing work on block number providers, fungible-trait migrations, and QUIC transport interoperability. Beyond code, I published a deep-dive write-up of the ping work on the Polkadot Forum so that the design rationale would be available to the wider ecosystem.

Below is a summary of my key contributions:

### Reliable & Resilient

#### **`litep2p`: Spec-Compliant Ping Protocol & Substream Keep-Alive Redesign**
After several review cycles, my overhaul of the `litep2p` ping protocol was merged in [PR #416](https://github.com/paritytech/litep2p/pull/416). The change brings the implementation in line with the [libp2p ping spec](https://github.com/libp2p/specs/blob/master/ping/ping.md). Pings are now repeated rather than sent only once on connect. Inbound and outbound substreams are reused for subsequent requests, which is required for `smoldot` compatibility. Ping substreams are also excluded from the connection keep-alive mechanism, so idle connections can be closed on timeout when only ping and identify substreams remain open. I tested the change across `litep2p` to `litep2p`, `litep2p` to pre-PR `litep2p`, and `litep2p` to `smoldot`. As a result, dead-peer detection now happens within roughly 25 seconds, which is meaningful for validators identifying unreachable peers during consensus.

To document the design and the cascading keep-alive redesign that the ping work required, I authored a Polkadot Forum article: [*A deep dive into overhauling litep2p's ping protocol*](https://forum.polkadot.network/t/a-deep-dive-into-overhauling-litep2ps-ping-protocol-to-support-periodic-pinging-spec-compliant-payloads-and-a-new-substreamkeepalive-mechanism-for-connection-lifecycle-management/17501). The post walks through periodic pinging, spec-compliant random payload verification, the new tagging of protocols as either keep-alive or non keep-alive (separating application protocols from infrastructure ones), and the backwards-compatibility considerations for older `litep2p` nodes.

#### **Introduce `try_state` Hook for Pallet Authorship**
I added a `try_state` hook to `pallet-authorship` to verify a key storage invariant. The implementation was merged in [PR #11215](https://github.com/paritytech/polkadot-sdk/pull/11215) and closes part of the broader [issue #239](https://github.com/paritytech/polkadot-sdk/issues/239) initiative to add `try_state` compliance across pallets in the Polkadot SDK.

#### **Introduce `try_state` Hook for Pallet BABE**
I implemented a `try_state` hook for `pallet-babe` covering all of its key storage invariants. The change was merged in [PR #11216](https://github.com/paritytech/polkadot-sdk/pull/11216) and continues the systematic effort to make consensus-critical pallets verifiable under runtime checks.

#### **Introduce `try_state` Hook for Pallet BEEFY MMR**
I extended the `try_state` initiative to the BEEFY MMR pallet in [PR #11734](https://github.com/paritytech/polkadot-sdk/pull/11734). The PR defines and asserts the invariants that hold for the pallet, and is currently open and under review.

#### **`try_state` for Pallet Atomic Swap: No Invariants to Assert**
Following up on the work I started last cycle for `pallet-atomic-swap` in [PR #10473](https://github.com/paritytech/polkadot-sdk/pull/10473), I went back through the pallet's storage and logic to determine which invariants a `try_state` hook should enforce. The conclusion was that the pallet has no invariants worth asserting at the storage level: its single `PendingSwaps` map only records open swap offers, and the pallet's correctness is enforced at the extrinsic boundary rather than through any cross-storage relationship. I therefore closed the PR with that finding, which removes `pallet-atomic-swap` from the list of pallets still pending `try_state` coverage under [issue #239](https://github.com/paritytech/polkadot-sdk/issues/239).

---

### Flexible & Developer-Focused

#### **Migrate `pallet-conviction-voting` to Fungible Traits**
I authored [PR #11142](https://github.com/paritytech/polkadot-sdk/pull/11142) to migrate `pallet-conviction-voting` from the legacy `Currency` and `LockableCurrency` traits to the modern `fungible` traits, replacing locks with freezes via `fungible::MutateFreeze`. The change replaces `type Currency` with `type Fungible` and `type RuntimeFreezeReason` in the pallet's `Config`, introduces a `FreezeReason::ConvictionVoting` composite enum, and converts all lock operations (`set_lock`, `extend_lock`, `remove_lock`) to their freeze equivalents. To preserve existing user state, I added a `SteppedMigration` (`LazyMigrationV0ToV1`) that lazily converts existing locks to freezes at runtime upgrade, together with a `v1_migration_step` benchmark and a storage version bump. This contributes to the broader fungibles migration tracked in [issue #226](https://github.com/paritytech/polkadot-sdk/issues/226).

#### **Expose Block Number Provider Name as a Constant**
I continued work on exposing the `BlockNumberProvider` identifier as a runtime constant in [PR #9091](https://github.com/paritytech/polkadot-sdk/pull/9091). The PR extends the `BlockNumberProvider` trait with an `IDENTIFIER` constant and adapts the `#[pallet::constant]` macro to accept attribute parameters, so that it can fetch values from associated constants on types. The end result is that DApp developers can reliably distinguish between local and Relay Chain block numbers in metadata. Review iteration is ongoing.

---

### Interoperable & Compatible

#### **`litep2p`: Support Dialing DNS Addresses Over QUIC**
I extended the QUIC transport in `litep2p` to resolve DNS multiaddresses (`/dns/`, `/dns4/`, `/dns6/`) before connecting, bringing it to feature parity with the existing TCP and WebSocket transports. The implementation in [PR #542](https://github.com/paritytech/litep2p/pull/542) closes [issue #406](https://github.com/paritytech/litep2p/issues/406) and removes a long-standing limitation that previously required QUIC peers to be addressed by raw IPs.

---

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e undefined% voting activity). Out of xx referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus x times (i.e undefined% voting agreement).  |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

---

## Misc

- [ ] Question(s):
- [ ] Concern(s):
- [ ] Comment(s):
