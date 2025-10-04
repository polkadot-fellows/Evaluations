# Argument-0005: Retention at Rank II

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2025/10/05) |
| **Submitted by**| Branislav Kontur                |


## Member details

- Matrix username: @branislav_kontur:parity.io
- Polkadot address: 1HFq3DbX4tqanTLAx2CAToWnHXg6LRLMzSD4JzYCzCQpw5E
- Current rank: 2
- Date of initial induction: 2024/05/03
- Date of last report: 2025/06/27
- Area(s) of Expertise/Interest: `Bridges, XCM, System Parachains, governance, benchmarking, testing, integration, Bulletin`


## Reporting period

- Start date: 2025/06/27
- End date: 2025/10/05

## Argument

This summary outlines my activities, contributions, and collaborations during the reporting period. My work remains aligned with the Polkadot Fellowship’s core mission: ensuring the protocol’s long-term safety and resilience while enabling its continuous evolution.

Over this period, I focused primarily on **governance resilience** in the context of the **Asset Hub Migration (AHM)**. While I did not directly contribute to the migration code itself, my work centered on advancing runtime configurations for the relay chain and system parachains to support the migrated **OpenGov** on AssetHub. This involved investigating relevant OpenGov scenarios and configurations, identifying required **XCM changes and origin propagations**, and designing unit and integration tests to ensure system parachains can support both OpenGov on the relay chain and OpenGov on AHM during and after the migration. This effort, conducted in close collaboration with **Karol Kokoszka**, was finalized and merged as two PRs ([Polkadot](https://github.com/polkadot-fellows/runtimes/pull/626), [Kusama](https://github.com/polkadot-fellows/runtimes/pull/776)). Additional feedback and testing are being tracked in [PR #900](https://github.com/polkadot-fellows/runtimes/pull/900).

I also reviewed several AHM-related PRs and assisted with the merge of the `oty-dev-asset-hub-migration-2506` branch, preparing fresh weights ([#887](https://github.com/polkadot-fellows/runtimes/pull/887)) and identifying benchmarking issues that led to subsequent fixes and backports ([#894](https://github.com/polkadot-fellows/runtimes/issues/894), [#895](https://github.com/polkadot-fellows/runtimes/pull/895), [#902](https://github.com/polkadot-fellows/runtimes/pull/902), [#892](https://github.com/polkadot-fellows/runtimes/pull/892)). I also addressed issues related to proper **Kusama-AHM/Polkadot-AHM feature propagation** for releases and benchmarking ([#903](https://github.com/polkadot-fellows/runtimes/pull/903)) and enabled **migration checks** ([#904](https://github.com/polkadot-fellows/runtimes/pull/904)), while helping with related **Polkadot SDK backports**.

As part of broader Fellows maintenance work, I contributed to the **unstable2507 bump**, which served as the base for AHM — e.g., updating Rust to 1.88.0 and integrating the latest `frame-omni-bencher` for the benchmarking bot ([#823](https://github.com/polkadot-fellows/runtimes/pull/823)), reviving the **MBM migration** ([#857](https://github.com/polkadot-fellows/runtimes/pull/857)), and resolving SDK TODOs and nits ([link](https://github.com/acatangiu/runtimes/pull/4)).

I actively look for issues and improvements across the ecosystem and propose solutions. For example, I identified problems with **XCM version subscriptions** ([#795](https://github.com/polkadot-fellows/runtimes/issues/795)), which were later resolved by Karol and the OpenGov referenda. I also contributed small improvements for `pallet-xcm` and `GenesisConfig` ([paritytech/polkadot-sdk#9075](https://github.com/paritytech/polkadot-sdk/issues/9075)) and worked on proper **benchmarking configurations for AHM**, ensuring XCM and asset delivery across sibling parachains ([#709](https://github.com/polkadot-fellows/runtimes/pull/709)).

My current focus is on the upcoming **Proof-of-Personhood (PoP)** features, where I lead and support the new **Bulletin solochain** delivery — handling issues, improvements, releases, planning, and the initial community validator launch ([Bulletin repo](https://github.com/paritytech/polkadot-bulletin-chain)). The Bulletin chain, currently running in pre-production ([wss://bulletin.rpc.amforc.com](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fbulletin.rpc.amforc.com#)), is designed to provide ephemeral storage and support one of the PoP features. It will be integrated with the **People chain** via a **substrate-to-substrate bridge**, where I am also guiding Anthony on an upcoming PR planned for merge into the Fellows repo ([link](https://github.com/antkve/runtimes/pull/1)).

Beyond these major areas, I continue to support the ecosystem through **code reviews, mentorship, and cross-team collaboration**. This includes assisting external contributors, such as helping **Hyperbridge** resolve testing issues ([#483](https://github.com/polytope-labs/hyperbridge/pull/483), [#487](https://github.com/polytope-labs/hyperbridge/pull/487)), and reviewing and supporting **Daniel Shiposha’s NFTs PR** ([#4300](https://github.com/paritytech/polkadot-sdk/pull/4300)) with related fixes and feedback ([link](https://github.com/UniqueNetwork/polkadot-sdk/pull/14)).

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity).  |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

