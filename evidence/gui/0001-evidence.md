# Evidence-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/01/09)                                                             |
| **Submitted by**| Guillaume Thiolliere                                                                        |


## Member details

- Matrix username: @guillaume:parity.io
- Polkadot address: 13psJuWEjBuZGaFqXvFnLMC6ME8RVVfQAhtFhydYjW45oKgZ
- Current rank: 0
- Date of initial induction: 2025/01/09
- Date of last report: N/A
- Area(s) of Expertise/Interest:
  - polkadot business-logic (aka the 'runtime')
  - the internals of the frame pallet framework
  - runtime and host APIs


## Reporting period

- Start date: 2024/08/01
- End date: 2025/01/09


## Evidence
Past work before the reporting period:
I contributed to the internals of the frame pallet framework by writing the FRAMEv2 pallet macro (updating from `decl_module!` to `#[pallet]` macro: https://github.com/paritytech/substrate/pull/6877).
I designed and implemented the instantiable pallet concepts (https://github.com/paritytech/substrate/pull/1800), this allows multiple instances of the same pallet in the runtime, bringing greater flexibility to pallets.
I implemented the counted storage map (https://github.com/paritytech/substrate/pull/9125), and the iterable storage map without linked list (https://github.com/paritytech/substrate/pull/4185). Those features ease development of new features in polkadot pallets.

Work for the reporting period:
I fixed tasks for instantiable pallets (https://github.com/paritytech/polkadot-sdk/pull/5194), further enhancing pallets flexibility.

In the substrate runtime primitives I contributed to the transaction extension implementation, this feature allows more flexibility in the runtime and enables us to deliver more features in polkadot system chains:
* I fixed implication order for tuple of tuple in transaction extension (https://github.com/paritytech/polkadot-sdk/pull/7028) making it easier to use the feature.
* I reviewed the PR and identified:
  * the PR was missing the pipeline for bare extrinsics, so weight wasn't checked nor registered for bare extrinsics: https://github.com/paritytech/polkadot-sdk/pull/3685#discussion_r1794069271
  * `CheckNonce` prepare was overriding the whole storage item with value coming from validate, potentially erasing other change in the account storage: https://github.com/paritytech/polkadot-sdk/pull/3685#discussion_r1698220569
  * The pipeline was made to allow multiple version of transaction extension but there was no plan to make the version part of any signed payload: https://github.com/paritytech/polkadot-sdk/pull/3685#issuecomment-2400404179

I also contributed to some cumulus runtime components, on storage weight reclaim:
* I found and fixed a minor bug in the reclaim calculation (https://github.com/paritytech/polkadot-sdk/pull/6140)
* I updated the transaction extension to wrap all transaction extensions, to provide a more accurate reclaim (https://github.com/paritytech/polkadot-sdk/pull/5273), this may improve parachain throughput.

In the polkadot runtime I found out the benchmark configuration was suboptimal, potentially overestimating some weights, and fixed it (https://github.com/polkadot-fellows/runtimes/pull/525).


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

