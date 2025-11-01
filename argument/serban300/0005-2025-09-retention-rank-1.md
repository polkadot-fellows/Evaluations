# Argument-0005: Retention at Rank 1

|                 |              |
| --------------- |--------------|
| **Report Date** | 2025/09/24   |
| **Submitted by**| Serban Iorga |


## Member details

- Matrix username: `@serban.iorga:parity.io`
- Polkadot address: `14oHMAJ5btnDCusHrTWraw1wTsLJwZeqPDLxusm1R1Zh3Vxa`
- Current rank: `1`
- Date of initial induction: `2024/04/22`
- Date of last report: `2025/07/07`
- Area(s) of Expertise/Interest:
    - `Bridges`
    - `BEEFY`
    - `MMR`
    - `Omni-Node`
    - `XCMP/HRMP/DMP`


## Reporting period

- Start date: `2025/07/08`
- End date: `2025/09/24`


## Argument

During this reporting period, I have been focusing mainly on reliability and efficiency improvements for the 
message passing mechanisms.

On the efficiency side I added support for 
[receiving double encoded XCMs through XCMP](https://github.com/paritytech/polkadot-sdk/pull/9588). For context, 
at the moment parachains pass XCM messages between them through XCMP pages that use the 
`XcmpMessageFormat::ConcatenatedVersionedXcm` format. These pages contain concatenated encoded `VersionedXcm`s 
and on the receiving side, in order to split the page into individual messages, we need to first decode them 
and then re-encode and forward them to the `pallet-messages-queue`. This adds extra overhead 
(about 2.5 microseconds + some cost per byte). My PR added a new (`XcmpMessageFormat::ConcatenatedOpaqueVersionedXcm`) 
format that will be used for pages with double-encoded XCMs. This makes the decoding much easier and almost free, 
improving the XCMP bandwidth. This new format is not used yet, and we'll have to come out with a roll-out plan next.

On the reliability side, I worked on some small fixes and improvements. Mentioning just a few:
- some small improvements related to the PoV accounting for the XCMP enqueueing logic:
  [1](https://github.com/paritytech/polkadot-sdk/pull/9641), [2](https://github.com/paritytech/polkadot-sdk/pull/9745).
- prepared a [referenda](https://polkadot.subsquare.io/referenda/1740) for reducing the number of  pending messages 
  per HRMP channel. This would prevent overloading the receiving parachains with too many messages at once.
- limited the number of signals per XCMP page to 3: https://github.com/paritytech/polkadot-sdk/pull/9781.

I also continued the work related to limiting and optimizing the heap memory usage in Polkadot. Here, there already was 
[a pending PR](https://github.com/paritytech/polkadot-sdk/pull/7902), but as part of the code review a completely 
different approach was suggested. In order to address this, I opened a 
[new PR](https://github.com/paritytech/polkadot-sdk/pull/9480).


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

