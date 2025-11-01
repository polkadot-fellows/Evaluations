# Argument-0004: Retention at Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission 2025/04/25                                                               |
| **Submitted by**| George Pisaltu                                                                              |


## Member details

- Matrix username: `@george.pisaltu:parity.io`
- Polkadot address: `128pmEUBSGjGeXZXNaAmomAJgVn77L74YT7Zdjd3fP63HWNP`
- Current rank: `1`
- Date of initial induction: `2024/08/16`
- Date of last report: `2025/02/03`
- Area(s) of Expertise/Interest: `System Parachains, FRAME`


## Reporting period

- Start date: 2025/02/03
- End date: 2025/04/25


## Argument

This reporting period I have been fully focused on advancing the Proof of Personhood effort. While
the project in its entirety is not available to the public yet, we have recently released the first
part of Proof of Personhood, which is [the people
registry](https://github.com/paritytech/polkadot-sdk/pull/8164) along with some adjacent structures.
In this argument I will focus on this part of the project, although we are continually making
progress in other areas as well.

The People registry is kept in `pallet-people`, which stores and manages identifiers of individuals
who have proven their personhood. It tracks their personal IDs, organizes their cryptographic keys
into rings, and allows them to use contextual aliases through authentication in extensions.

While no DIMs have been made public yet, the People pallet already implements an interface allowing
any DIMs to recognize and suspend personhood. I created a dummy DIM to act as a control panel
wherever the People registry is deployed in test environments, and will be extended to become a
production ready tool for governance to easily interact with the people set.

People are identified through a new cryptographic primitive, as defined in the
[`verifiable`](https://github.com/paritytech/verifiable) crate. People get the privilege of running
free transactions for supported calls through new `TransactionExtension` implementations and custom
origin types. I was heavily involved in the design and implementation of the member ring solution
using ring VRF cryptography, mitigating member privacy risks when onboarding a ring while avoiding
stalls in the onboarding queue.

When transactions include cryptographic proofs of belonging to the people set, the pallet's
transaction extension verifies these proofs before allowing the transaction to proceed. This enables
other pallets to check if actions come from unique persons while preserving privacy through the
ring-based structure. I played a critical role in the design and reference implementations of the
extension model we use to provide free transactions for recognized people.


## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referendums available for my rank to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

