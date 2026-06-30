# Argument-0008: Retention at Rank 1

|                 |              |
| --------------- |--------------|
| **Report Date** | 2026/06/30   |
| **Submitted by**| Serban Iorga |


## Member details

- Matrix username: `@serban.iorga:parity.io`
- Polkadot address: `14oHMAJ5btnDCusHrTWraw1wTsLJwZeqPDLxusm1R1Zh3Vxa`
- Current rank: `1`
- Date of initial induction: `2024/04/22`
- Date of last report: `2026/04/02`
- Area(s) of Expertise/Interest:
    - `Bridges`
    - `BEEFY`
    - `MMR`
    - `XCMP/HRMP/DMP`
    - `Omni-Node`
    - `Cumulus Node`
    - `Parachain Authoring`


## Reporting period

- Start date: `2026/04/03`
- End date: `2026/06/30`


## Argument

During this reporting period I have been focusing on the low-latency project: 
https://github.com/orgs/paritytech/projects/259.

One of the key innovations of the low-latency project is the introduction of V3 candidate descriptors with an explicit 
scheduling_parent field, separating the scheduling context (which determines validator group assignment) from the 
execution context (which determines parachain state). V3 candidates can be scheduled based on a different relay chain 
block than the one they execute against, enabling validators to assign backing responsibilities ahead of time 
while maintaining correct execution semantics. Related to this, I worked on PR 
https://github.com/paritytech/polkadot-sdk/pull/10742 that enables collators to build collations using the 
new descriptor format. The PR was started by `eskimor` and also contributed to by `iulianbarbu` and I drove it to 
completion.

Also on the cumulus side, as a follow-up, I opened and merged a couple of PRs that adjusted the logic for selecting 
the parent parachain header that we build on when creating V3 candidates:
- https://github.com/paritytech/polkadot-sdk/pull/12391
- https://github.com/paritytech/polkadot-sdk/pull/12395
- https://github.com/paritytech/polkadot-sdk/pull/12296

I also did some small cleanup related to the cumulus test runtime, in order to make it easier to create more flavors:
https://github.com/paritytech/polkadot-sdk/pull/12231 . This was needed in order to add more test cases for the 
tasks mentioned above.




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

