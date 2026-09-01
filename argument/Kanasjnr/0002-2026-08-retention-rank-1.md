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

I am Nasihudeen Jimoh (`Kanasjnr` on GitHub), seeking retention at Rank I. Since promotion in June ([referendum #541](https://collectives.subsquare.io/fellowship/referenda/541)), I have continued contributing to `polkadot-sdk`, with supporting work toward `polkadot-fellows/runtimes` and public protocol analysis on the Polkadot Forum.

A large share of my work this period was deprecation cleanup under [polkadot-sdk#11561](https://github.com/paritytech/polkadot-sdk/issues/11561), landing one removal per PR as reviewers requested. I merged **27** removals across FRAME, XCM, node, and pallet APIs — work that keeps the SDK surface honest so runtime authors are not steered toward dead paths. On the FRAME side this included removing deprecated hashing re-exports ([#12158](https://github.com/paritytech/polkadot-sdk/pull/12158)), the `frame_support::error` module ([#12149](https://github.com/paritytech/polkadot-sdk/pull/12149)), `AllowAll` / `DenyAll` / `Filter` ([#12250](https://github.com/paritytech/polkadot-sdk/pull/12250)), the `match_type` macro ([#12249](https://github.com/paritytech/polkadot-sdk/pull/12249)), `GenesisBuild` ([#12529](https://github.com/paritytech/polkadot-sdk/pull/12529)), `schedule::v1` and `schedule::v2` ([#12584](https://github.com/paritytech/polkadot-sdk/pull/12584), [#12665](https://github.com/paritytech/polkadot-sdk/pull/12665)), storage iterator helpers ([#12150](https://github.com/paritytech/polkadot-sdk/pull/12150)), `RuntimeHelper::execute_as_governance` ([#12682](https://github.com/paritytech/polkadot-sdk/pull/12682)), and staking / society aliases ([#12654](https://github.com/paritytech/polkadot-sdk/pull/12654), [#12655](https://github.com/paritytech/polkadot-sdk/pull/12655)). On the XCM and parachains side: `CurrencyAdapter`, `UnpaidLocalExporter`, and executor re-exports ([#12503](https://github.com/paritytech/polkadot-sdk/pull/12503), [#12504](https://github.com/paritytech/polkadot-sdk/pull/12504), [#12505](https://github.com/paritytech/polkadot-sdk/pull/12505)), `FilterAssetLocation` and related type aliases ([#12482](https://github.com/paritytech/polkadot-sdk/pull/12482), [#12472](https://github.com/paritytech/polkadot-sdk/pull/12472), [#12502](https://github.com/paritytech/polkadot-sdk/pull/12502)), and `AssetsToBlockAuthor` ([#12209](https://github.com/paritytech/polkadot-sdk/pull/12209)). On the node side: deprecated executor helpers ([#12652](https://github.com/paritytech/polkadot-sdk/pull/12652), [#12669](https://github.com/paritytech/polkadot-sdk/pull/12669)) and `BlockAnnounceValidator` ([#12501](https://github.com/paritytech/polkadot-sdk/pull/12501)). Further removals in this batch: [#12148](https://github.com/paritytech/polkadot-sdk/pull/12148), [#12156](https://github.com/paritytech/polkadot-sdk/pull/12156), [#12251](https://github.com/paritytech/polkadot-sdk/pull/12251), [#12664](https://github.com/paritytech/polkadot-sdk/pull/12664), [#12670](https://github.com/paritytech/polkadot-sdk/pull/12670), [#12671](https://github.com/paritytech/polkadot-sdk/pull/12671).

Beyond deprecation, I landed [try-runtime exposure in bridge-hub-test-utils](https://github.com/paritytech/polkadot-sdk/pull/11211). Two larger changes are approved and awaiting merge: [ExtrinsicBaseWeight refinement](https://github.com/paritytech/polkadot-sdk/pull/11732) and [descriptive module invalidity](https://github.com/paritytech/polkadot-sdk/pull/11724). Other open work includes gossip deduplication ([#12694](https://github.com/paritytech/polkadot-sdk/pull/12694)), state-trie-migration RPC hardening ([#12696](https://github.com/paritytech/polkadot-sdk/pull/12696)), XCM barrier weight accounting ([#11302](https://github.com/paritytech/polkadot-sdk/pull/11302)), `dispatch_as_signed` ([#11110](https://github.com/paritytech/polkadot-sdk/pull/11110)), private storage deprecation ([#11695](https://github.com/paritytech/polkadot-sdk/pull/11695)), further #11561 removals ([#12586](https://github.com/paritytech/polkadot-sdk/pull/12586), [#12683](https://github.com/paritytech/polkadot-sdk/pull/12683), [#12990](https://github.com/paritytech/polkadot-sdk/pull/12990)), and Asset Hub safe-mode / tx-pause ([runtimes#1164](https://github.com/polkadot-fellows/runtimes/pull/1164)).

For knowledge-sharing, I published the concluding part of my consensus-lab series: [The Double-Edged Sword of Finality](https://forum.polkadot.network/t/the-double-edged-sword-of-finality-simulating-runtime-upgrade-failures-in-substrate/17966). Using [substrate-consensus-lab](https://github.com/Kanasjnr/substrate-consensus-lab), I showed that GRANDPA finality is correctness-agnostic: a minority migration bug is quarantined by state-root divergence, but a supermajority-infected upgrade finalizes corrupt state permanently. The post ties those results to why Polkadot relies on governance delay, staging networks, and `try-runtime` before mainnet upgrades.

I intend to keep this mix of steady SDK maintenance and deeper FRAME/XCM work, and to participate more actively in Fellowship review and RFC discussion.

### Merged (this period)

- [#12158](https://github.com/paritytech/polkadot-sdk/pull/12158), [#12149](https://github.com/paritytech/polkadot-sdk/pull/12149), [#12209](https://github.com/paritytech/polkadot-sdk/pull/12209), [#12250](https://github.com/paritytech/polkadot-sdk/pull/12250), [#12249](https://github.com/paritytech/polkadot-sdk/pull/12249), [#11211](https://github.com/paritytech/polkadot-sdk/pull/11211), [#12482](https://github.com/paritytech/polkadot-sdk/pull/12482), [#12472](https://github.com/paritytech/polkadot-sdk/pull/12472), [#12503](https://github.com/paritytech/polkadot-sdk/pull/12503), [#12504](https://github.com/paritytech/polkadot-sdk/pull/12504), [#12505](https://github.com/paritytech/polkadot-sdk/pull/12505), [#12529](https://github.com/paritytech/polkadot-sdk/pull/12529), [#12502](https://github.com/paritytech/polkadot-sdk/pull/12502), [#12501](https://github.com/paritytech/polkadot-sdk/pull/12501), [#12148](https://github.com/paritytech/polkadot-sdk/pull/12148), [#12251](https://github.com/paritytech/polkadot-sdk/pull/12251), [#12584](https://github.com/paritytech/polkadot-sdk/pull/12584), [#12150](https://github.com/paritytech/polkadot-sdk/pull/12150), [#12652](https://github.com/paritytech/polkadot-sdk/pull/12652), [#12665](https://github.com/paritytech/polkadot-sdk/pull/12665), [#12664](https://github.com/paritytech/polkadot-sdk/pull/12664), [#12654](https://github.com/paritytech/polkadot-sdk/pull/12654), [#12671](https://github.com/paritytech/polkadot-sdk/pull/12671), [#12670](https://github.com/paritytech/polkadot-sdk/pull/12670), [#12156](https://github.com/paritytech/polkadot-sdk/pull/12156), [#12669](https://github.com/paritytech/polkadot-sdk/pull/12669), [#12655](https://github.com/paritytech/polkadot-sdk/pull/12655), [#12682](https://github.com/paritytech/polkadot-sdk/pull/12682)

### Open

- [#11110](https://github.com/paritytech/polkadot-sdk/pull/11110), [#11302](https://github.com/paritytech/polkadot-sdk/pull/11302), [#11674](https://github.com/paritytech/polkadot-sdk/pull/11674), [#11695](https://github.com/paritytech/polkadot-sdk/pull/11695), [#11724](https://github.com/paritytech/polkadot-sdk/pull/11724), [#11732](https://github.com/paritytech/polkadot-sdk/pull/11732), [#12157](https://github.com/paritytech/polkadot-sdk/pull/12157), [#12586](https://github.com/paritytech/polkadot-sdk/pull/12586), [#12683](https://github.com/paritytech/polkadot-sdk/pull/12683), [#12694](https://github.com/paritytech/polkadot-sdk/pull/12694), [#12696](https://github.com/paritytech/polkadot-sdk/pull/12696), [#12753](https://github.com/paritytech/polkadot-sdk/pull/12753), [#12990](https://github.com/paritytech/polkadot-sdk/pull/12990), [runtimes#1164](https://github.com/polkadot-fellows/runtimes/pull/1164)

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

