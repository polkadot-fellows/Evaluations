# Evidence-0002: Retention at Rank 2

|                 |              |
| --------------- | ------------ |
| **Report Date** | 2024/08/27   |
| **Submitted by**| Muharem      |


## Member details

- Matrix username: `@muharem:parity.io`
- Polkadot address: `12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2`
- Current rank: `2`
- Date of initial induction: `2023/11/11`
- Date of last report: `2024/05/04`
- Area(s) of Expertise/Interest: `System Parachains, FRAME, XCM`


## Reporting period

- Start date: 2024/05/04
- End date: 2024/08/27

## Evidence

It’s been a little over three months since I submitted my last retention letter ([letter1](https://github.com/polkadot-fellows/Evaluations/pull/6)), and with this letter, I want to share what I’ve been working on during this time, particularly in relation to the Polkadot Fellowship Program.

In recent month, I’ve been addressing an issue reported by users who were unable to access their funds on accounts created using the pure proxy feature. The users mistakenly assumed ownership of the same account on different parachains and subsequently received funds on those accounts ([polkadot-sdk/3288](https://github.com/paritytech/polkadot-sdk/issues/3288)). I’ve documented the problem and proposed a solution in a recently published RFC ([RFC: Pure Proxy Replication](https://github.com/polkadot-fellows/RFCs/pull/111)).

I’ve also started work on the next iteration of changes to the Treasury and Bounty pallets. A project document outlining the objectives and implementation details has been published ([polkadot-sdk/5500](https://github.com/paritytech/polkadot-sdk/issues/5500)). These changes include some of the most requested features and serve as the first step in moving Treasury functionality from the Relay Chain to the Asset Hub. Additionally, I’ve published an API specification for the spend call, which has been a source of considerable debate ([polkadot-sdk/4715](https://github.com/paritytech/polkadot-sdk/issues/4715)). This new specification will enable scenarios where a spend is commanded on one chain, with assets being withdrawn on another and deposited on yet another chain.

An issue with transaction payments using exchangeable assets on the Asset Hub was reported, where the paying account needed to maintain an existential deposit of a native asset, causing problems in certain cases. This issue was promptly addressed and resolved ([polkadot-sdk/pr/448](https://github.com/paritytech/polkadot-sdk/pull/4488)). In addition, transaction payments were migrated to use the fungibles traits ([runtimes/332](https://github.com/polkadot-fellows/runtimes/pull/332)). I also took over the asset rewards pallet and brought it to a state ready for review ([polkadot-sdk/3926](https://github.com/paritytech/polkadot-sdk/pull/3926)). Finally, the implementation of auto-incremented identifiers for new trust-backed assets has been included to the latest release ([polkadot-sdk/4757](https://github.com/paritytech/polkadot-sdk/pull/4757), [runtimes/346](https://github.com/polkadot-fellows/runtimes/pull/346), [runtimes/414](https://github.com/polkadot-fellows/runtimes/pull/414)).

In addition to these efforts, I’ve worked on several smaller features and maintenance tasks related to Frame and System Chains ([polkadot-sdk/4564](https://github.com/paritytech/polkadot-sdk/pull/4564), [polkadot-sdk/4807](https://github.com/paritytech/polkadot-sdk/pull/4807), [polkadot-sdk/5384](https://github.com/paritytech/polkadot-sdk/pull/5384), [runtimes/339](https://github.com/polkadot-fellows/runtimes/pull/339), [runtimes/383](https://github.com/polkadot-fellows/runtimes/pull/383)).

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |50%   |100%   | I have voted on 1 out of 2 referenda in which I was eligible to vote during this reporting period (i.e 50% voting activity). Out of 1 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 1 time (i.e 100 % voting agreement). | [ref 150](https://collectives.subsquare.io/fellowship/referenda/150) |
|II |N/A   |N/A   |   |  |
|III|N/A   |N/A   |   |  |
|IV |N/A   |N/A   |   |  |
|V  |N/A   |N/A   |   |  |
|VI |N/A   |N/A   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
