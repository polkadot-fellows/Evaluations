# Argument-0007: Retention at Rank 2

|                 |              |
| --------------- | ------------ |
| **Report Date** | 2025/11/28   |
| **Submitted by**| muharem      |


## Member details

- Matrix username: `@muharem:parity.io`
- Polkadot address: `12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2`
- Current rank: `2`
- Date of initial induction: `2023/11/11`
- Date of last report: `2025/08/25`
- Area(s) of Expertise/Interest: `System Parachains, FRAME, XCM`


## Reporting period

- Start date: 2025/08/25
- End date: 2025/11/28

## Argument

My primary focus was the Asset Hub Migration project, which supports the Minimal Relay objective defined in the [RFC](https://github.com/polkadot-fellows/RFCs/blob/main/text/0032-minimal-relay.md) and forms a core part of the [Plaza project](https://www.rob.tech/blog/plaza/).

During this reporting period, we successfully executed the migrations on Paseo, Kusama, and later on Polkadot. All three migrations completed smoothly and without any major issues.

My work centered on preparing Kusama and Polkadot for their respective migrations. This included finalizing the remaining pieces of functionality, such as the migration of Kusama-specific pallets  ([runtimes/875](https://github.com/polkadot-fellows/runtimes/pull/956),[runtimes/875](https://github.com/polkadot-fellows/runtimes/pull/875), [runtimes/885](https://github.com/polkadot-fellows/runtimes/pull/885), [sdk/9604](https://github.com/paritytech/polkadot-sdk/pull/9604)). I also spent a significant amount of time testing and dry-running the migrations, strengthening the overall process and integrating additional safeguards and configurations to mitigate potential issues during execution ([runtimes/990](https://github.com/polkadot-fellows/runtimes/pull/990), [runtimes/952](https://github.com/polkadot-fellows/runtimes/pull/952),[runtimes/970](https://github.com/polkadot-fellows/runtimes/pull/970), [runtimes/882](https://github.com/polkadot-fellows/runtimes/pull/882), [runtimes/896](https://github.com/polkadot-fellows/runtimes/pull/896), [runtimes/930](https://github.com/polkadot-fellows/runtimes/pull/930)). I worked on defining the migration runbook and establishing the acceptance criteria for a successful migration.

At the moment, I am preparing a proposal to move the remaining sources of deposits on the Relay Chain - specifically the parachain registrar deposits and HRMP channel deposits - out of the Relay Chain. I am also supporting the final steps required to bring multi-asset bounties into production; it is ready for release on Westend. Additionally, I am drafting a proposal for ordered payouts for Governance spends, ensuring that earlier approved spends have priority to execute within a defined timeframe.

Overall my biggest achievement is the successful Asset Hub migration which were my primary focus for almost a year.

Most of my contributions during this reporting period can be found here: [link](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Amuharem+%5BAHM%5D+created%3A2025-08-25..2025-11-28).


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
