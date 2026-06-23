# Argument-0009: Retention at Rank II

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2026/06/23) |
| **Submitted by**| Branislav Kontur                |


## Member details

- Matrix username: @branislav_kontur:parity.io
- Polkadot address: 1HFq3DbX4tqanTLAx2CAToWnHXg6LRLMzSD4JzYCzCQpw5E
- Current rank: 2
- Date of initial induction: 2024/05/03
- Date of last report: 2026/03/29
- Area(s) of Expertise/Interest: `Bulletin, Bridges, XCM, System Parachains, governance, benchmarking, testing, integration, IPFS, Bitswap`


## Reporting period

- Start date: 2026/03/29
- End date: 2026/06/23

## Argument

This summary outlines my activities, contributions, and collaborations during the reporting period (April–June 2026). Throughout the period I remained a core part of the team building Polkadot's storage stack, with a deep focus on the **Bulletin Chain** — concentrating on its productionalization, the release of its crates to crates.io, testing, and benchmarking — and keeping up substantial contributions across the Fellows runtimes and the Polkadot SDK.

### Bulletin Chain — technical work and delivery

My work on Bulletin spanned design, coordination, unblocking, and the harder cross-cutting pieces, which naturally results in fewer but more impactful changes.

A significant cross-cutting effort was the **Hand-Off Protocol (HOP)**. I helped push its main implementation PR through to merge in the Polkadot SDK [[1]](https://github.com/paritytech/polkadot-sdk/pull/11662), and contributed to the design choices and integration along the way [[2]](https://github.com/paritytech/polkadot-sdk/pull/11692#discussion_r3058702570). On the Bulletin side I helped with the HOP-based authorizations and the surrounding provider management, contributing to reviews, design and integration. Beyond HOP, I worked across the chain's productionalization — correctness and migration safety, testing, and console-ui operability [[3]](https://github.com/paritytech/polkadot-bulletin-chain/pull/610) [[4]](https://github.com/paritytech/polkadot-bulletin-chain/pull/557) [[5]](https://github.com/paritytech/polkadot-bulletin-chain/pull/614) [[6]](https://github.com/paritytech/polkadot-bulletin-chain/pull/534). All of these changes were subject to expert code review and run on functional networks.

I participated in designing the JSON-RPC methods for Bitswap retrieval — `bitswap_v1_get` [[7]](https://github.com/paritytech/json-rpc-interface-spec/pull/183) and its streaming variant [[8]](https://github.com/paritytech/json-rpc-interface-spec/pull/186); the original design document is internal, but it resulted in these public spec PRs.

This work paid off at Web3 Summit 2026, where the Bulletin Chain served as the **storage backend** for a number of live components — the **t3rminal**, the **dotli / DotNS** machinery, and the **playground** among them — running throughout the event **without any issues**. These components retrieved content over the **Bitswap / litep2p** path, with light-client access via the **smoldot** integration, exercising the full end-to-end storage and retrieval story under real, production-like load rather than a demo. This same stack is intended to carry forward into the production Polkadot deployment of Bulletin.

### Fellows runtimes

I drove the onboarding of the **Bulletin Polkadot runtime** into the Fellows runtimes [[9]](https://github.com/polkadot-fellows/runtimes/issues/1119), including the storage pallets and business-logic stage [[10]](https://github.com/polkadot-fellows/runtimes/pull/1170). I identified and investigated a **coretime-polkadot integration test** failure [[11]](https://github.com/polkadot-fellows/runtimes/issues/1133) and an **xcmp-queue benchmarking** (bench bot / omni-bencher) regression [[12]](https://github.com/polkadot-fellows/runtimes/issues/1130), and I kept up ongoing cleanups and reviews across the runtimes — asset-hubs, collectives and the emulated tests [[13]](https://github.com/polkadot-fellows/runtimes/pull/1192) [[14]](https://github.com/polkadot-fellows/runtimes/pull/1196) — as part of a broader effort to align all runtimes [[15]](https://github.com/polkadot-fellows/runtimes/issues/1135).

### Polkadot SDK support

To keep technical debt in check I opened an initiative to remove deprecated code across the SDK [[16]](https://github.com/paritytech/polkadot-sdk/issues/11561), which an external contributor then helped carry through a series of follow-up PRs. I also opened and investigated a **frame-omni-bencher regression** between `stable2512` and `stable2603` [[17]](https://github.com/paritytech/polkadot-sdk/issues/11686) that affected Fellows benchmarking, and contributed a generic-solution suggestion to the `pallet-whitelist` deferred-dispatch RFC discussion [[18]](https://github.com/paritytech/polkadot-sdk/issues/11199#issuecomment-4281865213), which led to a separate RFC by Muharem [[19]](https://github.com/paritytech/polkadot-sdk/issues/12224).

### Web3 Storage — MVP/Demo

**Web3 Storage** is a decentralized storage system built on Substrate with game-theoretic guarantees, where storage providers lock stake and face slashing for data loss while the chain acts as a credible threat rather than the hot path. I drove much of its MVP/Demo [[20]](https://github.com/paritytech/web3-storage) by creating and triaging issues, pushing PRs, and reviewing others' work across the repository, and deployed it to PreviewNet. The design (by Robert Klotzner (@eskimor)) and demo were also successfully presented at Web3 Summit 2026 by Robert and Naren Mudigal (@mudigal).

### Mentoring, external contributors and ecosystem support

I regularly invested time in sharing knowledge and enabling others. I acted as a technical point of contact and reviewer for Bulletin and Web3 Storage across teams, helped colleagues become self-sufficient with Bulletin deployments, and answered Bulletin and HOP questions in the relevant rooms. This included ongoing PR reviews across the Fellows [[21]](https://github.com/search?q=org%3Apolkadot-fellows+is%3Apr+reviewed-by%3Abkontur+updated%3A2026-03-29..2026-06-23&type=pullrequests) and other Polkadot-related [[22]](https://github.com/search?q=org%3Aparitytech+is%3Apr+reviewed-by%3Abkontur+updated%3A2026-03-29..2026-06-23&type=pullrequests) repositories. Throughout, I continued bridging discussions across teams and providing technical direction on storage, retrieval and deployment strategy.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity).  | There were no referenda I could participate in during the reporting period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
