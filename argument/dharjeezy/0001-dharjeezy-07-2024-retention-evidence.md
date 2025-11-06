# Evidence-0001: Retention at Rank I

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2024/01/07) |
| **Submitted by**| Damilare Akinlose               |


## Member details

- Matrix username: @dharjeezy/:matrix.org
- Polkadot address: 12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW
- Current rank: I
- Date of initial induction: 2024-04-29
- Date of last report: N/A
- Area(s) of Expertise/Interest: Substrate Runtime


## Reporting period

- Start date: 2024-04-29
- End date: 2024-07-29


## Evidence

I would like to share the tasks I believe are relevant to the Polkadot Fellowship Program.

## Code Contributions

### Feature

- **Description:** Full Unbond in Staking
  - **PR:** [Full Unbond in Staking](https://github.com/paritytech/polkadot-sdk/pull/3811)

Worked on implementing full unbond in staking, this involves creating an extrinsic to fully unbond 
a validator or nominator by first chilling the validator or nominator first before proceeding to fully
unbond.

- **Description:** Try State Hook for Bounties
  - **PR:** [Try State Hook for Bounties](https://github.com/paritytech/polkadot-sdk/pull/4563)

Implemented the try state hook for the Bounties pallet for Invariant checks.

### Maintainance

- **Description:** Download KeyValues in remote externalities early
  - **PR:** [Download KeyValues in remote externalities early](https://github.com/paritytech/polkadot-sdk/pull/3584)

Working on improving how we download key values in remote externalities by ensuring it is faster 
and with less overhead.

- **Description:** Include events for voting
  - **PR:** [include events for voting](https://github.com/paritytech/polkadot-sdk/pull/4613)

Introduce emission of events for when a vote is enacted and when a vote is removed in the
conviction voting pallet.


### Fellowship Runtime

- **Description:** Explicit default for testnet HostConfiguration
  - **PR:** [Explicit default for testnet HostConfiguration](https://github.com/polkadot-fellows/runtimes/pull/368)

Include configuration properties that are hidden by explicitly defining them in the Host Configuration.
