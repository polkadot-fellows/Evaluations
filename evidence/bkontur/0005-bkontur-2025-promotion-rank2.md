# Argument-0005: Promotion to Rank II

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2025/06/27) |
| **Submitted by**| Branislav Kontur                |


## Member details

- Matrix username: @branislav_kontur:parity.io
- Polkadot address: 1HFq3DbX4tqanTLAx2CAToWnHXg6LRLMzSD4JzYCzCQpw5E
- Current rank: 1
- Date of initial induction: 2024/05/03
- Date of last report: 2025/05/16
- Area(s) of Expertise/Interest: `Bridges, XCM, System Parachains, governance, benchmarking, testing, integration`


## Reporting period

- Start date: 2024/05/03
- End date: 2025/06/27

## Argument

I believe I have demonstrated both the technical depth and the collaborative maturity expected of a Rank II Fellow. My work consistently aligns with the Polkadot Fellowship’s core mission: ensuring the protocol's long-term safety and resilience while enabling its evolution. Below is a summary of my contributions across the most relevant domains, based on my previous retention arguments and ongoing work.

### Bridges

Over the last several quarters, I have been focusing on the **permissionless lanes** feature for Substrate-to-Substrate bridges. I authored and/or drove forward several key PRs ([\[1\]](https://github.com/paritytech/polkadot-sdk/pull/4949), [\[2\]](https://github.com/paritytech/polkadot-sdk/pull/5649), [\[3\]](https://github.com/paritytech/polkadot-sdk/pull/6231), [\[4\]](https://github.com/paritytech/polkadot-sdk/pull/6675), [\[5\]](https://github.com/paritytech/polkadot-sdk/pull/8324), [\[6\]](https://github.com/paritytech/polkadot-sdk/pull/8326), [\[7\]](https://github.com/paritytech/polkadot-sdk/pull/8368)), and initiated a [design document](https://hackmd.io/@bkontur/HyyuHlzAA) and deployment strategy for this feature on **AssetHub**, as part of the broader Polkadot/Kusama bridging vision.

I am now finalizing support for **deploying bridge messaging pallets directly on AssetHub** parachains - a cheaper messaging and/or avoiding the extra hop through BridgeHubs. However, this work was deprioritized in favor of other tasks (e.g. AHM-related). This work is nearly complete and currently undergoing internal review and security auditing.

I am also assisting with mentoring colleagues contributing to a new bridge that will support the **Proof of Personhood** feature, as referenced in George’s [argument](https://collectives.subsquare.io/fellowship/referenda/335).

Besides that, I have been helping Snowbridge deliver their V2, primarily through PR reviews.

### Governance Migration & D-Day Mechanism

I took **ownership of the D-Day governance design** for the upcoming **AssetHub governance migration (AHM)**, as mentioned in my previous retention argument. My contributions include:
- Analyzing governance fallback strategies,
- Developing a **working PoC** for governance rescue via proof-based voting from stalled chains,
- Preparing the [initial design document](https://hackmd.io/@bkontur/SJ07ySIlgx),
- Presenting this work at the **AHM retreat**, where it influenced major governance design decisions.

Following the conclusions of the AHM retreat, I reworked the design and authored a new, final document covering multiple alternatives. This document is currently under internal review and will be published once finalized.

In addition, I contributed various fixes (e.g., [PR #7592](https://github.com/paritytech/polkadot-sdk/pull/7592)) and provided support for the ongoing **XCM-based governance migration** (e.g., [PR #8210](https://github.com/paritytech/polkadot-sdk/pull/8210)), mentoring contributors through complex edge cases and migration-related challenges.

As part of the AHM OpenGov migration to AssetHubs, I identified a lack of test coverage for key governance scenarios - such as `authorize_upgrade` for system parachains - and implemented initial [unit tests](https://github.com/paritytech/polkadot-sdk/pull/7656) for runtimes, as well as more complex [integration tests](https://github.com/polkadot-fellows/runtimes/pull/626). With help from Karol Kokoszka, these tests were later ported to the polkadot-fellows repository: [https://github.com/polkadot-fellows/runtimes/pull/783](https://github.com/polkadot-fellows/runtimes/pull/783). These tests will be important in supporting the new OpenGov configurations on AssetHubs ([for Polkadot](https://github.com/polkadot-fellows/runtimes/pull/626), [for Kusama](https://github.com/polkadot-fellows/runtimes/pull/776)).

I am currently working on the last two PRs to prepare **OpenGov on AssetHubs** as part of the AHM initiative.


### XCM Evolution

While I haven’t authored new XCMv5 features, I’ve **reviewed nearly all major XCMv5 PRs**, contributed with fixes (e.g., [#6148](https://github.com/paritytech/polkadot-sdk/pull/6148), [#6467](https://github.com/paritytech/polkadot-sdk/pull/6467)), and opened design-level issues for improvements to `pallet-xcm` and `pallet-assets`.
In the course of this, I documented bugs (e.g., [XCMv5-v4 regression](https://github.com/paritytech/polkadot-sdk/issues/6585)) and helped with follow-up efforts. I also contributed to improvements around **XCM executor barriers** (e.g., [#7148](https://github.com/paritytech/polkadot-sdk/issues/7148)) and guided colleagues toward successful implementation.
Besides that I found other several XCM-related nits/bugs/improvements (for example, [[1]](https://github.com/paritytech/polkadot-sdk/issues/8185), [[2]](https://github.com/paritytech/polkadot-sdk/issues/8499), [[3]](https://github.com/paritytech/polkadot-sdk/issues/8583)).
I also helped Interlay/Kintsugi with XCM version issue.

### Work for Fellows: Tooling, Weights, Stability

I am actively maintaining and improving infrastructure in the **polkadot-fellows** repository:
- Delivered the missing **benchmark checking CI pipeline** using `frame-omni-bencher`,
- Generated weights for multiple runtime releases (we no longer need to do this manually - this is now handled by the bench bot - see the next point),
- Contributed to the **bench bot** for runtime benchmarking and validation, which can now generate valid weights (for example: [\[1\]](https://github.com/polkadot-fellows/runtimes/issues/770#issuecomment-2996621457), [\[2\]](https://github.com/polkadot-fellows/runtimes/issues/726)),
- Helped others complete stable SDK bumps (e.g., `stable2409`, `stable2412`, `stable2503`), resolving blocking issues along the way,
- Identified and fixed problems with review bots: https://github.com/polkadot-fellows/runtimes/issues/743

Beyond individual patches, I continue working on improving CI stability and contribute to enhancements. I also remain active as a PR reviewer.

### Reflections and Motivation

I proactively identify, create, and resolve issues across both the SDK and Fellows ecosystems. This includes contributing solutions to problems reported by external teams (e.g., Integritee, Encointer), and creating multiple mentoring tasks and "good first issues" to help onboard new contributors. My role at Parity has naturally evolved into one of **mentorship and delegation** - guiding contributors both inside and outside the organization, reviewing PRs across domains, and supporting upstream efforts in bridges, governance, and XCM.
I am ready to take on the **greater responsibility** associated with Rank II: participating in technical decision-making, voting on promotions, and helping uphold the safety and direction of the Polkadot protocol.

###  References

* Polkadot SDK Contributions: [PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Abkontur+)
* Polkadot Fellows Contributions: [PRs](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Abkontur+)
* Personal GitHub Board: [Link](https://github.com/orgs/paritytech/projects/188/views/1)

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

