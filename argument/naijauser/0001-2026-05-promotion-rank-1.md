# Argument-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/05/29)                                                             |
| **Submitted by**| naijauser                                                                       |


## Member details

- Matrix username: @naijauser:matrix.org
- Polkadot address: 12mzp6SdXsT9NbCwYptcTNeALheiaBVRSM7XpCb4Z3HP9wLP
- Current rank: Candidate
- Date of initial induction: 2026/05/19
- Date of last report: N/A
- Area(s) of Expertise/Interest: FRAME, Tooling, Network, Virtual Machine


## Reporting period

- Start date: 2025/11/01
- End date: 2026/05/29


## Argument
I have been actively contributing to the Polkadot ecosystem since November 2025. In that time I have contributed across three repositories — the core Polkadot-SDK, Polkadot Ecosystem Tests, and Try Runtime CLI.

For promotion to Rank 1, the Manifesto states as a requirement:
>Three clear examples of a modest but substantial contribution to protocol development

My argument contains only merged PRs from Polkadot-SDK and Polkadot Ecosystem Tests, along with their impact. Contributions to Try Runtime CLI are ongoing and linked at the end.

### Polkadot Ecosystem Tests
#### 1. Deepen Governance Pallet Conviction Voting Test Coverage
[polkadot-ecosystem-tests#556](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/556) deepens test coverage for the governance pallet. It covers voting (standard with conviction, split, split+abstain), vote removal, voting account lock and freezes before and after voting, and vote delegation.

#### 2. Add Test Coverage for Configuration Pallet
[polkadot-ecosystem-tests#563](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/563) adds test coverage for the configuration pallet. It covers all configuration options including Core Configuration, Scheduler Configuration, Dispute Configuration, Message Queue Configuration, and HRMP Configuration.

#### 3. Add Test Coverage for Registrar Pallet
[polkadot-ecosystem-tests#572](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/572) adds test coverage for the registrar pallet. It covers Registration Functions (reserve, register, force_register, deregister) and Lifecycle Management functions (swap, add_lock, remove_lock, schedule_code_upgrade, set_current_head).

#### 4. Add Test Coverage for Asset Rate Pallet
[polkadot-ecosystem-tests#576](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/576) adds test coverage for the asset rate pallet. It covers key scenarios of creating a new asset rate, updating an existing asset rate, removing an asset rate, and ensuring that only authorized origins can create, update, or remove rates.

#### Impact
These four contributions meaningfully expand the integration test coverage for core Polkadot runtime pallets. Collectively they exercise governance mechanics (conviction voting, delegation, locks), parachain lifecycle management (registration, code upgrades, swaps), relay chain configuration options across all major subsystems, and asset rate authorization. This coverage helps catch regressions in protocol-critical paths that unit tests alone may miss, increasing confidence in runtime upgrades.

### Polkadot-SDK
#### 5. Add support for asset V3 to V5 conversion of LocalPay
[polkadot-sdk#10657](https://github.com/paritytech/polkadot-sdk/pull/10657) adds V3→V5 asset conversion support to the `match_asset` function in `LocalPay`. The function previously only handled V4 and V5 assets — clients still encoding assets as V3 would fail asset matching entirely, blocking fee payment. The fix adds a V3→V5 conversion path (via V4), restoring compatibility for legacy clients without breaking existing behaviour.

#### 6 & 7. Remove `pallet::getter` usage from sassafras and Merkle Mountain Range pallets
The `pallet::getter` macro generates auto-named getter functions that are being phased out across the SDK in favour of explicit storage access, which is less error-prone and reduces macro expansion overhead. [polkadot-sdk#10460](https://github.com/paritytech/polkadot-sdk/pull/10460) removes all `pallet::getter` usages from the sassafras pallet and [polkadot-sdk#10437](https://github.com/paritytech/polkadot-sdk/pull/10437) does the same for the Merkle Mountain Range pallet, replacing them with the preferred syntax `Key::<T>::get()`.

#### Impact
These contributions span both protocol correctness and codebase health in the core SDK. The asset V3→V5 conversion fix ensures that runtimes using `LocalPay` handle versioned assets correctly across the XCM version gap, preventing potential failures in cross-chain fee payment. The `pallet::getter` removal from the sassafras and MMR pallets advances the ecosystem-wide deprecation of the macro, reducing compile-time overhead and aligning these pallets with the modern FRAME storage access convention.

A full picture of my contributions across Polkadot-SDK, Polkadot Ecosystem Tests, and Try Runtime CLI can be found below.

- [polkadot-sdk:@naijauser](https://github.com/paritytech/polkadot-sdk/pulls/naijauser)
- [polkadot-ecosystem-tests:@naijauser](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pulls?q=is%3Apr+author%3Anaijauser+)
- [try-runtime-cli:@naijauser](https://github.com/paritytech/try-runtime-cli/pulls/naijauser)

## Acknowledgement
Thanks to [Alexandre R. Baldé](https://github.com/rockbmb) for their thorough review and feedback on my PRs.

## Voting record
N/A

