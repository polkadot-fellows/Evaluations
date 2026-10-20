# Argument-0010: Retention at Rank I

|                 |                   |
| --------------- |-------------------|
| **Report Date** | 2026/10/17        |
| **Submitted by**| Damilare Akinlose |
| **Sponsored by**|               |

---

## Member details

- **Matrix username**: `@dharjeezy/:matrix.org`
- **Polkadot address**: `12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW`
- **Current rank**: `1`
- **Date of initial induction**: `2024-04-29`
- **Date of last report**: `2026/07/19`
- **Link to last report**: [Evaluations#327](https://github.com/polkadot-fellows/Evaluations/pull/327)
- **[Subsystems](../../subsystems.md) developed/maintained**:
  - Nodes (SDK, Omni-Node, RPCs, Light-clients, tooling): fork-aware transaction pool
  - Runtimes (FRAME, APIs, integrations): `try_state` invariants across FRAME pallets
  - Nodes (Networking, Security): `litep2p`

---

## Reporting period

- **Start date**: 2026/07/20
- **End date**: 2026/10/17

---

## Argument

I am applying for Rank I retention.

During this period, my work spanned three subsystems: Nodes (SDK), Runtimes (FRAME) and Nodes (Networking). On the node side, I started working on the fork-aware transaction pool (`fatxpool`). I merged a refactor that replaces `TransactionPoolWrapper` with a trait object and drops the phantom `Client` type parameter from `FullClientTransactionPool`, and opened a fix so transactions from retracted blocks reach the mempool. I continued the `try_state` invariant initiative ([issue #239](https://github.com/paritytech/polkadot-sdk/issues/239)), merging the hooks for `pallet-grandpa` and `pallet-core-fellowship` and opening eight more. In `litep2p`, I opened a PR making Kademlia serve multiple requests on one inbound substream, as the spec requires.

Below is a summary of my key contributions:

### Reliable & Resilient

#### **`fatxpool`: Add Transactions from Retracted Blocks to the Mempool**
I opened [PR #13482](https://github.com/paritytech/polkadot-sdk/pull/13482) to fix how the fork-aware transaction pool handles transactions from retracted blocks. Before, they were only resubmitted to the new view and never reached the mempool, so when the pool was at its limits they could be pushed out by mempool transactions whatever their priority. They are now added to the mempool as well, reusing the priority obtained while resubmitting them, and go through the usual replacement path when the mempool is full. A higher priority retracted transaction evicts lower ones, and a lower priority one is dropped. The PR also resubmits retracted transactions when the enacted block already has a view, which previously lost them for that view and its descendants. It closes [issue #6831](https://github.com/paritytech/polkadot-sdk/issues/6831) and is open and under review.

#### **Introduce `try_state` Hook for Pallet GRANDPA**
The `try_state` hook for `pallet-grandpa`, open at the time of my last report, was merged in [PR #12422](https://github.com/paritytech/polkadot-sdk/pull/12422). It defines and asserts the invariants of the pallet's authority-set and session state.

#### **Introduce `try_state` Hook for Pallet Core Fellowship**
The `try_state` hook for `pallet-core-fellowship`, also open at the time of my last report, was merged in [PR #12419](https://github.com/paritytech/polkadot-sdk/pull/12419). It checks that member ranking and parameter storage stay consistent.

#### **Introduce `try_state` Hook for Pallet Broker**
I opened [PR #13206](https://github.com/paritytech/polkadot-sdk/pull/13206) adding a `try_state` hook to `pallet-broker`, the pallet behind Coretime sales. The invariants it asserts:
- the stored configuration passes the same validity check `configure` applies
- sale info is consistent: cores sold never exceed cores offered, and a sale that offered cores always has a sellout price
- every region and every `InstaPoolContribution` covers at least one timeslice
- `Partial` and `Complete` potential renewals match how much of the core they actually assign
- pool history never strands revenue in the pallet's pot
- `AutoRenewals` stays sorted by core index, which its binary search relies on

The PR is open and under review.

#### **Introduce `try_state` Hooks for NIS, Offences, Node Authorization, MMR, Transaction Storage, Uniques, and NFTs Pallets**
I opened seven more `try_state` PRs, each defining and asserting the storage invariants that hold for its pallet:
- `pallet-nis`: [PR #13101](https://github.com/paritytech/polkadot-sdk/pull/13101)
- `pallet-offences`: [PR #13102](https://github.com/paritytech/polkadot-sdk/pull/13102)
- `pallet-node-authorization`: [PR #13104](https://github.com/paritytech/polkadot-sdk/pull/13104)
- `pallet-mmr`: [PR #13105](https://github.com/paritytech/polkadot-sdk/pull/13105)
- `pallet-transaction-storage`: [PR #13106](https://github.com/paritytech/polkadot-sdk/pull/13106)
- `pallet-uniques`: [PR #13107](https://github.com/paritytech/polkadot-sdk/pull/13107)
- `pallet-nfts`: [PR #13108](https://github.com/paritytech/polkadot-sdk/pull/13108)

All seven are open and under review.

---

### Flexible & Developer-Focused

#### **`fatxpool`: Hold the Transaction Pool as a Trait Object Instead of a Wrapper**
I merged [PR #12845](https://github.com/paritytech/polkadot-sdk/pull/12845) (+374/-545), which closes [issue #5489](https://github.com/paritytech/polkadot-sdk/issues/5489). `TransactionPoolWrapper` was a struct wrapping a boxed transaction pool, there only to give it a sized type, and it needed ~190 lines forwarding every trait method to the inner box. `TransactionPoolHandle` is now a type alias for the trait object itself, so the forwarding layer is gone.

The PR also folds in [issue #12942](https://github.com/paritytech/polkadot-sdk/issues/12942), which I opened after finding that the `Client` type parameter on `FullClientTransactionPool` was phantom: all three of its associated types resolve without it. Removing it also removed the `BlockIdTo` and `TaggedTransactionQueue` client bounds that existed only to build a pool. Those bounds are gone from `build_network`, `build_network_advanced`, `spawn_tasks`, `gen_rpc_module` and the cumulus `build_network`. The service parameter types now accept `?Sized` pools, so an alternative pool implementation can define its own error and transaction types. The change touches the service builders across Substrate, Polkadot, Cumulus and the omni-node.

---

### Interoperable & Compatible

#### **`litep2p`: Serve Multiple Kademlia Requests on One Inbound Substream**
I opened [PR #647](https://github.com/paritytech/litep2p/pull/647), which closes [issue #467](https://github.com/paritytech/litep2p/issues/467). The Kademlia spec requires implementations to handle further requests on a substream a peer has already used. `litep2p` was closing the substream after the first response, so go-libp2p peers kept losing their cached stream mid-conversation. Now, once the response is written, substreams opened by the remote go back to reading, with the existing 15s read timeout as the idle window, and `ADD_PROVIDER` no longer drops the substream just because the spec gives it no reply. The PR also stops treating a failure on one of those substreams as the peer disconnecting. Before, whenever an inbound substream timed out, every outbound query in flight with that peer failed. This improves interoperability with other libp2p implementations. The PR is open and under review.

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
