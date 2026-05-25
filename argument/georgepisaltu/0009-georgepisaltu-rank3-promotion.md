# Argument-0009: Promotion to Rank 3

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission 2026/02/24                                                               |
| **Submitted by**| George Pisaltu                                                                              |


## Member details

- Matrix username: `@george.pisaltu:parity.io`
- Polkadot address: `128pmEUBSGjGeXZXNaAmomAJgVn77L74YT7Zdjd3fP63HWNP`
- Current rank: `2`
- Date of initial induction: `2024/08/16`
- Date of last report: `2026/01/23`
- Area(s) of Expertise/Interest: `Proof of Personhood, System Parachains, FRAME`


## Reporting period

- Start date: 2024/08/16
- End date: 2026/02/24


## Argument

I have been part of the fellowship since August 2024 and I have been working on Polkadot technology
since July 2023. During this time, I have continuously expanded my knowledge on everything substrate
and FRAME and contributed to multiple layers of the stack. I have also designed and implemented new
functionality to existing pallets, creating the Polkadot experience of tomorrow for our users
through my contribution in leading the Proof of Personhood development. I am applying here for a
fast promote to rank 3 and hope existing Fellows agree with me that my existing contributions are
sufficient in breadth, depth and complexity to justify rank 3 in the Fellowship.

### Proof of Personhood

The rank 3 requirements in the manifesto state:

> Either played a supporting role in the ideation and a primary role in the formalisation of a major
protocol component; or played a supporting role in the code-design and a primary role in the
implementation of a major protocol component.

I have been working on Proof of Personhood for 2 years now and we have already made public the first
piece of the puzzle: [The People
Registry](https://forum.polkadot.network/t/the-people-registry/12749), as defined in
`pallet-people`, and its adjacent structures. Since then, the ring management logic in
`pallet-people` has been abstracted away into a members pallet, which is currently live on a Paseo
parachain for users to interact with, soon to be open-sourced. I am the technical owner of the
project and I am responsible for the technical design and implementation of all of its elements: the
people registry, DIM1, DIM2, people incentive schemes, free transactions and the delivery of all of
this to the Polkadot People chain, with more components planned and in the specification drafting
phase to be delivered in the future.

From the rank 3 expectations in the manifesto:

> becoming a Fellow indicates the individual has enough knowledge and skill to build substantial
protocol components (i.e. all but the major protocol components, e.g. a pallet or 2-10,000 line
crate) alone and with high expectations that they will be completed correctly and to a high standard

I am the core contributor of the people registry, member set, DIM1, people incentive scheme. I am
also the main contributor and advocate for the free transaction model through my work in Extrinsic
Horizon. I led the effort to develop both DIM1 and was heavily involved in the design of DIM2,
imminently available for general use with the launch of the Polkadot app. The DIMs' specifications
will be made public with their introduction in a People chain runtime upgrade and, as such, I cannot
go into the technical implementation and details in this letter. The DIMs have been released on a
Paseo parachain for users to interact with before the source code was made open-source.

A rank 3 member is expected to show:

> Demonstrable presence of knowledge sharing within the ecosystem.

I have been holding internal knowledge sharing sessions with people working on current and future
Polkadot core protocol elements as well as people building future applications on the core PoP
technology. These discussions have not been public due to the reason mentioned above, but I have had
multiple talks on:
- the People registry and how it leverages ring VRF;
- People authentication and the free transaction model it enables;
- DIM1 and DIM2, from specification to implementation both on-chain and in integrating clients;
- privacy-first reward schemes for people.

#### The People Registry

The People registry is kept in pallet-people, which stores and manages identifiers of individuals
who have proven their personhood. It tracks their personal IDs and their associated cryptographic
keys, and allows them to use contextual aliases through authentication in extensions. The People
registry uses the new `pallet-members` as a service for the management of the rings in which
people's keys are included. The system also grooms the rings through defragmenting and ensures
members are onboarded in batches to preserve privacy.

The People pallet implements an interface allowing any DIMs to recognize and suspend personhood. I
created a dummy DIM to act as a control panel wherever the People registry is deployed in test
environments, and will be extended to become a production ready tool for governance to easily
interact with the people set.

The expectations of a rank 3 member are:

> Occasionally innovative in API & code design, adapting/importing/inventing ideas that lead to effective
solutions

People are identified through a new cryptographic primitive, as defined in the
[`verifiable`](https://github.com/paritytech/verifiable) crate. People get the privilege of running
free transactions for supported calls through new `TransactionExtension` implementations and custom
origin types. I was a crucial contributor to the design and implementation of the member ring
solution using ring VRF cryptography, mitigating member privacy risks when onboarding a ring while
avoiding stalls in the onboarding queue.

When transactions include cryptographic proofs of belonging to the people set, the pallet's
transaction extension verifies these proofs before allowing the transaction to proceed. This enables
other pallets to check if actions come from unique persons while preserving privacy through the
ring-based structure. I played a critical role in the design and reference implementations of the
extension model we use to provide free transactions for recognized people.

#### Incentives for bootstrapping the initial people set

I designed and implemented an incentive mechanism for people who participate honestly and
consistently in the activities available in the first Proof of Personhood release, from taking part
in the recognition process themselves (going though the DIMs) to facilitating other people's
application process (i.e. people fulfilling the role of oracle for candidates' evidence in DIM1).
All of the rewards will be handed out periodically on-chain through payment rounds and distributed
to participants proportional to their contribution to the system.

As the rank 3 expectations in the manifesto state:

> The individual should by now be thinking in a very much in a security-conscious, game-theoretic
way, understanding that the systems whose design they are increasingly a part of must function
adequately even with a modest minority of malicious users.

The incentive provided to people is to always contribute, but especially so when there is low
activity, since the reward share of a single participant will be greater. The pallet allows a
privileged origin to set a certain amount as a reward for the ongoing payout round, so participants
do not know ahead of time how much one vote is worth. This system avoids two distinct scenarios
which lead to fewer votes (and less confidence in the outcome):

- when the reward is fixed per vote, it can be exhausted early;
- when the reward is known ahead of time and shared among all participants, after a certain number
  of people vote, the reward may be too small for a participant to bother voting in that round,
  making cases closer to the end of the payout round have a small turnout.

Initially, the rewards were available to participants only through a privacy voucher mechanism
leveraging the existing ring architecture to ensure that whoever is withdrawing a reward preserves
their privacy. This has been superseded by coinage, a UTXO-like private payment mechanism to which I
contributed in the design phase. Unlike the privacy voucher mechanism, coinage is open to
permissionless use.

#### Free transactions with spam protection

The origin system was designed to allow authorized entities to run free transactions in certain
contexts. In addition to allowing all on-chain activities to be performed for free by proven people
and candidates for DIMs, entities which have an authority's backing as being reasonably unique
(through a less strict mechanism than the DIMs) will also get a lesser amount of weight allocation
to submit their transactions for free (i.e. send funds to another account, for free). This will
enable the Polkadot app to provide UX which is at least as good as traditional services, which allow
people to send money to each other within the app for free.

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

### Other contributions

While Proof of Personhood has been and remains my main focus, I have contributed in other ways to
substrate and FRAME and I wish to continue to do so. Aside from reviews, my other notable
contributions are in the identity pallet, where I pushed a refactor to decouple usernames from
identities, along with a migration for existing instances of the pallet, and support for personal
usernames, which are system allocated usernames for recognized people.

### Considerations regarding my argument

While I have been contributing to Polkadot core protocols or components for more than two years now,
I was late to officially join the Fellowship, therefore showing a shorter tenure on-chain and
applying for the fast promotion.

Most of the components of Proof of Personhood are now publicly available on testnets such as Paseo,
but the source code will be open-sourced at a later date. I accept that the arguments which could be
made in this letter may be incomplete, but I will support my case to fellows before this argument is
put to a vote and answer any and all questions regarding my contributions.

The launch of the project live on the Polkadot people chain is imminent. When that happens, I
believe that the Fellowship will need a member of rank3+ as an owner and main contributor of these
features, as I believe is the case concerning all other core protocol features. I have been in the
position to lead the development of this project and wish to continue to do so and extend my role
and my responsibilities in the Fellowship as a rank 3 member. This can only happen on the fast
promotion path and I hope that the evidence I present in this letter justifies this.

### Publications

- [Introducing
  `TransactionExtension`](https://forum.polkadot.network/t/introducing-transactionextension/10827)
- [General transactions in extrinsic format](https://github.com/polkadot-fellows/RFCs/pull/84)
- [Extrinsic v5 definition and specification](https://github.com/polkadot-fellows/RFCs/pull/124)
- [Election mechanism for invulnerable collators on system
  chains](https://github.com/polkadot-fellows/RFCs/pull/138)
- [The People Registry](https://forum.polkadot.network/t/the-people-registry/12749)

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity).  |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

