# Argument-0008: Retention at Rank 2

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2026/03/25) |
| **Submitted by**| Christian Langenbacher          |


## Member details

- Matrix username: `@clang:matrix.org`
- Polkadot address: `16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3`
- Current rank: `2`
- Date of initial induction: `2024/03/27`
- Date of last report: `2026/01/10`
- Area(s) of Expertise/Interest: `Parachain Builder, Runtime, Clients`


## Reporting period

- Start date: 2026/01/10
- End date: 2026/03/25


## Argument

My argument primarily revolves around PRs and issues that I filed in the Polkadot SDK and Runtimes repositories. Additionally, I was quite active in Element chats, helping community members with technical questions.

### Finalize - Revamp of Penpal Asset Management and XCM Fee Payment

I have already mentioned the [PR](https://github.com/paritytech/polkadot-sdk/pull/10726) in the last report. As per the review, I have also added a `GenesisConfig` struct to the `pallet-asset-conversion`. Further simplifying the setup for the emulated integration tests, which will also be used in an upcoming PR, applying the same changes into the emulated tests in the runtimes repository.

Additionally, working on this PR that made the tests more production realistic, I have [identified](https://github.com/paritytech/polkadot-sdk/issues/11388) and [fixed](https://github.com/paritytech/polkadot-sdk/pull/11389) a bug in the `SwapFirstAssetTrader`. When the fees were exact, `Fungible(0)` was put into the holding register. This resulted in an `AssetTrapped(Fungible(0))` error that even failed to decode. While harmless, this results in event decoding errors for frontends that use the rust code as `Fungible(0)` fails to decode.

### NPoS: Expose election round (priority) in ElectionResult winners

I have patched [offline-election-tool](https://github.com/clangenb/offline-election-tool/tree/dev) to also display the priority of the winners in the election results. However, this patch required a PSDK patch to expose the validator priorities that were already computed in `seq_phragmen` and `phragmms`, but then discarded. I have [upstreamed](https://github.com/paritytech/polkadot-sdk/pull/11380) so that other projects can directly use the rust implementation to compute the priorities. I have prepared a follow-up [PR](https://github.com/clangenb/polkadot-sdk/pull/1) so that the mining functions do the same, but it needs more refinement.

### Identify and fix slot-based collator panic (Observed on AHP)

When a parachain collator starts with `--authoring=slot-based` and warp-syncs from scratch, it panics and shuts down the node as it did not properly wait for aura to be ready. I have identified this at a sys-collator I support and [fixed](https://github.com/paritytech/polkadot-sdk/pull/11381) it with the same mechanism that we use for the lookahead collators.

### Additional smaller contributions

#### Identify and fix slot-based collator panic (Observed on AHP)

When a parachain collator starts with `--authoring=slot-based` and warp-syncs from scratch, it panics and shuts down the node as it did not properly wait for aura to be ready. I have identified this at a sys-collator I support and [fixed](https://github.com/paritytech/polkadot-sdk/pull/11381) it with the same mechanism that we use for the lookahead collators.

#### Pallet Assets: Properly decrement supply during refund if asset is burned

When a user calls refund with `allow_burn = true`, their token balance is destroyed, but the asset's total supply was never updated. This caused total issuance to overcount. In production, burning path is rarely triggered. The fungibles trait interface always passes allow_burn = false, so only users manually submitting the refund extrinsic with the burn flag would hit it, however, it has been observed on Westend. It will need a migration there to correct the total issuance there, but I have fixed the [root cause](https://github.com/paritytech/polkadot-sdk/pull/11441) at least.

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
