# Argument-0005: Retention at Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/06/09)                                                             |
| **Submitted by**| Adrian Catangiu                                                                        |


## Member details

- Matrix username: @adrian:parity.io
- Polkadot address: 121dd6J26VUnBZ8BqLGjANWkEAXSb9mWq1SB7LsS9QNTGFvz
- Current rank: III (Fellow)
- Date of initial induction: 2023/06/12
- Date of last report: 2024/12/29
- Area(s) of Expertise/Interest: Trustless Bridges, XCM, System Chains, BEEFY


## Reporting period

- Start date: 2025/01/01
- End date: 2025/06/30


## Argument

During the reporting period I have continued work on improving the UX and feature set of Polkadot trustless bridges and XCM. I also explored how trustless bridges and XCM can enable Cross-Ecosystem-Businesses. The other main target of my focus was the Asset Hub Migration and introduction of smart contracts to Asset Hub.

### XCM UX improvements

Continuing the work from last year, XCMv5 development has now been finished, the features audited and released with Polkadot-SDK `stable2503` release. Myself and Cisco are actively working now to integrate it to System Chains.

I've finished the implementation of [XCM Empowered cross-chain origins](https://github.com/paritytech/polkadot-sdk/issues/6054) (main PRs: [[1]](https://github.com/paritytech/polkadot-sdk/pull/6336) and [[2]](https://github.com/paritytech/polkadot-sdk/pull/7983)) and am currently working to integrate the functionality to the Fellowship runtimes. This work will enable single-click (single-signature) complex cross-chain user journeys; e.g. User uses USDC on Asset Hub to DCA into DOT using Hydration; or User has account only on Asset Hub but can register identity (and pay fees, deposit, etc) on People chain in a single action.

In parallel, I've been working with Raymond on [XCM Observability & Debuggability](https://github.com/paritytech/polkadot-sdk/issues/6119) through a long list of PRs (tracked in the linked issue) meant to improve *Message Tracking* across chains, improve *on-chain visibility for root cause in case of errors*, and in general improve *debuggability*, as these were flagged as major UX and DX painpoints when working with XCM.

### Snowbridge major upgrade

Snowbridge is a trustless Polkadot<>Ethereum bridge operating live since last year (2024). Since its initial deployment it has received some new features and many improvements, all working on its initial design.  
In the background however the Snowfork team and the Parity Bridges team led by me have been working on a new design for this bridge to improve multiple aspects of it. [The design](https://github.com/paritytech/polkadot-sdk/blob/master/bridges/snowbridge/docs/v2.md) itself was completed last year and was covered by my previous reporting period. This reporting period, I provided critical contributions to the [implementation of said design](https://github.com/paritytech/polkadot-sdk/pull/7402).  

The new version of the bridge is not live yet, it is currently being integrated to Bridge Hub and Asset Hub runtimes and is estimated to go live in Q3 this year. However, test deployments of the bridge have been validated and based on data modeled from these test deployments, we are expecting significant cost reductions for users of the bridge, on top of the new features it brings.

Message average cost modeling for recent DOT and ETH prices and Ethereum gas costs:

|  | Polkadot -> Ethereum | Ethereum -> Polkadot |
|---|---|---|
| Snowbridge V1 (live) | ~ 7 USD | ~ 2 USD |
| Snowbridge V2 (Q3 2025) | 0.9 USD | 0.65 USD |

On top of lower costs, the new bridge implementation leverages XCMv5 to support complex, multi-destination asset transfers, accurate fees estimations and even arbitrary Smart Contract calls or Runtime calls over the bridge.

### Cross-Ecosystem-Businesses

I wrote [an article](https://hackmd.io/@acatangiu/SkxHNEnYcJl) on how trustless bridges in Polkadot can enable _Cross Ecosystem Unified Businesses_, and am currently discussing strategies with **Integritee**, **Bifrost**, **Peaq**, and **Robonomics** about how they can unify their Polkadot and Kusama businesses.

### Asset Hub Migration

I am also involved in the Asset Hub Migration, actively participating in design reviews for most components, recently working with Branislav on the design for ensuring Polkadot resilience even in situations where Asset Hub or potentially all parachains are bricked and we need some fallback governance mechanism on the Relay Chain to recover the Polkadot ecosystem. I will let Branislav share the detailed design once it is complete, but the high-level summary is that we will deploy a storage-proof based mechanism on the Relay Chain under which Asset Hub DOT-holders or Collectives Fellowship members can still vote, even in the case where Asset Hub (OpenGov) or Collectives (Fellowship) are stalled or bricked.  
I covered the required [XCM configuration changes]((https://github.com/polkadot-fellows/runtimes/pull/722)) to the Relay chain and Asset Hub to support cross-chain operations before, during and after the migration. I also [designed](https://github.com/polkadot-fellows/runtimes/pull/716) and [implemented](https://github.com/polkadot-fellows/runtimes/pull/607) the logic required to effectively migrate DOT total issuance tracking from the Relay Chain to Asset Hub.

## Voting record

Based on Oliver's [dashboard](https://fellowship.tasty.limo/), my global voting participation is 94.59% having voted on 70 out of 74 referenda in which I was eligible to vote.

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  | 94.59% | There were a few referenda where I initially voted one way, but later changed my vote in line with higher ranks consensus. |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- Consistent reviewer for both [Fellowship runtimes](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr++reviewed-by%3Aacatangiu+created%3A2025-01-01..2025-06-30+) and [Polkadot-SDK](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr++reviewed-by%3Aacatangiu+created%3A2025-01-01..2025-06-30+).

