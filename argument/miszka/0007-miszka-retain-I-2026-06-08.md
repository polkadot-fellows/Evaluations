# Argument-0007: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/06/08
| **Submitted by**| Michał Kucharczyk                                                                           |


## Member details

- Matrix username: `@michal:parity.io`
- Polkadot address: [14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo](https://collectives.statescan.io/#/accounts/14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo)
- Current rank: 1
- Date of initial induction: `2024/06/02`
- Date of last report: `2026/03/05`
- Area(s) of Expertise/Interest: `Substrate node` ,`Transaction Pool`, `ChainSpec/GenesisConfig`


## Reporting period

- Start date: 2026/03/05
- End date: 2026/06/08

## Argument

During this period I worked on the Substrate node, the fork-aware transaction pool, light-client data retrieval, test tooling, and JAM metrics observability.

**Light-client data retrieval (bitswap).** I worked on a streaming bitswap RPC: I extended the existing bitswap implementation with streaming functionality. The method is specified in [json-rpc-interface-spec#186](https://github.com/paritytech/json-rpc-interface-spec/pull/186), implemented node-side in [polkadot-sdk#12029](https://github.com/paritytech/polkadot-sdk/pull/12029), with matching light-client support in smoldot ([#3264](https://github.com/paritytech/smoldot/pull/3264), plus an advertised-address fix in [#3245](https://github.com/paritytech/smoldot/pull/3245)). To get some visibility into this load I proposed a light-client/bitswap metrics scheme ([polkadot-sdk#12083](https://github.com/paritytech/polkadot-sdk/issues/12083)) and added the litep2p bitswap metrics in [#12232](https://github.com/paritytech/polkadot-sdk/pull/12232). I also reviewed the related PRs: the bitswap client ([#12038](https://github.com/paritytech/polkadot-sdk/pull/12038)), `TransactionStorageApi` v2 ([#11939](https://github.com/paritytech/polkadot-sdk/pull/11939)), prefetched indexed transactions ([#12086](https://github.com/paritytech/polkadot-sdk/pull/12086)), and the runtime-api storage-overlay change ([#12084](https://github.com/paritytech/polkadot-sdk/pull/12084)), which deepened my knowledge of the bulletin chain.

**Fork-aware transaction pool.** The pool continues in maintenance mode, mostly around stuck-transaction edge cases. I looked into and fixed a case where a per-fork validation ban propagates across all views and silently rejects an otherwise-valid transaction for the full ban duration ([unban viewless transactions after mempool revalidation, #11731](https://github.com/paritytech/polkadot-sdk/pull/11731)), and fixed a wrong `inblock` event ([#11733](https://github.com/paritytech/polkadot-sdk/pull/11733)).

**Test tooling — Zombienet snapshots.** Building DB snapshots for warp-sync and light-client smoke tests had been hand-rolled in each test. I proposed ([zombienet-sdk#541](https://github.com/paritytech/zombienet-sdk/issues/541)) and added a snapshot API to the SDK.

**JAM / PolkaJam.** I continued the metrics observability work on [jamtart](https://github.com/paritytech/jamtart): after some further [events-streaming improvements](https://github.com/paritytech/jamtart/pull/14), I worked on [#15](https://github.com/paritytech/jamtart/pull/15) (a cross-event enricher, Grafana endpoints for JIP-3 telemetry, on-chain endpoints from JAM RPC, some database schema and query changes, and Grafana dashboards). This is still very much work in progress that I plan to get back to.

The [PoV size reclaim fix (#10215)](https://github.com/paritytech/polkadot-sdk/pull/10215) and [RFC-158](https://github.com/polkadot-fellows/RFCs/pull/158) remain open and carried over from the previous period.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | None. |   |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
