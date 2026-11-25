# Argument-0004: Retention at Rank I

| Report Date | 2026/24/11 |
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

During this reporting period I continued sustained contributions to the Polkadot SDK across the Coretime sale mechanics, FRAME pallet correctness and networking reliability. The bulk of the period went to `pallet-broker`, which runs the live Coretime chain, with the rest split between fee-handling pallets and `litep2p`.

### Economics (Coretime sales) and Scalability (Agile Coretime)

**Auto-renewal integrity ([#12689](https://github.com/paritytech/polkadot-sdk/pull/12689) merged and [#13842](https://github.com/paritytech/polkadot-sdk/pull/13842) awaiting review).** Auto-renewal is the mechanism that lets a parachain keep its core without bidding again every sale. The duplicate enable bug in `do_enable_auto_renew` allowed the same core to hold more than one `AutoRenewalRecord`, which broke the sorted-unique invariant on `AutoRenewals`. The ecosystem cost is concrete: `rotate_sale` and `renew_cores` would charge the payer once per duplicate, the shared `MaxAutoRenwals` bound would be consumed by spurious records, and `disable_auto_renew` which removes a single position would leave orphans behind. For a Parachain operator, that means being billed twice for one core, or losing the ability to disable a renewal cleanly. A second enable now returns `AutoRenewalAlreadyEnabled`, so the invariant holds on the live Coretime chain. 

The follow-up in `renew_cores` ([#13842](https://github.com/paritytech/polkadot-sdk/pull/13842)) closes the same gap on the remapping path, where a stale position would resurface as a renewal pointed at the wrong core on the next rotation, a failure that would only become visible at the sale boundary and becomes too late to correct cheaply.

**Sale and lease paths that are hard to reach and therefore easy to leave broken ([#13727](https://github.com/paritytech/polkadot-sdk/pull/13727) approved, [#13729](https://github.com/paritytech/polkadot-sdk/pull/13729) awaiting review, [#13728](https://github.com/paritytech/polkadot-sdk/pull/13728) awaiting review, [#13740](https://github.com/paritytech/polkadot-sdk/pull/13740) awaiting review, [#13730](https://github.com/paritytech/polkadot-sdk/pull/13730) awaiting review).** The Coretime chain runs continuously and its less travelled branches; `swap_leases`, the ignored and dropped outcomes in `process_revenue`, a zero `region_length` in config validation, `force_reserve` failure at sale rotation are exactly the ones that do not surface in ordinary operations and therefore accumulate risk silently.

### Runtimes (FRAME, APIs, integrations)

**[Scheduled call cancellation](https://github.com/paritytech/polkadot-sdk/pull/12688).** Named scheduled calls can be cancelled by the caller that created them and by other pallets acting on their behalf. `do_cancel_named` removed the task and its `Lookup` entry regardless of who cancelled, but cleared `Retries` and dropped the preimage only when the origin was present and the `schedule::v2::Named` and `v3::Named` Impls cancel task that left an orphaned `RetryConfig` pointing at a task that no longer exists, and a preimage that stayed requested with its deposit still held. For a user, that is a deposit locked against a call they cancelled; for a runtime integrator, it is state that does not reconcile. Cleanup now runs whenever the task is removed, matching the anonymous `do_cancel`, so cancelling a named call leaves the same clean state as cancelling an unnamed one (awaiting reviews).

**[Treasury asset canonicalization](https://github.com/paritytech/polkadot-sdk/pull/13461).** Runtimes that accept more than one representation of the same asset, a native asset and an asset-hub representation, or several wrapped forms need every spend path to agree on which form is canonical before the spend is recorded. Without a normalization hook, each spend path has to enforce that agreement itself, and any path that does not becomes a place where the treasury's accounting can drift from the asset actually held. The `CanonicalizeAssetKind` config item gives the runtime one place to normalize before a spend, so treasury accounting stays consistent regardless of which representation was submitted.

**Fee and transaction-extension coverage.** These pallets sit on the path every transaction and every runtime integrator touches, the ecosystem cost of an untested branch here is a silent regression, a refund that lands below ED and is lost, a `post_dispatch` that does not run, a credit API that behaves differently from its documentation, which surfaces as a support ticket from a wallet or a runtime team rather than as a failing test. The PRs this period add coverage for the weight reservation and refund math ([#13600](https://github.com/paritytech/polkadot-sdk/pull/13600)), characterize the below-ED refund behavior ([#13649](https://github.com/paritytech/polkadot-sdk/pull/13649)), exercise the `post_dispatch` paths ([#13592](https://github.com/paritytech/polkadot-sdk/pull/13592)), cover the extension paths ([#13590](https://github.com/paritytech/polkadot-sdk/pull/13590)), test the `TxPaymentCredit` API ([#13593](https://github.com/paritytech/polkadot-sdk/pull/13593)), and sweep the documentation ([#13584](https://github.com/paritytech/polkadot-sdk/pull/13584)). Each one converts a path that only a production incident would have exercised into a path with a documented expected outcome, which is what lets integrators build against these pallets without re-driving their behavior from source.

### Nodes (SDK, tooling, networking)

**litep2p address classification and connection limits ([#713](https://github.com/paritytech/litep2p/pull/713), [#712](https://github.com/paritytech/litep2p/pull/712)).** `is_global_multiaddr` decides whether a peer's address is globally routable, and `ConnectionLimits` bounds how many connections a node will hold. Both are correctness-critical and neither fails visibly in normal operation, a misclassified address routes traffic to a peer that cannot be reached, and a connection limit that is not enforced under load is how a node runs out of file descriptors and stops accepting peers. The ecosystem cost of an untested branch here is a node that degrades only under the conditions an operator cannot easily reproduce. The tests added this period pin down the classification and the limit enforcement, so a regression in either is caught before it reaches an operator's node.

**[sc-chain-spec error handling](https://github.com/paritytech/polkadot-sdk/pull/13945).** Chain-spec tooling is what builds, inspects and serves the configuration a node starts from, and it is routinely handed presets. A non-JSON preset previously aborted the process with a panic; a malformed preset now returns an error, so the build or the command fails with a message instead of a crash. For the people who maintain chain specs and the tooling around them, the difference is a diagnosable error at the point of the mistake rather than a panic that has to be traced back to its input.

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
