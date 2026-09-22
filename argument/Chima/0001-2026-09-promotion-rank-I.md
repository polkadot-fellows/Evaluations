# Argument-0001: Promotion to Rank I

|                  |              |
| ---------------- | ------------ |
| **Report Date**  | 2026/09/22   |
| **Submitted by** | Hillary Chima (PSYKYODAI) |


## Member details

- Matrix username: @psykyodai:matrix.org
- Polkadot address: 14miiyFptygSQMQUoeU8QJXHPYnb5JXSTDHMTiWNnwcxHYU1
- Current rank: Candidate
- Date of initial induction: 2026/09/18 ([application #27](https://collectives.subsquare.io/fellowship/applications/27))
- Date of last report: N/A
- Link to last report: N/A
- Area(s) of Expertise/Interest: FRAME/Runtime, JAM


## Reporting period

- Start date: 2025/07/05
- End date: 2026/09/22


## Argument

Before Polkadot I pentested wallets and smart contracts. On the runtime I look for rules people count on that the code doesn't enforce.

The work below covers a governance call anyone could front-run by taking its asset id first, a storage counter that went up when someone appended to a key that already existed, and a whitelisted call that could sit on the relay chain because nobody would pay to dispatch it. The first mattered most. The Individuality upgrade depended on that fix, but it wasn't in the release yet, so I proposed a migration in review that let the upgrade ship with PGAS working (see [Reviews](#reviews)).

I learned the runtime from other people's pull requests and the reviews on them. I want to do the same for others by reviewing runtime changes and helping move RFCs forward.

### 1. Asset ids reserved for governance

[polkadot-sdk#12378](https://github.com/paritytech/polkadot-sdk/pull/12378), raised in [#12302](https://github.com/paritytech/polkadot-sdk/issues/12302).

With auto-increment on, `force_create` had to use the next id in the sequence. Anyone creating an asset first took that id and made the governance call fail, and Asset Hub could not reserve a range for system assets below its 50,000,000 start. `ForceOrigin` can now create at any unused id while the sequence keeps running.

### 2. Merkle proof preallocation

[polkadot-sdk#12288](https://github.com/paritytech/polkadot-sdk/pull/12288), raised in [#9106](https://github.com/paritytech/polkadot-sdk/issues/9106).

Building a merkle proof in `binary-merkle-tree` reallocated its vector as it grew, though its final length, ⌈log2 n⌉, is known before the first step. The crate backs BEEFY MMR proofs and the bridges' BEEFY primitives. I allocate the proof at that length from the start.

### 3. Per-pool swap fee

[polkadot-sdk#12369](https://github.com/paritytech/polkadot-sdk/pull/12369), requested in [#12301](https://github.com/paritytech/polkadot-sdk/issues/12301).

Every pool in `pallet-asset-conversion` paid the same fee, 0.3% on Asset Hub, though stable and volatile pairs warrant different fees. I added an optional per-pool fee that falls back to the global one. It is set through a separate `create_pool_with_fee` call, so `create_pool` keeps its encoding, and existing pools need no migration.

### 4. Permissionless authorised dispatch (approved)

[polkadot-sdk#12452](https://github.com/paritytech/polkadot-sdk/pull/12452), implementing RFC [#12224](https://github.com/paritytech/polkadot-sdk/issues/12224).

Asset Hub governance can whitelist a relay-chain call by hash in a small XCM message, but someone still has to dispatch the full call on the relay chain. The RFC lets anyone do it unsigned and fee-free. I added `#[pallet::authorize]` to both dispatch calls in `pallet-whitelist` and moved to pool admission every check the dispatch would otherwise fail with nobody charged: runtime opt-in, the hash, a decodable preimage, and weight within the witness. Reviewed by bkontur, who cited it in supporting my induction.

### Honourable mentions

- [polkadot-sdk#13031](https://github.com/paritytech/polkadot-sdk/pull/13031) `frame-support`: appending to an existing key in `CountedStorageMap` or `CountedStorageNMap` raised the counter though no key was added, so `count()` stayed above the stored keys for good. I added the same `contains_key` guard that `append` uses. Reported in [#12782](https://github.com/paritytech/polkadot-sdk/issues/12782) by the Runtime Whitebox Fuzzer as medium severity. Reviewed by bkontur and gui, who cited it in supporting my induction.
- [polkadot-sdk#9107](https://github.com/paritytech/polkadot-sdk/pull/9107) `pallet-proxy`: the creation block in `PureCreated`, from the pallet's `BlockNumberProvider`. After the Asset Hub migration wallets could not easily find the relay-chain block a pure proxy was created in, which killing it requires. Reported by Nova Wallet in [#9066](https://github.com/paritytech/polkadot-sdk/issues/9066).

### Open

- [polkadot-sdk#12690](https://github.com/paritytech/polkadot-sdk/pull/12690) `paras`: replace the empty-vector validation-code sentinel in `UpcomingParasGenesis` with a dedicated `UpcomingParaGenesis`, plus a versioned migration for Westend and Rococo.

All pull requests: [paritytech/polkadot-sdk, author PSYKYODAI](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3APSYKYODAI)

### Reviews

[polkadot-fellows/runtimes#1233](https://github.com/polkadot-fellows/runtimes/pull/1233) Integrate Individuality into People and Asset Hub Polkadot (merged)

The upgrade's migration creates the PGAS asset at a fixed id, which Asset Hub's auto-increment ids reject without #12378 above. That fix was not in the 2604 release the runtimes build on, so the upgrade would have shipped with no PGAS asset and every PGAS flow dead. A backport or workaround was requested as urgent.

I [proposed a runtime-side migration instead of a backport](https://github.com/polkadot-fellows/runtimes/pull/1233#discussion_r3734893409): take `NextAssetId`, create PGAS, restore the counter, with a try-runtime check that the asset exists. I also noted what it leaves open. The two id ranges are then separated only by distance, so `create` stalls if the sequence reaches 2,000,000,000, and once #12378 is pinned its default allocator would move later permissionless ids into the reserved range. For that I proposed a `ReservedFloorAllocator` bounded by a floor governance can raise through `pallet-parameters`. The migration was adopted in [`2e987a5`](https://github.com/polkadot-fellows/runtimes/pull/1233/commits/2e987a5232635acbd77d225c04404a849ec8a2e5) and the PR merged.

## Voting record

N/A. Candidates hold no rank and are not eligible to vote on Fellowship referenda.


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
