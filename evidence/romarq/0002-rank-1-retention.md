# Argument-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/01/30)                                                             |
| **Submitted by**| Rodrigo Quelhas                                                                             |


## Member details

- Matrix username: @romarq:matrix.org
- Polkadot address: 12fiMKJP9t3gTFpHEXGYtdbZzwQciCpUcVFRnVXU4JYQLWvA
- Current rank: I
- Date of initial induction: 2025/10/06
- Date of last report: 2025/10/10
- Area(s) of Expertise/Interest: FRAME, Parachain Consensus


## Reporting period

- Start date: 2025/10/10
- End date: 2026/01/30


## Argument

During this reporting period, I have continued contributing to the Polkadot ecosystem with a focus on FRAME improvements, runtime migrations, and API modernization. My work has centered on reducing technical debt, improving developer experience, and enhancing the maintainability of the protocol's core infrastructure.

### Runtime Migration & Architecture Improvements

#### Single Block Migrations Refactor

I refactored the single block migration system by moving the migration logic from `frame_executive` to `frame_system` configuration ([**PR #844**](https://github.com/polkadot-fellows/runtimes/pull/844)). This change improves the architecture by providing better separation of concerns and making the migration system more intuitive for runtime developers. The PR was merged on October 12, 2025.

#### Multi-Block Storage Migration

I added a new multi-block migration to clear storage items under specific prefixes across multiple blocks ([**PR #10436**](https://github.com/paritytech/polkadot-sdk/pull/10436)). This migration enables safe and efficient large-scale storage cleanup operations, which is particularly valuable for runtime upgrades that need to remove deprecated storage structures without having the risk to stall the chain. The PR was opened on November 26, 2025.

### API Modernization & Deprecation

#### ValidateUnsigned Trait Deprecation

I opened a PR for deprecating of the `ValidateUnsigned` trait and the `#[pallet::validate_unsigned]` attribute macro ([**PR #10150**](https://github.com/paritytech/polkadot-sdk/pull/10150)). This deprecation is part of a broader effort to modernize the validation framework and reduce technical debt by consolidating validation logic into the newer transaction extension system. The PR was opened on October 28, 2025.

#### TransactionExtension Migration

To support the deprecation efforts and provide a reference implementation, I updated `pallet-example-offchain-worker` to use the modern `TransactionExtension` API instead of the deprecated validation patterns ([**PR #10716**](https://github.com/paritytech/polkadot-sdk/pull/10716)). This work demonstrates the migration path for other pallets and helps developers understand how to adopt the new patterns. The PR was merged on January 21, 2026.

### XCM Improvements

#### XCM Executor Optimization

I refactored the `dry_run_xcm` function to use `Config::XcmExecutor` directly instead of creating new executor instances ([**PR #10102**](https://github.com/paritytech/polkadot-sdk/pull/10102)). This optimization improves performance and ensures consistency in XCM testing and simulation workflows by reusing the configured executor. The PR was merged on October 24, 2025.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100% voting activity). | There were no referendums available for Rank I members to vote on during this reporting period. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
