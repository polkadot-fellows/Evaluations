# Evidence-0001: Retention at Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission 2024/11/14                                                               |
| **Submitted by**| George Pisaltu                                                                              |


## Member details

- Matrix username: `@george.pisaltu:parity.io`
- Polkadot address: `128pmEUBSGjGeXZXNaAmomAJgVn77L74YT7Zdjd3fP63HWNP`
- Current rank: `1`
- Date of initial induction: `2024/08/16`
- Date of last report: `-`
- Area(s) of Expertise/Interest: `System Parachains, FRAME`


## Reporting period

- Start date: 2024/08/16
- End date: 2024/11/14


## Evidence

During my first three months as a member, I have mainly been focused on delivering the new
[`TransactionExtension`](https://github.com/paritytech/polkadot-sdk/blob/1b0cbe99ab8537fa188952a203bdb73b0e5fdd3f/substrate/primitives/runtime/src/traits/transaction_extension/mod.rs#L161) interface to `polkadot-sdk`, which has now safely landed on `master`.

The introduction of `TransactionExtension` to replace `SignedExtension` was a huge effort and the
first step of [`Extrinsic Horizon`](https://github.com/paritytech/polkadot-sdk/issues/2415). The new
interface addresses many shortcomings of the previous one (e.g. proper weight accounting), but the
most important feature is configurable origin authorization. This will allow any substrate chain to
create extensions which authorize an origin through custom signature schemes, using different
signing algorithms than the ones defined by the runtime, over any on-chain state. This origin
authorization, used in tandem with the new `General` transactions introduced in
[RFC84](https://github.com/polkadot-fellows/RFCs/pull/84), will allow for truly free transactions in
the context defined and authorized by the runtime, where no pre-existing or funded account would
need to exist in order to run some logic on chain, provided some extension authorizes it. The
introduction of weights to the extensions now allows even authorization mechanisms which are compute
heavy, like ZK proofs, to run in the extension context. Previously, extensions were weightless and,
by convention, they had to perform minimal compute in order to limit this attack vector.

The previous extensions have been migrated to the new interface and now have accompanying
benchmarking code. The very base layer of substrate responsible for dispatching transactions has
been refactored to account for the worst case weight of an extension before the actual dispatch of
the call and also allow for weight refunds after the call was dispatched, similar to how the weight
system works for calls. Going forward, all extensions must take into account supporting transactions
which have an origin different than the traditionally signed origin in order to natively support the
free transaction use case.

I'm also very active in the design of phase 2 of Extrinsic Horizon and I'm actively supporting it in
its currently ongoing efforts, with the hope that it will simplify the current extension
infrastructure even more and make it more accessible for users who want to build free transactions.

I plan to deliver another [RFC to define version 5 of the extrinsic
specification](https://github.com/polkadot-fellows/RFCs/pull/124) and amend RFC84,
which defines the `General` transaction format. This RFC will also include native support for the
extension version byte as part of the signing payload of future extensions.

I have also been active in the [evolution of
`pallet-identity`](https://github.com/paritytech/polkadot-sdk/pull/5554), where I added
functionality to allow an authority to grant usernames based on a deposit the authority will put up,
sponsoring the username's existence on-chain. The authority can reclaim the deposit and remove the
username after a certain amount of time has passed, which solves the problem of permanent usernames
currently present on the People Chain. The pallet was refactored to decouple usernames and
identities in order to allow for correct deposit accounting in the case of sponsored usernames. The
username effort comes with a multi-block migration to support these storage changes.

I plan on being more active on the forum, where I want to evangelize the new `TransactionExtension`
interface and push people to adopt the new interface with hopes that it will unlock new use cases in
the Polkadot ecosystem.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity). | There were no referenda during the current period in which I was allowed to vote. I target to raise it to 90% at least for the next reporting period |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

