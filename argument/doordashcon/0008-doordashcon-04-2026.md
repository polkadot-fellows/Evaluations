# Argument-0008: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/04/10)                                                             |
| **Submitted by**| Jesse Chejieh                                                                        |


## Member details

- Matrix username: @doordashcon/:matrix.org
- Polkadot address: 12zsKEDVcHpKEWb99iFt3xrTCQQXZMu477nJQsTBBrof5k2h
- Current rank: II
- Date of initial induction: 2022/09/29
- Date of last report: 2025/12/27
- Area(s) of Expertise/Interest: FRAME, Runtime


## Reporting period

- Start date: 2025/12/27
- End date: 2026/04/10


## Argument
During this reporting period, focus remains on enhancing FRAME's governance infrastructure, specifically introducing time-delayed execution for dispatching whitelisted calls, improving treasury payout fairness and liquidity management, and laying the groundwork for permissionless automation primitives. This work is centered on making the treasury more resilient and flexible while expanding the capabilities of on-chain governance mechanisms.

### RFC: [Deferred Dispatch](https://github.com/paritytech/polkadot-sdk/pull/11336)
This solves a critical governance race condition. Previously, if a referendum enacted a whitelisted call before the Fellowship whitelisted it, the authorization is consumed and requires an entirely new referendum. Now, the dispatch is deferred/banked in storage. Once the call is whitelisted, any user can trigger execution. This prevents permanent loss of governance authorization due to simple timing mismatches.

### RFC: [Ordered Spend Payouts](https://github.com/paritytech/polkadot-sdk/pull/11603)
Enforces FIFO ordering per `AssetKind` to solve a fairness flaw in treasury payouts. Previously, smaller, later-approved spends could jump the queue and drain available liquidity, leaving larger, earlier-approved spends stuck indefinitely. Now, no spend gets paid until all earlier-approved spends of that asset are either paid or expired. This ensures approval order reflects actual payout priority, preventing liquidity fragmentation, and makes treasury behavior more predictable.

### Permissionless Scheduling Infrastructure
The existing scheduler is privileged, leaving contracts and regular accounts unable to automate future actions. I authored a [design implementation](https://hackmd.io/sLGQCmxiQyO4zXH46J6c4A) focusing on permissionless one-time or recurring `RuntimeCall` execution at future timestamps, pre-funding costs via deposit. Built on the FRAME Task System with an EVM precompile, this unlocks automated DeFi protocols, recurring payments, and autonomous on-chain agents.

### Treasury Asset Categories (Ongoing)
I continue developing [asset category support](https://github.com/paritytech/polkadot-sdk/pull/10381) for `pallet-treasury`, further aiding liquidity fragmentation by allowing the treasury to distribute payouts across multiple available assets in a predefined category, complementing the ordered payouts feature to create a more resilient treasury system.

### Runtime Maintenance & Operations
Adapting the [Secretary salary paymaster](https://github.com/polkadot-fellows/runtimes/pull/1067) into the existing Fellowship salary account. Reducing operational complexity and maintenance overhead for the collective's payment systems.

### Account Transition Notice
I would like to formally note the transition from the @Doordashcon GitHub and Matrix account to @jessechejieh for all future contributions and communications, as documented in the [Fellowship help-center](polkadot-fellows/help-center#15). Both accounts represent my work, and all future contributions will be pushed exclusively from @jessechejieh in Q2 2026.

## Voting record
|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II|80%   |100%  |I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e undefined% voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e undefined% voting agreement).  | No referenda requiring Rank II votes during this period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

