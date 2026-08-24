# Argument-0004: Promotion to Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026-07-13                                                                                  |
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

I have worked on Polkadot full-time since September 2024. I have held Rank I since December 2025, so this is a fast-track request, short of the one-year interval the Manifesto sets between ranks. The basis is not the interval but the work already owned.

My area is the correctness and verification of Polkadot SDK pallets and the Fellowship runtimes: the layer that decides whether a protocol change is safe before it reaches a live network. Over this period my role moved from writing tests against Polkadot to owning that layer. I exercise it through the tooling that runs it (Polkadot Ecosystem Tests and `try-runtime-cli`), through the release process that now depends on them, and through deeper methods applied directly to SDK pallets: runtime invariants, stateful fuzzing, and formal verification.

For Rank II the Manifesto expects the member to be "a core part of the team", "deeply familiar with at least one major area of the protocol", and "demonstrating a readiness to be a network maintainer through increased levels of availability". Testing is not itself a protocol component, and I do not claim otherwise. What I claim is the analytical improvement of protocol components: the invariants, fuzzers, and proofs below are contributed to the pallets themselves and reviewed by their maintainers, which is the Rank II expectation of primary responsibility for the analytical improvement of a major component. The release-gating and the Hollar finding are the availability and network-maintainer readiness the rank asks for. The evidence follows.


### Testing Polkadot SDK pallets and the Fellowship runtimes

The Fellowship runtimes are validated end-to-end by PET, which forks live network state and runs scenarios against the real runtimes: relay chains and system parachains, covering accounts, staking, governance, proxy, multisig, XCM, and more. Over this period my work made that suite a dependable part of the release process rather than a source of noise, and put it to use when releases are cut.

When a release is prepared, I triage PET's results against the proposed runtime. On [Release 2.3.0](https://github.com/polkadot-fellows/runtimes/pull/1195) (a production Polkadot/Kusama release) I went through the failures and separated three false positives from genuine issues: a DAP V1->V2 catch-up mint (~795k DOT into `total_issuance` on the first post-upgrade block) that tests reading issuance deltas misattributed as a bug; off-by-N timing failures from both Asset Hubs moving to 2-second blocks via elastic scaling, against PET's hardcoded 2 relay blocks per parachain block (correct value 3); and a pre-existing PET bug querying `pallet_bounties` on chains that use `pallet_multi_asset_bounties`. The same took place on [Integrate SDK 2604](https://github.com/polkadot-fellows/runtimes/pull/1159), where the mint interaction was first identified. This is the "on-call for the components of which they have a deep understanding" that the Manifesto describes for Rank II.

Earlier, the tests I wrote were part of the Asset Hub Migration validation on Kusama (Oct 2025) and Polkadot (Nov 2025), used in real time and in the [`ahm-dryrun`](https://github.com/paritytech/ahm-dryrun) dry-runs to check relay and Asset Hub runtimes. That work was cited in my Rank I promotion; I note it here as the start of the release-validation role that has continued since.


### Making the suite dependable in CI

Running PET as a regression gate in the Fellowship `runtimes` CI first required making it fast and reliable enough for a release pipeline, which was a substantial piece of engineering across several repositories.

PET runs on Chopsticks, so its throughput bounds PET's. I contributed performance and correctness fixes there: RPC caching, request coalescing, and a batched dry-run API ([#1028](https://github.com/AcalaNetwork/chopsticks/pull/1028), merged), and `rpcTimeout` forwarding ([#1034](https://github.com/AcalaNetwork/chopsticks/pull/1034), merged). In PET I shared the client object within suites to cut suite time ([PET#609](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/609), merged), ranked RPC endpoints by health to select the healthiest ([PET#616](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/616), merged), and pruned dead ones ([PET#635](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/635), merged). Production RPCs throttle, which surfaces as CI flakes rather than real failures, so I added a caching layer: first Chopsticks-as-cache, then Subway ([PET#622](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/622), merged), which needed upstream Subway work to expose per-upstream timeouts and retries ([subway#203](https://github.com/AcalaNetwork/subway/pull/203), merged). I then added vitest fork-pool sharding ([PET#619](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/619), merged), applied in `runtimes` ([#1180](https://github.com/polkadot-fellows/runtimes/pull/1180), merged).

With those in place, I reworked the `runtimes` `test.yml` to run PET as a matrix with per-suite retry/timeout, Subway caching, and filtering to the runtimes under the Fellowship's purview ([#1068](https://github.com/polkadot-fellows/runtimes/pull/1068), merged).


### `try-runtime-cli`

Validation across an upgrade has a second side, which is the state itself. I remain the maintainer of [`try-runtime-cli`](https://github.com/paritytech/try-runtime-cli), which checks a runtime's storage invariants against live chain state before and after an upgrade. Over this period I updated dependencies, fixed CI, and cut releases. Where PET checks observable behaviour against a forked network, `try-runtime` checks that the state transition of the upgrade preserves the runtime's own invariants.


### Deepening: invariants, fuzzing, and formal methods on pallets

The natural extension of this work is into the pallets themselves, before they reach a runtime. When a pallet destined for a system chain is under review, I now test it with a layered approach, applied directly in `polkadot-sdk`.

The first layer is `do_try_state`: runtime invariants encoding a pallet's accounting and structural assumptions, so a violation is caught during an upgrade. I contributed these to `pallet-recovery` ([#12490](https://github.com/paritytech/polkadot-sdk/pull/12490), awaiting review), and to `pallet-psm` while reviewing a stablecoin pallet authored by an external team ([#12154](https://github.com/paritytech/polkadot-sdk/pull/12154), awaiting review).

Invariants over a single snapshot cannot express properties that depend on a history of operations, so the second layer is state-aware fuzzing: a fuzzer that reads pallet state before each call and checks trajectory properties across a run ([#12155](https://github.com/paritytech/polkadot-sdk/pull/12155), awaiting review). The third, where the arithmetic warrants it, is formal methods: I modelled pallet state machines in Quint, applied Kani for bounded verification, and used hax with Lean to prove properties over unbounded integers. On the PSM review, a Lean proof that its decimal conversion cannot inflate value removes that class of bug from the test surface entirely. I have written this up in internal posts, which will be published once the underlying work is open-source.


### Fellowship salary migration to Hollar

Beyond SDK and runtime code, I applied the same testing to a Fellowship operational change. The Fellowship is migrating salary payments from USDT to Hollar. I wrote an E2E suite for the salary pallet ([PET#650](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/650)) and a [script](https://gist.github.com/rockbmb/29d2a8e514b3be63467019c461793012) that runs the next salary cycle under Hollar against forked Polkadot state.

The script found that Hollar is not a sufficient asset on Asset Hub: members without a DOT existential deposit would have their salary payout XCM fail silently. I wrote a [guide](https://hackmd.io/@rockbmb/ByLjpbjXMl) with the `forceAssetStatus` fix and its test procedure. A fellow used it to file the remediation, since executed: Fellowship [#574](https://collectives.subsquare.io/fellowship/referenda/574) whitelisting OpenGov [#1920](https://polkadot.subsquare.io/referenda/1920), making Hollar sufficient before the migration reached members.


### Security working group

I am a member of the Fellowship security working group, with access to its private findings repositories. During this period I used the testing methodology above to independently reproduce a known, previously-audited issue in a core pallet, and reported it through the working group. Details are in the group's private repositories.


### Public commentary

I authored a public [forum post](https://forum.polkadot.network/t/re-introducing-polkadot-ecosystem-tests-pet/17723) on PET, setting out how the suite works and inviting parachain teams to adopt it for their own runtimes, since the suites are chain-agnostic. The further posts on the invariant and formal-methods work stay internal while that work is closed-source, to be published once it can be opened.


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

Thanks to [ggwpez](https://collectives.subsquare.io/user/16a357f5Sxab3V2ne4emGQvqJaCLeYpTMx3TCjnQhmJQ71DX/fellowship), [Bryan Chen](https://collectives.subsquare.io/user/14DsLzVyTUTDMm2eP3czwPbH53KgqnQRp3CJJZS9GR7yxGDP/fellowship), [seadanda](https://collectives.subsquare.io/user/142zGifFwRrDbFLJD7LvbyoHQAqDaXeHjkxJbUVwmDYBD7Gf/fellowship), and [kianenigma](https://collectives.subsquare.io/user/1eTPAR2TuqLyidmPT9rMmuycHVm9s9czu78sePqg2KHMDrE/fellowship) for review and collaboration across the SDK, Fellowship runtimes, PET, and Chopsticks.
