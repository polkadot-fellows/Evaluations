# Argument-0003: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/08/09                                                             |
| **Submitted by**| Enoch                                                                        |


## Member details

- Matrix username: @runcomet:matrix.org
- Polkadot address: 14SRqZTC1d8rfxL8W1tBTnfUBPU23ACFVPzp61FyGf4ftUFg
- Current rank: I
- Date of initial induction: [2025-10-30](https://collectives.statescan.io/#/extrinsics/7488182-2)
- Date of last report: 2026/05/07
- Link to last report: [Argument-0002](https://github.com/polkadot-fellows/Evaluations/blob/main/argument/runcomet/0002-runcomet-04-2026-retain_at-rank-I.md) ([referendum 522](https://collectives.subsquare.io/fellowship/referenda/522))
- Area(s) of Expertise/Interest: FRAME, Node, Coretime


## Reporting period

- Start date: 2026/05/07
- End date: 2026/08/09


## Argument
The Coretime sale identity work merged this period. The rest went to maintenance and fixes from whitebox fuzzing reports.

### Coretime sale identity ([#10188](https://github.com/paritytech/polkadot-sdk/pull/10188), merged 2026/07/07)
`pallet-broker` sells bulk Coretime in successive sales, but a sale had no identifier. `SaleInfoRecord` and the `SaleInitialized` event carried only region boundaries, so indexers, renewal tooling and revenue accounting had to infer which sale a purchase or renewal belonged to from timeslice arithmetic. The PR adds a sequential `sale_index`, incremented on each `rotate_sale`. `MigrateV4ToV5` back-fills the record already on chain from the first sale's `region_begin`, supplied by the runtime through a `FirstSaleRegion` trait, so existing sales keep their real index instead of being renumbered.

### Maintenance ([#12630](https://github.com/paritytech/polkadot-sdk/pull/12630), merged 2026/07/21; [#12647](https://github.com/paritytech/polkadot-sdk/pull/12647), in review)
Two open issues where a runtime change left a recurring cost downstream: on client authors, and on every future release.

`pallet-staking-async`, unbonding era ([#12578](https://github.com/paritytech/polkadot-sdk/issues/12578)): the unbonding duration is now dynamic, 2 eras for pure nominators, who are no longer slashable, and `BondingDuration` for anyone who validated within the last `BondingDuration` eras. Clients could previously add a constant to the active era to get the unlock era. They now have to replicate `AreNominatorsSlashable`, the `LastValidatorEra` guard and the active era at inclusion, or read the ledger back, so every wallet and explorer reimplements runtime logic to show when a nominator's funds unlock, and any that kept the old constant shows a wrong date. `Event::Unbonded` now carries the `era` at which the amount becomes withdrawable. One field on an existing event and no migration; the prdoc calls out the shape change for decoders that hardcode it.

Westend system chains, executed migrations ([#11771](https://github.com/paritytech/polkadot-sdk/issues/11771)): one-shot migrations that have already run stay in the `Migrations` tuple and are re-read, re-audited and re-shipped on every release, but removing one that has not executed everywhere leaves state half-migrated. Each removal was checked against live Westend state (all system chains on spec 1024001) for its post-migration storage version, or, where the migration bumps no version, for the effect it was meant to leave. The [verification script](https://gist.github.com/runcomet/1fac906cf1197519a92a3c60aefed23e) is published so a reviewer can rerun it. Three migrations were kept, including the staking-async ones, since `Staking` is still at v17 on-chain. Westend system chains are where these tuples are staged before Kusama and Polkadot, so the method, and most of the list, carries to the production runtimes.

### Fixes from whitebox fuzzing reports ([#12689](https://github.com/paritytech/polkadot-sdk/pull/12689), [#12688](https://github.com/paritytech/polkadot-sdk/pull/12688), in review)
Two findings from a whitebox fuzzing sweep of FRAME pallets, each reduced to a reachable path and fixed.

`pallet-broker`, duplicate auto-renewal ([#12602](https://github.com/paritytech/polkadot-sdk/issues/12602)): `do_enable_auto_renew` derived its insertion index with `binary_search_by(..).unwrap_or_else(|e| e)`, which collapses the `Ok` and `Err` cases into the same position before `try_insert`, so enabling auto-renewal twice for a core inserted a duplicate `AutoRenewalRecord` and broke the sorted-unique invariant on `AutoRenewals`. The path is user-reachable: the `workload_end_hint` branch only reads `PotentialRenewals`, so the preconditions pass on every call. Duplicates make `rotate_sale`/`renew_cores` charge the payer once per copy, consume the `MaxAutoRenewals` bound shared with every other auto-renewing chain, and leave orphans behind `disable_auto_renew`, which removes a single position. This runs on the live Coretime chain. A second enable now returns `AutoRenewalAlreadyEnabled`.

`pallet-scheduler`, `cancel_named` state leak ([#12603](https://github.com/paritytech/polkadot-sdk/issues/12603)): `do_cancel_named` removed the task and its `Lookup` entry regardless of origin, but cleared `Retries` and dropped the preimage only inside the `origin.is_some()` branch. The `schedule::v2::Named` and `v3::Named` impls cancel with `origin = None`, which is how other pallets cancel, so those cancellations left an orphaned `RetryConfig` pointing at a task that no longer exists and a preimage that stays requested with its deposit held. Cleanup now runs whenever the task is removed, matching the anonymous `do_cancel`.

### `create_with_id` for `pallet-nfts` ([#11212](https://github.com/paritytech/polkadot-sdk/pull/11212), in review)
Collection IDs come from a counter, so a pallet that needs a fixed collection per on-chain entity cannot know the ID before creating it. Each one wraps `create_collection_with_id`, picks an ID out of the shared space and stores the mapping itself, which every consumer repeats and which can collide between them. Deriving the ID from the calling origin makes the mapping one-to-one and computable without a lookup.

### `pallet-asset-rewards` on the Asset Hubs ([runtimes#1222](https://github.com/polkadot-fellows/runtimes/pull/1222), in review)
Requested in [runtimes#921](https://github.com/polkadot-fellows/runtimes/issues/921) and blocked on [#9816](https://github.com/paritytech/polkadot-sdk/issues/9816), the missing `BlockNumberProvider` that made the pallet unusable on a parachain. That fix landed upstream; I confirmed the blocker was gone and did the integration. The Asset Hubs hold Polkadot's assets and liquidity but have no runtime primitive for rewarding holders who stake them, so reward programmes run off-chain or custodially. This wires `pallet-asset-rewards` and `pallet-assets-freezer` into both runtimes, with asset unions covering pool assets so LP tokens are stakeable, and `CreatePoolOrigin = EnsureSigned` behind a `HoldConsideration` deposit so pools are permissionless and their storage stays paid for. `BlockNumberProvider = RelaychainDataProvider` diverges from Asset Hub Westend: parachain block numbers pause and change cadence, which would rescale reward rates and expiries.

### Deferred dispatch end-to-end tests ([PET#595](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/595), in review)
Deferred dispatch changes how a whitelisted governance call reaches execution, and its failure modes (an authorisation consumed early, an entry removed before it expires, a preimage missing at execution) only show up against real runtime state, which is what `polkadot-ecosystem-tests` runs against before a release. The suite covers the success and failure paths on Kusama and Polkadot Asset Hub. This period it was refactored onto the shared-client pattern from [#609](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/609) at the reviewer's request.


## Voting record
|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |0 of 0 referenda in which I was eligible to vote.  |71 referenda opened this period, none on the `members` track. `MinRankOfClass` makes that the only class a Rank I member may vote on; the rest required Rank III or above.  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
