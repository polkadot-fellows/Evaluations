# Argument-0006: Promotion to Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/08/11                                                             |
| **Submitted by**| polka.dom                                                                        |


## Member details

- Matrix username: @polkadotdom:matrix.org
- Polkadot address: 1L66uQMKFnXKSZx9pCD5o56GvvP1i2Qns7CaS2AaKp9mnwc
- Current rank: 1
- Date of initial induction: [2025/05/06](https://collectives.statescan.io/#/extrinsics/6306997-2)
- Date of last report: [2026/07/01](https://github.com/polkadot-fellows/Evaluations/blob/main/argument/polkadotdom/0005-rank1-retention.md)
- Area(s) of Expertise/Interest: FRAME, System Parachains, Economics, Security


## Reporting period

- Start date: 2025/05/06
- End date: 2026/08/11

## Argument

Hello all, my name is Dom (alias polkadotdom). My tenure as a rank 1 member approaches 1 year, and my cumulative tenure is now 2+. Over that time I have designed, implemented, and launched important protocol changes, helped review the designs and changes of others, and promolgated/elucidated Polkadot as a whole through presentations and general presence. I delineate below my contributions thus far and humbly argue for promotion to rank 2. Thank you.

### Number 1 RFC 150, AHM, Hard Pressure Issuance, DAP

I'll begin with the work I consider most important, each piece touching a core part of the protocol.

**RFC 150 - Voting While Delegating.** It had long been requested that a user be able to vote simultaneous to their delegating. I proposed [RFC-150](https://github.com/polkadot-fellows/RFCs/pull/150), refined it through several rounds of fellow feedback, and saw it accepted in December of 2025. The [implementation](https://github.com/paritytech/polkadot-sdk/pull/9026) is complete and under review. I chose this work because I believe it allows our governance system to more accurately approximate ground truth voter preferences - by increasing delegation, and therefore turnout, everyone is better represented when decisions are made.

**AHM.** As the ecosystem approached the Asset Hub Migration, the Parity team needed state tests for each pallet migrating from relay to AH, functioning as a secondary assurance that all data was moving smoothly through XCM. I constructed these for [pallet-bounties](https://github.com/polkadot-fellows/runtimes/pull/669), [pallet-referenda](https://github.com/polkadot-fellows/runtimes/pull/672), [pallet-scheduler](https://github.com/polkadot-fellows/runtimes/pull/680), and [pallet-staking/staking-async](https://github.com/polkadot-fellows/runtimes/pull/727), a few complicated by cross-pallet state dependencies. Given the immutable and difficult-to-amend nature of a finalized blockchain, this struck me very much as a 'measure twice, cut once' situation. I am happy to report the state piping of these pallets went smoothly.

**'Hard Pressure' Issuance.** With the passing of [Ref 1710](https://polkadot.subsquare.io/referenda/1710), I worked with Kian, Oliver, and Paolo to [implement](https://github.com/polkadot-fellows/runtimes/pull/898) the new capped, stepped supply schedule. The code was a significant departure from the previous model and required new [stepped curve primitives](https://github.com/paritytech/polkadot-sdk/pull/9556), which I took the opportunity to generalize for the wider ecosystem. By the time it was audited, SRLabs found no issues with the logic. Following enactment this March, I [cleanly removed](https://github.com/polkadot-fellows/runtimes/pull/1112) the old static emission code. Polkadot's macro-economic strategy now rests in part on this system, and I'm proud to have carried it from referendum to release.

**DAP.** Finally, I helped push the new DAP staking changes through in accordance with [Jonas' designs](https://hackmd.io/@jonasW3F/rkN6BXE2ex), reviewing the relevant PRs from Ankan, Paolo, Andrei, and Cirko - including the [move of era reward minting into DAP itself](https://github.com/paritytech/polkadot-sdk/pull/11616). I found several bugs that were otherwise missed, [for ex.](https://github.com/paritytech/polkadot-sdk/pull/11651#discussion_r3073307397) The new system addresses long-standing concerns with flexibility in our treasury management and sets us up nicely for pUSD.

### Number 2 Serialize BTreeMap, RFC Reviews, Design Reviews (pUSD, Web3Storage, Low Latency)

Next, work that is perhaps less headline-worthy, but substantial all the same.

I [added serialization to the BoundedBTreeMap](https://github.com/paritytech/parity-common/pull/870) data structure to enable its use in genesis storage, and followed up by [exposing the derives through the umbrella crate](https://github.com/paritytech/polkadot-sdk/pull/7764). A small quality-of-life win for anyone seeking the same functionality.

As superhuman programmers emerge and RFC submission count rises, review is slowly becoming the main component of our jobs as fellows. I have tried to act accordingly. Over this tenure I reviewed, among others, [RFC 164 (open Aura authoring)](https://github.com/polkadot-fellows/RFCs/pull/164) - where I contributed meaningfully to the security considerations - [RFC 165 (post-quantum accounts)](https://github.com/polkadot-fellows/RFCs/pull/165), the Snowbridge [circuit breaker](https://github.com/polkadot-fellows/RFCs/pull/167) and [emergency pause](https://github.com/polkadot-fellows/RFCs/pull/166) proposals, [RFC 171 (asset-based storage deposits)](https://github.com/polkadot-fellows/RFCs/pull/171), and [RFC 173 (transaction replay prevention)](https://github.com/polkadot-fellows/RFCs/pull/173). Often I am the only reviewer, even on important submissions.

In the same vein, I took the time to review the larger design docs shaping Polkadot's next chapter: [pUSD](https://github.com/polkadot-fellows/RFCs/pull/155), the ['pragmatic Web3 storage' design](https://github.com/paritytech/polkadot-sdk/pull/10731) - where my review produced meaningful changes - and the ['low latency' design](https://github.com/paritytech/polkadot-sdk/pull/10449).

### Number 3 RFC 151 & its logic portion, Parameterization of Inflation, Ambassador Fellowship Work, Stored Proc Macro

Not everything lands, and I think an honest accounting should include the work that didn't.

I identified a signaling issue with our referenda system and proposed [RFC 151, Crowdsourced Decision Deposits](https://github.com/polkadot-fellows/RFCs/pull/151). Following Basti's initial implementation, I completed the logic portion, guarding against several possible griefs that could wipe deposits or otherwise 'jab' at participants, before passing the remaining work to an eager candidate, runcomet. The RFC was ultimately set aside as priorities shifted.

I set up the [parameterization of yearly DOT emission](https://github.com/polkadot-fellows/runtimes/pull/732), giving the people a voice in their own economic parameters. It was merged and live, but soon superseded by the hard pressure model above - and so I removed it with my own hands. Such is the way of things.

I built the [`stored` procedural macro](https://github.com/paritytech/polkadot-sdk/pull/8032), consolidating FRAME's confusing sprawl of storage-related derives into a simpler, more intuitive format. Though complete, it was closed when the maintenance churn was judged to outweigh the benefit.

Lastly, I worked alongside Clara to help the ambassador fellowship come online, largely through liaison with Lucy of the ambassadors, until they discontinued the approach this February under a shift of priorities.

While none of these live in the runtime today, each sharpened my judgement of what the protocol needs, and several seeded work now carried by others.

### Number 4 Fellowship calls, Element presence, Sub0 Presentation, Staking Dashboard Help

Beyond the code, I try to be a consistently present member of this collective. I have attended the fellowship and OpenDev calls throughout my tenure, giving updates on my work, and have remained generally available on Matrix - joining discussions on security, providing assurance to community advocates during the hard pressure transition, and helping newcomers find their footing.

At the annual Sub0 conference, I [presented](https://www.youtube.com/watch?v=yAYeV04-4sw) on how to best join the Technical Fellowship and offered simple [material](https://docs.google.com/document/d/1Y8Q63hOgnNoeOfNG2IiwqdMB1tw56jm1OMAfJibDGMU/edit?usp=sharing) to help candidates along that path, following up with an interview alongside Jay that I hope sparked some additional vigor within the community.

I also worked with Ross on [new features](https://github.com/polkadot-cloud/polkadot-staking-dashboard/issues/3362) for the Polkadot staking dashboard - one of which, surfacing how much validators are liquidating, I hope will produce a meaningful signal when selecting validators - and [flagged bugs](https://github.com/opensquare-network/subsquare/issues/7259) in our governance serving software that are now fixed.

### Number 5 A number of other smaller changes across Parity repos

Finally, the steady stream of smaller contributions that I believe keeps a codebase healthy. Before my induction I carried out the deprecation of the `pallet::getter` macro across a dozen pallets, from [authority-discovery](https://github.com/paritytech/polkadot-sdk/pull/4091) to [democracy](https://github.com/paritytech/polkadot-sdk/pull/4472) to [grandpa](https://github.com/paritytech/polkadot-sdk/pull/4529). Since then I have moved the [core-fellowship pallet to BlockNumberProvider](https://github.com/paritytech/polkadot-sdk/pull/6978) - a needed change before we can elastically scale the collectives chain - with the [salary pallet](https://github.com/paritytech/polkadot-sdk/pull/12403) now following. Sprinkled throughout are the little things: [try-runtime-cli documentation](https://github.com/paritytech/try-runtime-cli/pull/106), a [runtimes release bump](https://github.com/polkadot-fellows/runtimes/pull/987), an [AHM indexing fix](https://github.com/paritytech/polkadot-sdk/pull/8401), and other small patches across Parity repos. None individually noteworthy, but together I hope they paint a picture of someone who simply shows up.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |No referenda to vote on  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
