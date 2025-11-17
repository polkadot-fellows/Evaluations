# Argument-0002: Retention at Rank I

|                 |                      |
| --------------- | ---------------------|
| **Report Date** | 2025/11/17           |
| **Submitted by**| Ludovic Domingues    |


## Member details

- Matrix username: @krayt78:matrix.org
- Polkadot address: 14AgwoPjcRiEEJgjfHmvAqkjdERCG26WEvQUoGLuBzcXKMS2
- Current rank: Rank I
- Date of initial induction: 2024-06-18
- Date of last report: N/A
- Area(s) of Expertise/Interest: 
    - FRAME
    - Runtime

## Reporting period

- Start date: 2025/09/01
- End date: 2025/12/01

## Argument

During this reporting period, my work focused primarily on the ecosystem-wide migration from the legacy currency traits (Currency, ReservableCurrency, etc ...) to the new fungible traits. This initiative is a major modernization effort across FRAME, improving consistency, reducing API complexity, and laying the foundations for more flexible and robust asset handling in runtimes.

This migration affects multiple pallets, many of which require careful attention to storage transitions and semantic correctness. My work contributes directly to this wider Fellowship-driven effort.

I was busy working on [PR 9610](https://github.com/paritytech/polkadot-sdk/pull/9610), migrating pallet-indices from currency traits to fungible ones and therefore from reserve-based operations to the new hold/freeze-based mechanisms. This change is non trivial as it requires a migration file and testing to make sure that there are no issues post migration.

I also worked on [PR 10045](https://github.com/paritytech/polkadot-sdk/pull/10045), migrating pallet-lottery to the same new traits. This pallet does not require the transition to hold/freeze logic as it didnt use reserves before, but it might still need a migration file to make sure the storage is correct.

Due to major ecosystem events (sub0, AHM, and ongoing Fellowship activities), reviewer availability has been limited during this period. I have been actively seeking guidance from several maintainers to ensure my migrations follow the correct patterns and meet runtime safety expectations. But atm i have had no reviews yet which kind of limit my ability to work on multiple pallets at once while making sure that my reasoning is correct.

Alongside direct SDK contributions, I have also been helping educate new developers through PBA-X. While this does not count toward Fellowship contributions, it supports the broader ecosystem by onboarding new engineers and strengthening the developer pipeline for Substrate and Polkadot.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referendum in which I was eligible to vote (i.e NaN% voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e NaN% voting agreement).  |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 