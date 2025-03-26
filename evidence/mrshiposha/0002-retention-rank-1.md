# Evidence-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/03/26                                                                                  |
| **Submitted by**| Daniel Shiposha                                                                             |


## Member details

- Matrix username: `@mrshiposha:matrix.org`
- Polkadot address: `14aC2hfNZTX4sMHPh47MjGB4Vr4rVYHZgBid54vRKrZVBZQY`
- Current rank: Rank I
- Date of initial induction: 2024/12/11
- Date of last report: 2024/12/23
- Area(s) of Expertise/Interest: XCM, NFT


## Reporting period

- Start date: 2025/01/27
- End date: 2025/04/27

## Evidence

My primary focus during the reporting period was XCM, particularly improving and simplifying fee-related code.

I tested several scenarios of the DryRunApi Runtime API. During this testing, I found and then fixed the bug with XCM objects' versions returned to the client, preventing the API from being backward compatible (See the [PR](https://github.com/paritytech/polkadot-sdk/pull/7438)).
While fixing the XCM version bug, a couple of others concerning the XCM router's state consistency before performing the XCM dry run were found and fixed.

After that, I tried to simplify the XCM executor's Weight Trader. I haven't finished yet, as this appeared to be more complicated than anticipated.
The WIP branch can be found [here](https://github.com/UniqueNetwork/polkadot-sdk/tree/refactor/simplify-weight-trading).

I started tackling this for the following reasons:
* The XcmPaymentApi's `queryWeightToAssetFee` method implementation partially duplicates the code of the WeightTrader, and this can't be avoided with the current code structure in any chain. This can lead to fee estimation errors and unexpected cross-chain transaction results for a client.
* Different Weight Traders duplicate the overall trading logic; it could be simplified.
* The Traders' code deals with unnecessary API burden: 
    - They accept multiple assets as a formal parameter and extract the needed one. However, this is unnecessary since only one fee asset can be used to buy weight (see the `BuyExecution` and `PayFees` API).
    - They theoretically accept NFTs; however, it isn't obvious how to handle them properly in the weight trading context or in the XCM executor (again, because only one asset can be used to pay fees, it isn't obvious how NFTs should work with delivery fees).
      In practice, no Trader accepts NFTs, and the assumption of fungible fees is practically everywhere. Also, the XcmPaymentApi doesn't currently provide methods that work with NFTs.

## Voting record

None, since I am a Rank I member.

