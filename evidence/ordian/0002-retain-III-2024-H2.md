# Evidence-0002: Retention at Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/12/02                                                            |
| **Submitted by**| ordian                                                                       |


## Member details

- Polkadot address: `13aYUFHB3umoPoxBEAHSv451iR3RpsNi3t5yBZjX2trCtTp6`
- Current rank: III
- Date of initial induction: Seeding
- Date of last report: 2024/06/21
- Area(s) of Expertise/Interest: `Parachains Consensus`

## Reporting period

- Start date: 2024/06/22
- End date: 2024/12/02

## Salaryless

As you can see [here](https://collectives.subsquare.io/user/13aYUFHB3umoPoxBEAHSv451iR3RpsNi3t5yBZjX2trCtTp6/fellowship), I haven't claimed any fellowship salary and not goint to in the next salary period as well.

## Evidence

### `ParaInherent.enter` weights

I've [investigated](https://github.com/paritytech/polkadot-sdk/issues/849#issuecomment-2247895862) a long-time issue about `ParaInherent.enter` weight being overestimated.
It was one of the remaining blockers allowing Polkadot to scale to 1k validators and 200 cores.

Along with resolving the issue in the following PRs: [1](https://github.com/paritytech/polkadot-sdk/pull/5082), [2](https://github.com/paritytech/polkadot-sdk/pull/5270), a long-standing low-impact security issue have been addressed as well.

While digging into the `ParaInherent.enter` code, which serves as a critical on-chain part of shared security aspect of Polkadot (`Parachains Consensus`), a few refactoring ideas have been [suggested](https://github.com/paritytech/polkadot-sdk/issues/5520) to make the code more resilient and future-proof.

### Runtime API calling unmigrated storage

After our team have investigated a finality [issue](https://forum.polkadot.network/t/2024-09-17-polkadot-finality-lag-slow-parachain-production-immediately-after-runtime-upgrade-post-mortem/10057) that happened on Polkadot after a runtime upgrade, we have decided to prioritize fixing another long-standing [issue](https://github.com/paritytech/polkadot-sdk/issues/64).

Looking into the code that is outside of my expertise (substrate executor logic), I've created a [fix](https://github.com/paritytech/polkadot-sdk/pull/6029).
The PR has been later adjusted to the newly opened [RFC 123](https://github.com/polkadot-fellows/RFCs/pull/123) and is looking for feedback and reviews.

### Spammening

I have provided help with the (parachains) spammening project spanning across multiple areas
* Getting funds to register 30 parachains. This has proven to be a challenging task involving multiple teams at Parity, such as Finance and Security.
But as a result, our team got some experience working with multisigs, pure accounts and proxies.
Multix added support for coretime chains thanks to another fellowship member.
Hopefully, our setup will serve as a reference for similar future endeavors.
* Working on a browser script, an [issue](https://github.com/paritytech/subxt/pull/1871) with subxt_signer on `no_std` platform has been discovered and later fixed.
* Working on a feeless extrinsic, some [limitations](https://github.com/paritytech/polkadot-sdk/issues/6489) have been discovered.
* I've worked on several subxt scripts (e.g. coretime orchestration) and gained insights into constructing nested subxt calls dynamically, coretime inner workings and API among other things.

After the relay chain spammening, I've also started an investigation into potential overweight issue:
* https://github.com/ordian/replay-kusama-25876038

### Misc

As usual, I'm providing [PR reviews](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aordian) and direction around my area of expertise.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|III|70%   |100%  | During this period, I have voted on 75 out of 81 referenda in which I was eligible to vote (i.e 92.5% voting activity) with 100% agreement with higher ranks. | My overall voting activity is at 75.5% according to [this](https://github.com/ggwpez/substrate-scripts/blob/master/fellowship-voting-evidence.py) script. |
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
