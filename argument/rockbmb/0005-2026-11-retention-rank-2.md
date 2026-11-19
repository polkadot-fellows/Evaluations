# Argument-0005: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/11/19                                                                                  |
| **Submitted by**| rockbmb                                                                                     |
| **Sponsored by**| Bryan Chen (xlc)                                                                            |


## Member details

- Matrix username: @alexandre.balde@parity.io
- Polkadot address: 13jBAtYJar4xujPaEx41FxjSt9PqU7LqJRbySJiVdMtuWN42
- Current rank: 2
- Date of initial induction: [2025-10-28](https://collectives.statescan.io/#/extrinsics/7473060-2)
- Date of last report: 2026-07-13
- Link to last report: [Argument-0004](https://github.com/polkadot-fellows/Evaluations/blob/main/argument/rockbmb/0004-2026-07-promotion-rank-2.md)
- [Subsystems](../../subsystems.md) developed/maintained: Runtimes (Engineering, Security, Benchmarking); System chains


## Reporting period

- Start date: 2026/07/14
- End date: 2026/11/19


## Argument

I request retention at Rank II. My area is the correctness of SDK pallets and of the Fellowship runtimes: the code that holds user funds and executes what governance approves.

I spent most of this period on security findings, from the security working group's private repositories and from the bug bounty programme. The method is constant: reproduce the report, then fix it with a regression test, or refute it with the test or commit that proves it wrong. Either way, the verdict becomes a test that runs from then on, and the same question does not return to triage. The reports stay private; the fixes and tests below are public, grouped by what each defect threatened.

### Governance liveness

Referenda and the scheduler enact every other decision. When they misbehave, approved decisions do not execute, and no mechanism other than governance itself can recover them.

- `pallet-referenda` never removed the `TrackQueue` entry of a cancelled or killed referendum ([#13236](https://github.com/paritytech/polkadot-sdk/pull/13236), awaiting review).
- `pallet-referenda` could leave a referendum with `in_queue` set but no queue entry. An external contributor fixed one of the two paths that create this state; I took the PR over and fixed the other ([#12451](https://github.com/paritytech/polkadot-sdk/pull/12451), awaiting review).
- `pallet-scheduler` lets ordinary referendum submissions fill a block's agenda, and a passing referendum then misses its enactment slot. I reserved agenda capacity for governance tasks ([#12854](https://github.com/paritytech/polkadot-sdk/pull/12854), under review).
- An E2E test now covers the `DecidingCount` accounting that the queue fixes touch ([PET#684](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/684), merged).

### Permission boundaries

Proxies are the main tool for limiting what a delegate can do with an account, so the proxy type hierarchy must match the call filters exactly.

- The relay runtimes' `is_superset` lists `NonTransfer` as a superset of `Auction`, but the `NonTransfer` call filter blocks a call that the `Auction` filter allows. I fixed the hierarchy and added property tests on both relays that compare every superset relation against the filters ([runtimes#1281](https://github.com/polkadot-fellows/runtimes/pull/1281), merged).
- A reported proxy privilege escalation on the Asset Hubs was false. The refutation is now a PET suite that covers `add_proxy` across all proxy type pairs ([PET#691](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/691), merged).

### Fund accounting

- `pallet-vesting` locked the maximum of an account's genesis schedules instead of their sum ([#13016](https://github.com/paritytech/polkadot-sdk/pull/13016), merged).
- `pallet-broker` wrote a revenue claim's storage changes even when the claim's transfer failed ([#13040](https://github.com/paritytech/polkadot-sdk/pull/13040), merged).
- `pallet-psm` set its admin origins at creation and never updated them, so the previous owner of a transferred asset kept control of its PSM. A new `pallet-assets` owner-change callback updates them ([#13171](https://github.com/paritytech/polkadot-sdk/pull/13171), under review).

### Verification before deployment

Finding defects after deployment is the expensive order. The same methods, applied at review time, find them before enactment. `pallet-psm` mints the dotUSD stablecoin against collateral and is now live on Asset Hub; it is the pallet where I apply every layer:

- Runtime invariants, checked on every upgrade: merged for `pallet-psm` ([#12154](https://github.com/paritytech/polkadot-sdk/pull/12154)) and `pallet-recovery` ([#12490](https://github.com/paritytech/polkadot-sdk/pull/12490)).
- Coverage-guided and stateful fuzzers, with a CI smoke job ([#12155](https://github.com/paritytech/polkadot-sdk/pull/12155), awaiting review).
- Quint state-machine models, with a harness that tests the pallet against them ([#13291](https://github.com/paritytech/polkadot-sdk/pull/13291), [#13292](https://github.com/paritytech/polkadot-sdk/pull/13292), awaiting review). I used one of the model invariants to settle a triage verdict on a fee-accounting report this period: the models answer questions beyond the review they were written for.
- The PET E2E suite, rewritten for the pallet's multi-instance form ([PET#694](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/694), merged).

### Release validation

I maintain PET, which runs all of the above E2E suites against every Fellowship release, and I triage its results when a release is cut. This period that covered runtimes 2.4 ([PET#683](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/683), merged) and 2.5.1/2.5.2 ([PET#711](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/711), [PET#719](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/719), [PET#720](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/720), merged), plus new suites for Fellowship referenda with real whitelisting ([PET#663](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/663), merged) and for upgrades during relay cooldown windows ([PET#666](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/666), merged). I reviewed other contributors' governance suites ([PET#595](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/595), [PET#670](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/670)).

The three sections are one responsibility at three points in time: review, before a defect merges; release, before it deploys; and findings triage, after a report arrives. The last is the on-call availability that the Manifesto's Section 6 asks of Rank II for the areas a member knows deeply.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |No eligible referenda  |
|II |80%   |N/A   |0 of 0 (100%)   |No referenda on tracks open to Rank II during the period  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
