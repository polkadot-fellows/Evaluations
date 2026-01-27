# Argument-0005: Promotion at Rank IV

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/01/27)                                                             |
| **Submitted by**| Guillaume Thiolliere                                                                        |


## Member details

- Matrix username: @guillaume:parity.io
- Polkadot address: 13psJuWEjBuZGaFqXvFnLMC6ME8RVVfQAhtFhydYjW45oKgZ
- Current rank: I
- Date of initial induction: 2025/01/09
- Date of last report: 2025/11/02
- Area(s) of Expertise/Interest:
  - Polkadot business-logic (aka the 'runtime')
  - The internals of the FRAME pallet framework
  - Runtime and Host APIs


## Reporting period
- Start date: N/A
- End date: 2026/01/27


## Argument
I have worked on the Polkadot SDK from 2019–2022 and from August 2024 to the present.

In the former period, I implemented various features and improvements to the FRAME APIs. This work is still in the current code of the Polkadot SDK, and I regularly review the changes made to it; therefore, I think my expertise on the foundation of the Polkadot SDK is valuable to Polkadot. During this former period, I achieved the following:
I rewrote the `decl_*` macros into the new `pallet` macros, which substantially improved the developer experience ([PR](https://github.com/paritytech/substrate/pull/6877)).
I designed and implemented the instantiable pallet, allowing the reuse of a pallet with different configurations; this is used by Asset Hub for the various asset pallets ([PR](https://github.com/paritytech/substrate/pull/1800)).
I implemented the counted storage map ([PR](https://github.com/paritytech/substrate/pull/9125)) and the iterable storage map without a linked list ([PR](https://github.com/paritytech/substrate/pull/4185)).
I improved `construct_runtime` to automatically find pallet parts ([PR](https://github.com/paritytech/substrate/pull/9681)).
I contributed to improving the `parity-scale-codec` API by implementing the codec for `u8` using compile-time specialization; this technique was later used to implement optimizations for various types ([PR](https://github.com/paritytech/parity-scale-codec/pull/83)).
I also contributed to pallets such as Staking, Session, and others, although some of those pallets have changed quite a lot since then.
During my time off, I also contributed to the crate `macro_magic`, enabling a better experience when using the default config for Frame System or other pallets ([Issue](https://github.com/sam0x17/macro_magic/issues/3)).

Since August 2024, one key work has been Transaction Extensions, an improvement over Signed Extensions that allows for declaring more general transaction validation in a more flexible way than just unsigned and signed transactions. This work originated from Gavin Wood and was continued by George Pisaltu. I then made significant contributions to it: I identified issues in the original PR (missing logic for bare extrinsics ([comment](https://github.com/paritytech/polkadot-sdk/pull/3685#discussion_r1794069271)), version not part of any signed payload ([comment](https://github.com/paritytech/polkadot-sdk/pull/3685#issuecomment-2400404179)), contributed to refactoring the code, and completed follow-up work, including improved weight reclaim ([PR](https://github.com/paritytech/polkadot-sdk/pull/6140)) and enabling support for more than 12 extensions ([PR](https://github.com/paritytech/polkadot-sdk/pull/7028)), and other minor improvements.
I introduced `pallet::authorize` to replace the to-be-deprecated "validate unsigned" flow ([PR](https://github.com/paritytech/polkadot-sdk/pull/6324)). I believe `pallet::authorize` provides a better developer experience, and removing "validate unsigned" will also improve the maintainability of the Polkadot SDK.
I also made a presentation in a video meeting to explain the new Transaction Extensions ([YouTube Video](https://www.youtube.com/watch?v=H1Y4pm8KIUI)).

My main work after Transaction Extensions was on the private Proof-of-Personhood project. I contributed to the People pallet (`pallet-people`), the registrar for people that gathers them in rings to enable private interaction. One version has been published in the Polkadot SDK, but development still happens mostly in our currently private repository ([code](https://github.com/paritytech/polkadot-sdk/tree/f134881a56e7733a6b5171c81b05ce4df40dd695/substrate/frame/people)).
I designed and implemented the Origin Restriction pallet to limit people's anonymous interactions or other origins to a reasonable usage of block space ([code](https://github.com/paritytech/polkadot-sdk/tree/f134881a56e7733a6b5171c81b05ce4df40dd695/substrate/frame/origin-restriction)).
Much of this work is still private; I implemented a large part of DIM2 and two other pallets for the "Fairest Airdrop" ([referenda](https://polkadot.subsquare.io/referenda/1783)).

In parallel to this work, I also continued reviewing and contributing to the Polkadot SDK.
I added support for the Statement Store in the Omni-Node ([PR](https://github.com/paritytech/polkadot-sdk/pull/8076)).
I added a feature requested by the ecosystem in the Assets pallet ([PR](https://github.com/paritytech/polkadot-sdk/pull/7456)).
I advanced the development of Optimistic Funding by reviewing the [PR](https://github.com/paritytech/polkadot-sdk/pull/6994) and by implementing a solution ([PR](https://github.com/paritytech/polkadot-sdk/pull/8753)); unfortunately, this item is stale.
I found and fixed a small calculation error in the weight reclaim logic ([PR](https://github.com/paritytech/polkadot-sdk/pull/5273)).
I reviewed PRs such as the Host <-> Runtime interface refactor ([PR](https://github.com/paritytech/polkadot-sdk/pull/7375)), Pallet View Functions ([PR](https://github.com/paritytech/polkadot-sdk/pull/7412)), Pallet Asset Holder ([PR](https://github.com/paritytech/polkadot-sdk/pull/4530)), Pallet Multi-Asset Bounties ([PR](https://github.com/paritytech/polkadot-sdk/pull/8381)), and others ([PR list](https://github.com/paritytech/polkadot-sdk/pulls?page=1&q=is%3Apr+reviewed-by%3Agui1117+created%3A2024-07-25..2026-01-25)).
I always review deeply and sometimes find unexpected changes that are missed, such as the removal of the Alice Sudo key during a refactor ([comment](https://github.com/paritytech/polkadot-sdk/pull/7476#pullrequestreview-2622690960)) or that the migration multisig wrongly expected sr25519 accounts only ([comment](https://github.com/polkadot-fellows/runtimes/pull/929#discussion_r2382097269)).
I also found a way to check at compile-time (and most importantly without a breaking change) for duplicated enum variant indices in the `parity-scale-codec` derive macro ([comment](https://github.com/paritytech/parity-scale-codec/pull/628#issuecomment-2453814878)).
I found that the Polkadot runtime benchmark configuration was suboptimal, potentially overestimating some weights, and fixed it ([PR](https://github.com/polkadot-fellows/runtimes/pull/525)).
Following an unrelated audit, I found and fixed some potential spam of the transaction pool in the experimental tasks feature ([PR](https://github.com/paritytech/polkadot-sdk/pull/10162)); I also fixed it for instantiable pallets ([PR](https://github.com/paritytech/polkadot-sdk/pull/5194)).
I made various small contributions that help everyone's daily work, such as better error messages and sane CI messages: ([PR 1](https://github.com/paritytech/polkadot-sdk/pull/7142), [PR 2](https://github.com/paritytech/polkadot-sdk/pull/5506), [PR 3](https://github.com/paritytech/polkadot-sdk/pull/5580)).
I am also currently working on allowing multiple transaction extension pipelines in the same runtime ([PR](https://github.com/paritytech/polkadot-sdk/pull/7035)).

By regularly looking into the Polkadot SDK and questioning implementations, I also found and notified parity technologies of one moderate security issue three months before SRLabs. With rigorous testing, I also found panics in the `verifiable` crate regarding invalid member keys ([PR](https://github.com/paritytech/verifiable/pull/21)). I regularly raise issues and concerns about error-prone logic or loosely defined APIs to ensure we have a solid basis to work with.

Given this work, I am applying for promotion to Rank IV. While I have not held Rank III for a full year, I believe my contributions over the last year were worthy of Rank III.
I contributed to designs such as the new weight reclaim in the context of the new Transaction Extension pipeline, the API for `pallet::authorize`, and the mechanism for Origin Restriction. I implemented many features as listed above. I found genuine solutions for improving APIs and avoiding breaking changes, for example, for the `parity-scale-codec` compile-time check and the implementation of Transaction Extensions for more than 12 extensions. I provided numerous high-quality reviews, found and fixed issues in the codebase, and advocated for Polkadot by presenting the new Transaction Extension feature. I think my work on Proof-of-Personhood contributes to the future of Polkadot, as the project has been approved by the community in Referendum 1783 ([referenda](https://polkadot.subsquare.io/referenda/1783)). Also, although not committed yet, there is a discussion to explicitly add it to the Manifesto ([Issue](https://github.com/polkadot-fellows/help-center/issues/13)).

## Voting record
|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote. |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
