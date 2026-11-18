# Argument-0005: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026-11-12                                                                                  |
| **Submitted by**| rockbmb                                                                                     |


## Member details

- Matrix username: @alexandre.balde@parity.io
- Polkadot address: 13jBAtYJar4xujPaEx41FxjSt9PqU7LqJRbySJiVdMtuWN42
- Current rank: 2
- Date of initial induction: [2025-10-28](https://collectives.statescan.io/#/extrinsics/7473060-2)
- Date of last report: 2026-07-13
- Area(s) of Expertise/Interest: System Parachains, Polkadot Runtime, testing and security


## Reporting period

- Start date: 2026-07-14
- End date: 2026-11-12


## Evidence

I spent most of this period on security findings against the SDK and the Fellowship runtimes, from the security working group's private repositories and from the bug bounty programme. This included fixing some of the real reports, validating some as false positives, and appropriately closing them.
The remainder was the `pallet-psm` verification work from my last report, and PET maintenance.

### Security findings: triage and fixes

The reports are in the working group's private repositories; the fixes are public.

In the Fellowship runtimes, `is_superset` lists `NonTransfer` as a superset of `Auction`, but the `NonTransfer` call filter blocks a call that the `Auction` filter allows. I fixed the lattice and added property tests on both relays that check every superset relation against the filters ([runtimes#1281](https://github.com/polkadot-fellows/runtimes/pull/1281), merged).

In the SDK:

- `pallet-vesting`: at genesis, the pallet locked the maximum of an account's schedules instead of their sum ([#13016](https://github.com/paritytech/polkadot-sdk/pull/13016), merged).
- `pallet-broker`: when the transfer inside a revenue claim failed, the pallet still wrote the claim's other storage changes ([#13040](https://github.com/paritytech/polkadot-sdk/pull/13040), merged).
- `pallet-referenda`: the `TrackQueue` entry of a cancelled or killed referendum was never removed ([#13236](https://github.com/paritytech/polkadot-sdk/pull/13236), awaiting review).
- `pallet-referenda`: a referendum could be left with `in_queue` set but no queue entry. An external contributor fixed one of the two paths that create this state; I took the PR over and fixed the other ([#12451](https://github.com/paritytech/polkadot-sdk/pull/12451), awaiting review).
- `pallet-scheduler`: ordinary referendum submissions can fill a block's agenda, and a passing referendum then misses its enactment slot. I reserved agenda capacity for governance tasks ([#12854](https://github.com/paritytech/polkadot-sdk/pull/12854), under review).
- `pallet-psm`: the pallet set its admin origin at creation and never updated it, so the previous owner of a transferred asset kept PSM control. A new `pallet-assets` owner-change callback now updates it ([#13171](https://github.com/paritytech/polkadot-sdk/pull/13171), under review).

Two reports were refuted with tests: a proxy privilege escalation on the Asset Hubs ([PET#691](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/691), merged) and a `DecidingCount` accounting question ([PET#684](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/684), merged).

### Pallet verification

`pallet-psm` is now live on Asset Hub. This period:

- `do_try_state` expansion merged ([#12154](https://github.com/paritytech/polkadot-sdk/pull/12154)); same for `pallet-recovery` ([#12490](https://github.com/paritytech/polkadot-sdk/pull/12490)).
- libFuzzer and stateful fuzzer harnesses ([#12155](https://github.com/paritytech/polkadot-sdk/pull/12155), awaiting review).
- Quint models and a model-testing harness ([#13291](https://github.com/paritytech/polkadot-sdk/pull/13291), [#13292](https://github.com/paritytech/polkadot-sdk/pull/13292), awaiting review). I used one of the model invariants to settle a triage verdict this period.
- PET E2E suite rewritten for the multi-instance pallet ([PET#694](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/694), merged).

### Release validation and PET maintenance

I maintain PET and ran it against runtimes 2.4 and 2.5.1/2.5.2 ([PET#683](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/683), [PET#711](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/711), [PET#719](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/719), [PET#720](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/720), merged). New this period: a Fellowship referenda suite with real whitelisting ([PET#663](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/663), merged) and upgrade-test handling of relay upgrade cooldowns ([PET#666](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/666), merged). I reviewed other contributors' governance suites ([PET#595](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/595), [PET#670](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/670)).


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |No referenda to vote on  |
|II |80%   |N/A   |N/A   |No referenda on tracks open to Rank II during the period  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
