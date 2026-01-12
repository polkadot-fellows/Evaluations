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
- End date: 2026/01/10


## Argument

My argument primarily revolves around PRs and issues that I filed in the Polkadot SDK and Runtimes repositories. Additionally, I was quite active in Element chats, helping community members with technical questions.

### Revamp of Penpal Asset Management and XCM Fee Payment

Penpal was intended to have PEN as its native token and DOT as a foreign asset. However, DOT was ambiguously used as if it were the native token; for example, it was strictly used to pay both XCM execution and XCM delivery fees.

I performed a major revamp of Penpal’s configuration to clearly establish PEN as the first-class native token, while DOT is now properly treated as a foreign asset. As part of this work, I merged Penpal’s `Assets` and `ForeignAssets` pallet instances into a single `Assets` instance, thereby unifying asset management on Penpal while preserving the distinction between local and foreign assets at the `AssetsTransactor` level. I also integrated the `AssetConversion` and `AssetConversionTxPayment` pallets to retain the ability to automatically swap tokens for fee payment.

This constituted a breaking change for the integration testing environment involving Penpal, Asset Hub Westend, Asset Hub Rococo, Bridge Hub Westend, and Bridge Hub Rococo across multiple dimensions. Each test spans multiple chains and had to be carefully reviewed to ensure that invariants and test coverage remained intact. One additional example concerns helper macros, which implicitly assumed that the asset instance handling foreign assets was separate from the one handling local assets and was explicitly named `ForeignAssets`. While integrating these changes into the integration tests, I generalized these macros to allow specifying the name of the `Assets` instance. Not all implicit assumptions related to asset handling in the testing environment have been removed yet, but I plan to address them in follow-up work.

The [PR](https://github.com/paritytech/polkadot-sdk/pull/10726) integrating these changes has not yet been merged, but is expected to be merged soon.

### Document the `substrate_runtime` build flag

During the introduction of `pallet-revive`, the `substrate_runtime` build flag was added. This flag must be set in addition to `no_std` when compiling to WASM. The `substrate-wasm-builder` configures this automatically, so runtime developers typically do not encounter this requirement. However, I have repeatedly addressed confusion among ecosystem developers related to build errors caused by the missing `RUST_FLAG` over the past months [[1]](https://github.com/open-web3-stack/open-runtime-module-library/pull/1030#issuecomment-3301526064), [[2]](https://github.com/paritytech/polkadot-sdk/issues/10382#issuecomment-3561968206), [[3]](https://github.com/paritytech/polkadot-sdk/issues/9339).

To prevent further confusion, I added a dedicated paragraph to the documentation and prominently highlighted it in the Polkadot SDK README [[4]](https://github.com/paritytech/polkadot-sdk/pull/10514).

### Temporarily disable broken XCM error reporting

The XCM error reporting mechanism is partially [broken](https://github.com/paritytech/polkadot-sdk/issues/10078) and results in an XCM execution error when the enclosing XCM context requires fee payment. This issue went unnoticed because the instruction was typically used only in `UnpaidExecution` contexts. I identified the problem and temporarily [disabled](https://github.com/paritytech/polkadot-sdk/pull/10697) error reporting until a proper fix can be implemented.

### Additional contributions

Additionally, I was involved in [14 Polkadot SDK issues](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue%20involves%3Aclangenb%20updated%3A2025-09-15..2026-01-10), [9 Runtimes issues](https://github.com/polkadot-fellows/runtimes/issues?q=is%3Aissue%20involves%3Aclangenb%20updated%3A2025-09-15..2026-01-10), and authored several minor fixes in the Runtimes repository [[5]](https://github.com/polkadot-fellows/runtimes/pull/999), [[6]](https://github.com/polkadot-fellows/runtimes/pull/996).

Lastly, drawing on my accumulated development experience and operational knowledge of running validators, I have frequently assisted community members in Element chats. Regular participants in these discussions have likely observed my involvement.

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|------|----------------------|----------------------|----------------------------|----------|
| I    | 90%                  | N/A                  |                            |          |
| II   | 80%                  | N/A                  | No eligible referenda      |          |
| III  | 70%                  | 100%                 |                            |          |
| IV   | 60%                  | 90%                  |                            |          |
| V    | 50%                  | 80%                  |                            |          |
| VI   | 40%                  | 70%                  |                            |          |


## Misc

- [ ] Question(s):
- [ ] Concern(s):
- [ ] Comment(s):
