# Argument-0003: Retention at Rank I

|                  |                  |
| ---------------- | ---------------- |
| **Report Date**  | 2026/11/24       |
| **Submitted by** | Nasihudeen Jimoh |
| **Sponsored by** | Bryan Chen (XCM) |

## Member details

- Matrix username: @kanas0:matrix.org
- Polkadot address: 12pCUGSwoW4Xek48TLUHCFhrvAdjmciMMLJoRJD8HWP5saXH
- Current rank: I
- Date of initial induction: 2025/10/31
- Date of last report: 2026/08/25
- Link to last report: [Argument-0002: Retention at Rank I](https://github.com/polkadot-fellows/Evaluations/blob/main/argument/Kanasjnr/0002-2026-08-retention-rank-1.md)
- [Subsystems](../../subsystems.md) developed/maintained:
  - Runtimes (Engineering, Security, Benchmarking)
  - System chains
  - XCM
  - Staking

## Reporting period

- Start date: 2026/08/26
- End date: 2026/11/24

## Argument

Most of this period went into a kill switch for Asset Hub Polkadot. Next to that I kept fixing bugs and cleaning up in `polkadot-sdk`, where eleven of my PRs were merged ([list](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AKanasjnr+is%3Amerged+merged%3A2026-08-26..2026-11-24)). One of them is [descriptive module invalidity (#11724)](https://github.com/paritytech/polkadot-sdk/pull/11724), which was still waiting to be merged when I wrote my last argument.

I've grouped the work by subsystem.

### Runtimes / System chains: a kill switch for Asset Hub Polkadot

**The problem.** The dotUSD incident made it clear that when something breaks on Asset Hub, we can't stop the affected calls quickly. Even the Fellowship fast track is slower than an attacker needs to drain funds. Basti opened [runtimes#1338](https://github.com/polkadot-fellows/runtimes/issues/1338) for this. My earlier safe-mode / tx-pause PR ([runtimes#1164](https://github.com/polkadot-fellows/runtimes/pull/1164), which I listed as ongoing last time) didn't help here, because only governance could flip the switches, so it was just as slow. I closed it and started again with the design below, which still uses tx-pause underneath.

**The solution.** [runtimes#1344](https://github.com/polkadot-fellows/runtimes/pull/1344) adds `pallet-kill-switch` and wires it into Asset Hub Polkadot. How it works:

- Anyone can pause a target by putting down a deposit, and the pause ends by itself after a day.
- The Fellowship or Root can end it early with `unpause(target, slash)`. An honest pause gets its deposit back. A griefing one gets slashed, and the target goes on cooldown so it can't be paused again straight away.
- Anyone can extend a pause with another deposit. The Fellowship can extend it without one, up to a cap.
- Root can `force_pause`, and only Root can touch a pause that Root started.
- A target is a group of calls with its own deposit. There are four to start with: `Psm`, `Swaps`, `AssetTransfers` and `XcmTransfers`. The deposits are `pallet-parameters` values that only Root can change.
- Under the hood it pauses through tx-pause, whose own origins are set to nobody. It's in the base call filter and the XCM `SafeCallFilter`, so a paused call stays blocked inside `utility`, `proxy` and `multisig`, and through `Transact` too. System, governance and anything the chain needs to keep running can never be paused.
- The PR also adds a `KillSwitchApi` runtime API, along with benchmarks, tests and try-runtime checks.

Basti and Bryan are reviewing it. For the second part (inbound XCM), I posted a design on [#1338](https://github.com/polkadot-fellows/runtimes/issues/1338#issuecomment-7100017909). I've also written a runbook and a draft of what the Fellowship would commit to: who reacts, how fast, and when to slash or refund. Once the pallet has had some feedback, I'll put that up as a Members-track remark.

### Runtimes (Engineering, Security): FRAME fixes

**The problem.** `pallet-core-fellowship`, the Fellowship's own pallet, read salaries and periods by indexing straight into the `Params` vectors. Those vectors are only bounded by `MaxRank`, so `set_params` could store a shorter one. `get_salary`, `bump` and `promote` would then panic for any member whose rank was past the end ([#13141](https://github.com/paritytech/polkadot-sdk/issues/13141)).

**The solution.** All three places now use `get` and fall back to the default, so a rank past the end gets treated like rank 0 already is. There's a unit test for each one ([#13182](https://github.com/paritytech/polkadot-sdk/pull/13182), merged).

**The problem.** If a pallet rejected a transaction during validation, the pool only said `InvalidTransaction`, so wallets and indexers couldn't tell the user what went wrong ([#11337](https://github.com/paritytech/polkadot-sdk/issues/11337)).

**The solution.** I added a `Module(ModuleError)` variant at the end of `InvalidTransaction`, so none of the existing encodings change. Clients can now look the error up in metadata, the same way they already do for `DispatchError::Module` ([#11724](https://github.com/paritytech/polkadot-sdk/pull/11724), merged). While Reviewing it Basti noticed the error data comes back in different shapes from different RPC methods, so I opened [json-rpc-interface-spec#188](https://github.com/paritytech/json-rpc-interface-spec/issues/188).

### Staking: bags-list rebagging

**The problem.** `pallet-bags-list::on_idle` decided where to resume before its loop even ran. If it ran out of weight or got locked halfway, the cursor still skipped ahead past nodes it never processed. Those nodes then sat in the wrong bag until the scan wrapped around to the start again ([#13138](https://github.com/paritytech/polkadot-sdk/issues/13138)).

**The solution.** It now works out the resume point after the loop, from how many items it actually got through, so it's right however the loop ends. I added a test where the weight runs out before the count limit ([#13184](https://github.com/paritytech/polkadot-sdk/pull/13184), merged).

### Nodes: gossip deduplication

**The problem.** `sc-network-gossip` relied on `LruMap::insert` to catch duplicates. But `insert` also returns `true` when it replaces an existing entry, so calling `register_message` or `multicast` twice with the same message added it to the cache twice, and the copy could get rebroadcast ([#12607](https://github.com/paritytech/polkadot-sdk/issues/12607)).

**The solution.** It now checks `known_messages.get()` before inserting, which is what the incoming-message path already did ([#12694](https://github.com/paritytech/polkadot-sdk/pull/12694), merged).

### Ongoing maintenance

I kept going with the deprecation cleanup from last period. This time I removed `BuildModuleGenesisStorage` ([#12990](https://github.com/paritytech/polkadot-sdk/pull/12990)), the `build-spec` CLI subcommand ([#12586](https://github.com/paritytech/polkadot-sdk/pull/12586)), the old `BlockLength` constructors ([#13348](https://github.com/paritytech/polkadot-sdk/pull/13348)) and the `construct_runtime!` where clause ([#13349](https://github.com/paritytech/polkadot-sdk/pull/13349)). I also re-exported the hashing free functions through `sp_io` ([#12753](https://github.com/paritytech/polkadot-sdk/pull/12753)).

I also cut some dead code: the unused `ChildBountyCount` storage ([#13333](https://github.com/paritytech/polkadot-sdk/pull/13333), plus the runtime side in [runtimes#1328](https://github.com/polkadot-fellows/runtimes/pull/1328)), and the stale `pallet-people` and `pallet-dummy-dim` crates ([#13585](https://github.com/paritytech/polkadot-sdk/pull/13585)). There's probably more like this, so I opened [#13507](https://github.com/paritytech/polkadot-sdk/issues/13507) to audit for other unused storage, and [#13513](https://github.com/paritytech/polkadot-sdk/issues/13513) for `RingBuildingPeopleLimit`, which nothing ever reads or sets.

Still in review:

- [#12696](https://github.com/paritytech/polkadot-sdk/pull/12696): the state-trie-migration RPC panics on child roots of the wrong length.
- [#13612](https://github.com/paritytech/polkadot-sdk/pull/13612): `pallet-session` releases the key deposit from the wrong account.
- [#13645](https://github.com/paritytech/polkadot-sdk/pull/13645): `fungible` won't accept a deposit below ED into an account that has funds on hold.

Where the PRs from my last argument stand:

- [#11732](https://github.com/paritytech/polkadot-sdk/pull/11732) (`ExtrinsicBaseWeight`): I've made the requested changes, and it needs one last review.
- [#11302](https://github.com/paritytech/polkadot-sdk/pull/11302) (XCM barrier `Outcome::Incomplete`): the benchmarks have been re-run, and it's waiting on review.
- [#11695](https://github.com/paritytech/polkadot-sdk/pull/11695) (deprecating private pallet storage types): this is stuck on what to do about storage that old migrations still use.

### Reviews

I reviewed [#13699](https://github.com/paritytech/polkadot-sdk/pull/13699) and [#13674](https://github.com/paritytech/polkadot-sdk/pull/13674) in `polkadot-sdk`, and [runtimes#1285](https://github.com/polkadot-fellows/runtimes/pull/1285) (the AHMv2 migrator). That's not a lot. Next period I want to review more, mainly in Runtimes and XCM.

### Next period

- Get runtimes#1344 merged, and put the Fellowship commitments up for a vote.
- Open the inbound XCM PR (the second part of #1338).
- Get the PRs left over from 0002 merged.

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments                                                    |
| ----- | ------------------- | -------------------- | -------------------------- | ----------------------------------------------------------- |
| I     | 90%                 | N/A                  | N/A                        | No Rank I–eligible referenda to vote on during this period  |
| II    | 80%                 | N/A                  |                            |                                                             |
| III   | 70%                 | 100%                 |                            |                                                             |
| IV    | 60%                 | 90%                  |                            |                                                             |
| V     | 50%                 | 80%                  |                            |                                                             |
| VI    | 40%                 | 70%                  |                            |                                                             |

## Misc

- Question(s):
- Concern(s):
- Comment(s):
