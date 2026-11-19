# Argument-0008: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/11/18                                                                                  |
| **Submitted by**| Sergej Sakac                                                                                |
| **Sponsored by**| N/A (not claiming a salary)                                                                 |


## Member details

- Matrix username: @sergej.sakac:parity.io
- Polkadot address: 126X27SbhrV19mBFawys3ovkyBS87SGfYwtwa8J2FjHrtbmA
- Current rank: II
- Date of initial induction: Seeding
- Date of last report: 2026/08/09
- Link to last report: [Argument-0007](https://github.com/polkadot-fellows/Evaluations/pull/332)
- [Subsystems](../../subsystems.md) developed/maintained: Economics (Infra: Coretime sales, Stablecoins), Runtimes (FRAME, APIs, integrations)


## Reporting period

- Start date: 2026/08/10
- End date: 2026/11/18


## Argument

During this reporting period my work was on pUSD, the price oracle and Coretime, together with a set of fund-handling fixes in FRAME pallets. Most of it falls under the Economics subsystem (Coretime sales and stablecoins), and the pallet fixes fall under Runtimes (FRAME).

### pUSD

At the time of my last report the multi-instance rework of `pallet-psm` had just been merged into the SDK. This period was about getting it into production on Asset Hub Polkadot. The rework was not part of `stable2606`, so I backported it there, adapting it so that `frame-support` stays semver-minor on the stable branch ([polkadot-sdk#12952](https://github.com/paritytech/polkadot-sdk/pull/12952)). I then added the pallet to the Asset Hub Polkadot runtime, with a fixed creation deposit, a cap on the external assets per PSM, and creation restricted to the asset owner or Root ([runtimes#1252](https://github.com/polkadot-fellows/runtimes/pull/1252)). To check the configuration against real state rather than mocks, I added remote tests that load live USDT data from Asset Hub Polkadot and cover minting, redemption, fees, debt tracking and circuit breakers ([runtimes#1254](https://github.com/polkadot-fellows/runtimes/pull/1254)).

Bringing the pallet to production also surfaced a number of problems, which I fixed. The creation deposit was computed from a placeholder footprint that under-reported the storage a PSM actually occupies ([polkadot-sdk#12811](https://github.com/paritytech/polkadot-sdk/pull/12811)). The reset migration on Asset Hub Westend runs on every upgrade, so leaving it in would have wiped every PSM created from then on ([polkadot-sdk#13137](https://github.com/paritytech/polkadot-sdk/pull/13137)). A PSM admin could be set to the `None` origin, which would have left such a PSM under the control of whoever authors the block ([polkadot-sdk#13256](https://github.com/paritytech/polkadot-sdk/pull/13256)). Finally, PSMs managed provider references on their reserve account and fee destination themselves; I removed this so that both accounts follow the standard account rules ([polkadot-sdk#13626](https://github.com/paritytech/polkadot-sdk/pull/13626)).

### Price Oracle

The price oracle ([polkadot-sdk#13241](https://github.com/paritytech/polkadot-sdk/pull/13241)) provides on-chain prices of asset pairs such as DOT/USD, computed from data that block producers fetch from exchanges. I contributed a series of PRs that were merged into its feature branch.

The first group concerns how prices are formed. Each venue originally had a single vote per pair, so when a venue listed several markets for the same pair (for example spot and perpetual) only the first one counted, and nothing required a minimum number of sources. Every market now gets a vote, and a pair is only priced once it reaches a quorum of market votes ([polkadot-sdk#13346](https://github.com/paritytech/polkadot-sdk/pull/13346)). Pairs were hardcoded in the runtime, so adding one required a runtime upgrade; they are now registered by governance, together with cross rates such as DOT/USD derived from DOT/USDT and USDT/USD ([polkadot-sdk#13393](https://github.com/paritytech/polkadot-sdk/pull/13393)). The pallet also assumed that every market is priced from an order book; the pricing method is now chosen by the runtime ([polkadot-sdk#13396](https://github.com/paritytech/polkadot-sdk/pull/13396)).

The second group makes the oracle usable in practice. The pallet can read any exchange but needs a correct schema for each one, so I provided definitions for well-known exchanges, each tested against a recorded response ([polkadot-sdk#13249](https://github.com/paritytech/polkadot-sdk/pull/13249), [polkadot-sdk#13350](https://github.com/paritytech/polkadot-sdk/pull/13350)). Node operators also had no way to tell which pairs were not being priced or why, so I extended the runtime API and node logging to expose this ([polkadot-sdk#13555](https://github.com/paritytech/polkadot-sdk/pull/13555)) and added Prometheus metrics to the node service ([polkadot-sdk#13669](https://github.com/paritytech/polkadot-sdk/pull/13669)).

### Coretime

On-demand is the last part of Coretime still sold on the relay chain, which has to maintain an order queue, a spot price, ordering extrinsics and revenue tracking for it. I authored [RFC-0175](https://github.com/polkadot-fellows/RFCs/pull/175), which proposes moving on-demand sales to the Coretime chain. Orders are placed, priced and paid there, and the broker commits the sold blocks to the relay chain as one-shot core assignments through the same channel that bulk Coretime already uses, so the relay chain's `on_demand` pallet can be removed entirely. A draft implementation of one-shot assignments is in [polkadot-sdk#12936](https://github.com/paritytech/polkadot-sdk/pull/12936).

I also fixed two accounting bugs in `pallet-broker`. The auto-renewal fix from my last report, where a task could be charged for an unrelated task's renewal, was merged and backported ([polkadot-sdk#12750](https://github.com/paritytech/polkadot-sdk/pull/12750)). In the instantaneous pool, a provisionally pooled region could be pooled again without the earlier pooling being removed. The region was then counted twice, and the leftover share diluted the revenue of all other contributors and could never be claimed ([polkadot-sdk#13311](https://github.com/paritytech/polkadot-sdk/pull/13311)). A follow-up that keeps a pool share under one id for its whole life, so that later unpooling cannot miss it, is in review ([polkadot-sdk#13712](https://github.com/paritytech/polkadot-sdk/pull/13712)).

On the Fellowship runtimes side, I added the `pallet-broker` v5 `sale_index` migration to Coretime Polkadot and Kusama. This required determining the first-sale anchor of each chain (on Kusama `start_sales` ran twice), and I verified the result with try-runtime on live state ([runtimes#1357](https://github.com/polkadot-fellows/runtimes/pull/1357)). I also continued addressing review feedback on `pallet-coretime-market`, the implementation of RFC-17 ([polkadot-sdk#11802](https://github.com/paritytech/polkadot-sdk/pull/11802)).

### Fund-handling fixes

I also fixed several cases where pallets mishandled user or protocol funds.

In `pallet-asset-conversion`, a failed swap returned only part of the caller's funds: the credit was split into the amount to swap and the change, and the change was lost when the swap failed. The full amount is now returned ([polkadot-sdk#13601](https://github.com/paritytech/polkadot-sdk/pull/13601), backported to three stable branches). A separate change had made frozen pools usable in one direction only and left blocked pools being quoted for swaps that would fail; such pools are now rejected in both directions ([polkadot-sdk#13598](https://github.com/paritytech/polkadot-sdk/pull/13598)).

In `pallet-bounties`, payouts were computed from the free balance, which can include funds that cannot be transferred, and transfer failures were ignored. A claim could therefore succeed and remove the bounty without paying the beneficiary. Payouts now use the spendable balance and a failed transfer returns an error ([polkadot-sdk#13673](https://github.com/paritytech/polkadot-sdk/pull/13673)). In `pallet-staking-async`, expired era pots were drained ignoring locks, so a lock on a pot could outlive the funds backing it and reduce the rewards of later eras. Only the spendable balance is now moved out ([polkadot-sdk#13690](https://github.com/paritytech/polkadot-sdk/pull/13690)).

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | No referenda available for my rank during this period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
