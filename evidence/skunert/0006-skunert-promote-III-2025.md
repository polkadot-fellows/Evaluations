# Argument-0006: Promotion to Rank III

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2025/07/10 |
| **Submitted by** | skunert    |

## Member details

- Matrix username: `@sebastian:parity.io`
- Polkadot address: `1682A5hxfiS1Kn1jrUnMYv14T9EuEnsgnBbujGfYbeEbSK3w`
- Current rank: 2
- Date of initial induction: 2024/01/08
- Date of last report: 2025/04/30
- Area(s) of Expertise/Interest: `Cumulus Node`, `Substrate Node`, `Parachain Authoring`, `Weight`

## Reporting period

- Start date: 2024/02/06
- End date: 2025/04/30

## Argument

In order to provide proper evidence for my qualification for rank III, I will also reference contributions from the last years that are outside the reporting period.

### Technical Contributions
Manifesto Requirement:
> Either played a supporting role in the ideation and a primary role in the formalisation of a major protocol component; or played a supporting role in the code-design and a primary role in the implementation of a major protocol component.

My technical expertise and contributions focus mostly on Cumulus and other Parachain-related areas. The following excerpt of my projects shows that I have designed and implemented multiple major protocol components.

1. **Elastic Scaling Authoring**: Elastic scaling required significant changes to the Parachain authoring. The "lookahead" collator implementation built blocks based on incoming relay chain blocks. This means that blocks were being built on all relay-chain forks. I was in charge of designing and implementing a new cumulus authoring implementation. The key points are:
    - No longer author on all forks. This is necessary because we don't have the time budget anymore. Authoring for 3 cores corresponds to basically constant authoring or importing; there is no longer time for parallel blocks.
    - Support for block times faster than 6s. This reduces block latency and, together with elastic scaling, increases transaction throughput.
    - Asynchronous backing gave Parachains more flexibility when it comes to authoring. The new collator leverages this by not relying on relay chain blocks as authoring triggers and by decoupling block authoring opportunities from Parachain slots. Changing the slot duration is a hassle and should be avoided. Collators will now try to author at dynamic timepoints in the slot. These changes are also a stepping stone for further improvements like the 500ms blocks Bastian is working on.
    - Fork management. Since we now need to pick one relay-chain fork to author on, collators are prone to pick the wrong fork, which in turn can lead to parachain forks. Building on relay parents with an offset allows us to avoid forking at the cost of XCM latency. I designed and implemented a novel way to enforce this offset. Collators need to provide a number of descendants of the relay parent to the parachain runtime in order to prove that they are not authoring at the tip.
    - Relevant Pull Requests: [Introduction of slot-based collator](https://github.com/paritytech/polkadot-sdk/pull/4097), [Harden runtime constraints](https://github.com/paritytech/polkadot-sdk/pull/6825), [Decouple authoring from slots](https://github.com/paritytech/polkadot-sdk/pull/7569), [Allow building on older parents](https://github.com/paritytech/polkadot-sdk/pull/8299)

2. **PoV-reclaim:** Parachains have two weight dimensions that need to be respected: reference time and PoV size. The relay chain imposes a fixed limit that parachain-submitted PoVs need to respect. The impact of individual transactions is determined by worst-case benchmarking. However, it is desirable to reclaim overestimated PoV size in order to improve block utilization. I designed and implemented the initial reclaim mechanism on the Parachain node and runtime side, including design and implementation of changes in the PVF.
    - Relevant Pull Requests: [Documentation](https://github.com/paritytech/polkadot-sdk/pull/4244), [Respect Extrinsic Length](https://github.com/paritytech/polkadot-sdk/pull/4326), [Reclaim Runtime Implementation](https://github.com/paritytech/polkadot-sdk/pull/3002), [Reclaim Node Side Implementation](https://github.com/paritytech/polkadot-sdk/pull/1462), [RFC](https://polkadot-fellows.github.io/RFCs/approved/0043-storage-proof-size-hostfunction.html)

3. **Older/Smaller Projects:**
    - **Parachain RPC Mode:** Allows users to run Parachains without the need to sync a relay chain. A remote relay chain RPC (or light-client) can be specified via `--relay-chain-rpc-urls` and data is fetched from there. ([#835](https://github.com/paritytech/cumulus/pull/835), [#963](https://github.com/paritytech/cumulus/pull/963)). This change makes Parachain nodes significantly less taxing for their machines.
    - **Node Pinning:** I implemented a system to keep blocks pinned while subsystems in the node hold references to notifications ([#13157](https://github.com/paritytech/substrate/pull/13157)). This avoids race-conditions where consumers of these notifications never had the chance to act on received notifications. Additionally, they can choose to keep notifications around for later state access.

### Non-technical contributions

Manifesto requirement:
> Demonstrable presence of knowledge sharing within the ecosystem.

- Regular participant in fellowship calls
- Talks:
    - Sub0 2022: [Divorcing the Relay and Parachain Node in the Collator](https://www.youtube.com/watch?v=KkhF97Ud3lQ&pp=ygUUcG9sa2Fkb3QgcnBjIGRpdm9yY2XSBwkJwQkBhyohjO8%3D)
    - Sub0 2024: Slot-based authoring for elastic scaling (not recorded)
- Since mid-2024 I have been leading the Node-SDK team, overseeing multiple efforts:
    - [omni-node:](https://github.com/orgs/paritytech/projects/157) I took over the lead on this project from Kian. I am providing guidance and reviews for team members working on new features.
    - [fork-aware transaction pool:](https://github.com/orgs/paritytech/projects/156/views/6?sliceB) I am the main sparring partner and reviewer of fellowship member michal, who has been working on the new pool since last year.
- Very active reviewer on polkadot-sdk, spanning wide areas of the node: [review list](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+is%3Aopen+reviewed-by%3Askunert)

## Voting record

*Provide your voting record in relation to required thresholds for your rank.* 

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments                               |
| ----- | ------------------- | -------------------- | -------------------------- | -------------------------------------- |
| III   | 70%                 | N/A                  | TBD                        | Seeking promotion to this rank         |
| I     | 90%                 | N/A                  | N/A                        | There were no votes to participate in. |
| II    | 80%                 | N/A                  | N/A                        | There were no votes to participate in. |
| IV    | 60%                 | N/A                  |                            |                                        |
| V     | 50%                 | N/A                  |                            |                                        |
| VI    | 40%                 | N/A                  |                            |                                        
