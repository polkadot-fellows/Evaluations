# Argument-0003: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026-05-14                                                                                  |
| **Submitted by**| rockbmb                                                                                     |


## Member details

- Matrix username: @alexandre.balde@parity.io
- Polkadot address: 13jBAtYJar4xujPaEx41FxjSt9PqU7LqJRbySJiVdMtuWN42
- Current rank: 1
- Date of initial induction: [2025-10-28](https://collectives.statescan.io/#/extrinsics/7473060-2)
- Date of last report: 2026-02-13
- Area(s) of Expertise/Interest: System Parachains, Polkadot Runtime


## Reporting period

- Start date: 2026-02-14
- End date: 2026-05-31


## Evidence

During this reporting period I continued my work on testing pallets deployed on system chains.

### `pallet-psm`

`pallet-psm` is the stablecoin mechanism for pUSD on Asset Hub. Users deposit external assets and mint pUSD against them; the pallet must maintain invariants between reserves, debt, and issuance.

I added `try_state` checks and fuzz testing to the pallet ([#11805](https://github.com/paritytech/polkadot-sdk/pull/11805), awaiting review). The `try_state` checks encode the pallet's accounting invariants so they can be validated during runtime upgrades. The fuzzers — one coverage-guided, one stateful — exercise the pallet's state machine more thoroughly than unit tests alone.

I also wrote E2E tests for the pallet on Westend Asset Hub ([PET#592](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/592)), exercising it against live chain state rather than in isolation.

### `pallet-recovery` review

The revamped `pallet-recovery` ([SDK#10482](https://github.com/paritytech/polkadot-sdk/pull/10482)) handles account inheritance. As part of reviewing the pallet, I wrote E2E tests covering its lifecycle and failure modes ([PET#602](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/602), merged). The tests were run against a WASM override of Westend Asset Hub to exercise the pallet's integration before it lands on production.

### XCM type definitions

The SDK introduced a new `ConcatenatedOpaqueVersionedXcm` variant for double-encoded XCMs ([SDK#9588](https://github.com/paritytech/polkadot-sdk/pull/9588)), but the polkadot-js type definitions were missing it. This caused HRMP message decoding to fail with "Unable to create Enum via index 3" — breaking tooling that parses cross-chain messages. I added the missing variant to the `XcmpMessageFormat` enum ([polkadot-js/api#6255](https://github.com/polkadot-js/api/pull/6255), awaiting review).

### Supporting work

While not directly within the Manifesto's scope, I continued work on Polkadot Ecosystem Tests (PET) and upstream Chopsticks improvements that support my protocol testing efforts:

- Added E2E tests for `pallet-psm` on Westend Asset Hub ([PET#592](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/592)), complementing the SDK-level testing with integration tests against live chain state
- Contributed performance and correctness improvements to Chopsticks ([#1028](https://github.com/AcalaNetwork/chopsticks/pull/1028)) including RPC caching, request coalescing, and a batched dry-run API
- Re-enabled XCM tests broken by the `ConcatenatedOpaqueVersionedXcm` format change ([PET#613](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/613)), which led directly to the polkadot-js/api type fix above

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |No referenda to vote on  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
