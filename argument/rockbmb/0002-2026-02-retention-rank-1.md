# Argument-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026-02-13                                                                                  |
| **Submitted by**| rockbmb                                                                                     |


## Member details

- Matrix username: @alexandre.balde@parity.io
- Polkadot address: 13jBAtYJar4xujPaEx41FxjSt9PqU7LqJRbySJiVdMtuWN42
- Current rank: 1
- Date of initial induction: [2025-10-28](https://collectives.statescan.io/#/extrinsics/7473060-2)
- Date of last report: 2025-11-19
- Area(s) of Expertise/Interest: System Parachains, Polkadot Runtime


## Reporting period

- Start date: 2025-12-01
- End date: 2026-02-28


## Evidence

During this reporting period I continued my work on testing Polkadot protocol components through the Polkadot Ecosystem Tests (PET) project, while also contributing directly to the Polkadot SDK and the Fellowship runtimes CI infrastructure.

### Polkadot SDK contributions

I contributed improvements to pallet testing and SDK maintenance:

1. Contributions to the scheduler pallet: added some clarifying comments to calls in the scheduler pallet, `Lookup<T>` checks in unit tests, and a missing test verifying rescheduling of a task to a full block ([#10511](https://github.com/paritytech/polkadot-sdk/pull/10511), merged).
2. Added tests for `SenderInSignatories`/`SignatoriesOutOfOrder` error cases in `pallet-multisig` and clarifying notes to `approve_as_multi`/`as_multi` comments ([#10843](https://github.com/paritytech/polkadot-sdk/pull/10843), merged). This was a follow-up from PET end-to-end testing ([PET#305](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/305), [PET#323](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/323)).
3. Reworked the remote externality child key retrieval test, which was failing since the proxy pallet has no child storages ([#10866](https://github.com/paritytech/polkadot-sdk/pull/10866), merged).

### PET CI infrastructure improvements

I worked to improve the reliability and performance of PET in its own repository, and in the Fellowship runtimes repository's CI pipeline, where it can resume its function as a regression testing tool across Polkadot and Kusama networks:

1. Reworked CI to use Chopsticks servers as RPC caches to avoid timeouts caused by throttling/stalling from production RPC endpoints ([PET#504](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/504), merged). This addressed a recurring pain point where CI runs would fail due to network-level issues rather than actual test failures (tracking issue [PET#506](https://github.com/open-web3-stack/polkadot-ecosystem-tests/issues/506)).
2. Follow-up refactoring to the Chopsticks caching approach to instead use [Subway](https://github.com/AcalaNetwork/subway) (thanks @xlc) as the RPC proxy/cache ([PET#519](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/519), awaiting review).
3. Reworked the `test.yml` workflow in the Fellowship runtimes CI to use a test matrix with individual retry/timeout configurations, Subway-based RPC caching, and filtering to only run end-to-end suites for runtimes under the Fellowship's purview ([runtimes#1068](https://github.com/polkadot-fellows/runtimes/pull/1068), awaiting review). This closes [runtimes#1010](https://github.com/polkadot-fellows/runtimes/issues/1010).

### PET test coverage expansion

1. Fixed an issue where the scheduler pallet would ignore calls scheduled manually via `dev_setStorage` because `incompleteSince` was not being set ([PET#515](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/515), merged) — this was a subtle interaction between Chopsticks' storage injection and the scheduler's `service_agendas` scanning logic, which eliminates one common cause of spuriously failing tests.
    - This was minor, but in conjunction with the previous point, it should greatly improve overall reliability of PET in `runtimes`' CI.

## Voting record

N/A