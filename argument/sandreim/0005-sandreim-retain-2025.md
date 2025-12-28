# Argument-0005 Retention at Rank 3

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/12/08)                                                             |
| **Submitted by**| Andrei Sandu                                                                        |

## Member details

- Matrix username: @sandreim:parity.io
- Polkadot address: 13QdJvnJgfoitjrxESwrCWTaLMN8KvXxufDUucXM6EWGuxqh
- Current rank: 3
- Date of initial induction: 2023/07/18
- Date of last report: 2025/06/09
- Area(s) of Expertise/Interest: Parachain Consensus, Node Performance Engineering, Observability,
Stress and integration testing

## Reporting period

- **Start date:** 2025/06/10
- **End date:** 2025/12/08

## Argument

My primary objective during this period was to enhance the Polkadot Web3 application user experience by enabling faster and more reliable block times. Initially, I concentrated on the deployment of Elastic Scaling on Polkadot. In the latter half of the period, I developed a strategy to improve parachain block production reliability and delivered a few improvements in 2025. My contributions also included code supporting the investigation of block confidence issues and enhancements to the collator protocol's reliability.

### Elastic Scaling: Launch

Elastic Scaling was launched on the Polkadot RC in Sep 2025 after a series of consensus issues linked to the new V2 `CandidateReceipt`. The most recent issue resulted in a 30-minute block production stall on Kusama, highlighting a long-standing bug. I published the [postmortem](https://forum.polkadot.network/t/2025-08-24-kusama-stall-postmortem/14729) on the forum and created the [fix](https://github.com/paritytech/polkadot-sdk/pull/9564), tests, the `1.6.2` release (Polkadot), `1.7.1` (Kusama), and the referendums to patch the networks.

I worked on releasing the collator-side support for Elastic Scaling in the 2509 stable release. I implemented [docs updates](https://github.com/paritytech/polkadot-sdk/pull/9677), a CI runtime [upgrade test](https://github.com/paritytech/polkadot-sdk/pull/9811), a small [fix](https://github.com/paritytech/polkadot-sdk/pull/9703) for 500ms blocks, and ran long-duration tests.

### Elastic Scaling: Community Support

I provided direct assistance to the Peaq team to optimize their maximum Transaction Per Second (TPS) on their 500ms blocks testnet setup: [PRs](https://github.com/peaqnetwork/peaq-network-node/issues?q=state%3Aclosed%20is%3Apr%20author%3A%40me).

### Improved Parachain Block Production Reliability

I started this project by creating the [plan](https://github.com/orgs/paritytech/projects/119/views/27) to improve block confidence in 2025 and 2026. Block confidence is defined as the ratio of finalized to produced blocks. The goal is to increase transaction `in-block` status confidence, which is critical for low-latency Web3 applications.

I worked with my team to deploy the [Kusama Canary parachain](https://github.com/paritytech/polkadot-sdk/issues/9589), which provided logs to analyze and identify the [top issues](https://github.com/paritytech/polkadot-sdk/issues/9344#issuecomment-3548050625) affecting block confidence.

I improved collator connectivity with a pre-connect mechanism implemented in [#9929](https://github.com/paritytech/polkadot-sdk/pull/9929), [#10305](https://github.com/paritytech/polkadot-sdk/pull/10305), [#10446](https://github.com/paritytech/polkadot-sdk/pull/10446), as well as observability improvements in [#9417](https://github.com/paritytech/polkadot-sdk/pull/9417) and [#9844](https://github.com/paritytech/polkadot-sdk/pull/9844).

### Polkadot advocacy

I actively participated in the Polkadot Builder Party:

- Gave a [talk](https://www.youtube.com/watch?v=exhL2_gXScM) on the scalability of the Polkadot Cloud.
- Developed an [on-chain tic-tac-toe game](https://sandreim.github.io/letsplayagame/) for a live demonstration at the event. This showcased the improved user experience enabled by shorter block times (500ms blocks). The game backend is available in [this PR](https://github.com/paritytech/polkadot-sdk/pull/10165/) and the frontend code in [this repository](https://github.com/sandreim/tictactoe3).

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|III|70%   |100%  | 100% | 58 out of the 58 |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
