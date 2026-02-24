# Argument-0003: Retention at Rank I

|                 |                      |
| --------------- | ---------------------|
| **Report Date** | 2026-02-17           |
| **Submitted by**| Ludovic Domingues    |

## Member details

- Matrix username: @krayt78:matrix.org
- Polkadot address: 14AgwoPjcRiEEJgjfHmvAqkjdERCG26WEvQUoGLuBzcXKMS2
- Current rank: Rank I
- Date of initial induction: 2024-06-18
- Date of last report: 2025/11/17
- Area(s) of Expertise/Interest: 
    - FRAME
    - Runtime

## Reporting period

- Start date: 2025/12/01
- End date: 2026/03/01

## Argument

My main focus this period has been chipping away at the `Currency` → `fungible` migration tracked in [polkadot-sdk#226](https://github.com/paritytech/polkadot-sdk/issues/226). This is one of those long-running cleanup efforts that touches a lot of pallets - replacing the old `ReservableCurrency` / `LockableCurrency` patterns with the newer `fungible` hold/freeze model.

It's unglamorous work, but each pallet migration involves more than a find-and-replace. You need to introduce proper `HoldReason` variants, rewrite deposit logic, write storage migrations to move existing reserves over to holds, update benchmarks, and make sure it all plays nicely with the runtime configs.

Here are the PRs I've put up as part of this effort:

- **pallet-referenda** - [#10701](https://github.com/paritytech/polkadot-sdk/pull/10701)
- **pallet-lottery** - [#10045](https://github.com/paritytech/polkadot-sdk/pull/10045)
- **pallet-indices** - [#9610](https://github.com/paritytech/polkadot-sdk/pull/9610)
- **pallet-preimage** - [#11066](https://github.com/paritytech/polkadot-sdk/pull/11066)
- **pallet-multisig** - [#11064](https://github.com/paritytech/polkadot-sdk/pull/11064)

Some of these have been through multiple rounds of review already. I've been iterating on feedback from maintainers and other fellows throughout.

Alongside direct SDK contributions, I have also been helping educate new developers through PBA-X and the upcoming campus in Lisbon. While this does not count toward Fellowship contributions, it supports the broader ecosystem by onboarding new engineers and strengthening the developer pipeline for Substrate and Polkadot.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referendum in which I was eligible to vote (i.e NaN% voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e NaN% voting agreement).  |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

## Previous retention

My last retention evidence: [0002-2025-11-retention-rank-1.md](https://github.com/polkadot-fellows/Evaluations/blob/main/evidence/krayt78/0002-2025-11-retention-rank-1.md)
