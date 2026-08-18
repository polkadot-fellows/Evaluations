# Argument-0008: Retention at Rank 2

|                  |                                 |
| ---------------- | ------------------------------- |
| **Report Date**  | Date of submission (2026/07/29) |
| **Submitted by** | Tsvetomir Dimitrov              |

## Member details

- Matrix username: @tsvetomir:parity.io
- Polkadot address: 1QhVP5qzR2LfXqP77N1JcuwHoY7NH8JVRNFm1hSooE9d4pR
- Current rank: 2
- Date of initial induction: 2023/10/11
- Date of last report: 2026/05/12
- Area(s) of Expertise/Interest: Disputes, Collator protocol

## Reporting period

- Start date: 2026/05/12
- End date: 2026/07/29

## Argument

During this reporting period my focus was wrapping up the collator protocol revamp testing and
preparing it for deployment on Kusama. The main effort was testing how the revamp behaves under
malus-collator spam on Versi. The results were good but I still can't discuss them in public.

To get there I made some observability improvements:

- Logging: [polkadot-sdk pr-122282](https://github.com/paritytech/polkadot-sdk/pull/12282)
- Metrics: [polkadot-sdk pr-12582](https://github.com/paritytech/polkadot-sdk/pull/12582) (not
  merged but used during testing).

During testing I fixed the following issues in the revamp implementation:

- Under spam the channel between the persistence db writer and the subsystem was getting filled up
  which caused delays in processing slashes. Fixed in
  [polkadot-sdk pr-12260](https://github.com/paritytech/polkadot-sdk/pull/12260).

- Collators were sending its parachain PeerID with the ApprovedPeer UMP signal which would deny them
  from building up reputation. This would have flawed one of the main concepts of the revamp - give
  priority to high reputation collators. Fixed in
  [polkadot-sdk pr-12388](https://github.com/paritytech/polkadot-sdk/pull/12388)

I've also wrote additional integration tests:

- [polkadot-sdk pr-12675](https://github.com/paritytech/polkadot-sdk/pull/12675) - subsystem startup
  and registered parachains pruning.
- [polkadot-sdk pr-11189](https://github.com/paritytech/polkadot-sdk/pull/11189) - interoperation
  with collator protocol V1 collators which unfortunately we still have in production.

During the Versi testing with the malus collator I had to make some improvements in logging,
reliability and spam behaviour of the malus-collator which I can't share because the project is
still not open sourced.

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                                                                                                                                                                                      | Comments                                                                    |
| ----- | ------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| I     | 90%                 | N/A                  |                                                                                                                                                                                                                                                                 |                                                                             |
| II    | 80%                 | N/A                  | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e 100 % voting agreement). | There were no referendas I could participate in during the reporting period |
| III   | 70%                 | 100%                 |                                                                                                                                                                                                                                                                 |                                                                             |
| IV    | 60%                 | 90%                  |                                                                                                                                                                                                                                                                 |                                                                             |
| V     | 50%                 | 80%                  |                                                                                                                                                                                                                                                                 |                                                                             |
| VI    | 40%                 | 70%                  |                                                                                                                                                                                                                                                                 |                                                                             |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
