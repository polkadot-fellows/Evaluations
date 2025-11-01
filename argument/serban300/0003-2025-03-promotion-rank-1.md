# Argument-0003: Promotion to Rank 1

|                 |              |
| --------------- |--------------|
| **Report Date** | 2025/03/28   |
| **Submitted by**| Serban Iorga |


## Member details

- Matrix username: `@serban.iorga:parity.io`
- Polkadot address: `14oHMAJ5btnDCusHrTWraw1wTsLJwZeqPDLxusm1R1Zh3Vxa`
- Current rank: `0`
- Date of initial induction: `2024/04/22`
- Date of last report: `2024/10/02`
- Area(s) of Expertise/Interest:
    - `Bridges`
    - `BEEFY`
    - `MMR`
    - `Omni-Node`
    - `XCMP/HRMP`


## Reporting period

- Start date: `2024/10/03`
- End date: `2025/03/28`


## Argument

I was inducted as rank 1 through [referenda 93](https://collectives.subsquare.io/fellowship/referenda/93) on 
`2024/04/22` but I missed the latest retention deadline. I am submitting this argument looking to regain 
my former rank.

During this reporting period, I have been focusing on multiple areas:

I contributed to the effort to provide a stable test environment for the teams developing the Citizenship app by
upgrading and stabilizing the Bulletin chain and the People to Bulletin bridge.

During the previous reporting period I started working on limiting and optimizing the heap memory usage in Polkadot.
Following up on that work, I iterated on and merged the required [primitives](https://github.com/paritytech/parity-scale-codec/pull/616) 
in `parity-scale-codec` and started integrating them in `polkadot-sdk`. The final work here consist in lazily decoding
and setting a heap memory limit for the `RuntimeCall` and the [PR](https://github.com/paritytech/polkadot-sdk/pull/7902) 
for this is in review.

During the previous periods I have been working on adding support for reporting BEEFY fork equivocations. Following
up on that effort, I finished the last pieces and [enabled the equivocation reporting extrinsic](https://github.com/paritytech/polkadot-sdk/pull/6856).

I started contributing to an effort to optimize and improve the XCMP enqueuing logic, increasing the number of inbound 
messages that can be enqueued in a block from ~300 to >20k through [weight metering improvements](https://github.com/paritytech/polkadot-sdk/pull/7963) 
and [batching](https://github.com/paritytech/polkadot-sdk/pull/8021). I plan to continue working on this in the following period, having multiple options to 
improve this further.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                                                                                                                                                                                   | Comments |
|---|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
|III|70%   |100%  | I have voted on 0 out of 0 referenda in which I was eligible to vote. | -        |
|I  |90%   |N/A   |                                                                                                                                                                                                                                                              |          |
|II |80%   |N/A   |                                                                                                                                                                                                                                                              |          |
|III|70%   |100%  |                                                                                                                                                                                                                                                              |          |
|IV |60%   |90%   |                                                                                                                                                                                                                                                              |          |
|V  |50%   |80%   |                                                                                                                                                                                                                                                              |          |
|VI |40%   |70%   |                                                                                                                                                                                                                                                              |          |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

