# Evidence-0003: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/10/31) |
| **Submitted by**| Adrian Catangiu |


## Member details

- Matrix username: @adrian:parity.io
- Polkadot address: 121dd6J26VUnBZ8BqLGjANWkEAXSb9mWq1SB7LsS9QNTGFvz
- Current rank: 2
- Date of initial induction: 2023/06/12
- Date of last report: 2024/07/30
- Area(s) of Expertise/Interest: Bridges, XCM, Asset Hub, Bridge Hub, BEEFY


## Reporting period

- Start date: 2024/07/30
- End date: 2024/10/31


## Evidence

During the reporting period covered by this letter, I was focused on future iterations of Polkadot trustless bridges and the next iteration of the XCM protocol, in both cases heavily focused on improving UX while also delivering new features.

### Bridges

I initially ideated how Polkadot trustless bridges deployed on System Chains should take advantage of the Bridge Hub blockspace available and allow periodic **free** consensus updates. This way, system bridges connectivity and liveness are offered as a public good to the Polkadot Ecosystem. Users of these bridges would only have to cover the costs for their particular messages to be bridged, while the bridge consensus updates would be subsidized. Another way to look at it is that the communication infrastructure is subsidized, while the communication service is paid by customers using that service. After settling on a design together, Slava and Branislav implemented and deployed this change to the Polkadot<>Kusama bridge, leading to a [25x reduction in fees for P<>K bridge](https://hackmd.io/@bkontur/bridges-free-header-submission#Testing-and-Results). Similarly, I worked with Snowfork team on the design and Clara implemented [free consensus updates for the P<>E bridge](https://github.com/paritytech/polkadot-sdk/pull/5201). This will be deployed live with runtimes 1.4.x release.

I organized a live workshop where engineers from the Parity Bridges and Snowfork teams met to design and work on the next iteration of Snowbridge in a hackathon style. The major improvements to Snowbridge we focused on were UX, decentralization and regulatory compliance challenges. The many hours of whiteboarding have since been distilled in the following [Snowbridge V2 design doc](https://github.com/paritytech/polkadot-sdk/blob/master/bridges/snowbridge/docs/v2.md).

Following the big-picture initiatives to [make Polkadot more accessible](https://www.parity.io/blog/polkadot-smartcontract-platform), I have analyzed how to [increase bridge accessibility to builders](https://forum.polkadot.network/t/expose-builder-facing-bridging-components-on-asset-hub/10421) by splitting the overall bridge architecture into user/builder-facing functionality directly available on Asset Hub and abstracted-away bridge transport protocol infrastructure living on Bridge Hub. As a result, we pivoted with the deployment of the new P<>K bridge feature [Permissionless dedicated bridge lanes](https://github.com/paritytech/polkadot-sdk/issues/6044), and it will now be deployed to Asset Hub.

To better explain how Polkadot Parachain builders can integrate these trustless bridges, I created the following articles: [DotSama parachains options for using Polkadot<>Kusama bridge](https://hackmd.io/@acatangiu/B1oGPAQkkg) and [Polkadot parachains options for using Polkadot<>Ethereum bridge (Snowbridge)](https://hackmd.io/@acatangiu/Hy4xduIk1g).

I fortunately also had time to write some bridges code and added [support for registering and transferring Polkadot, Kusama and Ethereum assets across P<>K bridge](https://github.com/polkadot-fellows/runtimes/pull/421).

### XCM

A lot of my energy went into XCM this year, including the past three months covered by this letter. I can categorize XCM efforts into _existing XCM_ and _future XCM_.

On the topic of _existing XCM_ I think the most impactful work was delivering [Fees estimation support for XCMs spanning multiple chains](https://github.com/polkadot-fellows/runtimes/issues/479) and [XCM fees using any asset through autoswap](https://github.com/paritytech/polkadot-sdk/issues/6050), where Cisco did most of the heavy lifting, but where I believe I was nonetheless instrumental with ideation, reviews and guidance.

On the topic of _future XCM_, we've also made considerable progress on designing, formalizing and implementing a set of new features that will be released with a new XCM `v5` version. I will focus on the ones that I worked on:

Complex asset transfers support, where XCM should **support multi-hop, multi-asset transfer programs**. Example 1: _run XCM program on Bifrost that transfers BNC, USDT and GLMR to Moonbeam while going through Asset Hub_, or example 2: _run XCM program on Hydration that transfers HDX, USDT and KSM to Asset Hub Kusama over the P<>K bridge (Hydration->PAH->KAH)_.  
I formalized this support through [RFC#100](https://github.com/polkadot-fellows/RFCs/pull/100), then implemented it in [[xcm-v5] implement InitiateTransfer instruction](https://github.com/paritytech/polkadot-sdk/pull/5876).

[Empowered cross-chain origins](https://github.com/paritytech/polkadot-sdk/issues/6054) where we want to consolidate and align location to account derivation - so that the same account is derived on all ecosystem parachains for consistency and better UX, support permissionless Origin Aliases across chains - to support local accounts to allow other locations (or derived accounts) to alias them, and support single or multi-hop asset transfers that preserve the original origin - to allow users to transfer assets, pay for fees and Transact in a single XCM program.  
For the last part, I proposed and got in [RFC#122](https://github.com/polkadot-fellows/RFCs/pull/122), then implemented support for it in [[xcm-v5] InitiateTransfer can alias XCM original origin on destination](https://github.com/paritytech/polkadot-sdk/pull/5971).  

I have also created this [Roadmap project board for the Bridges+XCM team](https://github.com/orgs/paritytech/projects/145/views/8) to inform downstream users of what is being worked on and when it will be delivered, but also show what's not yet scheduled or not even on our radar. I am hoping builders and users can let us know when they think we are missing something or we should prioritize something different.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 1 out of 1 referenda in which I was eligible to vote during this reporting period (i.e 100% voting activity). I have voted in line with the consensus (i.e 100 % voting agreement). | [ref 150](https://collectives.subsquare.io/fellowship/referenda/150) |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

### General activity during this reporting period (2024/07/30 - 2024/10/31)

- [Reviewed 72 Polkadot-SDK PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aacatangiu+created%3A2024-07-30..2024-10-30+),
- [Authored/opened 21 new issues in Polkadot-SDK](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue+author%3Aacatangiu+created%3A2024-07-30..2024-10-30+),
- [Reviewed 25 Fellowship runtimes PRs](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr++reviewed-by%3Aacatangiu+created%3A2024-07-30..2024-10-30),
- [Authored/opened 10 new issues in Fellowship runtimes repo](https://github.com/polkadot-fellows/runtimes/issues?q=is%3Aissue+author%3Aacatangiu+created%3A2024-07-30..2024-10-30),
- Regular active participant on OpenDev calls,
- [Active in Polkadot forum](https://forum.polkadot.network/u/acatangiu/activity).
