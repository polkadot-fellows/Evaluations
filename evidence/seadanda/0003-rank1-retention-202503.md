# Argument-0003: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/03/22                                                                                  |
| **Submitted by**| Dónal Murray                                                                                |


## Member details

- Matrix username: `@donal:parity.io`
- Polkadot address: <a target='_blank' href='https://collectives.statescan.io/#/accounts/142zGifFwRrDbFLJD7LvbyoHQAqDaXeHjkxJbUVwmDYBD7Gf'>142zGifFwRrDbFLJD7LvbyoHQAqDaXeHjkxJbUVwmDYBD7Gf</a>
- Current rank: **I**
- Date of initial induction: `2024/06/02`
- Date of last report: `2024/12/14`
- Area(s) of Expertise/Interest: `System Parachains, Agile Coretime`


## Reporting period

- Start date: 2024/12/14
- End date: 2025/03/22

## Argument
In this reporting period my main focus has been the realisation of RFC-32 - minimal relay. I have been driving the Asset Hub Migration (AHM) project: moving staking, governance and balances, along with associated functionality, off the relay and onto the Polkadot Hub. This has involved leading a team of developers working across many areas of the system, making architectural decisions, and defining migration scope and trade-offs.
I have been providing technical guidance to ecosystem teams about the migration plan, implementation and timeline through presentations, AMAs and calls with individual teams, and the [Polkadot Forum](https://forum.polkadot.network/t/asset-hub-migration-2025/11129/5).

AHM represents a significant breaking change for many user-facing applications. We have been working to minimise the disruption and give teams as much warning and time to test as possible.
To help with this, I developed a test runtime (Asset Hub Next) representing the future functionality and deployed it as a [new temporary parachain](https://polkadot.js.org/apps/?rpc=wss://westend-asset-hub-next-rpc.parity-chains-scw.parity.io#/explorer) on Westend. We distributed the details with a sidecar instance and critical user journey documentation to help wallets, DApps and CEXs test their integrations some months in advance while the actual migration code is still being written.
The parachain will be removed after we complete the full migration on Westend, therefore the code is on [this branch in `polkadot-sdk`](https://github.com/paritytech/polkadot-sdk/pull/6996), which will not be merged to master.

Another part of the AHM project was improving the end to end testing of the runtimes. I have led a team aiming to improve the end to end story in Polkadot, beginning with those parts relevant to AHM, which has contributed many test cases to the ecosystem tests repository. More directly, I put together [structured scripts](https://github.com/paritytech/ahm-dryrun) to allow repeatably forking the network, running the migration and running end to end tests on the post-migration state. These tests will be expanded over the coming weeks to allow dry running and verifying each network's migration end to end with the real state before actually going on chain.

I prepared the Westend Asset Hub runtime [for Westend](https://github.com/paritytech/polkadot-sdk/pull/7997), which serves as a development branch for the full migration until the staking work is finalised and merged.
Although I did not write the main state migration code, integrating these pallets to the SDK involved some small changes to make it work on Westend and with the `stable2503` release, including [rewriting the `BoundedBTreeMap` decoding logic](https://github.com/paritytech/parity-common/pull/906) to allow deriving `DecodeWithMemTracking` since some calls introduced in the migrator pallets include types based on this.

In the reporting period I have begun onboarding another new developer to the ecosystem via my team in Parity, where I continue in my capacity as System Parachains team lead and mentor.
As usual, issues, code and review contributions across multiple repos since my last report can be found on my GitHub profile [`seadanda`](https://github.com/seadanda).

With respect to governance, I have been involved in various stages of the fellowship release cycle, defining the scope of upgrades, testing and proposing them on chain.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0% voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e 0 % voting agreement). |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):