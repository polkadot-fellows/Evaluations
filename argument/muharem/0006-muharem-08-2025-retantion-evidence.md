# Argument-0006: Retention at Rank 2

|                 |              |
| --------------- | ------------ |
| **Report Date** | 2025/08/25   |
| **Submitted by**| muharem      |


## Member details

- Matrix username: `@muharem:parity.io`
- Polkadot address: `12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2`
- Current rank: `2`
- Date of initial induction: `2023/11/11`
- Date of last report: `2025/05/22`
- Area(s) of Expertise/Interest: `System Parachains, FRAME, XCM`


## Reporting period

- Start date: 2025/05/22
- End date: 2025/08/25

## Argument

My primary focus remains the Asset Hub Migration project, which supports the Minimal Relay objective defined in the [RFC](https://github.com/polkadot-fellows/RFCs/blob/main/text/0032-minimal-relay.md) and forms a core part of the [Plaza project](https://www.rob.tech/blog/plaza/).

In the previous report, I mentioned that we had executed a full test migration on the Westend test network. Although the migration was largely successful, we identified several issues and areas for improvement. Over the past three months, I’ve focused on addressing these and preparing for the next stage: running the migration on Paseo, Polkadot’s test network.

As part of this work, I implemented a new control flow system that improves acknowledgment timing for migration-related XCM messages, making the delivery pipeline faster and more predictable. Additionally, the system buffers migration messages until they are confirmed as successfully processed, enabling us to replay messages via a root call in unexpected scenarios ([polkadot-fellows/runtimes/780](https://github.com/polkadot-fellows/runtimes/pull/780)). I also integrated a prioritization mechanism for XCM processing that ensures migration messages are handled ahead of unrelated traffic on the Relay Chain and Asset Hub, preventing spam from interfering with migration execution ([polkadot-fellows/runtimes/774](https://github.com/polkadot-fellows/runtimes/pull/774), [polkadot-fellows/runtimes/772](https://github.com/polkadot-fellows/runtimes/pull/772), [polkadot-fellows/runtimes/787](https://github.com/polkadot-fellows/runtimes/pull/787)).

To make the migration more robust, I built support for idempotency, which allows us to move the migration state cursor backward and rerun stages if needed ([polkadot-fellows/runtimes/808](https://github.com/polkadot-fellows/runtimes/pull/808)). I also introduced warm-up and cool-off phases, with configurable durations, to allow for system checks immediately before and after the migration ([polkadot-fellows/runtimes/786](https://github.com/polkadot-fellows/runtimes/pull/786), [polkadot-fellows/runtimes/841](https://github.com/polkadot-fellows/runtimes/pull/841)).

At this point, the codebase for the Paseo migration is ready. Since Paseo mirrors the Polkadot runtimes (Relay Chain and Asset Hub), this milestone effectively represents code readiness for the Polkadot production migration. We also used this phase to close out a number of outstanding TODOs that were previously blocked by SDK version dependencies.

I’ve now started work on preparing the Kusama migration. This includes setting up the required pallets on Asset Hub, adapting the migrator pallets, and implementing migration logic for Kusama-specific functionality, such as recovery and society ([polkadot-fellows/runtimes/862](https://github.com/polkadot-fellows/runtimes/pull/862)).

Most of my contributions during this reporting period can be found here: [link](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Amuharem+%5BAHM%5D+created%3A2025-05-22..2025-08-25).


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
