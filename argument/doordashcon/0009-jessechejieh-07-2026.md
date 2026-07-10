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
The FRAME scheduler is privileged, so contracts and ordinary accounts cannot schedule future actions on-chain. Without a permissionless primitive, recurring payments, automated DeFi strategies like liquidations and rebalancing, and autonomous agents rely on off-chain keepers, which are trust-assumed and can silently stop. This period the scheduler moved from [design](https://hackmd.io/sLGQCmxiQyO4zXH46J6c4A) to a working proof-of-concept [`pallet-cron`](https://github.com/jessechejieh/polkadot-sdk/blob/jc-cron-poc/substrate/frame/cron/src/lib.rs) for one-time and recurring `RuntimeCall` execution on the FRAME Task System, so any account can pay to schedule a call the runtime then executes. The open question was doing this without opening a spam or unfunded-execution vector: storage deposits go through `Consideration`, each run is charged at execution-time prices from prepaid funds, scheduled calls share a per-block weight budget, and call filters are re-checked at execution so a later-restricted call cannot slip through. [#12227](https://github.com/paritytech/polkadot-sdk/pull/12227) auto-bounds `RuntimeTask: From<Task<Self>>` in FRAME, removing per-pallet boilerplate for pallets on the Task System.

### RFC: [Deferred Dispatch](https://github.com/paritytech/polkadot-sdk/pull/11336) (ongoing)
`pallet-whitelist` gates high-privilege governance calls behind Fellowship approval. Today, if a referendum enacts a whitelisted call before the Fellowship has whitelisted it, the authorization is consumed and the whole referendum must be re-run, so a timing mismatch between two independent governance tracks can permanently burn a passed decision. Deferred dispatch banks the enacted call in storage instead of consuming the authorization; once whitelisting lands, anyone can trigger execution. This removes a class of governance stalls that today need manual re-coordination. This period addressed review feedback and integration testing.

### RFC: [Ordered Spend Payouts](https://github.com/paritytech/polkadot-sdk/pull/11603) (ongoing)
`pallet-treasury` pays approved spends in whatever order they are claimed, so a smaller, later-approved spend can be paid ahead of a larger, earlier-approved one and drain available liquidity, leaving earlier commitments stuck until more funds arrive. FIFO-per-`AssetKind` ordering makes payout order follow approval order, so treasury behaviour is predictable and approval is a real commitment to pay. It overlaps with Treasury Asset Categories ([#10381](https://github.com/paritytech/polkadot-sdk/pull/10381)) on the same dispatchables and `Spends` migration, so this period the two implementations are being reconciled.

### Runtime Operations
The [Secretary Collective budget increase](https://github.com/polkadot-fellows/runtimes/pull/1172) doubles its monthly budget to onboard a Technical Coordinator. The collective runs the Fellowship's operational load; a dedicated coordinator moves that off individual Fellows so it no longer depends on ad-hoc volunteering.

### OpenDev Hosting Pilot
OpenDev is the Fellowship's open technical call, and it had lapsed, leaving technical coordination without a regular synchronous venue. Under the [hosting pilot](https://hackmd.io/529HcCT2TCGYQVRIYoeDzg) I resumed and now host these calls. The [2026/06/30 session](https://forum.polkadot.network/t/opendev-call-proceedings-30-june-2026/18029) centered on asset-based storage deposits and settled on migrating pallets off hardcoded `Currency` deposits onto `Consideration`.

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
