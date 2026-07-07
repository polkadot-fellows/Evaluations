# Argument-0009: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/07/07                                                             |
| **Submitted by**| Jesse Chejieh                                                                        |


## Member details

- Matrix username: @jessechejieh:matrix.org
- Polkadot address: 12zsKEDVcHpKEWb99iFt3xrTCQQXZMu477nJQsTBBrof5k2h
- Current rank: II
- Date of initial induction: 2022/09/29
- Date of last report: 2026/04/10
- Link to last report: https://github.com/polkadot-fellows/Evaluations/pull/276
- Area(s) of Expertise/Interest: FRAME, Runtime


## Reporting period

- Start date: 2026/04/10
- End date: 2026/07/07

## Argument
During this reporting period, focus remained on FRAME governance automation and treasury resilience: the permissionless scheduler moved from design to a working implementation, both open RFC implementations advanced through review, and I began hosting the Fellowship's monthly OpenDev calls.

### Permissionless Scheduling ([#9966](https://github.com/paritytech/polkadot-sdk/issues/9966), ongoing)
The permissionless scheduler moved from design to a [proof-of-concept](https://hackmd.io/sLGQCmxiQyO4zXH46J6c4A) pallet: one-time and recurring `RuntimeCall` execution on the FRAME Task System. Community input shaped the cost and safety model. Storage deposits go through `Consideration`, each run is charged at execution-time prices from prepaid funds, scheduled calls share a per-block weight budget, and call filters are re-checked at execution. [#12227](https://github.com/paritytech/polkadot-sdk/pull/12227) (merged) auto-bounds `RuntimeTask: From<Task<Self>>` in FRAME, removing per-pallet boilerplate for pallets built on the Task System.

### RFC: [Deferred Dispatch](https://github.com/paritytech/polkadot-sdk/pull/11336) (ongoing)
Continued deferred dispatch for `pallet-whitelist`: a referendum-enacted whitelisted call is banked in storage instead of consuming the authorization when enactment races ahead of whitelisting. This period addressed review feedback and integration-tested the pallet against the Fellowship runtimes.

### RFC: [Ordered Spend Payouts](https://github.com/paritytech/polkadot-sdk/pull/11603) (ongoing)
Continued the FIFO-per-`AssetKind` treasury payout ordering. It overlaps with Treasury Asset Categories ([#10381](https://github.com/paritytech/polkadot-sdk/pull/10381)) on the same dispatchables and `Spends` migration, so the two implementations are being reconciled.

### Runtime Maintenance & Operations
The [Secretary Collective budget increase](https://github.com/polkadot-fellows/runtimes/pull/1172) doubles the collective's monthly budget for onboarding a Technical Coordinator.

### OpenDev Hosting Pilot
Under the [hosting pilot](https://hackmd.io/529HcCT2TCGYQVRIYoeDzg), currently running the Fellowship's monthly OpenDev calls. The first, on 2026/06/30, centred on RFC #171 (asset-based storage deposits) and settled on migrating pallets off hardcoded `Currency` deposits onto `Consideration` as a priority; [proceedings](https://forum.polkadot.network/t/opendev-call-proceedings-30-june-2026/18029) are on the Forum.

## Voting record
|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |100%  |I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e undefined% voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e undefined% voting agreement).  | No referenda requiring Rank II votes during this period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
