# Evidence-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/12/23                                                                                  |
| **Submitted by**| Daniel Shiposha                                                                             |


## Member details

- Matrix username: `@mrshiposha:matrix.org`
- Polkadot address: `14aC2hfNZTX4sMHPh47MjGB4Vr4rVYHZgBid54vRKrZVBZQY`
- Current rank: Candidate
- Date of initial induction: 2024/12/11
- Date of last report: N/A
- Area(s) of Expertise/Interest: XCM, NFT


## Reporting period

- Start date: N/A
- End date: N/A

## Evidence

I was made a Fellowship Candidate in December 2024, thanks to Bryan Chen.

I'm seeking to become a Rank I member. According to the Manifesto, I must provide evidence of a modest but substantial contribution to protocol development.
I have been working in the Ecosystem since February 2022 as a Unique Network parachain team member and have made several contributions to Substrate and Polkadot.

Since early 2023, my main focus of activity has been XCM. My task is to facilitate cross-chain NFT interoperability (where the term "non-fungible token" is understood in a broad sense as any "unique on-chain object").

I authored an accepted XCM RFC about custom asset claimers (https://github.com/polkadot-fellows/xcm-format/blob/master/proposals/0037-custom-asset-claimer.md),
proposed another one about XCM Asset Metadata (https://github.com/polkadot-fellows/RFCs/pull/125) which is currently in the review process,
reported XCM-related issues (https://github.com/paritytech/polkadot-sdk/issues/5878, https://github.com/paritytech/polkadot-sdk/issues/4073, https://github.com/paritytech/polkadot-sdk/issues/4841, https://github.com/polkadot-fellows/xcm-format/pull/55#discussion_r1617630672), participated in XCM-related discussions (primarily concerning fee estimation, see the on-going one an example: https://github.com/paritytech/polkadot-sdk/issues/6126).

Also, I'm trying to introduce general and granular interfaces for NFT solutions (whatever the definition of a "unique object" is used within it) so they can be used across different runtime modules, including facilitating the creation of XCM NFT asset transactors. See the motivation of this PR: https://github.com/paritytech/polkadot-sdk/pull/5620 and its supposed-to-be-follow-up: https://github.com/paritytech/polkadot-sdk/pull/4300.

Before this activities, I contributed several fixes to Substrate:
* https://github.com/paritytech/substrate/pull/12594. Fix for the `construct_runtime` macro: There was a bug with the `#[cfg(feature = "...")]` attributes inside the macro that prevented using more than one such attribute (i.e., you could have only one optional feature-gated pallet but not many).
* https://github.com/paritytech/substrate/pull/12222. Fix for the template node's runtime by adding the `ConstFeeMultiplier` struct: The default fee multiplier multiplied the fees by zero. This was hard to notice and led to equal fees for all the extrinsics regardless of their weight. As the template node is a basis for building new chains, this fix is meant to save the new builders from unintended flat fees for every possible transaction in their chain.
* https://github.com/paritytech/substrate/pull/13410. Adds a `SubmitOrigin` setting to the `pallet-democracy` Config, generalizing the origin that can be used to submit a proposal.
* https://github.com/paritytech/substrate/pull/13349. Extends the `frame_support::trait::tokens::nonfungible(s)_v2::Inspect` trait and adds a Runtime API for the `pallet-nfts` with the interface following the `Inspect` trait.

Besides the code, I was a speaker on Sub0 2023 in Lisbon (https://www.youtube.com/watch?v=4DAHuWUvbwI) and Sub0 Asia 2024 (https://www.youtube.com/watch?v=xmLWjiujNAg) discussing possible NFT interactions between chains via XCM.

## Voting record

None, since I am a candidate.

