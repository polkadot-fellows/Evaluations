# Evidence-0004: Retention at Rank 2

|                 |              |
| --------------- | ------------ |
| **Report Date** | 2025/02/26   |
| **Submitted by**| Muharem      |


## Member details

- Matrix username: `@muharem:parity.io`
- Polkadot address: `12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2`
- Current rank: `2`
- Date of initial induction: `2023/11/11`
- Date of last report: `2024/11/21`
- Area(s) of Expertise/Interest: `System Parachains, FRAME, XCM`


## Reporting period

- Start date: 2024/11/21
- End date: 2025/02/26

## Evidence

Over the past three months, I have been continuing the work on migrating subsystems like Governance, Staking, and Balances to Asset Hub, as outlined in my previous [report](https://github.com/polkadot-fellows/Evaluations/blob/main/evidence/muharem/0003-muharem-11-2024-retantion-evidence.md). Following the research and planning phase mentioned earlier, Oliver and I have begun the implementation phase for the pallets' data migration. I have introduced two pallets, `rc-migrator` and `ah-migrator`, to facilitate the migration process. We have merged the data migration for at least half of the migrating pallets into the development branch and integrated these pallets into the Asset Hub runtime ([full list](https://github.com/polkadot-fellows/runtimes/issues/555)). This includes migrating account balances along with associated holds, freezes, locks, and reserves, as well as the Governance system, where for the active and passed but not yet enacted proposals, I have provided a call mapper to minimize user impact. Currently, we are working on a test environment that will allow us to dry-run the migration, ensuring we adhere to the resource (weight limits) allocated for the migration. You can find my work in the [PRs](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Amuharem+%5BAHM%5D+is%3Aclosed) and view the full development branch diff here [link](https://github.com/polkadot-fellows/runtimes/compare/main...dev-asset-hub-migration).

This work aligns with the Minimal Relay goal outlined in the [RFC](https://github.com/polkadot-fellows/RFCs/blob/main/text/0032-minimal-relay.md) and is part of the [Plaza project](https://www.rob.tech/blog/plaza/).

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
