# Argument-0005: Retention at Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/07/01                                                             |
| **Submitted by**| polka.dom                                                                        |


## Member details

- Matrix username: @polkadotdom:matrix.org
- Polkadot address: 1L66uQMKFnXKSZx9pCD5o56GvvP1i2Qns7CaS2AaKp9mnwc
- Current rank: 1
- Date of initial induction: [2025/05/06](https://collectives.statescan.io/#/extrinsics/6306997-2)
- Date of last report: [2026/03/28](https://github.com/polkadot-fellows/Evaluations/blob/d379fc31aee1ee53b3ca58f1bfa553940271b10a/evidence/polkadotdom/0004-rank1-retention.md)
- Area(s) of Expertise/Interest: FRAME, System Parachains, Economics, Security


## Reporting period

- Start date: 2026/03/28
- End date: 2026/07/01

## Argument

### DAP Staking Changes

This session I helped push the new DAP changes through in accordance with [Jonas' designs](https://hackmd.io/@jonasW3F/rkN6BXE2ex). The work involved reviewing all relevant PRs being submitted by Paolo, Andrei, and Cirko. I found several bugs that were otherwise missed, [for ex.](https://github.com/paritytech/polkadot-sdk/pull/11651#discussion_r3073307397)

The new DAP staking system addresses overall concerns with flexibility in our treasury management and sets us up nicely for pUSD.

### Block Number Provider - Core Fellowship pallet

I have continued my work on switching the [core-fellowship pallet](https://github.com/paritytech/polkadot-sdk/tree/master/substrate/frame/core-fellowship/src) to use BlockNumberProvider- a needed change before we can elastically scale the collectives chain. [Review](https://github.com/paritytech/polkadot-sdk/pull/6978) is in progress.

### RFC Review

Work continues on reviewing outstanding RFCs. As superhuman programmers emerge, and fellow count rises, we are starting to see an uptick in RFC submission count. Often I am the only one reviewing [even important RFCs](https://github.com/polkadot-fellows/RFCs/pull/165). I feel we could all spend a little more time doing this as it slowly becomes the main component of our jobs as fellows.

### Design review

As Polkadot evolves, we have seen a number of design review docs submitted. This session I took the time to review both ['pragmatic storage'](https://github.com/paritytech/polkadot-sdk/pull/10731) and ['low latency'](https://github.com/paritytech/polkadot-sdk/pull/10449) designs, finding meaningful changes in the storage designs.

### Community

As a fellow, I also try when I can to contribute to discussions on Matrix, having joined on discussions regarding security and help with newcomers. I have also attended the relevant fellowship calls and just been generally available on matrix.

### Staking dashboard & Subsquare feature help

I have worked with Ross on [new features](https://github.com/polkadot-cloud/polkadot-staking-dashboard/issues/3362) for the Polkadot staking dashboard. One of the features, seeing how much validators are liquidating, I'm hoping will produce a meaningful signal when selecting validators. I, for one, want to see my validators are committed to our economy.

In addition I [flagged](https://github.com/opensquare-network/subsquare/issues/7259) a few bugs in our governance serving software (subsquare) that are now fixed.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |No referenda to vote on  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
