# Argument-0007: Retention at Rank 1

|                 |              |
| --------------- |--------------|
| **Report Date** | 2026/04/02   |
| **Submitted by**| Serban Iorga |


## Member details

- Matrix username: `@serban.iorga:parity.io`
- Polkadot address: `14oHMAJ5btnDCusHrTWraw1wTsLJwZeqPDLxusm1R1Zh3Vxa`
- Current rank: `1`
- Date of initial induction: `2024/04/22`
- Date of last report: `2026/01/05`
- Area(s) of Expertise/Interest:
    - `Bridges`
    - `BEEFY`
    - `MMR`
    - `Omni-Node`
    - `XCMP/HRMP/DMP`


## Reporting period

- Start date: `2026/01/06`
- End date: `2026/04/02`


## Argument

During this reporting period I have been focusing on multiple areas.

During one of the previous reporting periods I added support for 
[receiving double encoded XCMs through XCMP](https://github.com/paritytech/polkadot-sdk/pull/9588). This strategy makes 
the XCMP pages decoding much easier and almost free, improving the XCMP bandwidth. However, this new format was 
not used yet, since we didn't have any way to know which parachains support it.
During the current reporting period I came out with a roll-out plan. Specifically, I implemented a negotiation 
strategy between parachains in order to switch to using double encoded XCMs when supported: 
https://github.com/paritytech/polkadot-sdk/pull/11263 .

During the previous reporting periods I have been working on limiting and optimizing the heap memory usage in Polkadot.
During the current reporting period I continued that work, by opening a 
[PR](https://github.com/paritytech/polkadot-sdk/pull/11147) that tackles the last opened issue related to this, 
namely tracking and limiting the nested memory used by XCM Transact instructions. The PR hasn't been merged yet, but 
the initial feedback related to the direction of the solution has been positive.

Also, I contributed with a [small refactoring related to BEEFY](https://github.com/paritytech/polkadot-sdk/pull/10763)
that helped an open source customer that was looking to use BEEFY with other crypto types and hashing algorithms.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                                                                                                                                                                                  | Comments |
|---|---------------------|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
|I  | 90%                 |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote. | -        |                                                                                                                                                                                                                                                            |          |
|II | 80%                 |N/A   |                                                                                                                                                                                                                                                             |          |
|III| 70%                 |100%  |                                                                                                                                                                                                                                                             |          |
|IV | 60%                 |90%   |                                                                                                                                                                                                                                                             |          |
|V  | 50%                 |80%   |                                                                                                                                                                                                                                                             |          |
|VI | 40%                 |70%   |                                                                                                                                                                                                                                                             |          |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s): 

