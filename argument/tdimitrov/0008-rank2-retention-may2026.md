# Argument-0008: Retention at Rank 2

|                  |                                 |
| ---------------- | ------------------------------- |
| **Report Date**  | Date of submission (2026/05/12) |
| **Submitted by** | Tsvetomir Dimitrov              |

## Member details

- Matrix username: @tsvetomir:parity.io
- Polkadot address: 1QhVP5qzR2LfXqP77N1JcuwHoY7NH8JVRNFm1hSooE9d4pR
- Current rank: 2
- Date of initial induction: 2023/10/11
- Date of last report: 2026/02/25
- Area(s) of Expertise/Interest: Disputes, Collator protocol

## Reporting period

- Start date: 2025/12/08
- End date: 2026/02/25

## Argument

During this reporting period, my primary focus was still the collator protocol revamp and the
malus-collator (testing tool for the revamp).

I have fixed a few collator revamp related issues discovered during audits and testing:

- Each validator has got a limited number of peer scores it can track. When this limit is reached
  some peers need to be pruned from the database in order to keep it in a reasonable size. The initial
  implementation of pruning gave edge to new peers because it used only the timestamp of the last bump
  when evicting peers to the DB. As a result, a high score collator which was inactive for a while can
  easily be evicted by new peers with minimal score. To fix this a the ratio of
  `calculate score / time_since_last_bump` is calculated for each peer and the one with minimal score
  is evicted from the DB. The change is implemented in
  [polkadot-sdk pr-11576](https://github.com/paritytech/polkadot-sdk/pull/11576).
- When starting the node with a warp sync and we hit a period near the `WARP_SYNC_TARGET_BLOCK`
  (each 512 blocks) we might not be able to call a runtime apis for some blocks, which will yield an
  error in the collator protocol revamp. To prevent the subsystem from exiting these errors aren't
  bubbled up anymore. Implemented in
  [polkadot-sdk pr-11496](https://github.com/paritytech/polkadot-sdk/pull/11496).
- Decrease the log level of some noisy logs -
  [polkadot-sdk pr-11417](https://github.com/paritytech/polkadot-sdk/pull/11417).
- Sync the values of `CONNECTED_PEERS_PARA_LIMIT` in experimental collator protocol and
  `MAX_AUTHORITY_INCOMING_STREAMS` in peer_set. Implemented in
  [polkadot-sdk pr-11762](https://github.com/paritytech/polkadot-sdk/pull/11762).
- Simpler advertisement fetching mechanism.
  [polkadot-sdk pr-11008](https://github.com/paritytech/polkadot-sdk/pull/11008)

In malus-collator the most notable improvement is the implementation of the automatic targets
discovery. Initially the malus-collator required a list of peer ids of its target. With this change
it supports automatic discovery of the validators of a given para plus tracking them on session
changes. I can't provide a link to the PR since the project is not open sourced yet.

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
