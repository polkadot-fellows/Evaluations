# Argument-0004: Retention at Rank 1

|                 |              |
| --------------- |--------------|
| **Report Date** | 2025/07/07   |
| **Submitted by**| Serban Iorga |


## Member details

- Matrix username: `@serban.iorga:parity.io`
- Polkadot address: `14oHMAJ5btnDCusHrTWraw1wTsLJwZeqPDLxusm1R1Zh3Vxa`
- Current rank: `1`
- Date of initial induction: `2024/04/22`
- Date of last report: `2025/03/28`
- Area(s) of Expertise/Interest:
    - `Bridges`
    - `BEEFY`
    - `MMR`
    - `Omni-Node`
    - `XCMP/HRMP/DMP`


## Reporting period

- Start date: `2025/03/29`
- End date: `2025/07/07`


## Argument

During this reporting period, I have been focusing on multiple areas, but my main contributions have been related to 
the message passing mechanisms.

During the previous reporting period, I started contributing to an effort to optimize and improve the XCMP 
enqueuing logic, increasing the number of inbound messages that can be enqueued in a block from ~300 to >20k. 
Following up on that work, I merged one more [PR](https://github.com/paritytech/polkadot-sdk/pull/8344) that improves 
the weight metering accuracy by accounting for the position where the messages are being enqueued inside the 
message queue page. The number of inbound messages that can be enqueued in a block remains ~20k.

Also related to message passing mechanisms, I made [some changes to the parachain receiving logic for XCMP and DMP]
(https://github.com/paritytech/polkadot-sdk/pull/8860) by adding some offchain processing before forwarding the messages
to the parachain `set_validation_data` inherent. A number of messages are forwaded to `set_validation_data` in the 
current block in their full form, while the remaining messages are hashed in the current block and will be forwarded 
in their full form over the next blocks, when the parachain has enough bandwidth.

I also continued the work related to limiting and optimizing the heap memory usage in Polkadot, by merging a 
[PR](https://github.com/paritytech/polkadot-sdk/pull/8234) that limits the decoded size of an `UncheckedExtrinsic` call.


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

