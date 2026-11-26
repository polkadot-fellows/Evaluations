# Argument-0004: Retention at Rank I

| Report Date | 2026/24/11 |
|---|---|
| Submitted by | Enoch(runcomet) |
| Sponsored by | Donál |

## Member details

- Matrix username: @runcomet:matrix.org
- Polkadot address: 14SRqZTC1d8rfxL8W1tBTnfUBPU23ACFVPzp61FyGf4ftUFg
- Current rank: I
- Date of initial induction: 2025/10/30
- Date of last report: 2026/08/09
- Link to last report: Argument-0003 (Referendum [#600](https://collectives.subsquare.io/fellowship/referenda/600))
- [Subsystems](https://github.com/polkadot-fellows/Evaluations/blob/main/subsystems.md) developed/maintained: Runtimes (FRAME, APIs, integrations), Economics (Infra: Coretime sales, Stablecoins; Governance: Issuance, DAP), Nodes (SDK, tooling, networking)

## Reporting period

- Start date: 2026/08/09
- End date: 2026/24/11

## Argument

This period I worked on the Polkadot SDK in three areas: Coretime sales, FRAME pallet correctness, and networking. Most work went to `pallet-broker`. The rest went to fee pallets and `litep2p`.

### Economics (Coretime sales) and Scalability (Agile Coretime)

**Auto-renewal integrity ([#12689](https://github.com/paritytech/polkadot-sdk/pull/12689) merged).** Auto-renewal lets a parachain keep its core without bidding every sale. `do_enable_auto_renew` let one core hold several `AutoRenewalRecords`. This broke the sorted-unique invariant on `AutoRenewals`. Three failures followed. The payer was charged once per duplicate. Spurious records consumed `MaxAutoRenwals`. `disable_auto_renew` left orphans behind. Operators could be billed twice for one core, or lose clean cancellation. A second enable now returns `AutoRenewalAlreadyEnabled`, so the invariant holds on the live Coretime chain.

The `renew_cores` follow-up ([#13842](https://github.com/paritytech/polkadot-sdk/pull/13842)) fixes the same problem on remapping. A stale position would point a renewal at the wrong core. That error only appears at the next sale, when fixing it costs a governance action.

**Sale and lease paths ([#13727](https://github.com/paritytech/polkadot-sdk/pull/13727) approved, [#13729](https://github.com/paritytech/polkadot-sdk/pull/13729), [#13728](https://github.com/paritytech/polkadot-sdk/pull/13728), [#13740](https://github.com/paritytech/polkadot-sdk/pull/13740), [#13730](https://github.com/paritytech/polkadot-sdk/pull/13730) awaiting review).** The Coretime chain runs continuously, but some branches are rarely hit. These include `swap_leases`, ignored and dropped outcomes in `process_revenue`, zero `region_length` in config validation, and `force_reserve` failure at rotation. These paths do not surface in ordinary operation. Risk accumulates silently.

### Runtimes (FRAME, APIs, integrations)

**[Scheduled call cancellation](https://github.com/paritytech/polkadot-sdk/pull/12688).** Named scheduled calls can be cancelled by the caller that created them and by other pallets acting on their behalf. `do_cancel_named` removed the task and its `Lookup` entry regardless of who cancelled, but cleared `Retries` and dropped the preimage only when the origin was present and the `schedule::v2::Named` and `v3::Named` Impls cancel task that left an orphaned `RetryConfig` pointing at a task that no longer exists, and a preimage that stayed requested with its deposit still held. For a user, that is a deposit locked against a call they cancelled; for a runtime integrator, it is state that does not reconcile. Cleanup now runs whenever a task is removed, matching anonymous `do_cancel`.

**[Treasury asset canonicalization](https://github.com/paritytech/polkadot-sdk/pull/13461).** Some runtimes accept several representations of one asset. Every spend path must agree on the canonical form before recording a spend. Without a hook, each path enforces this itself, and drift creeps in. `CanonicalizeAssetKind` gives the runtime one normalization point. Treasury accounting stays consistent whichever representation was submitted.

**Fee and transaction-extension coverage.** These pallets sit on every transaction path. An untested branch regresses silently: a below-ED refund lost, a skipped `post_dispatch`, a credit API that diverges from its docs. These show up as support tickets, not failing tests. This period's PRs add coverage for weight reservation and refund math ([#13600](https://github.com/paritytech/polkadot-sdk/pull/13600)), below-ED refunds ([#13649](https://github.com/paritytech/polkadot-sdk/pull/13649)), `post_dispatch` ([#13592](https://github.com/paritytech/polkadot-sdk/pull/13592)), extensions ([#13590](https://github.com/paritytech/polkadot-sdk/pull/13590)), the `TxPaymentCredit` API ([#13593](https://github.com/paritytech/polkadot-sdk/pull/13593)), and documentation ([#13584](https://github.com/paritytech/polkadot-sdk/pull/13584)). Each turns a path only a production incident would exercise into one with a documented expected outcome.

### Nodes (SDK, tooling, networking)

**litep2p address classification and connection limits ([#713](https://github.com/paritytech/litep2p/pull/713), [#712](https://github.com/paritytech/litep2p/pull/712)).** `is_global_multiaddr` decides whether a peer address is globally routable. `ConnectionLimits` bounds a node's connections. Both are correctness-critical and fail invisibly. A misclassified address routes traffic to an unreachable peer. An unenforced limit lets a node exhaust file descriptors. The tests added this period pin down classification and limit enforcement, so regressions are caught before an operator sees them.

**[sc-chain-spec error handling](https://github.com/paritytech/polkadot-sdk/pull/13945).** Chain-spec tooling builds and serves node configuration and is routinely handed presets. A non-JSON preset used to panic. A malformed preset now returns an error, so the command fails with a message instead of a crash. Maintainers get a diagnosable error at the point of the mistake.

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
| I | 90% | N/A | N/A | No referenda for my rank |
| II | 80% | N/A | | |
| III | 70% | 100% | | |
| IV | 60% | 90% | | |
| V | 50% | 80% | | |
| VI | 40% | 70% | | |

## Misc

Question(s):

Concern(s):

Comment(s):
