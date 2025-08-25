# Argument-0004: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/08/25                                                                                  |
| **Submitted by**| Daniel Shiposha                                                                             |


## Member details

- Matrix username: `@mrshiposha:matrix.org`
- Polkadot address: `14aC2hfNZTX4sMHPh47MjGB4Vr4rVYHZgBid54vRKrZVBZQY`
- Current rank: Rank I
- Date of initial induction: 2024/12/11
- Date of last report: 2025/06/10
- Area(s) of Expertise/Interest: XCM, NFT


## Reporting period

- Start date: 2025/07/12
- End date: 2025/09/29

## Argument

During the reporting period:
1. I identified an AHM-related issue with pallet-xcm's transfer_assets extrinsic: https://github.com/paritytech/polkadot-sdk/issues/9054.
The issue breaks XCM transfers of DOT in some cases after AHM.
NOTE: formally, this falls into the previous report period, though the previous retention argument was submitted before this issue was identified.
2. The XCM NFT PR with the new XCM adapters that use granular NFT traits was merged: https://github.com/paritytech/polkadot-sdk/pull/4300.
The new adapters are used in Westend Asset Hub in place of the old ones for pallet-uniques tokens.
3. I opened a PR with the implementation of new NFT traits for pallet-nfts: https://github.com/paritytech/polkadot-sdk/pull/9537.
The previous PRs introduced the traits and implemented them for pallet-uniques only.
This PR also adds an XCM Asset Transactor for pallet-nfts to Westend Asset Hub, as well as the derivatives NFTs hosted within pallet-nfts.



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
