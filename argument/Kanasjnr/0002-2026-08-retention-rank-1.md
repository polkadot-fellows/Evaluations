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

I took ownership of [polkadot-sdk#11561](https://github.com/paritytech/polkadot-sdk/issues/11561) and drove deprecation cleanup across the SDK, landing one removal per PR as reviewers requested. The goal is to retire dead APIs so runtime authors are not steered toward unsupported paths. The most impactful merges this period dropped long-deprecated surfaces that had already been superseded for multiple release cycles — `schedule::v1` ([#12584](https://github.com/paritytech/polkadot-sdk/pull/12584)), `GenesisBuild` ([#12529](https://github.com/paritytech/polkadot-sdk/pull/12529)), XCM builder and executor re-exports ([#12503](https://github.com/paritytech/polkadot-sdk/pull/12503), [#12505](https://github.com/paritytech/polkadot-sdk/pull/12505)), and deprecated native/wasm executor helpers ([#12669](https://github.com/paritytech/polkadot-sdk/pull/12669)). Further removals across FRAME, XCM, node, and pallets are tracked in the issue; see [all merged PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AKanasjnr+is%3Amerged) and [open PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AKanasjnr+is%3Aopen).

Beyond deprecation, I landed [try-runtime exposure in bridge-hub-test-utils](https://github.com/paritytech/polkadot-sdk/pull/11211). [ExtrinsicBaseWeight refinement](https://github.com/paritytech/polkadot-sdk/pull/11732), which corrects base extrinsic weight for FRAME-benchmarked runtimes, and [descriptive module invalidity](https://github.com/paritytech/polkadot-sdk/pull/11724), which gives wallets and indexers actionable rejection reasons instead of opaque module indices, have both been approved and are pending merge. I am also working on XCM barrier weight accounting ([#11302](https://github.com/paritytech/polkadot-sdk/pull/11302)) and Asset Hub safe-mode / tx-pause deployment ([runtimes#1164](https://github.com/polkadot-fellows/runtimes/pull/1164)).

For knowledge-sharing, I published the concluding part of my consensus-lab series: [The Double-Edged Sword of Finality](https://forum.polkadot.network/t/the-double-edged-sword-of-finality-simulating-runtime-upgrade-failures-in-substrate/17966). Using [substrate-consensus-lab](https://github.com/Kanasjnr/substrate-consensus-lab), I showed that GRANDPA finality is correctness-agnostic: a minority migration bug is quarantined by state-root divergence, but a supermajority-infected upgrade finalizes corrupt state permanently. The post ties those results to why Polkadot relies on governance delay, staging networks, and `try-runtime` before mainnet upgrades.

I intend to keep this mix of steady SDK maintenance and deeper FRAME/XCM work, and to participate more actively in Fellowship review and RFC discussion.

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

