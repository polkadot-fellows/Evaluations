# Evidence-0003: Promotion to Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/02/20)                                                             |
| **Submitted by**| Tsvetomir Dimitrov                                                                        |


## Member details

- Matrix username: @tsvetomir:parity.io
- Polkadot address: 1QhVP5qzR2LfXqP77N1JcuwHoY7NH8JVRNFm1hSooE9d4pR
- Current rank: 1
- Date of initial induction: 2023/10/11
- Date of last report: 2024/08/28
- Area(s) of Expertise/Interest: Disputes, Agile Coretime


## Reporting period

- Start date: 2024/11/28
- End date: 2025/02/20


## Evidence

During  this reporting period I worked on a refined version of the collation fairness ([polkadot-sdk
issue-797](https://github.com/paritytech/polkadot-sdk/issues/1797)). The PR is incomplete since I
had to focus on the AssetHub migration.

For the AssetHub migration I am working on separating the coupling between the session and staking
pallets. Since they should be on separate networks (session on relay chain and staking on AssetHub)
they can't communicate directly with each other anymore. To overcome this I picked up an idea from
[gpestana](https://github.com/gpestana) to introduce two new pallets which communicate with each
other over XCM and provide data to staking and session pallets. The initial effort for this is in
[polkadot-sdk pr-7582](https://github.com/paritytech/polkadot-sdk/pull/7582). At the moment I am working on
integrating the pallets in Westend and AssetHub-Next.

I've also submitted two governance proposals for bumping `schedulerParams.lookahead` configuration
parameter to 3. More information about this can be found in the corresponding referendas for
[Kusama](https://kusama.subsquare.io/referenda/488) and
[Polkadot](https://polkadot.subsquare.io/referenda/1436).

Since I am applying for a rank 2 promotion I want to back my request with some examples of impactful
work I did in the past:
- In the previous reporting period I implemented a collation fetching fairness implementation for the
  collator protocol - [polkadot-sdk pr-4880](https://github.com/paritytech/polkadot-sdk/pull/4880).
- In the end of 2023 and the beginning of 2024 I worked on validator disabling strategy in the
  runtime. Its essence was to disable an offending validator till the end of the current era so that
  the damage to network, its nominators and itself is limited. The work is split in multiple PRs:
  [polkadot-sdk pr-2226](https://github.com/paritytech/polkadot-sdk/pull/2226), [polkadot-sdk
  pr-1259](https://github.com/paritytech/polkadot-sdk/pull/1259) [polkadot-sdk
  pr-1257](https://github.com/paritytech/polkadot-sdk/pull/1257) and [polkadot-sdk
  pr-2889](https://github.com/paritytech/polkadot-sdk/pull/2889). This was a team effort with
  [ordian](https://github.com/ordian/), [eskimor](https://github.com/eskimor/) and
  [Overkillus](https://github.com/Overkillus/).
- In 2022 I worked on a runtime api versioning implementation in Substrate. The work was done in
  [substrate pr-1779](https://github.com/paritytech/substrate/pull/11779) with a lot of guidance
  from [bkchr](https://github.com/bkchr).
- I was a co-author of [Stalled parachains on Kusama - post
  mortem](https://forum.polkadot.network/t/stalled-parachains-on-kusama-post-mortem/3998) and author
  of [Finality stall on Kusama (15.02.2024) - post
  mortem](https://forum.polkadot.network/t/finality-stall-on-kusama-15-02-2024-post-mortem/6398).

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e 100 % voting agreement). | There were no referendas I could participate in during the reporting period |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):

