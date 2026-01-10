# Argument-0007: Retention at Rank 2

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2026/01/10) |
| **Submitted by**| Christian Langenbacher          |


## Member details

- Matrix username: `@clang:matrix.org`
- Polkadot address: `16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3`
- Current rank: `2`
- Date of initial induction: `2024/03/27`
- Date of last report: `2025/09/15`
- Area(s) of Expertise/Interest: `Parachain Builder, Runtime, Clients`


## Reporting period

- Start date: 2025/09/15
- End date: 2025/01/10


## Argument
My argument mostly revolves around PRs and issues that I filed in the Polkadot-SDK and Runtimes repository. Additionally, I was quite active in the element chats helping out community members with technical questions.

### Revamp Penpal's Asset Management and XCM Fee Payment
Penpal was supposed to have PEN as the native token and DOT as a foreign asset. However, the DOT was ambiguously used as if it were the native token, e.g. it was strictly used to pay both XCM execution and XCM delivery fees.

I did a major revamp of Penpal's configuration to clearly make PEN the first class citizen as a native token, while DOT is now properly treated as a foreign asset.
While doing so, I merged Penpal's pallet `Assets` and `ForeignAssets` instance into a single `Assets` instance, unifying asset management on Penpal, keeping the distinction between
local assets and foreign assets on the `AssetsTransactor` level. I also integrated the `AssetConversion` and `AssetConversionTxPayment` pallet keep the ability to autoswap tokens for fee payment.

This was a breaking change with respect to the integration testing environment for Penpal, Asset Hub Westend, Asset Hub Rococo, Bridge Hub Westend, Bridge Hub Rococo on many angles. Each test involves multiple chains, and had to be carefully reviewed to ensure that invariants and test coverage is still intact. An additional example are the helper macros, which implicitly assumed that the asset instance handling foreign assets is separate from the one handling local assets, and that is also called `ForeignAssets`. So while integration the changes into the integration-tests I made those macros more generic allow to specify the name of the `Assets` instance. Not all implicit assumptions in the testing environment involving assets have been removed yet, but I plan to do so in follow-up work.

The [PR](github.com/paritytech/polkadot-sdk/pull/10726) integrating all these changes has not been merged yet, but it should be merged soon.

### Document the `substrate_runtime` build flag
During the course of introducing pallet-revive the`substrate_runtime` build flag was introduced, which needs to be set additionally to `no_std` when compiling to WASM. The `substrate-wasm-builder` does this automatically, so runtime developers usually do not come across this caveat. However, I have addressed confusions of ecosystem developers regarding build erros due to the missing `RUST_FLAG` multiple times in the past months, [[1]](https://github.com/open-web3-stack/open-runtime-module-library/pull/1030#issuecomment-3301526064),[[2]](https://github.com/paritytech/polkadot-sdk/issues/10382#issuecomment-3561968206),[[3]](https://github.com/paritytech/polkadot-sdk/issues/9339).

To prevent further confusion, I have added a paragraph in the documentation, but also placed it prominently in the README of the PSDK [[4]](https://github.com/paritytech/polkadot-sdk/pull/10514).

### Temporarily disable broken XCM error reporting
The XCM error reporting mechanism, is partially [broken](https://github.com/paritytech/polkadot-sdk/issues/10078) and results in an XCM execution error if the enclosing XCM context requires fee payment. This was undiscovered as the instruction was usually used in `UnpaidExecution` contexts only. I discovered it and simply [disabled](https://github.com/paritytech/polkadot-sdk/pull/10697) the reporting until a proper fix is implemented.


### Trivia
Additionally, I was involved in [14 PSDK issues](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue%20involves%3Aclangenb%20updated%3A2025-09-15..2026-01-10), [9 Runtimes Issues](https://github.com/polkadot-fellows/runtimes/issues?q=is%3Aissue%20involves%3Aclangenb%20updated%3A2025-09-15..2026-01-10), and authored some minor fixes in the runtimes repository [[5]](https://github.com/polkadot-fellows/runtimes/pull/999), [[6]](https://github.com/polkadot-fellows/runtimes/pull/996).

Lastly, with my accumulated developer experience and operational knowledge regarding running validators, I have been helping out community members in the Element chats quite frequently. Those who follow the chats have likely seen my partaking there.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|----------------------|----------------------------|---|
|I  |90%   | N/A                  | No elligible referenda     |  |
|II |80%   | N/A                  |                            |  |
|III|70%   | 100%                 |                            |  |
|IV |60%   | 90%                  |                            |  |
|V  |50%   | 80%                  |                            |  |
|VI |40%   | 70%                  |                            |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
