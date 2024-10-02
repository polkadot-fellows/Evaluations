# Evidence-0002: Retention at Rank 1

|                 |              |
| --------------- |--------------|
| **Report Date** | 2024/10/02   |
| **Submitted by**| Serban Iorga |


## Member details

- Matrix username: `@serban.iorga:parity.io`
- Polkadot address: `14oHMAJ5btnDCusHrTWraw1wTsLJwZeqPDLxusm1R1Zh3Vxa`
- Current rank: `1`
- Date of initial induction: `2024/03/12`
- Date of last report: `2024/07/03`
- Area(s) of Expertise/Interest: 
  - `Bridges`
  - `BEEFY`
  - `MMR`
  - `Omni-Node`


## Reporting period

- Start date: 2024/07/04
- End date: 2024/10/02


## Evidence

In the current reporting period, my main contributions have been related to Omni-Node and `parity-scale-codec`.

### Omni-Node

I worked on separating the generic logic from `polkadot-parachain-bin` in a library (`polkadot-parachain-lib`): 
https://github.com/paritytech/polkadot-sdk/pull/5288 . This enables the parachain teams to build their own slightly 
customized node, without duplicating the code in `polkadot-parachain-bin`.

I have added support for starting nodes with `u64` block number in `polkadot-parachain-lib`: 
https://github.com/paritytech/polkadot-sdk/pull/5269 . This was needed in order to support a parachain use case:
https://github.com/paritytech/polkadot-sdk/issues/4787 .

I have added support for starting a node with manual seal to `polkadot-parachain-lib`: 
https://github.com/paritytech/polkadot-sdk/pull/5586 . This is aimed at improving parachain development/debugging speed.

### parity-scale-codec

I worked on adding support for tracking and limiting the heap memory usage while decoding: 
https://github.com/paritytech/parity-scale-codec/pull/616 .

### Other

I added benchmarks for the BEEFY forking equivocation logic: https://github.com/paritytech/polkadot-sdk/pull/5188 .

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 1 referenda in which I was eligible to vote (0% voting activity). |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s): 

