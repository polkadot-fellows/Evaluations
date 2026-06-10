# Argument-0003: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/06/08)                                                             |
| **Submitted by**| Rodrigo Quelhas                                                                             |


## Member details

- Matrix username: @romarq:matrix.org
- Polkadot address: 12fiMKJP9t3gTFpHEXGYtdbZzwQciCpUcVFRnVXU4JYQLWvA
- Current rank: I
- Date of initial induction: 2025/10/06
- Date of last report: 2026/01/30
- Area(s) of Expertise/Interest: FRAME, Parachain Consensus


## Reporting period

- Start date: 2026/01/30
- End date: 2026/06/08


## Argument

During this reporting period, I have continued contributing to the Polkadot ecosystem with a focus on modernizing the validation framework, improving tooling, and addressing bugs across the wider Substrate dependency tree.

### Validation Framework Modernization

#### `ValidateUnsigned` Deprecation Merged

The deprecation of the `ValidateUnsigned` trait and the `#[pallet::validate_unsigned]` attribute macro ([**PR #10150**](https://github.com/paritytech/polkadot-sdk/pull/10150)) was merged on April 2, 2026. This unblocks the wider migration of pallets to the modern `TransactionExtension` API and removes long-standing technical debt around unsigned transaction validation.

#### `pallet-im-online` Migration

I migrated `pallet-im-online` from the deprecated `ValidateUnsigned` trait to the `TransactionExtension` API ([**PR #11235**](https://github.com/paritytech/polkadot-sdk/pull/11235), merged on June 9, 2026). This was one of the larger pallets still relying on the legacy validation pattern, and the migration provides another reference example for downstream parachain teams.

#### `pallet-mixnet` Migration

The migration of `pallet-mixnet` to `#[pallet::authorize]` ([**PR #11010**](https://github.com/paritytech/polkadot-sdk/pull/11010)) is still under review. It follows the same pattern as the previously merged `pallet-example-offchain-worker` migration.

### Tooling & Developer Experience

#### Workspace Dependency Inheritance Check

I opened a CI check ensuring all workspace member crates inherit shared dependencies from the workspace root instead of pinning their own versions ([**PR #11422**](https://github.com/paritytech/polkadot-sdk/pull/11422)). This prevents duplicate dependency versions creeping into the build graph, which previously caused subtle compilation issues and longer build times.

#### subxt 0.44 → 0.50 Bump and Upstream Bug Fix

I drove the migration of the polkadot-sdk workspace's `subxt`, `subxt-metadata`, and `subxt-signer` dependencies from 0.44 to 0.50 ([**PR #12096**](https://github.com/paritytech/polkadot-sdk/pull/12096)). subxt 0.50 introduces a block-anchored client API and splits `subxt::Error` into per-operation sub-errors, requiring substantial refactoring of `pallet-revive-eth-rpc`, `frame-benchmarking-cli`, and `polkadot-omni-node-lib`. The PR is currently parked pending a subxt patch release that includes the bug fix below; I plan to resume it once that lands.

While preparing the bump I identified an upstream bug in `subxt 0.50.1`: `SubstrateConfigBuilder::set_genesis_hash` silently dropped the configured hash, breaking the fully-offline transaction signing path used by `frame-benchmarking-cli`. I submitted and got merged a fix in subxt itself ([**PR #2236**](https://github.com/paritytech/subxt/pull/2236)), wiring the builder field through to `Config::genesis_hash()`. The same bug also affected `PolkadotConfig` via delegation, so both configurations were repaired by the single change.

### Multi-Block Migration Helper

The multi-block migration that clears storage items under a given prefix across many blocks ([**PR #10436**](https://github.com/paritytech/polkadot-sdk/pull/10436)) opened during the previous reporting period remains under review. It provides a safe, chunked alternative to ad-hoc single-block migrations for large storage cleanups.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100% voting activity). | There were no referendums available for Rank I members to vote on during this reporting period. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
