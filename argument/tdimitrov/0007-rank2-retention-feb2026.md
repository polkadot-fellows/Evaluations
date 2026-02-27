# Argument-0005: Retention at Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/02/25)                                                             |
| **Submitted by**| Tsvetomir Dimitrov                                                                          |


## Member details

- Matrix username: @tsvetomir:parity.io
- Polkadot address: 1QhVP5qzR2LfXqP77N1JcuwHoY7NH8JVRNFm1hSooE9d4pR
- Current rank: 2
- Date of initial induction: 2023/10/11
- Date of last report: 2025/12/08
- Area(s) of Expertise/Interest: Disputes, Collator protocol


## Reporting period

- Start date: 2025/12/08
- End date: 2026/02/25


## Argument

During this reporting period, my primary focus was driving the collator protocol revamp to
completion. I finalized @alindima’s work on the collation manager and the main subsystem
([polkadot-sdk pr-8541](https://github.com/paritytech/polkadot-sdk/pull/8541)).
Additionally, I developed a comprehensive test plan for the new implementation and a deployment
strategy for rolling out the changes on Westend. During testing I discovered two new issues:
- If `request_candidates_pending_availability` runtime call fails during reputation bumps extraction
  the processing of the rest of the candidates was terminated. Fixed in
  [polkadot-sdk pr-10610](https://github.com/paritytech/polkadot-sdk/pull/10610).
- A service race in libp2p (which was also discovered by @lexnv). I helped with the fix validation
  since it was easy to reproduce with the malus-collator. The fix by @lexnv is in
  [litep2p pr-525](https://github.com/paritytech/litep2p/pull/525). Disclaimer: I have no
  contribution for the fix itself.

I also verified the protocol’s resilience against spam attacks and confirmed that the collator scoring
system functions correctly. Both were validated using malus-collator and local zombienet-sdk tests.
Finally, I applied minor fixes to malus-collator and extended it with a new malicious behavior.

Since the collator revamp testing and malus-collator development are still not open sourced I can't
give too much details about the actual test results and contributions to the Polkadot network.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e 100 % voting agreement). | There were no referendas I could participate in during the reporting period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):

