# Evidence-0005: Retention at Rank 2

|                 |              |
| --------------- | ------------ |
| **Report Date** | 2025/05/22   |
| **Submitted by**| muharem      |


## Member details

- Matrix username: `@muharem:parity.io`
- Polkadot address: `12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2`
- Current rank: `2`
- Date of initial induction: `2023/11/11`
- Date of last report: `2025/02/26`
- Area(s) of Expertise/Interest: `System Parachains, FRAME, XCM`


## Reporting period

- Start date: 2025/02/26
- End date: 2025/05/22

## Evidence

My main focus continues to be the Asset Hub Migration project, which aligns with the Minimal Relay goal outlined in the [RFC](https://github.com/polkadot-fellows/RFCs/blob/main/text/0032-minimal-relay.md) and forms a core part of the [Plaza project](https://www.rob.tech/blog/plaza/). It has now been nearly five months since we entered the implementation phase. During the reporting period, I completed the account migration module, covering all edge cases such as parachain registrar and HRMP deposits. Together with Oliver, we finalized the data migration and mapping for all relevant pallets. I also completed the benchmarking and weight accounting for both the sending side (Relay Chain) and the receiving side (Asset Hub). Most of my contributions during this reporting period can be found here: [link](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Amuharem+%5BAHM%5D+is%3Aclosed+created%3A2025-02-26..2025-05-22).

In week 20 of this year, we conducted an in-person working session with the migration team and researchers from W3F. The goal was to review our key decisions, address outstanding topics such as Doomsday Governance, and define the next steps toward a production-ready migration. During this meeting, we executed a full test migration on the Westend network. While the process was largely successful, we encountered an issue related to the back pressure system and identified a misused function. These findings have been documented and incorporated into the production migration checklist to further harden the process.

As part of the production migration preparations, I explored Async Backing and Elastic Scaling to improve throughput and shorten the overall migration time. To ensure Async Backing would be available before the migration, I enabled it on Kusama Asset Hub [polkadot-fellows/runtimes/659](https://github.com/polkadot-fellows/runtimes/pull/659). This involved thoroughly understanding the mechanisms (with support from @skunert and @Andrei) and writing emulated test scenarios to validate the setup.

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
