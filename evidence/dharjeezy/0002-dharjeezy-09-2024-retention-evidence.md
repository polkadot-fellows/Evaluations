# Evidence-0002: Retention at Rank I

|                 |                                |
| --------------- |--------------------------------|
| **Report Date** | Date of submission (2024/10/1) |
| **Submitted by**| Damilare Akinlose              |


## Member details

- Matrix username: `@dharjeezy/:matrix.org`
- Polkadot address: `12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW`
- Current rank: `1`
- Date of initial induction: `2024-04-29`
- Date of last report: `2024-07-01`
- Area(s) of Expertise/Interest: `FRAME & Runtime`


## Reporting period

- Start date: 2024/07/29
- End date: 2024/10/29


## Evidence
I discussed about how to ensure that pallet MQ message processing is transactional and I also implemented the enforcement of transactional processing to [Pallet MQ message processing](https://github.com/paritytech/polkadot-sdk/pull/5198).

I also had to refactor what I did before when I introduced a new extrinsic for full unbonding in pallet staking, but it was later advised that instead of introducing a new extrinsic, it will make sense
to actually support chilling first when a user calls unbond to unbond all amount staked. You can find details of the implementation [here](https://github.com/paritytech/polkadot-sdk/pull/3811).

I added a new invariant [try state check](https://github.com/paritytech/polkadot-sdk/pull/5465) in the nomination-pools pallet for checking that a pool's point can never be lower than the stake in the same pool.

I implemented a different way of constructing [genesis config values](https://github.com/polkadot-fellows/runtimes/pull/451) for all runtimes, how it was previously done is by using json, this newer implementation made use of
the `RuntimeGenesisConfig` instead.

I also included [events to be emitted](https://github.com/paritytech/polkadot-sdk/pull/4613) for voting and removal of vote in conviction pallet.

I also worked on invariants try state checks for the [membership pallet](https://github.com/paritytech/polkadot-sdk/pull/5850).

I am currently working on adding various invariant [try state checks for the democracy pallet](https://github.com/paritytech/polkadot-sdk/pull/5879).

I believe my contributions to the Polkadot ecosystem this past reporting period has been vital and are in cognisance to what the Technical Fellowship upholds for a Rank I member. 
I am also thankful and grateful to the insights and counsel given me by the higher ranks and co-rank member of the Fellowship which has enabled me to be active and being a member of the Fellowship.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                       | Comments                                                                        |
|---|---|---|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
|I  |90%   |N/A   | I have voted on 0 out of 2 referenda, during this period, I really did not pay attention to them | I'd do better on looking out for proposals under my track and vote accordingly. |
|II |80%   |N/A   |                                                                                                  |                                                                                 |
|III|70%   |100%  |                                                                                                  |                                                                                 |
|IV |60%   |90%   |                                                                                                  |                                                                                 |
|V  |50%   |80%   |                                                                                                  |                                                                                 |
|VI |40%   |70%   |                                                                                                  |                                                                                 |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s): 