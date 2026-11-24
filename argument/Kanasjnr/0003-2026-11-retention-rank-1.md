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

This period most of my time went into one piece of system-chain safety work, a kill switch for Asset Hub Polkadot, alongside steady correctness and cleanup work in `polkadot-sdk`. Eleven of my `polkadot-sdk` pull requests were merged in the period ([list](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AKanasjnr+is%3Amerged+merged%3A2026-08-26..2026-11-24)). They include [descriptive module invalidity (#11724)](https://github.com/paritytech/polkadot-sdk/pull/11724), which was still pending when I submitted my last argument.

The sections below are organised by subsystem.

### Runtimes / System chains: a kill switch for Asset Hub Polkadot

**The problem.** The dotUSD incident showed that once something goes wrong on Asset Hub, the chain has no quick way to stop the affected calls. Even the Fellowship fast track takes longer than an exploit needs to drain funds. Basti opened [runtimes#1338](https://github.com/polkadot-fellows/runtimes/issues/1338) to fix that. My earlier safe-mode / tx-pause deployment ([runtimes#1164](https://github.com/polkadot-fellows/runtimes/pull/1164), listed as ongoing in my last argument) only gave governance-controlled switches, which doesn't solve the reaction-time problem. I closed it in favour of the design below, which builds on tx-pause rather than replacing it.

**The solution.** [runtimes#1344](https://github.com/polkadot-fellows/runtimes/pull/1344) adds a new `pallet-kill-switch` and wires it into Asset Hub Polkadot:

- **Pausing.** Anyone can pause a target by putting up a deposit. The pause expires on its own after a day.
- **Ending a pause.** The Fellowship or Root can end a pause early with `unpause(target, slash)`: an honest pause gets its deposit back, and a griefing pause is slashed and the target put on cooldown.
- **Extending a pause.** Anyone can extend a pause with another deposit, and the Fellowship can extend one without a deposit, up to a cap.
- **Root.** Root can `force_pause`, and only Root can change a pause that Root started.
- **Targets.** Targets are runtime-defined groups of calls, each with its own deposit: `Psm`, `Swaps`, `AssetTransfers` and `XcmTransfers` to start with. Deposits are `pallet-parameters` values that only Root can change.
- **Enforcement.** Pauses are enforced through tx-pause, whose own origins are set to nobody. The kill switch sits in both the base call filter and the XCM `SafeCallFilter`, so a paused call is also blocked inside `utility`/`proxy`/`multisig` and through `Transact`. System, governance and the pallets the chain needs to keep running can never be paused.
- **Testing and tooling.** The PR includes a `KillSwitchApi` runtime API, benchmarks, tests and try-runtime checks.

The PR is in review with Basti and Bryan. I also posted the design for the second phase, covering inbound XCM, on [#1338](https://github.com/polkadot-fellows/runtimes/issues/1338#issuecomment-7100017909). I've written an operational runbook and a proposed set of Fellowship commitments (who reacts, how fast, and when to slash or refund). Once there's feedback on the pallet, I'll put the commitments up as a Members-track remark.

### Runtimes (Engineering, Security): FRAME correctness

**The problem.** `pallet-core-fellowship`, the Fellowship's own pallet, read salary and period values by indexing directly into `Params` vectors. Those vectors are only bounded by `MaxRank`, so a `set_params` call could store a shorter vector, and `get_salary`, `bump` and `promote` would then panic for any member ranked past its end ([#13141](https://github.com/paritytech/polkadot-sdk/issues/13141)).

**The solution.** All three call sites now look values up with `get` and fall back to the default, so an out-of-range rank degrades the same way rank 0 already does. Each case has a unit test ([#13182](https://github.com/paritytech/polkadot-sdk/pull/13182), merged).

**The problem.** When a transaction failed validation inside a pallet, the transaction pool reported only a generic `InvalidTransaction`, so wallets and indexers couldn't tell users why it was rejected ([#11337](https://github.com/paritytech/polkadot-sdk/issues/11337)).

**The solution.** I appended a `Module(ModuleError)` variant to `InvalidTransaction`, without changing any existing encoding. Clients can now resolve the rejection against metadata the same way they resolve `DispatchError::Module` ([#11724](https://github.com/paritytech/polkadot-sdk/pull/11724), merged). While doing this I found that the error data shape is inconsistent across RPC methods, and filed it as [json-rpc-interface-spec#188](https://github.com/paritytech/json-rpc-interface-spec/issues/188).

### Staking: bags-list rebagging

**The problem.** `pallet-bags-list::on_idle` set its resume cursor from a count budget computed *before* the loop. If the weight meter ran out or the pallet locked partway through, the cursor still jumped past nodes that had never been processed, and those nodes stayed in the wrong bag until the scan eventually wrapped around ([#13138](https://github.com/paritytech/polkadot-sdk/issues/13138)).

**The solution.** The resume point is now computed after the loop, from the number of items it actually processed, which is correct however the loop ends. A regression test covers the case where weight runs out before the count budget ([#13184](https://github.com/paritytech/polkadot-sdk/pull/13184), merged).

### Nodes: gossip deduplication

**The problem.** `sc-network-gossip` used `LruMap::insert` as its dedup guard. `insert` returns `true` for replacements too, so calling `register_message` or `multicast` twice with the same message added duplicate cache entries, which could then be rebroadcast ([#12607](https://github.com/paritytech/polkadot-sdk/issues/12607)).

**The solution.** An explicit `known_messages.get()` check now runs before the insert, matching the incoming-message path ([#12694](https://github.com/paritytech/polkadot-sdk/pull/12694), merged).


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
