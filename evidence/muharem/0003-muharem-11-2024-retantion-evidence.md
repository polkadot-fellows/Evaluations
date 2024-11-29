# Evidence-0003: Retention at Rank 2

|                 |              |
| --------------- | ------------ |
| **Report Date** | 2024/11/21   |
| **Submitted by**| Muharem      |


## Member details

- Matrix username: `@muharem:parity.io`
- Polkadot address: `12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2`
- Current rank: `2`
- Date of initial induction: `2023/11/11`
- Date of last report: `2024/08/27`
- Area(s) of Expertise/Interest: `System Parachains, FRAME, XCM`


## Reporting period

- Start date: 2024/08/27
- End date: 2024/11/21

## Evidence

During this reporting period, my main focus has been on researching, understanding, and beginning the implementation of migrating subsystems like Governance, Staking, and Balances from the Relay Chain to the Asset Hub. This work aligns with the Minimal Relay goal outlined in the [RFC](https://github.com/polkadot-fellows/RFCs/blob/main/text/0032-minimal-relay.md) and is part of the [Plaza project](https://www.rob.tech/blog/plaza/). I've been analyzing each Relay Chain pallet and its dependencies to determine which should be migrated to the Asset Hub, which need to be partially maintained, and which should remain on the Relay Chain. Some of this work can be seen in this [document](https://docs.google.com/spreadsheets/d/13W0BvrqD7jNOJzWQhyUr5ez0LmUgNQDX22BISiqYlco). Some subsystems, such as parachain slots, must remain on the Relay Chain for functionality. However, these subsystems are coupled with crowdloan fundraising accounts containing currently inaccessible user balances that need to be migrated to the Asset Hub. These cases require state inspection and a specific [solution](https://github.com/muharem/polkadot-runtimes/pull/4). Similar work is ongoing regarding user and system accounts, their balances, and reference counts. Additionally, I've been collaborating with Oliver (@ggwpez) to explore methods for state migration from the Relay Chain to the Asset Hub and identifying potential issues. We are currently setting up a test environment to dry-run the state migration via XCM with a fixed portion of resources/weight allocated for the migration execution so that migration time can be predictable and the parts of the system not involved in the migration can continue functioning.

I am currently mentoring a new engineer (@davidk-pt) in the ecosystem who is working on the next iteration of Treasury and Bounty pallets, following the plan I outlined in my previous report ([polkadot-sdk/5500](https://github.com/paritytech/polkadot-sdk/issues/5500)). We have completed implementing new indexes for child bounties ([polkadot-sdk/6255](https://github.com/paritytech/polkadot-sdk/pull/6255)) and added a new call to streamline the bounty and curator approval process ([polkadot-sdk/5961](https://github.com/paritytech/polkadot-sdk/pull/5961)). We're also making progress on refactoring the pallets to use new payout mechanics, which will enable proposals in various assets and multi-chain payouts ([polkadot-sdk/6189](https://github.com/paritytech/polkadot-sdk/pull/6189)).

I have completed the implementation of the Meta Transactions pallet, and the PR is now ready for review ([polkadot-sdk/6428](https://github.com/paritytech/polkadot-sdk/pull/6428)). This feature enables free transactions and introduces new flows for dapps, such as improved proxy account workflows and custom transaction payment schemes. It addresses a key item from the community’s wishlist ([polkadot-sdk/3901](https://github.com/paritytech/polkadot-sdk/pull/3901)). You can read more about the use cases here ([polkadot-sdk/266](https://github.com/paritytech/polkadot-sdk/pull/266)).

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   | None |
|II |80%   |N/A   |   | None |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
