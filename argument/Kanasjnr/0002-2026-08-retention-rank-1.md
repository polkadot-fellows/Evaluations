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

My main maintenance work this period has been executing the [polkadot-sdk#11561](https://github.com/paritytech/polkadot-sdk/issues/11561) deprecation campaign on my own initiative, landing one removal per PR as reviewers requested. I merged twenty-seven removals across FRAME, XCM, node, and pallet APIs — work that keeps the SDK surface honest so runtime authors are not steered toward dead paths. The most consequential of these dropped legacy surfaces already superseded for multiple release cycles: `schedule::v1` ([#12584](https://github.com/paritytech/polkadot-sdk/pull/12584)), `GenesisBuild` ([#12529](https://github.com/paritytech/polkadot-sdk/pull/12529)), and deprecated native/wasm executor helpers ([#12669](https://github.com/paritytech/polkadot-sdk/pull/12669)). This is the kind of active maintenance §6.2 expects at Rank I: unglamorous, but it only compounds if someone does it steadily.

Beyond deprecation, I landed changes that close real gaps. I exposed the `try-runtime` feature in `bridge-hub-test-utils` ([#11211](https://github.com/paritytech/polkadot-sdk/pull/11211)) so bridge-hub upgrade testing is available through the normal feature flag. Two larger changes are approved and awaiting merge: [ExtrinsicBaseWeight refinement](https://github.com/paritytech/polkadot-sdk/pull/11732), which corrects base extrinsic weight accounting for runtimes that depend on FRAME benchmarks; and [descriptive module invalidity](https://github.com/paritytech/polkadot-sdk/pull/11724), which gives wallets and indexers actionable invalidity reasons instead of opaque module indices. I also have correctness fixes under review — gossip message deduplication ([#12694](https://github.com/paritytech/polkadot-sdk/pull/12694)), hardening state-trie-migration RPC against malformed child roots ([#12696](https://github.com/paritytech/polkadot-sdk/pull/12696)), and XCM barrier weight accounting ([#11302](https://github.com/paritytech/polkadot-sdk/pull/11302)) — and am working toward Fellowship runtimes with Asset Hub safe-mode / tx-pause deployment ([runtimes#1164](https://github.com/polkadot-fellows/runtimes/pull/1164)).

For knowledge-sharing, I published the concluding part of my consensus-lab series: [The Double-Edged Sword of Finality](https://forum.polkadot.network/t/the-double-edged-sword-of-finality-simulating-runtime-upgrade-failures-in-substrate/17966). Using [substrate-consensus-lab](https://github.com/Kanasjnr/substrate-consensus-lab), I showed that GRANDPA finality is correctness-agnostic: a minority migration bug is quarantined by state-root divergence, but a supermajority-infected upgrade finalizes corrupt state permanently. The post ties those results to why Polkadot relies on governance delay, staging networks, and `try-runtime` before mainnet upgrades — a concrete illustration of the maintenance-vs-autonomisation trade-off §6.2 asks members to be aware of.

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

