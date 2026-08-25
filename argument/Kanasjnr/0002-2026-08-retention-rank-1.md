# Argument-0002: Retention at Rank I


|                  |                  |
| ---------------- | ---------------- |
| **Report Date**  | 2026/08/25       |
| **Submitted by** | Nasihudeen Jimoh |


## Member details

- Matrix username: @kanas0:matrix.org
- Polkadot address: **12pCUGSwoW4Xek48TLUHCFhrvAdjmciMMLJoRJD8HWP5saXH**
- Current rank: I
- Date of initial induction: 2025/10/31
- Date of last report: 2026/05/25
- Link to last report: [Argument-0001: Promotion to Rank I](https://github.com/polkadot-fellows/Evaluations/blob/main/argument/Kanasjnr/0001-2026-05-promotion-rank-1.md)
- Area(s) of Expertise/Interest: FRAME, XCM, Omni-Node, consensus (BABE/GRANDPA), System parachain runtimes

## Reporting period

- Start date: 2026/05/26
- End date: 2026/08/25

## Argument

I am Nasihudeen Jimoh (`Kanasjnr` on GitHub), a Fellowship **Rank I** member seeking **retention**. I was promoted via [Fellowship referendum #541](https://collectives.subsquare.io/fellowship/referenda/541) after [Evaluations#289](https://github.com/polkadot-fellows/Evaluations/pull/289). Since then I have continued steady contribution to `polkadot-sdk`, with supporting work toward `polkadot-fellows/runtimes` and public protocol analysis.

Per [Manifesto §6.2](https://github.com/polkadot-fellows/manifesto/blob/main/manifesto.pdf), Rank I expects **aspiration, knowledge-discovery, knowledge-sharing and active maintenance**, plus continued **modest but substantial** protocol contribution. Below I address those expectations for this period.

### Deprecation cleanup under #11561 (active maintenance)

Following review guidance to land **one removal per PR**, I continued the [polkadot-sdk#11561](https://github.com/paritytech/polkadot-sdk/issues/11561) deprecation Issue and merged **27** removals this period across FRAME, XCM, node, staking, and schedule APIs:

**FRAME / support / storage**

- [polkadot-sdk#12158](https://github.com/paritytech/polkadot-sdk/pull/12158) — `sp_core` hashing re-exports → `sp_crypto_hashing`
- [polkadot-sdk#12149](https://github.com/paritytech/polkadot-sdk/pull/12149) — `frame_support::error` module
- [polkadot-sdk#12250](https://github.com/paritytech/polkadot-sdk/pull/12250) — `AllowAll` / `DenyAll` / `Filter`
- [polkadot-sdk#12249](https://github.com/paritytech/polkadot-sdk/pull/12249) — `match_type` macro
- [polkadot-sdk#12148](https://github.com/paritytech/polkadot-sdk/pull/12148) — `GetStorageVersion::current_storage_version`
- [polkadot-sdk#12150](https://github.com/paritytech/polkadot-sdk/pull/12150) — `StorageIterator` / `StorageKeyIterator`
- [polkadot-sdk#12156](https://github.com/paritytech/polkadot-sdk/pull/12156) — `migration::remove_storage_prefix`
- [polkadot-sdk#12529](https://github.com/paritytech/polkadot-sdk/pull/12529) — `GenesisBuild` trait
- [polkadot-sdk#12584](https://github.com/paritytech/polkadot-sdk/pull/12584) — `schedule::v1` module
- [polkadot-sdk#12665](https://github.com/paritytech/polkadot-sdk/pull/12665) — `schedule::v2` traits
- [polkadot-sdk#12671](https://github.com/paritytech/polkadot-sdk/pull/12671) — `FixedPoint::try_sqrt`
- [polkadot-sdk#12670](https://github.com/paritytech/polkadot-sdk/pull/12670) — `Utility::derivative_account_id`
- [polkadot-sdk#12682](https://github.com/paritytech/polkadot-sdk/pull/12682) — `RuntimeHelper::execute_as_governance`
- [polkadot-sdk#12664](https://github.com/paritytech/polkadot-sdk/pull/12664) — `TREASURER_INDEX` constants
- [polkadot-sdk#12654](https://github.com/paritytech/polkadot-sdk/pull/12654) — `pallet_staking::ExposureOf`
- [polkadot-sdk#12655](https://github.com/paritytech/polkadot-sdk/pull/12655) — `pallet_society::RawEvent` alias

**XCM / Cumulus / parachains**

- [polkadot-sdk#12209](https://github.com/paritytech/polkadot-sdk/pull/12209) — `AssetsToBlockAuthor`
- [polkadot-sdk#12482](https://github.com/paritytech/polkadot-sdk/pull/12482) — `FilterAssetLocation`
- [polkadot-sdk#12472](https://github.com/paritytech/polkadot-sdk/pull/12472) — `ConvertedConcreteAssetId`
- [polkadot-sdk#12503](https://github.com/paritytech/polkadot-sdk/pull/12503) — `CurrencyAdapter`
- [polkadot-sdk#12504](https://github.com/paritytech/polkadot-sdk/pull/12504) — `UnpaidLocalExporter`
- [polkadot-sdk#12505](https://github.com/paritytech/polkadot-sdk/pull/12505) — `JustTry` / `Identity` re-exports
- [polkadot-sdk#12502](https://github.com/paritytech/polkadot-sdk/pull/12502) — `ForeignChainAliasAccount`
- [polkadot-sdk#12251](https://github.com/paritytech/polkadot-sdk/pull/12251) — `RelaychainBlockNumberProvider`

**Node**

- [polkadot-sdk#12501](https://github.com/paritytech/polkadot-sdk/pull/12501) — `BlockAnnounceValidator` type alias
- [polkadot-sdk#12652](https://github.com/paritytech/polkadot-sdk/pull/12652) — `new_native_or_wasm_executor`
- [polkadot-sdk#12669](https://github.com/paritytech/polkadot-sdk/pull/12669) — `NativeElseWasmExecutor`

**Why it matters:** Deprecated APIs accumulate debt for runtime and tooling authors. Removing them on a consistent cadence keeps the SDK surface honest, reduces accidental use of dead paths.

Full merged list : [polkadot-sdk PRs by Kanasjnr (closed)](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AKanasjnr+is%3Aclosed).

### Other merged work

- [polkadot-sdk#11211](https://github.com/paritytech/polkadot-sdk/pull/11211) — expose the `try-runtime` feature in `bridge-hub-test-utils`, so upgrade-path testing for bridge hubs is available through the normal feature flag rather than a hidden gap.

### Knowledge-sharing

I published the sixth (and concluding) part of the consensus-lab series:

- [The Double-Edged Sword of Finality: Simulating Runtime Upgrade Failures in Substrate](https://forum.polkadot.network/t/the-double-edged-sword-of-finality-simulating-runtime-upgrade-failures-in-substrate/17966) (2026-06-28)

It uses [substrate-consensus-lab](https://github.com/Kanasjnr/substrate-consensus-lab) to show that GRANDPA finality is correctness-agnostic: a minority migration bug is quarantined by state-root divergence, while a ≥2/3 infected majority finalizes corrupt state. That motivates governance delays, staging networks, and `try-runtime` before mainnet upgrades tying simulator results back to real Substrate operational practice.

Earlier parts of the series (slot collisions → gossip lag → partitions → GRANDPA-lite → mempool/state roots) remain linked from that post.

### Ongoing work

[Open PRs in polkadot-sdk](https://github.com/paritytech/polkadot-sdk/pulls/Kanasjnr) include both continued deprecation and non-trivial fixes / features still under review:

- Approved, awaiting merge: ExtrinsicBaseWeight refinement ([#11732](https://github.com/paritytech/polkadot-sdk/pull/11732))
- Awaiting merge: descriptive module invalidity ([#11724](https://github.com/paritytech/polkadot-sdk/pull/11724))
- Correctness / reliability: gossip local-message dedup ([#12694](https://github.com/paritytech/polkadot-sdk/pull/12694)); state-trie-migration RPC rejecting wrong-length child roots without panicking ([#12696](https://github.com/paritytech/polkadot-sdk/pull/12696))
- FRAME / XCM (under review): `dispatch_as_signed` ([#11110](https://github.com/paritytech/polkadot-sdk/pull/11110)); XCM barrier / weight accounting ([#11302](https://github.com/paritytech/polkadot-sdk/pull/11302)); private storage deprecation ([#11695](https://github.com/paritytech/polkadot-sdk/pull/11695))
- Further #11561 removals still open (e.g. [#12586](https://github.com/paritytech/polkadot-sdk/pull/12586), [#12681](https://github.com/paritytech/polkadot-sdk/pull/12681), [#12683](https://github.com/paritytech/polkadot-sdk/pull/12683), [#12990](https://github.com/paritytech/polkadot-sdk/pull/12990))
- System chains: Asset Hub safe-mode / tx-pause ([runtimes#1164](https://github.com/polkadot-fellows/runtimes/pull/1164))

### Commitment

I intend to keep shipping #11561 removals, land the in-flight correctness and FRAME/XCM PRs, and deepen participation in Fellowship review and RFC discussion at Rank I.

## Voting record


| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments                                                   |
| ----- | ------------------- | -------------------- | -------------------------- | ---------------------------------------------------------- |
| I     | 90%                 | N/A                  | N/A                        | No Rank I–eligible referenda to vote on during this period |
| II    | 80%                 | N/A                  |                            |                                                            |
| III   | 70%                 | 100%                 |                            |                                                            |
| IV    | 60%                 | 90%                  |                            |                                                            |
| V     | 50%                 | 80%                  |                            |                                                            |
| VI    | 40%                 | 70%                  |                            |                                                            |




## Misc

- Question(s):
- Concern(s):
- Comment(s):

