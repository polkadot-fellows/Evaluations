# Argument-0006: Promotion to Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/08/01                                                             |
| **Submitted by**| Jesse Chejieh                                                                        |


## Member details

- Matrix username: @doordashcon/:matrix.org
- Polkadot address: 12zsKEDVcHpKEWb99iFt3xrTCQQXZMu477nJQsTBBrof5k2h
- Current rank: I
- Date of initial induction: 2022/09/29
- Date of last report: 2025/06/20
- Area(s) of Expertise/Interest: FRAME, Collectives


## Reporting period

- Start date: 2024/01/10
- End date: 2025/08/01


## Argument
Since joining the Fellowship, I’ve focused on the collective parachain, empowering developers, and hardening runtime primitives. Below I detail systems I’ve built, mentored, or refined, each addressing critical gaps in protocol flexibility, safety, or accessibility. Every contribution aligns with Rank II’s mandate in the Fellowship Manifesto §6.3.1: to own major components, share knowledge, and prepare for network stewardship.


### Collectives Parachain Contributions

Built the Secretary Collective([`Polkadot`](https://github.com/polkadot-fellows/runtimes/pull/347) & [`Westend`](https://github.com/paritytech/polkadot-sdk/pull/9024)) with [`NoOpPoll`](https://github.com/paritytech/polkadot-sdk/pull/5311)—a trait that lets collectives opt out of voting mechanics.

My work on the collectives parachain extended to hardening core functionality - from fixing edge cases in [`MaxRank`](https://github.com/paritytech/polkadot-sdk/pull/3393) logic to implementing [`benchmark clamping`](https://github.com/paritytech/polkadot-sdk/pull/7720) that also revealed the need for a generic [`type converter`](https://github.com/paritytech/parity-common/pull/909) for the Get trait. Enabling type-safe transformations that extends its initial use case.


### Developer Relations & UX Improvements

My commitment to Polkadot operates on two equally vital fronts: Technical Contibutions and knowledge dissemination/sharing. Through streaming sessions, what began as a private study group is now adapted as part of the [Polkadot Africa Initiative](https://www.youtube.com/watch?v=4b46skkPMi4&list=PL9kJus-1a41k2QQAdhcUFto6-XGrYq0La&index=2) as the "Runtime Developer Guide" and "Runtime Development Guide" focucing on both aiding developers in untilizing the Polkadot stack and keeping up to date with recent developments respectively. This has translated in code contributions and increased developer activity in the region, here are some contributions over this reporting period: [Psykyodai](https://github.com/paritytech/polkadot-sdk/pull/9107) implemented the BlockNumberProvider for PureCreated Events to address UX concerns raised by Valentun/Nova Wallet; [Runcomet](https://github.com/paritytech/polkadot-sdk/pull/6267) created genesis dev accounts while [rainb0w-pr0mise](https://github.com/paritytech/polkadot-sdk/pull/6321) developed the Utility Call Fallback; and [Nathy-bajo](https://github.com/paritytech/polkadot-sdk/pull/7320) enhanced the Proxy pallet with view functions for runtime-specific type configuration - all demonstrating the growing technical capability.



### Honorable Mentions

I addressed a critical accounting oversight in [`pallet-balances`](https://github.com/paritytech/polkadot-sdk/issues/6974) where essential events were missing, impacting systems that depend on balance update tracking. Two key gaps were identified and rectified: First, the fungible trait implementation for Hold/Release operations had omitted event emissions when balances were placed on hold or released. Second, Burn/Mint events were not being published when Credit/Debt fungible types were dropped, despite total issuance being adjusted.

Helped in creating comprehensive documentation that demystifies [on-chain processes](https://github.com/polkadot-fellows/dashboard/pull/134)—from salary cycle management to rank approval workflows—through detailed visual guides and technical specifications for the fellowship dashboard. Documenting core parameters like the promotion/demotion timelines while developing step-by-step interaction guides for key functions including evidence submission and payout period.

During this period I also spearheaded the [implementation](https://github.com/polkadot-fellows/runtimes/pull/736) of the Ambassador Fellowship's new [technical specification](https://docs.google.com/document/d/1Y9O8AoRx-4g0kAwOZAEblTu8RSAUgnqNSzie_TXy0go/edit?tab=t.y6mnd3cxgh81). This involved aligning the fellowship's operational requirements with Substrate's runtime constraints.

Enabling permissionless onboarding at Rank 0 through `InductionDeposit`, which required reconfiguring both `pallet-core-fellowship` and `pallet-ranked-fellowship` and ensuring comprehensive benchmark coverage.

Although this configuration might not be used in the runtime, I count this as readiness to address the needs of the ecosystem.


### Reflection

This period marks my evolution from executing isolated fixes to owning critical protocol subsystems. Where I once resolved specific issues. Advancement to Rank II would accelerate this trajectory by enabling deeper protocol ownership and serving as primary on-call maintainer for components I've built.

I stand ready to uphold Rank II's mandate: merging protocol expertise with ecosystem stewardship to make Polkadot more accessible and resilient.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | N/A  | No Rank-I votes this year; counts as 100 % activity. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

