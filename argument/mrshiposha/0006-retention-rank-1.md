# Argument-0006: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/02/28                                                                                  |
| **Submitted by**| Daniel Shiposha                                                                             |


## Member details

- Matrix username: `@mrshiposha:matrix.org`
- Polkadot address: `14aC2hfNZTX4sMHPh47MjGB4Vr4rVYHZgBid54vRKrZVBZQY`
- Current rank: Rank I
- Date of initial induction: 2024/12/11
- Date of last report: 2025/11/24
- Area(s) of Expertise/Interest: XCM, NFT


## Reporting period

- Start date: 2025/12/21
- End date: 2026/03/21

## Argument

During the reporting period, I continued working on XCM refactoring (https://github.com/paritytech/polkadot-sdk/issues/7095).

In the previous reporting period, I attempted to approach this task by developing a proc-macro to help generate different XCM versions ([illustration of the original idea](https://gist.github.com/mrshiposha/9454dab3362c5d56dc067e2c7730640d), [PoC](https://github.com/UniqueNetwork/polkadot-sdk/tree/xcm-refactor)).

However, it turned out that the proc-macro implementation in that form was too complex, and its usage also felt somewhat clumsy.
Because of this, I considered alternative options, such as developing a separate tool to generate XCM versions, but that approach seemed even more cumbersome.

After further consideration, I returned to the proc-macro idea in a refined form.
The description of the current approach can be found here: https://gist.github.com/mrshiposha/f19f55a89cb90895e4c420e7f72bbc9e.
This version appears significantly simpler and should be relatively straightforward to implement.


Additionally, I helped update the unique-instances adapters as part of Adrian's PR introducing imbalance tracking in XCM:
- Adrian's PR: https://github.com/paritytech/polkadot-sdk/pull/10384
- My commit: https://github.com/paritytech/polkadot-sdk/pull/10384/changes/062c5082aba56f014962509bd633cab9da33a7b5

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   | There were no referenda I was eligible to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
