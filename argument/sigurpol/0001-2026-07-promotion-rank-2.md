# Argument-0001: Fast Promotion to Rank II

|                  |                  |
| ---------------- | ---------------- |
| **Report Date**  | 2026/07/30       |
| **Submitted by** | Paolo La Camera  |


## Member details

- Matrix username: @paolo:parity.io
- Polkadot address: 15JDUd4QXoArDgwzkAFhSnFvV8LSwAXE7t1A5gpaGoEc5qDE
- Current rank: 0 (Candidate)
- Date of initial induction: 2026/01/26
- Date of last report: N/A
- Area(s) of Expertise/Interest: staking


## Reporting period

- Start date: 2025/04/01
- End date: 2026/07/30


## Argument

I am requesting an exceptional fast promotion from Candidate directly to Rank II.

I have worked on Polkadot full-time since April 2025 and have been a Candidate since January 2026, so this request is short of the interval the Manifesto expects between ranks. The basis is not the interval but the area I already own: **staking on Polkadot**, where I have been lead developer since the start of 2026.

### 1. DAP — delivered, and live on Polkadot

I was the lead developer responsible for delivering the **Dynamic Allocation Pool (DAP)**: halting the losses from a reward system that paid far more than securing the validator set required, landing the budgeted model that replaces it, and laying the ground for what follows — operational costs denominated in stablecoin, and beyond. I delivered it against a [fixed schedule](https://forum.polkadot.network/t/polkadot-staking-changes-progress-timeline/17436), Phase 1 by mid-March and Phase 2 through Q2, both on time: designing and implementing directly, reviewing the team's output, setting priorities, driving the rollout from the SDK through Westend to Polkadot, addressing issues found during audit, and communicating the change to the community and major stakeholders.

My own contributions start with the pallets themselves: I designed and implemented the first version of `pallet-dap` ([#10576](https://github.com/paritytech/polkadot-sdk/pull/10576)) and of `pallet-dap-satellite` ([#10597](https://github.com/paritytech/polkadot-sdk/pull/10597) - now generalized into `pallet-accumulate-and-forward`). From there I owned DAP's money-flow half: issuance accounting for the pre-funded buffer ([#10957](https://github.com/paritytech/polkadot-sdk/pull/10957)), slashed bounty and referendum deposits routed into DAP instead of destroyed ([#11716](https://github.com/paritytech/polkadot-sdk/pull/11716)), XCM delivery fees kept out of the staking pot ([#11700](https://github.com/paritytech/polkadot-sdk/pull/11700)), production weight metering ([#11811](https://github.com/paritytech/polkadot-sdk/pull/11811)), and the design issues that settled where burns, fees and slashes route ([#11408](https://github.com/paritytech/polkadot-sdk/issues/11408), [#11409](https://github.com/paritytech/polkadot-sdk/issues/11409), [#11410](https://github.com/paritytech/polkadot-sdk/issues/11410), [#11704](https://github.com/paritytech/polkadot-sdk/issues/11704)). 

On the rest of DAP deliverables, I was lucky to have an **exceptional team member** in **Ankan**, who developed the budget distribution, the drip-funded era pots ([#11616](https://github.com/paritytech/polkadot-sdk/pull/11616)), the traits behind the budget split ([#11513](https://github.com/paritytech/polkadot-sdk/pull/11513)) and the validator self-stake incentive ([#11651](https://github.com/paritytech/polkadot-sdk/pull/11651), [#11979](https://github.com/paritytech/polkadot-sdk/pull/11979)). Reviewing, contributing and challenging that work — and learning from him while doing it — was one of the real pleasures of this half of the year.

### 2. Release engineering and cross-cutting SDK work

**Releases 2.1.0 and 2.1.1.** DAP Phase 1 could only reach Polkadot through a Fellowship runtime release, and that release first needed the SDK bumped from `stable2507` to `stable2512` — a painful upgrade. I drove it end to end: the dependency bump ([runtimes#1059](https://github.com/polkadot-fellows/runtimes/pull/1059)), the compilation fixes across both relay chains, both Asset Hubs, coretime, bridge-hub, people and glutton ([runtimes#1062](https://github.com/polkadot-fellows/runtimes/pull/1062), 152 files), the follow-up move to SDK 2512-2 ([runtimes#1084](https://github.com/polkadot-fellows/runtimes/pull/1084)), and the release preparation itself carrying the DAP Phase 1 changes ([runtimes#1065](https://github.com/polkadot-fellows/runtimes/pull/1065), 104 files).

**Release 2.3.1.** I drove this patch release ([runtimes#1205](https://github.com/polkadot-fellows/runtimes/pull/1205)), cut to pin the nomination-pools unbonding bound across the fast-unbond flip on Asset Hub Polkadot ([runtimes#1201](https://github.com/polkadot-fellows/runtimes/pull/1201)). 

Outside staking, I also fixed the Kusama Asset Hub recovery benchmarks, where the time-delay guards could not be satisfied under the benchmarking feature ([runtimes#1183](https://github.com/polkadot-fellows/runtimes/pull/1183)).

**Benchmarking correctness in the SDK.** I fixed a timing leak that counted bulk setup operations into measured time, eventually tracing the root cause to the linker dropping the jemalloc shim on Linux ([#10802](https://github.com/paritytech/polkadot-sdk/pull/10802), [#10947](https://github.com/paritytech/polkadot-sdk/pull/10947), [#11069](https://github.com/paritytech/polkadot-sdk/pull/11069), [#11114](https://github.com/paritytech/polkadot-sdk/pull/11114)).

**Smaller cross-cutting work.** Removing the dead governance and treasury surface left on the Westend relay chain after AHM ([#11763](https://github.com/paritytech/polkadot-sdk/pull/11763), [#11796](https://github.com/paritytech/polkadot-sdk/pull/11796), [#11843](https://github.com/paritytech/polkadot-sdk/pull/11843)), and making the CI that gates runtime changes faster and wider in coverage ([#10972](https://github.com/paritytech/polkadot-sdk/pull/10972), [#11158](https://github.com/paritytech/polkadot-sdk/pull/11158)).

Most of this is not staking work. I include it because the Manifesto weighs contributions on more than their subject matter: §4.5.2 counts timeliness — "was the functionality delivered at the optimum time for maximum value to be extracted through its existence?" — among the criteria for code contributions; §4.5.3 asks that "the individual is persistently and consistently making themselves available for the support of the network"; and §6.3 expects a member at this rank to be "a core part of the team". Taking on work outside my own domain because a deadline depended on it is where those qualities are tested.

### 3. Closing AHM technical debt around session keys

**Setting session keys on Asset Hub.** After AHM, validators still had to set their session keys on the Relay Chain even though staking itself had moved to Asset Hub. I developed and delivered the path that lets them set keys on Asset Hub instead, and deprecated the Relay-Chain route: a refundable storage deposit so the operation is paid for and reclaimable ([#11222](https://github.com/paritytech/polkadot-sdk/pull/11222), [#11168](https://github.com/paritytech/polkadot-sdk/pull/11168)), consumer-reference tracking and deposit release for externally set keys ([#11197](https://github.com/paritytech/polkadot-sdk/pull/11197)), and a key-ownership proof across the boundary ([#11255](https://github.com/paritytech/polkadot-sdk/pull/11255)). I shipped it in the Fellowship runtimes ([runtimes#1101](https://github.com/polkadot-fellows/runtimes/pull/1101)), had the public documentation updated to match ([polkadot-docs#1550](https://github.com/polkadot-developers/polkadot-docs/issues/1550), [#1551](https://github.com/polkadot-developers/polkadot-docs/issues/1551)), and communicated the change to validators directly, working through the issues they hit. Every Polkadot validator now goes through this interface.

**The `StakingOperator` proxy.** I introduced a proxy type that lets validators delegate day-to-day staking operations without exposing their stash, then hardened it and shipped it in the Fellowship runtimes ([#10980](https://github.com/paritytech/polkadot-sdk/pull/10980), [#11203](https://github.com/paritytech/polkadot-sdk/pull/11203), [runtimes#1093](https://github.com/polkadot-fellows/runtimes/pull/1093)). This mattered once the minimum validator self-stake rose to 10,000 DOT, to ease validators' compliance.

### 4. Availability and network maintenance

The Manifesto (§6.3) asks a member at this rank to be "demonstrating a readiness to be a network maintainer through increased levels of availability", and adds that "excellent candidates will already be 'on-call' for the components of which they have a deep understanding". Four concrete instances:

#### The Asset Hub election stall (2026-06-30)

A referendum lowering the chilling threshold to 32% chilled 67 under-bonded validators, which dropped the best achievable election score below a static `MinimumScore` floor. No solution could be accepted, and era progression, reward payouts and unbonding froze.

I owned this end-to-end: diagnosis, the fast-tracked on-chain fix ([referendum 1914](https://polkadot.subsquare.io/referenda/1914)), reimbursement of the honest community miner whose deposits were slashed during the stall ([referendum 1915](https://polkadot.subsquare.io/referenda/1915)), public and internal communication throughout, and the follow-up hardening work it identified. Resolved in three days. I then published the [post-mortem](https://forum.polkadot.network/t/2026-06-30-staking-election-stall-postmortem/18077) on the Polkadot Forum: ~4,500 words on timeline, root cause, remediation and the five systemic improvements it produced, written to be legible to validators and nominators as well as to protocol engineers.
It is also what I put forward for the second Rank II requirement, "At least one published long-form semi-technical article concerning Polkadot" (§6.3.1).

#### Kusama AHM blocker

A staking issue found during the Kusama Asset Hub migration needed an immediate solution. I replaced automatic era pruning with an [explicit lazy-pruning extrinsic](https://github.com/paritytech/polkadot-sdk/pull/9632), shipped it, and built a standalone bot so eras could be cleaned up. I then added automatic support in the staking-miner bot.

#### Society collusion

When a Society member was found to have claimed membership without proof-of-ink, I co-authored the [`kick_member` extrinsic](https://github.com/paritytech/polkadot-sdk/pull/11154) for the Founder and shipped the runtime side ([runtimes#1101](https://github.com/polkadot-fellows/runtimes/pull/1101)) the same week, so remediation was possible while it still mattered. Outside my area, but it needed doing.

#### Day to day

I am the staking team's public interface: the go-to contact in multiple validator Matrix rooms, for W3F, and for major ecosystem operators.

### 5. Fixing security issues

I triaged and fixed multiple reports against staking from external auditing and the bug-bounty programme, covering slashing logic — cancelled slashes still applicable through `apply_slash`, and `cancel_deferred_slash` failing when the same offence is re-reported at a slightly higher fraction — unbounded `BufferedOffences` storage letting an attacker outrun slashing, bags-list rebagging abuse, arbitrary decrease of the relay-chain consumer count, and a panic reachable by a malicious solution miner.

Other fixes include `can_inc_consumer` silently blocking session-key rotation for max-consumer accounts ([#11573](https://github.com/paritytech/polkadot-sdk/pull/11573)), a role-blind `reap_stash` allowing batch-reaping of live stakers ([#12199](https://github.com/paritytech/polkadot-sdk/pull/12199)), and a nomination-pools reward-snapshot ordering bug where `set_commission_max` could destroy accrued rewards ([#12397](https://github.com/paritytech/polkadot-sdk/pull/12397)).

This work also reaches me from outside staking, and I take it when it is urgent. For example, most recently I was pinged about `pallet-society` failing to return the funds of discarded payouts to the Society pot, and fixed it ([#12590](https://github.com/paritytech/polkadot-sdk/pull/12590)).

### 6. The off-chain election solver (staking miner)

I am the sole developer of [`polkadot-staking-miner`](https://github.com/paritytech/polkadot-staking-miner), which computes the validator election off-chain and submits a NPoS solution to select the validator set, and I am the person on call for it in production.

I rewrote it completely so it works against `pallet-election-provider-multi-block` and `pallet-staking-async`: a new architecture around long-lived connections, multi-page submission, automatic deposit reclaim, [lazy era pruning](https://github.com/paritytech/polkadot-staking-miner/pull/1158), a [malicious-solution mode](https://github.com/paritytech/polkadot-staking-miner/pull/1187) to exercise the verifier's rejection path, and a [min-score guard](https://github.com/paritytech/polkadot-staking-miner/pull/1291) so honest miners are not slashed. I then took it to production: deployment on Westend, Paseo, Kusama and Polkadot Asset Hub, retirement of the old miner, and the dashboards, metrics and alarms that page me when an election fails.

### References

- Polkadot SDK: https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Asigurpol
- Fellowship runtimes: https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Asigurpol
- Staking miner: https://github.com/paritytech/polkadot-staking-miner/pulls?q=is%3Apr+author%3Asigurpol


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | N/A | |
|II |80%   |N/A   |   | |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Acknowledgements

Thanks to [kianenigma](https://collectives.subsquare.io/user/1eTPAR2TuqLyidmPT9rMmuycHVm9s9czu78sePqg2KHMDrE/fellowship) and Ankan for introducing me to the beauty of staking, for the reviews, the invaluable help, and for trusting me with it; to Jonas Gehrlein for the economic grounding and vision behind the DAP work; and to [ggwpez](https://collectives.subsquare.io/user/16a357f5Sxab3V2ne4emGQvqJaCLeYpTMx3TCjnQhmJQ71DX/fellowship) and [seadanda](https://collectives.subsquare.io/user/142zGifFwRrDbFLJD7LvbyoHQAqDaXeHjkxJbUVwmDYBD7Gf/fellowship) for the guidance, help and review across the Fellowship runtimes and the Asset Hub migration. Thanks to [claravanstaden](https://collectives.subsquare.io/user/12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8/fellowship) and [pandres95](https://collectives.subsquare.io/user/12gMhxHw8QjEwLQvnqsmMVY1z5gFa54vND74aMUbhhwN6mJR/fellowship) in particular for the support through the SDK 2512 upgrade and the 2.1.0 release, and to [bkchr](https://collectives.subsquare.io/user/13fvj4bNfrTo8oW6U8525soRp6vhjAFLum6XBdtqq9yP22E7/fellowship) for the review and guidance on the benchmarking fixes. Thanks also to the other Fellowship members I have had the pleasure of working with over this period.
