# Evidence-0003: Retention at Rank 1

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2025/02/22) |
| **Submitted by**| Branislav Kontur                |


## Member details

- Matrix username: @branislav_kontur:parity.io
- Polkadot address: 1HFq3DbX4tqanTLAx2CAToWnHXg6LRLMzSD4JzYCzCQpw5E
- Current rank: 1
- Date of initial induction: 2024/05/03
- Date of last report: 2024/11/29
- Area(s) of Expertise/Interest: `Bridges, XCM, System Parachains, benchmarking, testing, integration`


## Reporting period

- Start date: 2024/11/30
- End date: 2025/02/22


## Evidence

This summary outlines my activities, contributions, and collaborations during the reporting period.

My regular agenda around (P/K) Bridges is focused on advancing the stream where we aim to deploy bridge messaging pallets directly on AssetHub ([Issue 6116](https://github.com/paritytech/polkadot-sdk/issues/6116)). Besides that, I worked on a small pallet refactor to support Snowbridge V2 ([PR 7492](https://github.com/paritytech/polkadot-sdk/pull/7492)).

However, a higher priority has been the upcoming AssetHub migration (AHM), where I took ownership of the D-Day governance sub-issue. I began with a short analysis of the current state ([comment](https://github.com/paritytech/polkadot-sdk/issues/5588#issuecomment-2633365808)) and explored possible solutions. D-Day governance refers to migrating governance from the Relay Chain to AssetHub while ensuring the ability to restart or rescue a stalled parachain from another parachain. For example, Collectives could rescue AssetHub and vice versa. As part of this issue, I identified several problems, which I am addressing by either connecting different issues and components (e.g., [Issue 7445](https://github.com/paritytech/polkadot-sdk/issues/7445)) or implementing fixes directly (e.g., [Issue 7574](https://github.com/paritytech/polkadot-sdk/issues/7574)).
I am also working on reviewing, identifying, and proposing solutions for governance migration itself ([[1]](https://github.com/paritytech/polkadot-sdk/issues/7578), [[2]](https://github.com/paritytech/polkadot-sdk/issues/7577), [[3]](https://github.com/paritytech/polkadot-sdk/issues/7591), or [PoC for a XcmPallet calls conversion](https://github.com/polkadot-fellows/runtimes/pull/600)), as well as improving testing support: [PR 7656](https://github.com/paritytech/polkadot-sdk/pull/7656).

Regarding my XCM-related work, while reviewing one of the Snowbridge V2 PRs, I identified several issues around the `xcm-executor` `type Barrier` ([Issue 7148](https://github.com/paritytech/polkadot-sdk/issues/7148)). I primarily provided guidance to others for implementation.

For the `polkadot-fellows` repository, I applied the `stable2409` patch for Bridges ([PR 519](https://github.com/polkadot-fellows/runtimes/pull/519)). I prepared fresh weights for the 1.4.0 release ([PR 522](https://github.com/polkadot-fellows/runtimes/pull/522)). I migrated `CollectivesPolkadot` XCM weights from fixed to measured ones ([PR 547](https://github.com/polkadot-fellows/runtimes/pull/547)). I helped set up benchmarks for the remote-proxy pallet ([PR 573](https://github.com/polkadot-fellows/runtimes/pull/573)).

I have also been actively identifying and fixing various issues, including: [Fixing `parity-publish`](https://github.com/paritytech/parity-publish/pull/43), [Addressing a Fellows CI nit](https://github.com/polkadot-fellows/runtimes/pull/530), [Fixing CI check-migrations](https://github.com/polkadot-fellows/runtimes/issues/531), [Investigating and addressing a PAPI CI problem](https://github.com/polkadot-api/polkadot-api/issues/918), [Identifying a `try-runtime` issue](https://github.com/paritytech/try-runtime-cli/issues/109) and proposing a temporary fix for Fellows ([PR 590](https://github.com/polkadot-fellows/runtimes/pull/590)).

I actively participate in PR reviews for `polkadot-fellows` and `polkadot-sdk`. I have also created several mentoring and "good first issue" tasks, which can be found [here](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue%20state%3Aopen%20author%3Abkontur%20created%3A%3E2024-11-30%20%20created%3A%3C2025-02-22).

Overall, if anyone is interested in my current focus on the most important topics, please check my board: [GitHub Board](https://github.com/orgs/paritytech/projects/188/views/1).

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity).  | - |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

