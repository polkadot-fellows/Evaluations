# Evidence-0004: Promotion to Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/11/29) |
| **Submitted by**| Adrian Catangiu |


## Member details

- Matrix username: @adrian:parity.io
- Polkadot address: 121dd6J26VUnBZ8BqLGjANWkEAXSb9mWq1SB7LsS9QNTGFvz
- Current rank: 2
- Date of initial induction: 2023/06/12
- Date of last report: 2024/10/31
- Area(s) of Expertise/Interest: Trustless Bridges, XCM, Asset Hub, Bridge Hub, BEEFY


## Reporting period

- Start date: 2024/01/01
- End date: 2024/12/31


## Evidence

During this year I have been doing work in the Polkadot Ecosystem across the spectrum, from vision to design to execution to evangelization for a number of important Polkadot goals:

---

### Trustless Bridges

The large bulk of the work developing BEEFY I've done before 2024, but at the beginning of this year I took the final steps of [launching BEEFY on Kusama](https://kusama.polkassembly.io/referenda/343), subsequently [on Polkadot](https://twitter.com/polkaworld_org/status/1779882346180960406), thus enabling important subsequent projects building on Polkadot like Snowbridge or Hyperbridge.

I have played a critical role in the launches of the [Polkadot<>Kusama](https://forum.polkadot.network/t/polkadot-kusama-bridge/2971/25) and [Polkadot<>Ethereum](https://x.com/_snowbridge/status/1803847629178311064) trustless bridges on Polkadot's and Kusama's Bridge Hubs and integrating them with Polkadot's and Kusama's Asset Hubs. Launching each of these bridges was a multi-year effort, where I have consistently contributed in each step: design, code, reviews, security audits, offchain infrastructure setup, governance proposals, deployment coordination, and contributed Evangelism articles on [Parity](https://www.parity.io/blog/trustless-interoperability) and [Polkadot official blogs](https://polkadot.com/blog/the-landscape-of-trustless-bridges-on-polkadot). Following the launches, I continued actively working on improvements and future iterations of these bridges:

I initially ideated how Polkadot trustless bridges deployed on System Chains should take advantage of the Bridge Hub blockspace available and allow periodic **free** consensus updates. This way, system bridges connectivity and liveness are offered as a public good to the Polkadot Ecosystem. Users of these bridges would only have to cover the costs for their particular messages to be bridged, while the bridge consensus updates would be subsidized. Another way to look at it is that the communication infrastructure is subsidized, while the communication service is paid by customers using that service. After settling on a design together, Slava and Branislav implemented and deployed this change to the Polkadot<>Kusama bridge, leading to a [25x reduction in fees for P<>K bridge](https://hackmd.io/@bkontur/bridges-free-header-submission#Testing-and-Results). Similarly, I worked with Snowfork team on the design, and Clara implemented [free consensus updates for the P<>E bridge](https://github.com/paritytech/polkadot-sdk/pull/5201). This will be deployed live with runtimes 1.4.x release.

I organized [a live workshop](https://x.com/_snowbridge/status/1834569673045852412) where engineers from the Parity Bridges and Snowfork teams met to design and work on the next iteration of Snowbridge in a hackathon style. The major improvements to Snowbridge we focused on were UX, decentralization, and regulatory compliance challenges. The many hours of whiteboarding have since been distilled in the following [Snowbridge V2 design doc](https://github.com/paritytech/polkadot-sdk/blob/master/bridges/snowbridge/docs/v2.md).

Following the big-picture initiatives to [make Polkadot more accessible](https://www.parity.io/blog/polkadot-smartcontract-platform), I have analyzed how to [increase bridge accessibility to builders](https://forum.polkadot.network/t/expose-builder-facing-bridging-components-on-asset-hub/10421) by splitting the overall bridge architecture into user/builder-facing functionality directly available on Asset Hub and abstracted-away bridge transport protocol infrastructure living on Bridge Hub. As a result, we pivoted with the deployment of the new P<>K bridge feature [Permissionless dedicated bridge lanes](https://github.com/paritytech/polkadot-sdk/issues/6044), and it will now be deployed to Asset Hub.

To better explain how Polkadot Parachain builders can integrate these trustless bridges, I created the following articles: [DotSama parachains options for using Polkadot<>Kusama bridge](https://forum.polkadot.network/t/dotsama-parachains-options-for-using-polkadot-kusama-bridge/10873) and [Polkadot parachains options for using Polkadot<>Ethereum bridge (Snowbridge)](https://forum.polkadot.network/t/polkadot-parachains-options-for-using-polkadot-ethereum-bridge-snowbridge/10889).

I can also showcase code contributions in this area: adding [extrinsics for complex XCM transfers](https://github.com/paritytech/polkadot-sdk/pull/3695) like the ones required when going over multiple hops as we do with bridges, support for [registering assets on Asset Hubs over the bridge](https://github.com/paritytech/polkadot-sdk/pull/5435), support for transferring [any Polkadot, Kusama and Ethereum assets across P<>K bridge](https://github.com/polkadot-fellows/runtimes/pull/421), testing [emulated bridge transfers](https://github.com/paritytech/polkadot-sdk/pull/4870), Snowbridge improvements like [avoiding trapping fees dust](https://github.com/paritytech/polkadot-sdk/pull/5563), [free consensus updates](https://github.com/paritytech/polkadot-sdk/pull/5560) and more flexible [account conversion for Ethereum accounts](https://github.com/paritytech/polkadot-sdk/pull/6221).

----

### XCM

#### Stabilizing XCM within Ecosystem

The ecosystem has had a rough start of the year when it comes to XCM because of a system upgrade that introduced XCM transport fees for cross-chain messages. Unfortunately, the change broke many ecosystem live XCM usecases including crosschain transfers, with many users ending up with trapped funds.  

Coincidentally, it was also the start of this year when I took over Parity's XCM team. My first point of focus was to **stabilize XCM within the Ecosystem**, I created [a hotfix](https://github.com/paritytech/polkadot-sdk/pull/3142) that we quickly deployed, then spent considerable time and energy with Cisco helping the ecosystem integrate the fix, rework their XCM programs where needed, and then helping users recover their trapped funds.

Once the fire was put out, I put in efforts to increase our emulated cross-chain tests coverage and avoid similar issues of breaking the ecosystem. As a result, I have a number of PRs that [add XCM cross-chain tests](https://github.com/polkadot-fellows/runtimes/pull/114), then [more tests](https://github.com/paritytech/polkadot-sdk/pull/4870), [some more tests](https://github.com/paritytech/polkadot-sdk/pull/5338), and [even more tests](https://github.com/polkadot-fellows/runtimes/pull/428). During this time, I was also [pushing for ecosystem tests](https://github.com/polkadot-fellows/runtimes/issues/171#issuecomment-1935532409), for which we now have [a framework ready](https://github.com/polkadot-fellows/runtimes/issues/171#issuecomment-2496612799) to be populated by the ecosystem, thanks to Ser Xiliang Chen.

#### Alleviating top XCM painpoints

The next point of focus was improving XCM UX by targeting the top XCM painpoints as described by the ecosystem.
I used the Polkadot forum to coordinate with the ecosystem on these: [XCM UX & DX improvements](https://forum.polkadot.network/t/xcm-user-and-developer-experience-improvements/4511/21?u=acatangiu). The full details are there, I am going to list here only the things that I worked on.

The most important XCM UX improvement revolved around fees, achieved by delivering [Fees estimation support for XCMs spanning multiple chains](https://github.com/polkadot-fellows/runtimes/issues/479) and [XCM fees using any asset through autoswap](https://github.com/paritytech/polkadot-sdk/issues/6050), where Cisco did most of the heavy lifting, but where I believe I was nonetheless instrumental with ideation, reviews, and guidance. Further XCM fees UX improvements will be available in XCMv5 through the new [PayFees instruction](https://github.com/polkadot-fellows/RFCs/pull/105) which consolidates execution and transport and even custom fees.

I added new [`pallet-xcm` functionality](https://github.com/paritytech/polkadot-sdk/pull/3695) (and follow-up [improvement](https://github.com/paritytech/polkadot-sdk/pull/4260)) to support complex, multi-hop asset transfers.

I also made general XCM usability enhancements on system chains like [removing XCM SafeCallFilter](https://github.com/polkadot-fellows/runtimes/pull/285), [allowing arbitrary XCM execution](https://github.com/polkadot-fellows/runtimes/pull/345), and [allowing signed origins to send arbitrary XCMs](https://github.com/polkadot-fellows/runtimes/pull/407).

#### Future protocol: XCMv5

The discovered limitations, UX challenges, and lessons learned have also influenced the design and subsequent delivery of the protocol's next iteration: XCMv5. There is much to say here, but I will limit the contents of this letter to my own contributions:

Real-world cross-chain, maybe even cross-consensus, business scenarios can span multiple chains and require moving multiple assets; as such, it is critical that XCM can natively support **multi-hop, multi-asset transfer programs**.
I formalized this support through [RFC#100](https://github.com/polkadot-fellows/RFCs/pull/100), then implemented it in [[xcm-v5] implement InitiateTransfer instruction](https://github.com/paritytech/polkadot-sdk/pull/5876).

I defined a milestone called [empowered cross-chain origins](https://github.com/paritytech/polkadot-sdk/issues/6054) where we want to consolidate and align location to account derivation, so that the same account is derived on all ecosystem parachains for consistency and better UX. We also want to [support permissionless Origin Aliases](https://github.com/paritytech/polkadot-sdk/pull/6336) across chains. This will allow local accounts to authorize other locations (or derived accounts) to alias them. Finally, we want to support single or multi-hop asset transfers that preserve the original origin, to allow users to transfer assets, pay for fees and Transact in a single XCM program. For this, I proposed and finalized [RFC#122](https://github.com/polkadot-fellows/RFCs/pull/122), then implemented support for it in [[xcm-v5] InitiateTransfer can alias XCM original origin on destination](https://github.com/paritytech/polkadot-sdk/pull/5971).

Another UX improvement is [RFC#101](https://github.com/polkadot-fellows/RFCs/pull/101) for finding an alternate mechanism that allows removing `require_weight_at_most` from XCM `Transact` for better UX.

Ultimately, authored or reviewed every PR that went in [XCMv5](https://github.com/paritytech/polkadot-sdk/pull/4826).

----

### Tackling Polkadot Ecosystem fragmentation

In line with what has now crystalized under the concept of **Polkadot Hub**, I started ecosystem consolidation efforts, trying to reduce ecosystem fragmentation through adoption and integration of Asset Hub as an ecosystem gateway.

To this end, I did the first episodes, [YouTube ep.1](https://www.youtube.com/watch?v=fdkIMEm-GYk) and [ep.2](https://www.youtube.com/watch?v=JFjVT4vj7cw), of an Asset Hub Webinar laying out the motivation and foundation of why and how the ecosystem parachains can unlock massive exposure by integrating and using Asset Hub at its full potential.

I authored several [forum posts](https://forum.polkadot.network/t/managing-sas-on-multiple-reserve-chains-for-same-asset/7538/7?u=acatangiu) pushing for parachains to switch their DOT/KSM reserve to Asset Hub, also providing them with technical solutions to do so.

Created [a plan for exposing builder-facing bridging components on Asset Hub](https://forum.polkadot.network/t/expose-builder-facing-bridging-components-on-asset-hub/10421) and presented it to the ecosystem.

----

### Roadmap

I have created and actively maintain this [Roadmap project board for the Parity Bridges+XCM team](https://github.com/orgs/paritytech/projects/145/views/8) to inform downstream users of what is being worked on and when it will be delivered, but also show what's not yet scheduled or not even on our radar. I am hoping builders and users can let us know when they think we are missing something or we should prioritize something different.

I also published [an article on the Parity blog](https://www.parity.io/blog/polkadot-xcm-improvements) discussing the XCM recent and future roadmap, trying to raise awareness and get more engagement.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 3 out of 3 referenda in which I was eligible to vote during this reporting period (i.e 100% voting activity). I have voted in line with the consensus (i.e 100 % voting agreement). | [ref 103](https://collectives.subsquare.io/fellowship/referenda/103), [ref 131](https://collectives.subsquare.io/fellowship/referenda/131), [ref 150](https://collectives.subsquare.io/fellowship/referenda/150) |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- I migrated the XCM spec & XCM RFCs from Parity to the Polkadot Fellowship,
- Consistent reviewer for both [Fellowship runtimes](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr++reviewed-by%3Aacatangiu+created%3A2024-01-01..2024-12-31) and [Polkadot-SDK](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aacatangiu+created%3A2024-01-01..2024-12-31+),
- Regular active participant on OpenDev calls,
- [Active in Polkadot forum](https://forum.polkadot.network/u/acatangiu/activity).

