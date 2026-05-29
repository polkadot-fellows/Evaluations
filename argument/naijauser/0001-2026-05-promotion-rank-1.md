# Argument-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/05/29)                                                             |
| **Submitted by**| naijauser                                                                       |


## Member details

- Matrix username: @naijauser:matrix.org
- Polkadot address: 12mzp6SdXsT9NbCwYptcTNeALheiaBVRSM7XpCb4Z3HP9wLP
- Current rank: Candidate
- Date of initial induction:2026/05/19
- Date of last report: N/A
- Area(s) of Expertise/Interest: FRAME, Tooling, Network, Virtual Machine


## Reporting period

- Start date: 2025/11/01
- End date: 2026/05/29


## Argument
I have been actively contributing to the Polkadot ecosystem since November 2025. In that time I have contributed across three repositories touching the core Polkadot-SDK, Ecosystem Testing, and Tooling.

For promotion to Rank 1, the Manifesto states as a requirement:
>Three clear examples of a modest but substantial contribution to protocol development

My argument will contain only merged PRs across the repositories I have contributed to.

### Polkadot Ecosystem Tests
#### 1. Deepen Governance Pallet Conviction Voting Test Coverage
[polkadot-ecosystem-tests#556](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/556) deepens test coverage for the governance pallet. It covers voting (standard with conviction, split, split+abstain), vote removal, voting account lock and freezes before and after voting, vote delegation, and vote removal.

#### 2. Add Test Coverage for Configuration Pallet
[polkadot-ecosystem-tests#563](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/563) adds test coverage for the configuration pallet. It covers all configuration options including Core Configuration, Scheduler Configuration, Dispute Configuration, Message Queue Configuration, and HRMP Configuration.

#### 3. Add Test Coverage for Registrar Pallet
[polkadot-ecosystem-tests#572](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/572) adds test coverage for the registrar pallet. It covers Registration Functions (reserve, register, force_register, deregister) and Lifecycle Management functions (swap, add_lock, remove_lock, schedule_code_upgrade, set_current_head).

#### 4. Add Test Coverage for Asset Rate Pallet
[polkadot-ecosystem-tests#576](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/576) adds test coverage for the asset rate pallet. It covers key scenarios of creating a new asset rate, updating an existing asset rate, removing an asset rate and ensuring that only authorized origins can create, update, or remove rates.

### Polkadot-SDK
#### 5. Add support for asset V3 to V5 conversion of LocalPay
[polkadot-sdk#10657](https://github.com/paritytech/polkadot-sdk/pull/10657) adds support for conversion of versioned asset from V3 to V5.

#### 6. Remove `pallet::getter` usage from sassafras pallet
[polkadot-sdk#10460](https://github.com/paritytech/polkadot-sdk/pull/10460) removes `pallet::getter` from the sassafras pallet and replaces it with the preferred syntax `Key::<T>::get()`.

#### 7. Remove `pallet::getter `usage from merkel mountain range pallet
[polkadot-sdk#10437](https://github.com/paritytech/polkadot-sdk/pull/10437) removes `pallet::getter` from the sassafras pallet and replaces it with the preferred syntax `Key::<T>::get()`.

I have broad interests in the Polkadot ecosystem. My goals are to challenge myself and push the limits of my knowledge through meaningful contributions that help sustain and advance the network. A full picture of my active contributions across the Polkadot-SDK, Polkadot Ecosystem Tests, and Try Runtime Cli repositories can be seen using these links.

- [polkadot-sdk:@naijauser](https://github.com/paritytech/polkadot-sdk/pulls/naijauser)
- [polkadot-ecoystem-tests:@naijauser](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pulls?q=is%3Apr+author%3Anaijauser+)
- [try-runtime-cli:@naijauser](https://github.com/paritytech/try-runtime-cli/pulls/naijauser)

## Acknowledgement
Thanks to [Alexandre R. Baldé](https://github.com/rockbmb) for their thorough review and feedback on my PRs.

## Voting record
N/A
