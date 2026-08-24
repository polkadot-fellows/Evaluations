# Argument-0009: Retention at Rank I

|                 |                   |
| --------------- |-------------------|
| **Report Date** | 2026/07/19        |
| **Submitted by**| Damilare Akinlose |

---

## Member details

- **Matrix username**: `@dharjeezy/:matrix.org`
- **Polkadot address**: `12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW`
- **Current rank**: `1`
- **Date of initial induction**: `2024-04-29`
- **Date of last report**: `2026/04/25`
- **Area(s) of Expertise/Interest**: `FRAME/Runtime & Node`

---

## Reporting period

- **Start date**: 2026/04/26
- **End date**: 2026/07/19

---

## Argument

I am applying for Rank I retention.

During this period, most of my work continued the `try_state` invariant initiative ([issue #239](https://github.com/paritytech/polkadot-sdk/issues/239)). I merged two more `try_state` hooks, for `pallet-beefy-mmr` and `pallet-membership`, and opened nine more `try_state` PRs across consensus, governance, collectives, and utility pallets. Each one defines and asserts the storage invariants that hold for the pallet. Alongside this, my `litep2p` QUIC DNS support was merged, and I continued the `pallet-conviction-voting` migration to the `fungible` traits.

Below is a summary of my key contributions:

### Reliable & Resilient

#### **Introduce `try_state` Hook for Pallet BEEFY MMR**
The `try_state` hook for the BEEFY MMR pallet, which was open and under review at the time of my last report, was merged in [PR #11734](https://github.com/paritytech/polkadot-sdk/pull/11734). The PR defines and asserts the storage invariants that hold for the pallet, as part of [issue #239](https://github.com/paritytech/polkadot-sdk/issues/239).

#### **Introduce `try_state` Hook for Pallet Membership**
I completed and merged a `try_state` hook for `pallet-membership` in [PR #5850](https://github.com/paritytech/polkadot-sdk/pull/5850). The change verifies the pallet's key storage invariants, including the relationship between the `Members` set and the `Prime` member.

#### **Introduce `try_state` Hook for Pallet Conviction Voting**
I opened [PR #12418](https://github.com/paritytech/polkadot-sdk/pull/12418) adding a `try_state` hook to `pallet-conviction-voting`, defining and asserting the invariants across its voting and delegation storage. The PR is open and under review.

#### **Introduce `try_state` Hook for Pallet Core Fellowship**
I opened [PR #12419](https://github.com/paritytech/polkadot-sdk/pull/12419) adding a `try_state` hook to `pallet-core-fellowship`, verifying the consistency of member ranking and parameter storage. The PR is open and under review.

#### **Introduce `try_state` Hook for Pallet Child Bounties**
I opened [PR #12233](https://github.com/paritytech/polkadot-sdk/pull/12233) adding a `try_state` hook to `pallet-child-bounties`, asserting invariants such as the accounting relationship between parent bounties and their children. The PR is open and under review.

#### **Introduce `try_state` Hook for Pallet GRANDPA**
I opened [PR #12422](https://github.com/paritytech/polkadot-sdk/pull/12422) adding a `try_state` hook to `pallet-grandpa`, covering the invariants of its authority-set and session state. The PR is open and under review.

#### **Introduce `try_state` Hook for Pallet Derivatives**
I opened [PR #12421](https://github.com/paritytech/polkadot-sdk/pull/12421) adding a `try_state` hook to `pallet-derivatives`, defining and asserting the invariants that hold for the pallet. The PR is open and under review.

#### **Introduce `try_state` Hook for Pallet Oracle**
I opened [PR #12631](https://github.com/paritytech/polkadot-sdk/pull/12631) adding a `try_state` hook to `pallet-oracle`, asserting the consistency of its feed and value storage. The PR is open and under review.

#### **Introduce `try_state` Hook for Pallet I'm Online**
I opened [PR #12632](https://github.com/paritytech/polkadot-sdk/pull/12632) adding a `try_state` hook to `pallet-im-online`, verifying the invariants of its heartbeat and authored-block tracking. The PR is open and under review.

#### **Introduce `try_state` Hook for Pallet Indices**
I opened [PR #12633](https://github.com/paritytech/polkadot-sdk/pull/12633) adding a `try_state` hook to `pallet-indices`, asserting the invariants around index-to-account assignments and their deposits. The PR is open and under review.

#### **Introduce `try_state` Hook for Pallet Lottery**
I opened [PR #12634](https://github.com/paritytech/polkadot-sdk/pull/12634) adding a `try_state` hook to `pallet-lottery`, verifying the consistency of ticket, participant, and pot accounting. The PR is open and under review.

---

### Flexible & Developer-Focused

#### **Migrate `pallet-conviction-voting` to Fungible Traits**
I continued work on [PR #11142](https://github.com/paritytech/polkadot-sdk/pull/11142), which migrates `pallet-conviction-voting` from the legacy `Currency` and `LockableCurrency` traits to the `fungible` traits, replacing locks with freezes via `fungible::MutateFreeze`. The PR introduces a `FreezeReason::ConvictionVoting` composite enum, converts all lock operations to their freeze equivalents, and adds a `SteppedMigration` (`LazyMigrationV0ToV1`) that lazily converts existing locks to freezes at runtime upgrade, along with its benchmark and a storage version bump. Review iteration continued through this cycle. This contributes to the broader fungibles migration tracked in [issue #226](https://github.com/paritytech/polkadot-sdk/issues/226).

---

### Interoperable & Compatible

#### **`litep2p`: Support Dialing DNS Addresses Over QUIC**
My extension of the `litep2p` QUIC transport to resolve DNS multiaddresses (`/dns/`, `/dns4/`, `/dns6/`) before connecting was merged in [PR #542](https://github.com/paritytech/litep2p/pull/542). This brings QUIC to feature parity with the existing TCP and WebSocket transports, closes [issue #406](https://github.com/paritytech/litep2p/issues/406), and removes a limitation that previously required QUIC peers to be addressed by raw IPs.

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
