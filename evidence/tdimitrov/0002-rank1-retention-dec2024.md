# Evidence-0002: Retention at/Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/11/28)                                                             |
| **Submitted by**| Tsvetomir Dimitrov                                                                        |


## Member details

- Matrix username: @tsvetomir:parity.io
- Polkadot address: 1QhVP5qzR2LfXqP77N1JcuwHoY7NH8JVRNFm1hSooE9d4pR
- Current rank: 1
- Date of initial induction: 2023/10/11
- Date of last report: 2024/08/28
- Area(s) of Expertise/Interest: Disputes, Agile Coretime


## Reporting period

- Start date: 2024/08/28
- End date: 2024/11/28


## Evidence

During this reporting period I've finished my work on Agile Cortime migration testing on Polkadot.
Unfortunately the chopsticks migration test which I wrote gave a false positive result (due to [this
issue](https://github.com/AcalaNetwork/chopsticks/issues/823)) and we had to release another
migration which fixes the Agile Coretime state. The migration was mainly done by @donal and
@eskimor. I've contributed with testing and reviews. [Link to the
PR](https://github.com/polkadot-fellows/runtimes/pull/458).

Next I worked on an implementation of collation fetching fairness for Agile Coretime. It is part of
[polkadot-sdk #1797](https://github.com/paritytech/polkadot-sdk/issues/1797). The problem turned out
to be more complicated than I estimated initially which lead to a few iterations of the
implementation. I made some wrong assumptions and went for a simple implementation which was not
covering all cases. After figuring this out I did a rework which was more complex but covered all
the edge cases. [Link to the PR](https://github.com/paritytech/polkadot-sdk/pull/4880). At the time
I am writing this evidence the PR is still not merged but it is pending a final code review and
hopefully will be merged when the referenda is open for voting.

I am also working on the async backing parameters removal
([issue](https://github.com/paritytech/polkadot-sdk/issues/5079)). I did some preparations in the
backing subsystem by removing the fallback code handling the absence of prospective parachains
subsystem. [Link to the PR](https://github.com/paritytech/polkadot-sdk/pull/6215).

During the reporting period I did small fixes for flaky zombienet tests which were breaking the CI
pipeline. Link to [PR1](https://github.com/paritytech/polkadot-sdk/pull/6268) and
[PR2](https://github.com/paritytech/polkadot-sdk/pull/6236).

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

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

