# Argument-0007: Retention at Rank III

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2026/07/23 |
| **Submitted by** | skunert    |

## Member details

- Matrix username: `@sebastian:parity.io`
- Polkadot address: `1682A5hxfiS1Kn1jrUnMYv14T9EuEnsgnBbujGfYbeEbSK3w`
- Current rank: 3
- Date of initial induction: 2024/01/08
- Date of last report: 2026/01/25
- Link to last report: [Referendum 467](https://collectives.subsquare.io/fellowship/referenda/467)
- Area(s) of Expertise/Interest: `Cumulus Node`, `Substrate Node`, `Parachain Authoring`, `Weight`

## Reporting period

- Start date: 2026/01/25
- End date: 2026/07/17

## Argument

During this reporting period my own technical focus was on enabling storage chains to sync with warp sync, which was not possible before. In addition, I continued my usual mentoring, tech leadership and review activities on `polkadot-sdk`.

### Syncing support for storage chains

Chains built on `pallet-transaction-storage` (like the Bulletin Chain) index large data payloads in the node database as a side effect of block execution. This model breaks down for nodes that do not execute every block from genesis: a node that tip-syncs past a `Renew` extrinsic after warp-sync never executed the original `Store`. Therefore does not hold the referenced payload locally and will be unable to serve this data or produce blocks. I designed and implemented the mechanism that closes this gap by fetching missing payloads from the network during sync:

- **`TransactionStorageApi` v2** ([#11939](https://github.com/paritytech/polkadot-sdk/pull/11939)): New runtime API version that allows the client to query which transactions are indexed by a block, so missing payloads can be identified without re-executing history. I also prepared the Bulletin Chain for the new API version ([bulletin#471](https://github.com/paritytech/polkadot-bulletin-chain/pull/471)).
- **Bitswap client** ([#12038](https://github.com/paritytech/polkadot-sdk/pull/12038)): `sc-network` previously only served inbound bitswap requests. I added a public client API for fetching CID-addressed data from peers, including wiring outbound requests through the litep2p backend. Follow-up: sync peer roles are now exposed to consumers of sync events ([#12598](https://github.com/paritytech/polkadot-sdk/pull/12598)).
- **Prefetched indexed transactions** ([#12086](https://github.com/paritytech/polkadot-sdk/pull/12086)): A carrier mechanism in `sc-client-db` that lets block-import implementations supply payloads and index operations that block execution cannot provide, covering both tip-sync (payload missing) and gap-sync (block not executed) cases.
- **`StorageChainBlockImport`** ([#12242](https://github.com/paritytech/polkadot-sdk/pull/12242)): A block-import wrapper that detects missing payloads for `Renew` operations during tip-sync, fetches them over bitswap and hands them to the database backend via the carrier above.

Along the way I found and fixed a ParityDB correctness bug where a store + reference on the same value within one transaction resulted in the value not being stored at all ([#12082](https://github.com/paritytech/polkadot-sdk/pull/12082)), and extended the client runtime-API interface to support calls on top of a custom storage overlay ([#12084](https://github.com/paritytech/polkadot-sdk/pull/12084)).

As a follow-up, I am currently reworking the bitswap client and server ([#12686](https://github.com/paritytech/polkadot-sdk/pull/12686)): Bitswap moves out of `sc-network` into a dedicated `sc-network-bitswap` crate, replacing the backend-specific implementations with a single actor-driven service and a streaming handle API. This centralizes CID deduplication, peer selection, retries, failover and backpressure handling, simplifies the integration with storage-chain sync, and improves test coverage. This work is in progress.

### System chain contributions

- **Polkadot People Chain block production fix** ([runtimes#1154](https://github.com/polkadot-fellows/runtimes/pull/1154)): After the migration to 24s Aura slots, collators produced blocks only infrequently and logged `Slot must increase`. With elastic scaling, multiple blocks per slot must be permitted. I fixed the runtime configuration and prepared release 2.2.2, which was enacted via [Referendum 519](https://collectives.subsquare.io/fellowship/referenda/519).
- Moved the runtime upgrade testing guide into the `runtimes` repository to make the release process better documented ([runtimes#1066](https://github.com/polkadot-fellows/runtimes/pull/1066)).

### Node maintenance & robustness

I continue to apply general fixes across the node. I fixed a warp sync stall of up to 30 minutes ([#11152](https://github.com/paritytech/polkadot-sdk/pull/11152)), simplified the parent-search logic in the cumulus block-building path ([#10998](https://github.com/paritytech/polkadot-sdk/pull/10998)), fixed missed transaction status updates in the fork-aware transaction pool ([#10965](https://github.com/paritytech/polkadot-sdk/pull/10965)) and added Asset Hub Polkadot support to the omni-node ([#10978](https://github.com/paritytech/polkadot-sdk/pull/10978)).
One more workstream that is in flight is an improvement to the compact proof encoding that we use in Substrate. I removes duplicates from the proof encodings. The work is under review [here](https://github.com/paritytech/trie/pull/233).

### Knowledge sharing, reviews & advisory

- I continue to lead the Node-SDK team at Parity, guiding and onboarding contributors on node-related projects.
- We took the Smoldot project into the Node-SDK team, I onboarded the contributors onto the projects and led the discussions around bug fixes, improvements and scalability.
- Very active reviewer during the reporting period:
  - polkadot-sdk PRs (67): [list](https://github.com/paritytech/polkadot-sdk/pulls?q=is:pr+reviewed-by:skunert+created:2026-01-25..2026-07-17)
  - Runtime PRs (6): [list](https://github.com/polkadot-fellows/runtimes/pulls?q=is:pr+reviewed-by:skunert+created:2026-01-25..2026-07-17)
  - Bulletin Chain PRs (4): [list](https://github.com/paritytech/polkadot-bulletin-chain/pulls?q=is:pr+reviewed-by:skunert+created:2026-01-25..2026-07-17)
  - Smoldot (45): [list](https://github.com/paritytech/smoldot/pulls?q=is:pr+reviewed-by:skunert+created:2026-01-25..2026-07-17)
- Regular participant in fellowship calls.

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                    | Comments |
| ----- | ------------------- | -------------------- | --------------------------------------------------------------------------------------------- | -------- |
| III   | 70%                 | 100%                 | I have voted on 53 out of 62 referenda in which I was eligible to vote (85% voting activity). |          |
