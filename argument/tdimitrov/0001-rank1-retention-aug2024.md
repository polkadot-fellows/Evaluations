# Evidence-0000: Retention at/Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/08/28)                                                             |
| **Submitted by**| Tsvetomir Dimitrov                                                                          |


## Member details

- Matrix username: @tsvetomir:parity.io
- Polkadot address: 1QhVP5qzR2LfXqP77N1JcuwHoY7NH8JVRNFm1hSooE9d4pR
- Current rank: 1
- Date of initial induction: 2023/10/11
- Date of last report: NA
- Area(s) of Expertise/Interest: Disputes, Agile Coretime


## Reporting period

- Start date: 2024/05/26
- End date: 2024/08/28

## Evidence

During the last three months I was involved with validator disabling strategy implementation and
Agile Coretime testing.

For validator disabling I was responsible for implementing a generic disabling strategy interface in
the staking pallet and also implementing a concrete disabling strategy used in Polkadot. PR with the
changes: https://github.com/paritytech/polkadot-sdk/pull/2226. It's important to note that the
disabling strategy as a whole was a team effort. I was responsible just for the runtime
implementation part.

I joined late to the Agile Coretime efforts and contributed mainly with testing and bug fixes. My
contributions:
 - Fix for multiple parachains sharing a single core. When two parachains were set to share a core
   they were 'skipping slots'. The issue was that not all subsystems were using the claim queue to
   check what's scheduled in the future. The PR is co-authored by @alindima.
   PR: https://github.com/paritytech/polkadot-sdk/pull/4724
 - Fix in the runtime migration transferring legacy parachains leases to Coretime chain. There were
   two issues with the runtime migration. (1) parachains without a legacy lease in the current
   period but with a legacy lease in the future were not trasnferred to the Coretime chain and (2)
   time slice calculation formula was wrong.
   PRs: https://github.com/paritytech/polkadot-sdk/pull/5380 and
   https://github.com/polkadot-fellows/runtimes/pull/426
 - The previous issues was discovered with a chopsticks test performing the runtime upgrade and
   verifying the state after the migration. The code for the test is in this
   repo: https://github.com/tdimitrov/polkadot-coretime-launch-test
 - Add Agile Coretime to Polkadot. I've picked up a draft PR by @eskimor enabling Agile Coretime on
   Polkadot and ported it ontop of the latest release and finished the necessary configurations.
   PR: https://github.com/polkadot-fellows/runtimes/pull/401

Besides code contributions I am also an active code reviewer.
My reviews: https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Atdimitrov+



## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 2 referenda in which I was eligible to vote (i.e 0 % voting activity). Out of 2 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e 0 % voting agreement).| I missed both chances to cast my first vote and I have no excuse for this. I'll pay more attention to the referendums in the future. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):

