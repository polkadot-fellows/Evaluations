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

* I identified an AHM-related issue with pallet-xcm's transfer_assets extrinsic: https://github.com/paritytech/polkadot-sdk/issues/9054.
The issue breaks XCM transfers of DOT in some cases after AHM.
NOTE: formally, this falls into the previous report period, though the previous retention argument was submitted before this issue was identified.

* The XCM NFT PR with the new XCM adapters that use granular NFT traits was merged: https://github.com/paritytech/polkadot-sdk/pull/4300.
The new adapters are used in Westend Asset Hub in place of the old ones for pallet-uniques tokens.
  * The new adapters (`UniqueInstancesAdapter` and `UniqueInstancesDepositAdapter`) essentially supersede the old ones, `NonFungibleAdapter` and `NonFungiblesAdapter`.
  The old adapters use one of the two old NFT trait sets. Despite being in frame-support, the said traits are mostly related to pallet-uniques. Even inside FRAME, we have another NFT pallet, pallet-nfts, that doesn't use them and can't be used with the old adapters (also, it has a bit different NFT destruction logic, so there is no correct way to use the old adapter with this pallet, even if the said traits were implemented for it).
  Some time ago, new NFT traits were introduced that addressed the limitations and design issues of the old trait sets (see https://github.com/paritytech/polkadot-sdk/pull/5620, "Design Issues" section),
  The new XCM NFT adapters use this improved interface (which is granular and extendable by design). They can be implemented for any NFT solution. Consequently, any NFT solution can be coupled with the new XCM NFT adapters.
  * This PR replaced the old adapter for pallet-uniques with the new one in Westend Asset Hub.
  * Apart from the adapters, this PR introduces a new pallet to FRAME: pallet-derivatives.
  The purpose of the pallet-derivatives is to cover the following derivative asset support scenarios:
    - The pallet-derivatives can serve as an API for creating and destroying derivatives (e.g., derivative collections).
    - It can store a mapping between the foreign original ID (e.g., XCM AssetId or (AssetId, AssetInstance)) and the local derivative ID.
  See pallet-derivatives README and its docs for further details.

* I opened a PR with the implementation of new NFT traits for pallet-nfts: https://github.com/paritytech/polkadot-sdk/pull/9537.
The previous PRs implemented them for pallet-uniques only.
This PR also:
   * adds an XCM Asset Transactor for pallet-nfts to Westend Asset Hub using the XCM NFT adapter types from the PR described above.
   * uses pallet-derivatives to provide derivatives NFTs support hosted within pallet-nfts.
Overall, this PR allows tokens existing within pallet-nfts to participate in XCM transfers. Also, it paves the way to registering foreign NFT collections on Westend Asset Hub and receiving foreign NFTs. This might help explore XCM NFT use cases, having a running AH testnet capable of both transferring the original NFTs (i.e., originally minted on AH) but also hosting derivative NFTs.

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
