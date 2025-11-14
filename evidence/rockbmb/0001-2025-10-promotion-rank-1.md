# Argument-0001: Promotion to Rank I Dan

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (YYYY-MM-DD)                                                             |
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
- End date: 2024-11-15


## Argument

I have been working on Polkadot continuously since September 2024.

During this time, as mentioned in my [request for induction](https://collectives.subsquare.io/fellowship/applications/8),
I have focused mainly on testing protocol components of the Polkadot SDK, such as pallets, runtimes and networks, through
the Polkadot Ecosystem Tests project.

For promotion to I Dan, the Manifesto states as a requirement:

> Three clear examples of a modest but substantial contribution to protocol development

Below, I list these, and explain why they are sufficient for I Dan.

### AHM Testing

About I Dan, the Manifesto also states that:

> being available and playing a crucial operational role for a network fix

is expected of an individual seeking I Dan.

I assisted with the testing process for the Asset Hub Migration in the Westened and Paseo testnets, and in the Kusama
and Polkadot networks.
During the run-up to the migration, the tests I wrote as part of PET were used to validate the functionality of relay
chain/asset hub runtimes.

Furthermore, at the moment of the Kusama (Oct 7th)/Polkadot (Nov 4th) migrations, these PET tests were part of larger
manual + automated testing processes to validate the migration's result.



### General Runtime Testing

### EIP-150 compliance in `pallet-revive` gas-metering

Under the supervision of Fellowship Member [Alex](https://collectives.subsquare.io/user/15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1/fellowship), I worked on implementing [EIP-150](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-150.md) in `pallet-revive`'s gas metering.
Ultimately, the [conclusion](https://github.com/paritytech/polkadot-sdk/pull/6890#issuecomment-2582594003) was that it was not possible at the time, as it removed the possibility of dry-running a
contract call's execution -  this is essential to estimating the computational cost in Polkadot-native units (ref time/proof size).


*Explain why your contributions in relation to Polkadot are worthy of retention/promotion. Refer to the terms in Section 6 of the [Manifesto](https://github.com/polkadot-fellows/manifesto/blob/main/manifesto.pdf) and provide links to relevant content (e.g. code, articles, media, etc.) to show that you are meeting all the requirements.*

## Voting record

N/A

## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

### Acknowledgements

Thanks to [seadanda](https://collectives.subsquare.io/user/142zGifFwRrDbFLJD7LvbyoHQAqDaXeHjkxJbUVwmDYBD7Gf/fellowship), [Oliver](https://collectives.subsquare.io/user/16a357f5Sxab3V2ne4emGQvqJaCLeYpTMx3TCjnQhmJQ71DX/fellowship), [muharem](https://collectives.subsquare.io/user/12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2/fellowship), [kianenigma](https://collectives.subsquare.io/user/1eTPAR2TuqLyidmPT9rMmuycHVm9s9czu78sePqg2KHMDrE/fellowship), [Alex](https://collectives.subsquare.io/user/15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1/fellowship) for all the assistance with my work in the Polkadot SDK, and [Bryan Chen](https://collectives.subsquare.io/user/14DsLzVyTUTDMm2eP3czwPbH53KgqnQRp3CJJZS9GR7yxGDP/fellowship) for reviewing all of my PET/Chopsticks contributions.