# Evidence-0002: Promotion to Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/03/05
| **Submitted by**| Michał Kucharczyk                                                                           |


## Member details

- Matrix username: `@michal:parity.io`
- Polkadot address: [14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo](https://collectives.statescan.io/#/accounts/14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo)
- Current rank: 0
- Date of initial induction: `2024/06/02`
- Date of last report: `2024/10/02`
- Area(s) of Expertise/Interest: `Substrate node` ,`Transaction Pool`, `ChainSpec/GenesisConfig`


## Reporting period

- Start date: 2024/10/02
- End date: 2024/03/05

## Evidence

The fork-aware transaction pool implementation, introduced in [pull request #4639](https://github.com/paritytech/polkadot-sdk/pull/4639), has been successfully merged. I have published a [post](https://forum.polkadot.network/t/the-fork-aware-transaction-pool/10468) that provides a concise summary of this new transaction pool, explaining the necessity behind its development, the issues encountered with the previous implementation, and guidance on how to operate it. Additionally, the post includes links to the existing documentation for further reference.

The next milestone is achieving (feature completeness)[https://github.com/orgs/paritytech/projects/156/views/6], ensuring that transaction pool handles most edge cases correctly. Throughout the reporting period, I have focused on enhancing a fork-aware transaction pool to tackle the objectives detailed in the follow-up [ticket](https://github.com/paritytech/polkadot-sdk/issues/5472). My primary goal was to tackle the challenge of properly handling the limits of the transaction pool and transactions' priorities. During high-pressure situations, the transaction pool should accept higher-priority transactions and remove those with lower priority, preventing it from getting clogged with stalled transactions. In addition I've implemented proper handling of invalid transactions reported by block builder, and also a reasonable [behaviour](https://github.com/paritytech/polkadot-sdk/pull/6661) of transaction pool in situtation where finality is stalled.

I conducted initial performance evaluations for 2-second blocks, leading to some easy improvements in the initial implementation, and identified ([details](https://github.com/paritytech/polkadot-sdk/issues/7399)) one more optimization which will be implemented soon. I also added some [metrics](https://github.com/paritytech/polkadot-sdk/pull/7505) which allow to track the transcation events timings.

I mentored and co-authored the [implementation](https://github.com/paritytech/polkadot-sdk/pull/7257) of framework for repeatable end-to-end zombie-net based tests which is aimed to track performance regressions, and catch some rare bugs.

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

