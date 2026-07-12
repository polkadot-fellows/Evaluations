# Argument-0004: Promotion to Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026-07-XX                                                                                  |
| **Submitted by**| rockbmb                                                                                     |


## Member details

- Matrix username: @alexandre.balde@parity.io
- Polkadot address: 13jBAtYJar4xujPaEx41FxjSt9PqU7LqJRbySJiVdMtuWN42
- Current rank: 1
- Date of initial induction: [2025-10-28](https://collectives.statescan.io/#/extrinsics/7473060-2)
- Date of last report: 2026-05-14
- Area(s) of Expertise/Interest: System Parachains, Polkadot Runtime, testing and security

## Reporting period

- Start date: 2024-09-01
- End date: 2026-07-13

## Argument

I have worked on Polkadot full-time since September 2024, focused on the testing and security of protocol components: pallets, runtimes, and the runtime upgrade process. I have held Rank I since December 2025, so this is a fast-track request, short of the one-year interval the Manifesto sets between ranks. The evidence below covers the current reporting period, with earlier work referenced where it gives context.

For Rank II, the Manifesto expects the member to be "a core part of the team", "deeply familiar with at least one major area of the protocol", and "demonstrating a readiness to be a network maintainer through increased levels of availability". I address these throughout.


### PET at release time

Fellowship runtime releases are tested with PET, and I triage its results when a release is cut. On [Release 2.3.0](https://github.com/polkadot-fellows/runtimes/pull/1195) (production Polkadot/Kusama release) I went through the PET failures and separated three false positives from real issues: a DAP V1->V2 catch-up mint (~795k DOT into `total_issuance` on the first post-upgrade block) that tests reading issuance deltas misattributed as a bug; off-by-N timing failures from both Asset Hubs moving to 2-second blocks via elastic scaling, against PET's hardcoded 2 relay blocks per parachain block (correct value 3); and a pre-existing PET bug querying `pallet_bounties` on chains that use `pallet_multi_asset_bounties`. The same on [integration of SDK 2604](https://github.com/polkadot-fellows/runtimes/pull/1159), where the mint interaction was first identified.


### Fellowship salary migration to Hollar

The Fellowship is migrating salary payments from USDT to Hollar. I wrote an E2E suite for the salary pallet ([PET#650](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/650)) and a [script](https://gist.github.com/rockbmb/29d2a8e514b3be63467019c461793012) that runs the next salary cycle under Hollar against forked Polkadot state.

The script found that Hollar is not a sufficient asset on Asset Hub: members without a DOT existential deposit would have their salary payout XCM fail silently. I wrote a [guide](https://hackmd.io/@rockbmb/ByLjpbjXMl) with the `forceAssetStatus` fix and its test procedure. A fellow used it to file the remediation, since executed: Fellowship [#574](https://collectives.subsquare.io/fellowship/referenda/574) whitelisting OpenGov [#1920](https://polkadot.subsquare.io/referenda/1920), making Hollar sufficient before the migration reached members.


### PET in the `runtimes` CI

To run PET as a regression gate in the Fellowship `runtimes` CI, I first had to make it fast and reliable enough for a release pipeline. PET runs on Chopsticks, so I contributed performance and correctness fixes there (RPC caching, request coalescing, a batched dry-run API ([#1028](https://github.com/AcalaNetwork/chopsticks/pull/1028), merged)) and `rpcTimeout` forwarding ([#1034](https://github.com/AcalaNetwork/chopsticks/pull/1034), merged). In PET I shared the client object within suites to cut suite time ([PET#609](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/609), merged), ranked RPC endpoints by health ([PET#616](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/616), merged), and pruned dead ones ([PET#635](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/635), merged). Production RPCs throttle, so I added a caching layer, first Chopsticks-as-cache then Subway ([PET#622](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/622), merged), which needed upstream Subway work to expose per-upstream timeouts and retries ([subway#203](https://github.com/AcalaNetwork/subway/pull/203), merged). Finally I added vitest fork-pool sharding ([PET#619](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/619), merged), applied in `runtimes` ([#1180](https://github.com/polkadot-fellows/runtimes/pull/1180), merged).

With that in place, I reworked the `runtimes` `test.yml` to run PET as a matrix with per-suite retry/timeout, Subway caching, and filtering to Fellowship runtimes ([#1068](https://github.com/polkadot-fellows/runtimes/pull/1068), merged).


### `try-runtime-cli`

I remain the maintainer of [`try-runtime-cli`](https://github.com/paritytech/try-runtime-cli), which validates runtime upgrades against live chain state. I continued to update dependencies, fix CI, and cut releases during this period.


### Pallet review

When pallets destined for system chains are under review, I test them with a layered approach: `try_state` invariants encoding accounting and structural assumptions, state-aware fuzzers checking properties of operation histories that a single `try_state` snapshot cannot, and formal methods where the arithmetic warrants it (Quint, Kani, hax+Lean).

I contributed `try_state` checks and fuzzers to `pallet-recovery` ([#12490](https://github.com/paritytech/polkadot-sdk/pull/12490), awaiting review). I applied the same to `pallet-psm` ([#12154](https://github.com/paritytech/polkadot-sdk/pull/12154), [#12155](https://github.com/paritytech/polkadot-sdk/pull/12155), awaiting review) while reviewing a stablecoin pallet authored by an external team; there, a Lean proof that its decimal conversion cannot inflate value removes that class of bug from the test surface.


### Security working group

I am a member of the Fellowship security working group, with access to its private findings repositories. During this period I used the testing methodology to independently reproduce a known, previously-audited issue in a core pallet, and reported it through the working group. Details are in the group's private repositories.


### Public commentary

I authored a public [forum post](https://forum.polkadot.network/t/re-introducing-polkadot-ecosystem-tests-pet/17723) on PET, inviting parachain teams to adopt the suite for their own runtimes. I have written further posts on the pallet testing and formal-methods work; these stay internal while that work is closed-source, to be published once it can be opened.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |No referenda to vote on  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Acknowledgements

Thanks to ggwpez, bkchr, seadanda, kianenigma, and xlc for review and collaboration across the SDK, Fellowship runtimes, PET, and Chopsticks.
