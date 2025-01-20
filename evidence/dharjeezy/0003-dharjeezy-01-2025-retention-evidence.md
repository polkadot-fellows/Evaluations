# Evidence-0003: Retention at Rank I

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2025/01/13) |
| **Submitted by**| Damilare Akinlose               |


## Member details

- Matrix username: `@dharjeezy/:matrix.org`
- Polkadot address: `12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW`
- Current rank: `1`
- Date of initial induction: `2024-04-29`
- Date of last report: `2024-10-01`
- Area(s) of Expertise/Interest: `FRAME & Runtime`


## Reporting period

- Start date: 2024/10/29
- End date: 2025/01/29


## Evidence
### 1. Work on Full Unbonding in `pallet-staking`

During this reporting period, I completed my work with the [Full Unbonding](https://github.com/paritytech/polkadot-sdk/pull/3811), 
in `pallet-staking` ensuring that the weight is accurately accounted for and sufficiently testing. 

### 2. Work on Try State Hook in `pallet-democracy`

I finalized the implementation of try-state hook invariants for [pallet democracy](https://github.com/paritytech/polkadot-sdk/pull/5879), ensuring that all invariants are properly maintained, 
which enhances the reliability and correctness of tests for the pallet.

### 3. BlockNumberProvider for Pallets Migrating to AssetHub
A deterministic clock is essential for migrating pallets from the Relay Chain to Asset Hub. Implementing a configurable block number simplifies this process by reducing the need for manual block number mapping. 
This ensures a smooth migration of pallet states, free from disruptions or inconsistencies caused by block number differences. 
Prior to these changes, the pallets always use the system block number, all pallets affected by these changes can allow some runtime to opt to use the relay chain block number.
The pallets i worked on are: [pallet referenda](https://github.com/paritytech/polkadot-sdk/pull/6338), [pallet conviction voting](https://github.com/paritytech/polkadot-sdk/pull/6621),
[pallet society](https://github.com/paritytech/polkadot-sdk/pull/6623), and [pallet nomination pool](https://github.com/paritytech/polkadot-sdk/pull/6715)

### 4. Tracing for Logging in Fork aware Transaction Pool

I began exploring the fork-aware transaction pool to understand its functionality in detail. During this process, I identified several outstanding issues requiring attention. 
As a starting point, I focused on updating the logging mechanism for the fork-aware transaction pool, transitioning from the `log` crate to the `tracing` crate. 
The work done can be found [here](https://github.com/paritytech/polkadot-sdk/pull/6897).

### 5. Arc definition in TransactionPool

To optimize the propagation of network transactions, avoiding unnecessary copying or cloning of extrinsic data is crucial.
The proposed solution involves incorporating `Arc` into the transaction function of the `TransactionPool` trait.
This change ensures efficient data sharing while maintaining performance and memory safety.  [TransactionPool trait](https://github.com/paritytech/polkadot-sdk/pull/7042)


### 6. use RuntimeGenesisConfig in genesis config presets

I finalized the implementation to ensure that genesis configuration presets utilize a more appropriate `RuntimeGenesisConfig` definition. 
This was made feasible by updates to certain pallets, which now support the use of the `[#serde(skip)]` annotation in their configurations where it was previously missing.
The completed work can be found [here](https://github.com/polkadot-fellows/runtimes/pull/451). 

I am humbly applying for Rank I retention


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                                                                                                                                                                                 | Comments                                                                        |
|---|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0% voting activity). Out of xx referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus x times (i.e 0% voting agreement). | |
|II |80%   |N/A   |                                                                                                                                                                                                                                                            |                                                                                 |
|III|70%   |100%  |                                                                                                                                                                                                                                                            |                                                                                 |
|IV |60%   |90%   |                                                                                                                                                                                                                                                            |                                                                                 |
|V  |50%   |80%   |                                                                                                                                                                                                                                                            |                                                                                 |
|VI |40%   |70%   |                                                                                                                                                                                                                                                            |                                                                                 |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s): 