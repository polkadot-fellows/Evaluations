# Argument-0002: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/09/21                                                                                  |
| **Submitted by**| Karol Kokoszka                                                                              |

## Member details

- Matrix username: @karol:parity.io
- Polkadot address: 1556APd4jcMDRod9SUxfTwGLasqFy3y3QFMGokkBwTdk2tev
- Current rank: II
- Date of initial induction: 2025/05/21
- Date of last report: 2026/06/03
- Link to last report: https://github.com/polkadot-fellows/Evaluations/blob/main/argument/karolk91/0001-rank-2-promotion.md
- Area(s) of Expertise/Interest: XCM, Bulletin Chain, Governance, Runtime, Node, end-to-end & integration testing

## Reporting period

- Start date: 2026/06/03
- End date: 2026/09/21

## Argument

During this reporting period I focused on Levity. I took ownership of releasing and deploying its next phase to Polkadot. This included reviews, pallet releases, testnet verification, support for other teams, stress testing, and coordination with node operators. I also continued contributing to ecosystem projects: I completed Polkadot-Kusama bridge support in Chopsticks, added features to the [referendum testing tool](https://github.com/karolk91/polkadot-referenda-tester/) and maintained it, and added Bulletin Chain scenarios to the Polkadot Ecosystem Tests.


### Levity (Bulletin Chain + HOP)

Preparing the Polkadot launch required onboarding more collators. I took technical ownership of preparing and testing referendum [#1918](https://polkadot.subsquare.io/referenda/1918), which added invulnerables to the Bulletin Chain collator set, and I submitted it on-chain. The referendum has been executed.

My most important work was taking over the integration of the Bulletin Chain into the Fellowship runtimes and completing it in [#1170](https://github.com/polkadot-fellows/runtimes/pull/1170). This deployed the Bulletin Chain's main business logic on Polkadot in the [2.4.0 runtime release](https://github.com/polkadot-fellows/runtimes/releases/tag/v2.4.0).

I worked on HOP testing and integration. I added HOP scenarios to the stress-testing tooling ([#797](https://github.com/paritytech/polkadot-bulletin-chain/pull/797)), and gated HOP uploads on the `HopRuntimeApi` authorization check in the community [iOS](https://github.com/paritytech/polkadot-ios-community/pull/47) and [Android](https://github.com/paritytech/polkadot-android-community/pull/28) apps.

I am one of the leading engineers on Levity. My work includes new features, improvements to the testing tools, and reviews of other people's changes. A full list exists in the [polkadot-bulletin-chain](https://github.com/paritytech/polkadot-bulletin-chain) repository, in [the pull requests I am involved in](https://github.com/paritytech/polkadot-bulletin-chain/pulls?q=is%3Apr+involves%3Akarolk91+sort%3Aupdated-desc).

### Chopsticks

I completed the Polkadot-Kusama bridge support for Chopsticks, which allows testing of bridged scenarios. I merged it in [#1029](https://github.com/AcalaNetwork/chopsticks/pull/1029), and Chopsticks 1.5.0 contains it.

### Governance: Polkadot Referenda Tester

I added support for the bridged scenario where the Polkadot Fellowship whitelists a call on the Kusama Asset Hub ([#45](https://github.com/karolk91/polkadot-referenda-tester/pull/45)). Other additions include chaining several referenda into a single dry run and running post-referendum test scripts ([#54](https://github.com/karolk91/polkadot-referenda-tester/pull/54)). I continue to maintain the project so that it works with the latest runtimes.

### Polkadot Ecosystem Tests

I added the scenario where the Polkadot Fellowship whitelists a call on the Kusama Asset Hub ([#643](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/643)), and extended the existing system, upgrade and XCM suites to cover Bulletin Polkadot ([#682](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/682)).


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote. | There were no valid referenda I was eligible to vote on |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
