# Argument-0004: Retention at Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/07/02)                                                             |
| **Submitted by**| Tsvetomir Dimitrov                                                                          |


## Member details

- Matrix username: @tsvetomir:parity.io
- Polkadot address: 1QhVP5qzR2LfXqP77N1JcuwHoY7NH8JVRNFm1hSooE9d4pR
- Current rank: 2
- Date of initial induction: 2023/10/11
- Date of last report: 2025/02/20
- Area(s) of Expertise/Interest: Disputes, Agile Coretime, Collator protocol


## Reporting period

- Start date: 2025/02/20
- End date: 2025/07/02


## Argument

During the reporting period I worked on the AssetHub Migration, more concretely on decoupling
`pallet-session` from `pallet-staking` (which became `pallet-staking-async`). I did the initial
implementation of `pallet-staking-async-ah-client` and `pallet-staking-async-rc-client`. The former
lives on relay chain and implements the interface of the former `pallet-staking` while the latter
lives on AssetHub and implements the interface of `pallet-session`. The pallets communicate with
each other with XCM messages. The change is implemented in:
- [polkadot-sdk pr-7582](https://github.com/paritytech/polkadot-sdk/pull/7582)
- [polkadot-sdk pr-7658](https://github.com/paritytech/polkadot-sdk/pull/7658)
- [polkadot-sdk pr-7941](https://github.com/paritytech/polkadot-sdk/pull/7941)

I was also involved in the [dispute storm on Kusama](https://forum.polkadot.network/t/2025-05-09-kusama-dispute-storm-postmortem/12947) investigation. More concretely I was working on
the emergency patch to unstall the relay chain (more details in [polkadot-sdk pr-8483](https://github.com/paritytech/polkadot-sdk/pull/8483)). As part of the efforts to mitigate the dispute storm issue I've
implemented a per session validator indices caching in `dispute-coordinator` because it involved an
expensive key derivation operation which was executed on each new leaf.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e 100 % voting agreement). | There were no referendas I could participate in during the reporting period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):

