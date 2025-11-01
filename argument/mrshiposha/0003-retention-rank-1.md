# Argument-0003: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/06/10                                                                                  |
| **Submitted by**| Daniel Shiposha                                                                             |


## Member details

- Matrix username: `@mrshiposha:matrix.org`
- Polkadot address: `14aC2hfNZTX4sMHPh47MjGB4Vr4rVYHZgBid54vRKrZVBZQY`
- Current rank: Rank I
- Date of initial induction: 2024/12/11
- Date of last report: 2025/03/26
- Area(s) of Expertise/Interest: XCM, NFT


## Reporting period

- Start date: 2025/04/27
- End date: 2025/07/11

## Argument

During the reporting period, two of my pull requests were merged.

1. https://github.com/paritytech/polkadot-sdk/pull/8281. A simple common implementation for `XcmPaymentApi::query_weight_to_asset_fee` that can be easily used by any chain Runtime.
This PR is a simple alternative to https://github.com/paritytech/polkadot-sdk/pull/8202.
It uses a workaround instead of a big refactoring.

2. https://github.com/paritytech/polkadot-sdk/pull/5620: This PR introduces a new set of traits that represent different asset operations in a granular and abstract way.
The new abstractions provide an interface for collections and tokens for use in general and XCM contexts.

Also, I updated and refactored the related XCM NFT PR containing the XCM adapters that use the new NFT traits: https://github.com/paritytech/polkadot-sdk/pull/4300.
It is in the review process. It also contains a new `pallet-derivatives` Pallet to simplify different support scenarios of derivative assets (see the PR description, crate docs, and test docs for details).

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   | There were no referenda I was eligible to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
