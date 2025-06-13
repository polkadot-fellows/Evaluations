# Evidence-0003: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/06/13
| **Submitted by**| Michał Kucharczyk                                                                           |


## Member details

- Matrix username: `@michal:parity.io`
- Polkadot address: [14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo](https://collectives.statescan.io/#/accounts/14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo)
- Current rank: 1
- Date of initial induction: `2024/06/02`
- Date of last report: `2025/03/05`
- Area(s) of Expertise/Interest: `Substrate node` ,`Transaction Pool`, `ChainSpec/GenesisConfig`


## Reporting period

- Start date: 2025/03/05
- End date: 2025/06/13

## Evidence

The fork-aware transaction pool was rolled out to the parity nodes on Westend, Kusama relaychain and system parachains, and Polkadot system parachains. I supported deployment, debugging, and verification.

During the report period, I focused on performance bottlenecks and reliability issues in the new pool, especially when it comes to propertly handling transaction pool limits in the conditions of heavy load. I also improved performance and realiability for handling elastic scaling (7k txs per 2s block).

During the heavy load testing of txpool I also identified some performance problems with current transaction protocol definition and implementation ([internal parity report](https://github.com/paritytech-secops/eng_findings/issues/12)). I wrote the [draft proposal for transactions/v2](https://github.com/paritytech/polkadot-sdk/pull/8128/), a new protocol to reduce bandwidth usage by separating transaction advertisement and full data transmission. I addressed and discussed feedback from the community. The draft forms a ground work for implementation and RFC. The proposed protocol is open for future extensions with some interesting features like set-reconciliation.

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

