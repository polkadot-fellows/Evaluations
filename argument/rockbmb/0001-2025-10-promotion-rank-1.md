# Argument-0001: Promotion to I Dan

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025-11-19)                                                             |
| **Submitted by**| rockbmb                                                                                     |


## Member details

- Matrix username: @alexandre.balde@parity.io
- Polkadot address: 13jBAtYJar4xujPaEx41FxjSt9PqU7LqJRbySJiVdMtuWN42
- Current rank: Candidate
- Date of initial induction: [2025-10-28](https://collectives.statescan.io/#/extrinsics/7473060-2)
- Date of last report: N/A
- Area(s) of Expertise/Interest: System Parachains, Polkadot Runtime


## Reporting period

- Start date: 2024-09-01
- End date: 2025-11-15


## Argument

I have been working on Polkadot continuously since September 2024.

During this time, as mentioned in my [request for induction](https://collectives.subsquare.io/fellowship/applications/8),
I have focused mainly on testing protocol components of the Polkadot SDK, such as pallets, runtimes and networks, through
the Polkadot Ecosystem Tests (PET) project.

For promotion to I Dan, §6.2.1. of the Manifesto states as a requirement:

> Three clear examples of a modest but substantial contribution to protocol development

Below, I list these, and explain why they are sufficient for I Dan.

### AHM Testing

About I Dan, §6.2.1. of the Manifesto states another expectation:

> being available and playing a crucial operational role for a network fix

I assisted with the testing process for the Asset Hub Migration in the Westened and Paseo testnets, and in the Kusama
and Polkadot networks.
During the run-up to the migration, the tests I wrote as part of PET were used to validate the functionality of relay
chain/asset hub runtimes (and other runtimes, too).

Furthermore, upon the Kusama (Oct 7th)/Polkadot (Nov 4th) migrations, these PET tests were part of larger
manual + automated (CI) testing processes to validate the migration's result, validation which was provided in real-time.
For more, see the [`ahm-dryrun`](https://github.com/paritytech/ahm-dryrun?tab=readme-ov-file#e2e-tests) project, where
PET was used in AHM dry-runs to validate relay/AH runtimes.

Some examples of findings (Polkadot SDK/Fellowship Runtimes):
1. [Issue](https://github.com/paritytech/polkadot-sdk/issues/9986) with burning funds in post-migration relay chains
2. [Issue](https://github.com/polkadot-fellows/runtimes/pull/740) with missing call filters for some relay chain proxy types
3. [Issue](https://github.com/paritytech/polkadot-sdk/issues/8056) regarding pure proxies

### General Runtime Testing

As part of the previous point, but also as its own endeavour, I used PET to test protocol components of the
Kusama/Polkadot networks.
An extensive (but not exhaustive) list of pallets/components tested can be found [here](https://github.com/paritytech/ahm-dryrun?tab=readme-ov-file#e2e-tests).

From this came some contributions to the Polkadot SDK:
1. Added event emission to some pallets' extrinsics ([identity](https://github.com/paritytech/polkadot-sdk/pull/6261), [vesting](https://github.com/paritytech/polkadot-sdk/pull/8171), [proxy](https://github.com/paritytech/polkadot-sdk/pull/7995), [conviction voting](https://github.com/paritytech/polkadot-sdk/pull/6544), [nomination pools](https://github.com/paritytech/polkadot-sdk/pull/7377))
2. Improved unit tests in some pallets (e.g. [vesting](https://github.com/paritytech/polkadot-sdk/pull/8171/files), [staking](https://github.com/paritytech/polkadot-sdk/pull/7553))
3. As a follow-up to the liquidity restriction issue (issue opened by Fellowship member [RomarQ](https://collectives.subsquare.io/user/12fiMKJP9t3gTFpHEXGYtdbZzwQciCpUcVFRnVXU4JYQLWvA/fellowship)), I created a multi-network regression [suite](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/377) engineered to fail on (combinations of) this problem, giving visibility into which networks are still affected. It can be run against any runtime in which this error occurs (i.e. ones combining pallets using `Currency` traits and others using `Fungible`), and once the runtime consumes the upstream fix, the suite can be switched to ensure compliance

### EIP-150 compliance in `pallet-revive` gas-metering

Under the supervision of Fellowship Member [Alex](https://collectives.subsquare.io/user/15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1/fellowship), I worked on implementing [EIP-150](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-150.md) in `pallet-revive`'s gas metering.

### Short note about EIP-150

EIP-150 enforces an artificial stack depth limit to contract calls by limiting the gas available to a child call to
`63/64`ths of the parent's available gas at the time of the call.

Otherwise, the call limit would be 1024. At 1023 calls, subsequent attempts to increase the call stack would silently
fail, *but* continue contract execution, which opens a class of call depth attacks (e.g. maliciously call something 1023
times before a certain call).

With EIP-150, there'd be an (inversely) exponential decay in the amount of gas available: no gas -> contract call fails
and changes would be reverted.

---

Ultimately, the [conclusion](https://github.com/paritytech/polkadot-sdk/pull/6890#issuecomment-2582594003) was that it
was not possible at the time, as it removed the possibility of dry-running a contract call's execution -  this is
essential to estimating the computational cost in Polkadot-native weight (ref time/proof size).

Not being able to implement it in a straightforward way means that 1-to-1 parity with the EVM execution model will
require an alternative gas metering solution than the one I attempted.

## Voting record

N/A

## Acknowledgements

Thanks to [seadanda](https://collectives.subsquare.io/user/142zGifFwRrDbFLJD7LvbyoHQAqDaXeHjkxJbUVwmDYBD7Gf/fellowship), [Oliver](https://collectives.subsquare.io/user/16a357f5Sxab3V2ne4emGQvqJaCLeYpTMx3TCjnQhmJQ71DX/fellowship), [muharem](https://collectives.subsquare.io/user/12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2/fellowship), [Ankan](https://collectives.subsquare.io/user/16aQgRVKfD22NehdzZD2VPoenP2hvx8RS2gUirfk6abiCies/fellowship), [kianenigma](https://collectives.subsquare.io/user/1eTPAR2TuqLyidmPT9rMmuycHVm9s9czu78sePqg2KHMDrE/fellowship), [Alex](https://collectives.subsquare.io/user/15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1/fellowship) for all the assistance with my work in the Polkadot SDK, and [Bryan Chen](https://collectives.subsquare.io/user/14DsLzVyTUTDMm2eP3czwPbH53KgqnQRp3CJJZS9GR7yxGDP/fellowship) for reviewing all of my PET/Chopsticks contributions.