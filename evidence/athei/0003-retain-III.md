# Evidence-0003: Retention at Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/11/05)                                                             |
| **Submitted by**| Alexander Theißen                                                                           |

## Member details

- Matrix username: @alex:parity.io
- Polkadot address: 15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1
- Current rank: III
- Date of initial induction: Seeding
- Date of last report: 2025/03/12
- Area(s) of Expertise/Interest: System Chain Pallets (Smart Contracts), PolkaVM, Virtual Machines, Host Functions

## Reporting period

- Start date: 2025/03/15
- End date: 2025/09/15

## Argument

In this reporting period, I continue being focused on getting `pallet_revive` and its supporting software ready
to be deployed on Polkadot. In addition to the gas mapping and pre-compile SDK this mainly consisted of removing
remaining incompatablities to Ethereum. I also spent a substantial amount of time coaching and onboarding new hires
through in-depth code reviews and github issues.

### API & Code Design

In this section, I list only major design work. I also implemented those designs.

#### Precompile SDK for `pallet_revive`

So far `pallet_revive` did not possess the ability to be extended with custom pre-compiles. Those are
required to expose Polkadot specific functionality to contracts.

I designed a set of traits that allow downstream code to extend `pallet_revive` with additional APIs. In addition to some
pallet internal pre-compiles `pallet_assets` and `pallet_xcm` make use of this functionality.
Those pre-compiles were implemented by other developers without much difficulty suggesting a solid design.

PR: [Replace adhoc pre-compiles with pre-compile framework](https://github.com/paritytech/polkadot-sdk/pull/8262)

#### Define how Ethereum gas is mapped to Polkadot Weight

In order to process Ethereum transaction we need to deal with the fact that they only contain a single one dimensional `gas_limit`
to set the maximum allowed resource consumption of a transaction.

We need to map this to our multi dimensional resource model `(ref_time, proof_size, storage_deposit)`. Especially the storage deposit
is complicated as it does not represent a transaction fee. The design needed to balance resource consumption soundness, safety and compatability.

The design we came up with (co-authored by Torsten Stueber) improves over existing schemes (Frontier, Accala) by making different tradeoffs. But also
by being more complicated and hence more difficult to get implement.

[High Level Design Doc](https://hackmd.io/@athei/HyHQEkFJWg)

[Addendum describing required changes to transaction payments](https://hackmd.io/@athei/Sk88_m3qlg)

[Formalisation by Torsten Stueber](https://shade-verse-e97.notion.site/Gas-Mapping-Challenges-Revised-26c8532a7ab580db8222c2ce3023669e)

[First PR implementing changes to pallet_transaction_payment](https://github.com/paritytech/polkadot-sdk/pull/9780)

[Second PR implementing the actual mapping in pallet_revive](https://github.com/paritytech/polkadot-sdk/pull/9803)

#### Raising the maximum contract size and stack depth

The maximum (PVM) contract size and call stack depth was severily limited due to memory limitations of the runtime.

I defined the requirements (but not implemented) for a new instruction caching behavior in PolkaVM and used that
to proof that higher limits are possible and safe. I encoded the proof/check into `revive::integrity_test` and raised the
limits.

PR: [Raise contract size limit to one megabyte and raise call depth to 25](https://github.com/paritytech/polkadot-sdk/pull/9267)

### Code Contributions

In addition to my larger design heavy contributions I also list some other noteable work.

#### Adding a new signature type to Polkadot

In order to allow wallets to sign Polkadot extrinsics (as opposed to Eth transactions) with an Ethereum style key pair
I added a new signature type. We already allowed this before but the address derivation did not produce the address expected
by Ethereum tooling.

PR: [Allow sending transactions from an Ethereum address derived account id](https://github.com/paritytech/polkadot-sdk/pull/8757)

#### Releasing `pallet_revive` on Kusama

I bumped the fellowship runtimes to the latest SDK, added `pallet_revive` and created the release.

### Social Interaction

This period my interactions mostly consisted of coaching or on on-boarding co-workers. At lot more people
got involved with contracts this reporting period. This took a fair shair of my attention. Time well spent.

After this crunch I intent to focus more on external contributions to support users and spread knowldge
beyond Parity.

## Voting Record

Please keep in mind that, in the absence of better tooling, I derived these numbers by manually inspecting Subsquare.
I used the [slider on subsquare](https://collectives.subsquare.io/user/15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1/fellowship)
to filter for the timespan between referendum #296 and #392.


|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|--------|---------------------|----------------------|----------------------------|----------|
|   III  |        70%          |         100%         |             ~94%           |          |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
