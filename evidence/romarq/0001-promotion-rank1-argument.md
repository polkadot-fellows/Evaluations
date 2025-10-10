# Evidence-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/10/10)                                                             |
| **Submitted by**| Rodrigo Quelhas                                                                             |


## Member details

- Matrix username: @romarq:matrix.org
- Polkadot address: 12fiMKJP9t3gTFpHEXGYtdbZzwQciCpUcVFRnVXU4JYQLWvA
- Current rank: 0
- Date of initial induction: 2025/10/06
- Date of last report: N/A
- Area(s) of Expertise/Interest: FRAME, Parachain Consensus

## Reporting period

- Start date: 2024/03/05  
- End date: 2025/10/10

## Argument

My experience spans over seven years in blockchain engineering, with the past few years dedicated to Polkadot, currently as a core developer at Moonbeam.

Over the past few months, I have made various contributions to the Polkadot ecosystem, including bug fixes, refactors, and small feature implementations. These contributions have focused on improving developer experience and maintainability, aligning with the Fellowship's goals of supporting robust and sustainable development of the protocol.

Joining the Fellowship allows me to more actively engaged with the Polkadot ecosystem and help shape technical directions collaboratively. I believe my contributions reflect the expectations outlined for Rank 1 in the [Manifesto](https://github.com/polkadot-fellows/manifesto/blob/main/manifesto.pdf).

### Key Contribution Links

#### [polkadot-sdk#8108](https://github.com/paritytech/polkadot-sdk/pull/9451)
Fixed a bug in `pallet-balances` where the `reserve` and `can_reserve` methods from Currency trait were incorrectly preventing new reserves when an account's free balance was lower than its frozen balance, even if the usable balance was sufficient after accounting for the reserved balance.

#### [polkadot-sdk#9638](https://github.com/paritytech/polkadot-sdk/pull/9638) and [polkadot-sdk#9451](https://github.com/paritytech/polkadot-sdk/pull/9451) and [polkadot-fellows#844](https://github.com/polkadot-fellows/runtimes/pull/844)

Officially deprecated `OnRuntimeUpgrade` parameter in `frame_executive::Executive` and updated all runtimes to use `SingleBlockMigrations` from `frame_system::Config`.

#### [polkadot-sdk#9869](https://github.com/paritytech/polkadot-sdk/pull/9869) and [polkadot-sdk#9662](https://github.com/paritytech/polkadot-sdk/pull/9662)

These pull requests removed deprecated and unused consensus-related code from the codebase, which reduced technical debt and simplifed the codebase for future maintenance.

[**Other merged PRs to polkadot-sdk**](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3ARomarQ+is%3Aclosed)  

These pull requests include bug fixes, code refactoring, and minor feature enhancements, all of which have helped improve code quality and maintainability for other developers in the ecosystem.

## Voting record

New member — no voting history yet