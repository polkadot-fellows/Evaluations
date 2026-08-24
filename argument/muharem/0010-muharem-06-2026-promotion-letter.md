# Argument-0010: Promotion to Rank III

|                 |              |
| --------------- | ------------ |
| **Report Date** | 2026/06/22   |
| **Submitted by**| muharem      |


## Member details

- Matrix username: `@muharem:parity.io`
- Polkadot address: `12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2`
- Current rank: `2`
- Date of initial induction: `2023/11/11`
- Date of last report: `2026/05/27`
- Area(s) of Expertise/Interest: `System Parachains, FRAME, XCM`


## Reporting period

- Start date: 2023/11/11
- End date: 2026/06/22

## Argument

I joined the Fellowship at Rank II in November 2023. Since then, my role within the ecosystem has gradually evolved from implementing protocol features and components to taking responsibility for the design, delivery, and operation of protocol initiatives spanning multiple domains.

The clearest example of this progression is the Asset Hub Migration project, which became my primary focus for most of the past year.

### Asset Hub Migration

The Rank III requirements state:

> Either played a supporting role in the code-design and a primary role in the implementation of a major protocol component.

The Asset Hub Migration was a major protocol initiative whose objective was to move user-facing functionality from the Relay Chain to Asset Hub in support of the Minimal Relay direction and the broader Plaza vision.

I worked on the project from its early research phase through design, implementation, testing, and ultimately execution on Paseo, Kusama, and Polkadot.

Early in the project, I explored and presented several possible approaches for performing the migration. One of the options I proposed was to execute the migration through XCM rather than relying on off-chain migration. This approach was ultimately adopted and became a core part of the migration architecture. I also proposed building a dedicated migration framework alongside the runtimes rather than deeply integrating migration logic into existing SDK components. This gave us greater flexibility, reduced dependency-management overhead, and allowed us to iterate significantly faster throughout development.

Another important architectural decision concerned consistency guarantees during migration. I proposed treating the migration as an atomic process while permitting temporary inconsistencies during execution, with user interaction disabled for affected subsystems until the migration completed. This significantly reduced implementation complexity while preserving the correctness guarantees required by the protocol and helped keep the migration manageable throughout development.

My work spanned many areas of the migration effort, from migration infrastructure and execution flow to subsystem-specific migrations. This included ownership of the Balances and Governance migrations, covering account balances together with holds, freezes, locks, reserves, and associated account state, as well as active governance state and proposals. Each subsystem introduced its own technical and operational challenges and required balancing implementation complexity, migration safety, and existing protocol expectations.

As the migration moved closer to production, my focus increasingly shifted toward operational robustness. I designed and implemented mechanisms such as replayability, idempotent execution, migration traffic prioritization, acknowledgment handling for migration messages, warm-up and cool-off stages, and recovery procedures. I also introduced benchmarking and weight accounting on both the sending (Relay Chain) and receiving (Asset Hub) sides of the migration pipeline. This allowed migration throughput to be tuned based on the actual processing capacity of Asset Hub, preventing excessive backpressure while maintaining predictable execution. In addition, I participated in defining migration acceptance criteria and execution procedures.

The project ultimately culminated in successful migrations on Paseo, Kusama, and Polkadot without major incidents. Beyond the technical implementation itself, it required sustained decision-making across architecture, execution, testing, operational planning, and coordination over the course of more than a year.

### Protocol Development

Before and alongside the migration effort, I worked extensively on Governance, Treasury, Asset Hub, and related protocol infrastructure.

My contributions during this period included governance improvements, Multi-Asset Bounties, transaction payment infrastructure, asset-related infrastructure and functionality, XCM-related work, runtime releases, and migration-related infrastructure. This included enabling transaction fee payment through non-native assets, contributing to cross-chain functionality and Asset Hub capabilities, and supporting the continued evolution of governance and treasury systems. Several of these efforts involved protocol design, RFCs, and long-term ownership beyond the initial implementation.

More recently, I have been involved in the exploration of decentralized stablecoin designs for Polkadot. The goal of this work is to investigate a permissionless framework that would enable stablecoin launches within the ecosystem under different configurations and governance models. My contributions have focused on evaluating architectural trade-offs, reviewing implementations, proposing design changes, and helping shape the technical direction of the initiative.

Throughout this period, I also continued contributing reviews, runtime release work, and fixes across the SDK and runtime codebases. In recent months, I have been spending more time identifying and addressing correctness and security issues as part of broader efforts to improve the robustness of the systems I work on.

### Knowledge Sharing and Mentorship

The Rank III requirements state:

> Demonstrable presence of knowledge sharing within the ecosystem.

Over time, I have increasingly focused on helping other contributors become productive in areas where I previously held primary responsibility.

I mentored [@dhirajs0](https://github.com/dhirajs0) on Governance topics, and [@cirko33](https://github.com/cirko33) on Meta Transactions. More recently, I have also been working closely with [@Szegoo](https://github.com/Szegoo) on economic infrastructure initiatives.

One example is @dhirajs0’s growth within the Governance domain. Over time, he has taken ownership of a substantial portion of the Governance-related work that I previously led, allowing me to move into a more advisory role while remaining available for design discussions and final technical decisions.

Knowledge sharing has also taken the form of technical reviews, design discussions, forum posts, runtime reviews, and helping contributors communicate and document their work. While not all publications were authored under my name, I have often guided their technical content and supported the resulting community discussions.

### Summary

Over the last two years, my role within the ecosystem has evolved from implementing protocol features to taking responsibility for protocol initiatives spanning multiple domains.

The Asset Hub Migration was the largest completed project I helped deliver during this time and brought together many of the technical, operational, and coordination responsibilities I had gradually taken on. Alongside this work, I increasingly focused on mentoring contributors and supporting delivery across multiple areas of the protocol.


### Selected References

* Asset Hub Migration PRs  
  <https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Amuharem+%5BAHM%5D>
* SDK PRs for the period  
  <https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Amuharem+created%3A%3E2023-11-11>
* RFC: Permissionless Authorized Dispatch for pallet-whitelist  
  <https://github.com/paritytech/polkadot-sdk/issues/12224>
* RFC: Deferred Dispatch for pallet-whitelist  
  <https://github.com/paritytech/polkadot-sdk/issues/11199>
* RFC: Ordered Spend Payouts  
  <https://github.com/paritytech/polkadot-sdk/issues/11100>
* RFC: Treasury API for Cross-Chain Transfers  
  <https://github.com/paritytech/polkadot-sdk/issues/4715>
* RFC: Meta Transaction Implementation  
  <https://github.com/paritytech/polkadot-sdk/issues/4123>
* Forum Post: Multi-Asset Bounties  
  <https://forum.polkadot.network/t/multi-asset-bounties-now-live-on-westend-testing-and-roadmap/16899>
* Forum Post: Meta Transactions Support for Polkadot  
  <https://forum.polkadot.network/t/meta-transactions-support-for-polkadot/17551>
* Forum Post: Multi-Asset Treasury and Milestone-Based Spends  
  <https://forum.polkadot.network/t/multi-asset-treasury-and-milestone-based-spends/6780>

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   | None |
|II |80%   |N/A   |   | None |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
