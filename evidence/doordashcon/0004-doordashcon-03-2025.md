# Argument-0004: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/03/25                                                             |
| **Submitted by**| Jesse Chejieh                                                                      |


## Member details

- Matrix username: @doordashcon/:matrix.org
- Polkadot address: 12zsKEDVcHpKEWb99iFt3xrTCQQXZMu477nJQsTBBrof5k2h
- Current rank: I
- Date of initial induction: 2022/09/29
- Date of last report: 2024/12/22
- Area(s) of Expertise/Interest: FRAME


## Reporting period

- Start date: 2024/12/22
- End date: 2025/03/25


## Argument
### 1. Contributions to the Tooling Collective and Member Management
During this reporting period, I worked on configurations for the tooling collective which led me to identify and resolved a critical benchmarking mismatch in `pallet_core_fellowship` generating invalid ranks exceeding runtime-configured `MaxRank` values ([#7720](https://github.com/paritytech/polkadot-sdk/pull/7720)). This manifested specifically in edge cases like `MaxRank=1`.

The solution implements dynamic rank clamping via `r.min(T::MaxRank::get())`, enforcing runtime constraints while preserving backward compatibility with type-safe conversions via `ConvertU16ToU32`.

I am currently investigating same benchmarking patterns in `pallet_treasury` to ensure consistent rank handling across collectives.

### 2. Developer Relations
Continue to proactively strengthened developer engagement through hands-on mentorship with the study group.

Some contributor highlights this period include [Nathy-bajo](https://github.com/Nathy-bajo) and his contribution adding view functions to the Proxy pallet for runtime-specific type configuration([#7320](https://github.com/paritytech/polkadot-sdk/pull/7320)) along side other maintenance contributions.

[Runcomet's](https://github.com/runcomet) creation of [genesis dev accounts](https://github.com/paritytech/polkadot-sdk/pull/7320) and ongoing implementation of [RFC 0097](https://github.com/paritytech/polkadot-sdk/pull/7398).

#### Next Phase
Moving forward I will be taking the study group public through the Polkadot Africa initiative and look forward to fostering developers in the ecosystem, combining online sessions and in-person workshops to scale developer onboarding across traditional tech communities and undergraduate programs.

### 3. Contributions on the Accounting System(`pallet-balances`)

Improved the accounting system of the balances pallet, modifying [event emision](https://github.com/paritytech/polkadot-sdk/pull/7250) to enable reliable balances reconciliation of the Burn/Mint operations and Hold/release Operations.


I humbly request for retention at Rank I.



## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e undefined% voting activity). Out of xx referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus x times (i.e undefined% voting agreement).  |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

