# Argument-0003: Promotion to Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission 2025/04/24                                                               |
| **Submitted by**| George Pisaltu                                                                              |


## Member details

- Matrix username: `@george.pisaltu:parity.io`
- Polkadot address: `128pmEUBSGjGeXZXNaAmomAJgVn77L74YT7Zdjd3fP63HWNP`
- Current rank: `1`
- Date of initial induction: `2024/08/16`
- Date of last report: `2025/02/03`
- Area(s) of Expertise/Interest: `System Parachains, FRAME`


## Reporting period

- Start date: 2024/08/16
- End date: 2025/04/24


## Argument

I have been part of the fellowship since August 2024 and I have been working on Polkadot technology
since July 2023. During this time, I have continuously expanded my knowledge on everything substrate
and FRAME and contributed to multiple layers of the stack. I have also designed and implemented new
functionality to existing pallets, creating the Polkadot experience of tomorrow for our users. While
I have been contributing to Polkadot core protocols or components since almost two years now, I was
late to officially join the Fellowship, therefore showing a shorter tenure on-chain. I am applying
here for a fast promote to rank 2 and hope existing Fellows agree with me that my existing
contributions are sufficient in breadth, depth and complexity to justify rank 2 in the Fellowship.

### Extrinsic Horizon

I played an active role in developing, designing and improving core features of the
`TransactionExtension` interface to `polkadot-sdk`, phase 1 of [Extrinsic
Horizon](https://github.com/paritytech/polkadot-sdk/issues/2415). The main purpose of the new
interface is to allow for custom origin authentication and mutation before dispatching a call in a
transaction. This, in turn, provides the machinery in substrate to enable free transactions, i.e.
valid transactions run by users without funding an account with the existential deposit or any funds
to pay for transaction fees. This is a huge development in substrate-based chains, which previously
could only function on signed or unsigned transactions, heavily relying on the account model.

I oversaw the [delivery of
`TransactionExtension`](https://github.com/paritytech/polkadot-sdk/pull/3685) with all that it
entailed. While I discussed the `TransactionExtension` effort before in greater detail, I will
summarize the technical contribution as:
- wrote the [RFC introducing General transactions](https://github.com/polkadot-fellows/RFCs/pull/84)
- wrote the [RFC defining v5 extrinsics](https://github.com/polkadot-fellows/RFCs/pull/124)
- designed weights to `TransactionExtension` operations and introduced benchmarks and weights for
  existing extensions
- integrated the extension weights in existing FRAME weight accounting
- migrated existing extensions to the new interface

The implementation in phase 1 of Extrinsic Horizon paved the way for a [clean implementation of
phase 2](https://github.com/paritytech/polkadot-sdk/pull/6324), which was designed to use the custom
origin authentication in `TransactionExtension` to replace unsigned transactions and
`ValidateUnsigned` with a custom origin specific to each pallet which would bypass the fee and nonce
transaction extension checks. I contributed the design of this feature and I was involved in the
discussions behind its implementation as well as the reviews.

For more information about the `TransactionExtension` contribution and its impact, please refer to
[this long-form semi-technical forum
post](https://forum.polkadot.network/t/introducing-transactionextension/10827) where I explain the
feature to the community.

### People registry in Proof of Personhood

I have been working on Proof of Personhood for over a year now and recently we have made public the
first piece of the puzzle: [the people
registry](https://github.com/paritytech/polkadot-sdk/pull/8164), as defined in `pallet-people`, and
its adjacent structures.

The People registry is kept in pallet-people, which stores and manages identifiers of individuals
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

### Other contributions

While Proof of Personhood has been and remains my main focus, I have contributed in other ways to
substrate and FRAME and I wish to continue to do so. Aside from reviews, my other notable
contributions are in the identity pallet, where I pushed a refactor to decouple usernames from
identities, along with a migration for existing instances of the pallet, and support for personal
usernames, which are system allocated usernames for recognized people.

### Publications

- [Introducing
  `TransactionExtension`](https://forum.polkadot.network/t/introducing-transactionextension/10827)
- [General transactions in extrinsic format](https://github.com/polkadot-fellows/RFCs/pull/84)
- [Extrinsic v5 definition and specification](https://github.com/polkadot-fellows/RFCs/pull/124)
- [Election mechanism for invulnerable collators on system
  chains](https://github.com/polkadot-fellows/RFCs/pull/138)

## Voting record

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

