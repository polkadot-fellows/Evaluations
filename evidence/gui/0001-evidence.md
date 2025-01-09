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
For context, this is some past work, before the reporting period: 2019-2022:
* Wrote the FRAMEv2 pallet macro. Updating from `decl_module!` to `#[pallet]` macro: https://github.com/paritytech/substrate/pull/6877
* Instantiable pallet concept: https://github.com/paritytech/substrate/pull/1800
* Implemented the elision of pallet parts in construct_runtime: https://github.com/paritytech/substrate/pull/9681
* Implemented counted storage map: https://github.com/paritytech/substrate/pull/9125
* derive `*NoBound` macros: https://github.com/paritytech/substrate/pull/7280
* Iterable storage map without linked list: https://github.com/paritytech/substrate/pull/4185

This is some work for the reporting period:
* FRAME: Fix tasks for instantiable pallets: https://github.com/paritytech/polkadot-sdk/pull/5194
* Improve the precision of benchmarks for system chains, potentially resulting in better resource usage of the system chains. https://github.com/polkadot-fellows/runtimes/pull/525
* Fix implication order for tuple of tuple in transaction extension: https://github.com/paritytech/polkadot-sdk/pull/7028
* Update and fix on storage weight reclaim:
  * fix calculation when underestimating the refund: https://github.com/paritytech/polkadot-sdk/pull/6140
  * update for transaction extension: calculate the proof size including all transaction extensions: https://github.com/paritytech/polkadot-sdk/pull/5273
* Various comments and contribution in the transaction extension PR: https://github.com/paritytech/polkadot-sdk/pull/3685
  * The PR was missing the pipeline for bare extrinsics, so weight wasn't checked nor registered for bare extrinsics: https://github.com/paritytech/polkadot-sdk/pull/3685#discussion_r1794069271
  * Subtle comments like `CheckNonce` prepare was overriding the whole storage item with value coming from validate, potentially erasing other change in the account storage: https://github.com/paritytech/polkadot-sdk/pull/3685#discussion_r1698220569
  * The pipeline was made to allow multiple version of transaction extension but there was no plan to make the version part of any signed payload: https://github.com/paritytech/polkadot-sdk/pull/3685#issuecomment-2400404179
  * Currently implementing the next step of the transaction extension horizon: https://github.com/paritytech/polkadot-sdk/pull/6324



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

- [ ] Question(s): Some people suggested to fast track to rank 2, if people support it, I would be happy to submit the same evidence for an additional promotion. Or give more details if required.

- [ ] Concern(s): 

- [ ] Comment(s): 

