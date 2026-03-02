# Argument-0005: Retention at Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/12/19)                                                             |
| **Submitted by**| Adrian Catangiu                                                                        |


## Member details

- Matrix username: @adrian:parity.io
- Polkadot address: 121dd6J26VUnBZ8BqLGjANWkEAXSb9mWq1SB7LsS9QNTGFvz
- Current rank: III (Fellow)
- Date of initial induction: 2023/06/12
- Date of last report: 2025/06/09
- Area(s) of Expertise/Interest: Trustless Bridges, XCM, System Chains, BEEFY


## Reporting period

- Start date: 2025/07/01
- End date: 2025/12/31


## Argument

During the reporting period I have continued my focus and contributions on Asset Hub Migration, Asset Hub capabilities and XCM.

### Asset Hub Migration

Design reviews, code reviews, planning, dependency untangling, etc - overall, I believe the core AHM team considers me as one of their own having supported them along the way.

Some linkable examples:

Owning and driving the main AHM production release (Kusama+Polkadot fellowship release) and AHM deployment plan and calendar (handed over to Donal towards end-of-Q3).

- [Upgrade to Polkadot-SDK stable2506 #817](https://github.com/polkadot-fellows/runtimes/pull/817)
- [Upgrade to Polkadot-SDK unstable2507 #849](https://github.com/polkadot-fellows/runtimes/pull/849)
- [Release 1.7.0 #859 (including OpenGov refs and comms)](https://github.com/polkadot-fellows/runtimes/pull/859)
- [Public coordination accross the fellowship members](https://matrix.to/#/!bMWYTUFeSoYacMOlpS:matrix.parity.io/$kXsNtBQBveYdVUG_IfiBJxMQYCrlXK7pP3GoxvUp8o4?via=parity.io&via=matrix.org&via=matrix.parity.io)
- [Pushing subsequent 1.7.1 through OpenGov](https://polkadot.polkassembly.io/referenda/1756)

Helping Serban with planning and executing (staged rollout with dependencies) a [XCMP/DMP vulnerability fix](https://github.com/paritytech/polkadot-sdk/pull/8860) mandatory for AHM.

Flagging XCM DOT transfer issues post-AHM then delivering fixes and mitigations through Cisco and Karol and ecosystem partners like Paraspell: [details here](https://forum.polkadot.network/t/mandatory-action-guide-for-ahm-broken-native-crosschain-transfers/14634).

### Technical Individual Contributions

[Integrate "Empowered XCM Origins" features to System Chains #799](https://github.com/polkadot-fellows/runtimes/pull/799) - Better UX, more powerful usecases, already under integration by major dapps (Hydration for easy bridge transfers, Bifrost for BNC token unification across Polkadot and Kusama, Nova for single-click/single-sign transfer+swap+transfer-back, and others).

[Add reserves info to support non-teleportable Foreign Assets on Asset Hub #9948](https://github.com/paritytech/polkadot-sdk/pull/9948) - Required to support HOLLAR on Asset Hub, important to PoP, also makes Foreign Assets more flexible in general.

[XCM executor keeps track and resolves all imbalances created by XCM operations #10384](https://github.com/paritytech/polkadot-sdk/pull/10384) - The PR implements a comprehensive system for tracking asset imbalances in the XCM Executor using `ImbalanceAccounting` traits. This correctly addresses the issue of potential issuance invariant violations by ensuring that assets are not prematurely burned or minted during XCM execution, particularly in holding, traps, and claims. The use of unsafe operations for cloning and forgetting imbalances is well-encapsulated within safe abstractions like BackupAssetsInHolding and the ClaimAssets logic. Additionally, the introduction of `quote_weight` improves the efficiency of fee queries.

### Snowbridge support

Helping Snowbridge recover user funds for failed TXs following 1.7.1 runtimes upgrade: [ref 407](https://collectives.subsquare.io/fellowship/referenda/407) where I did review/audit for the fix plus the proposed retroactive recovery.

Helping Snowbridge upgrade Ethereum side contracts for Snowbridge v2: [ref 1763](https://polkadot.subsquare.io/referenda/1763)/[ref 408](https://collectives.subsquare.io/fellowship/referenda/408) where again I provided review/audit.

## Voting record

Based on [my membership page](https://collectives.subsquare.io/user/121dd6J26VUnBZ8BqLGjANWkEAXSb9mWq1SB7LsS9QNTGFvz/fellowship) on Subsquare Polkadot Fellowship dashboard, my participation rate in the last 6 months: `Participation Rate 96.88% Win Rate 100.00%`.

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  | 96.88% |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- Consistent reviewer for both [Fellowship runtimes](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr++reviewed-by%3Aacatangiu+created%3A2025-07-01..2025-12-30+) and [Polkadot-SDK](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr++reviewed-by%3Aacatangiu+created%3A2025-07-01..2025-12-30+).

