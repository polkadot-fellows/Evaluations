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

During this reporting period I worked on pUSD, the price oracle and Coretime, and fixed fund-handling bugs in several FRAME pallets.

### pUSD

I backported the multi-instance `pallet-psm` to `stable2606` ([polkadot-sdk#12952](https://github.com/paritytech/polkadot-sdk/pull/12952)), added it to the Asset Hub Polkadot runtime ([runtimes#1252](https://github.com/polkadot-fellows/runtimes/pull/1252)), and added remote tests for it that run against live Asset Hub Polkadot state ([runtimes#1254](https://github.com/polkadot-fellows/runtimes/pull/1254)).

I also fixed several issues in the pallet. The creation deposit used a placeholder footprint that under-reported the storage `create_psm` writes ([polkadot-sdk#12811](https://github.com/paritytech/polkadot-sdk/pull/12811)). A PSM admin could be set to the `None` origin ([polkadot-sdk#13256](https://github.com/paritytech/polkadot-sdk/pull/13256)). PSMs managed provider references on their reserve account and fee destination, which I removed ([polkadot-sdk#13626](https://github.com/paritytech/polkadot-sdk/pull/13626)). On Asset Hub Westend I removed the PSM reset migration, which would have wiped newly created PSMs on every upgrade ([polkadot-sdk#13137](https://github.com/paritytech/polkadot-sdk/pull/13137)).

### Price Oracle

I contributed to the price oracle ([polkadot-sdk#13241](https://github.com/paritytech/polkadot-sdk/pull/13241)) with PRs merged into its feature branch. Each venue had one vote per pair, so only the first market of a venue counted; every market now votes, and a pair is priced only once it reaches a quorum ([polkadot-sdk#13346](https://github.com/paritytech/polkadot-sdk/pull/13346)). Pairs were hardcoded in the runtime; pairs and their cross rates are now registered by governance ([polkadot-sdk#13393](https://github.com/paritytech/polkadot-sdk/pull/13393)). The pallet assumed order-book pricing; the pricing method is now set by the runtime ([polkadot-sdk#13396](https://github.com/paritytech/polkadot-sdk/pull/13396)). I also added tested schema definitions for well-known exchanges ([polkadot-sdk#13249](https://github.com/paritytech/polkadot-sdk/pull/13249), [polkadot-sdk#13350](https://github.com/paritytech/polkadot-sdk/pull/13350)), node logging for failing venues and unpriced pairs ([polkadot-sdk#13555](https://github.com/paritytech/polkadot-sdk/pull/13555)), and Prometheus metrics ([polkadot-sdk#13669](https://github.com/paritytech/polkadot-sdk/pull/13669)).

### Coretime

I authored [RFC-0175](https://github.com/polkadot-fellows/RFCs/pull/175), which proposes moving on-demand Coretime sales from the relay chain to the Coretime chain and removing the relay chain's `on_demand` pallet. A draft implementation is in [polkadot-sdk#12936](https://github.com/paritytech/polkadot-sdk/pull/12936).

In `pallet-broker`, the auto-renewal fix from my last report was merged and backported ([polkadot-sdk#12750](https://github.com/paritytech/polkadot-sdk/pull/12750)). I fixed a provisionally pooled region being counted twice in the instantaneous pool when pooled again, which diluted the revenue of other contributors ([polkadot-sdk#13311](https://github.com/paritytech/polkadot-sdk/pull/13311)); a follow-up is in review ([polkadot-sdk#13712](https://github.com/paritytech/polkadot-sdk/pull/13712)). I added the `pallet-broker` v5 `sale_index` migration to Coretime Polkadot and Kusama ([runtimes#1357](https://github.com/polkadot-fellows/runtimes/pull/1357)), and continued addressing review feedback on `pallet-coretime-market`, the RFC-17 implementation ([polkadot-sdk#11802](https://github.com/paritytech/polkadot-sdk/pull/11802)).

### Fund-handling fixes

In `pallet-asset-conversion`, a failed swap returned only part of the caller's funds; the full amount is now returned ([polkadot-sdk#13601](https://github.com/paritytech/polkadot-sdk/pull/13601)). Frozen or blocked pools were treated as usable; they are now rejected ([polkadot-sdk#13598](https://github.com/paritytech/polkadot-sdk/pull/13598)).

In `pallet-bounties`, payouts were computed from the free balance and transfer failures were ignored, so a claim could succeed without paying the beneficiary. Payouts now use the spendable balance, and failed transfers return an error ([polkadot-sdk#13673](https://github.com/paritytech/polkadot-sdk/pull/13673)).

In `pallet-staking-async`, expired era pots were drained ignoring locks. Only the spendable balance is now moved out ([polkadot-sdk#13690](https://github.com/paritytech/polkadot-sdk/pull/13690)).

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
