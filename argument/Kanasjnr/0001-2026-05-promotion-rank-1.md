# Argument-0001: Promotion to Rank I


|                  |                  |
| ---------------- | ---------------- |
| **Report Date**  | 2026/05/25       |
| **Submitted by** | Nasihudeen Jimoh |


## Member details

- Matrix username: @kanas0:[matrix.org](http://matrix.org)
- Polkadot address: **12pCUGSwoW4Xek48TLUHCFhrvAdjmciMMLJoRJD8HWP5saXH**
- Current rank: Candidate 
- Date of initial induction: 2025/10/31
- Date of last report: N/A
- Area(s) of Expertise/Interest: FRAME, XCM, Omni-Node, System parachain runtimes

## Reporting period

- Start date: 2025/11/01
- End date: 2026/05/25

## Argument

I am Nasihudeen Jimoh (`Kanasjnr` on GitHub), a Fellowship **Candidate** inducted on **2025/10/31**, seeking promotion to **Rank I (Dan 1)**. My work since induction has focused on `polkadot-sdk` and, where it affects live networks, `polkadot-fellows/runtimes` , improving FRAME developer experience, transaction validation, benchmarking accuracy, bridge tooling, and system-chain configuration.

Per [Manifesto §6.2.1](https://github.com/polkadot-fellows/manifesto/blob/main/manifesto.pdf), promotion to Rank I requires **three clear examples of modest but substantial contribution** to protocol development, among other qualities (independence, component involvement, protocol awareness). Below I address those requirements directly.

### Three substantial contributions (merged)

#### 1. `#[stored]` procedural macro for FRAME storage types

[polkadot-sdk#10195](https://github.com/paritytech/polkadot-sdk/pull/10195) introduces a `#[stored]` attribute that collapses the repetitive derives, `scale_info`/`codec` attributes, and trait bounds required when defining pallet storage types.

**Why it matters:** Storage definitions are a daily task for runtime developers; the previous pattern was verbose and easy to get wrong (especially around `MaxEncodedLen` and phantom types). This is a **non-trivial simplification** of a core FRAME workflow similar in spirit to improving the ergonomics of a language primitive used across every runtime.

#### 2. Migrate deprecated `async-std` to `tokio` in bridge relay crates

[polkadot-sdk#11214](https://github.com/paritytech/polkadot-sdk/pull/11214) removes the deprecated `async-std` dependency from the workspace and migrates affected **bridges/relays** crates (`equivocation-detector`, `finality-relay`, `messages-relay`, `parachains-relay`, `relay-substrate-client`, `relay-utils`, `substrate-relay-helper`) to **tokio** primitives already used elsewhere in the workspace.

**Why it matters:** Bridge relayers are operationally important for trust-free connectivity; keeping their async stack on a maintained runtime avoids security/maintenance drift and aligns the codebase with workspace standards.

#### 3. Metadata-based Aura authority ID detection in Omni-Node

[polkadot-sdk#11107](https://github.com/paritytech/polkadot-sdk/pull/11107) adds optional **metadata-based detection** of the correct Aura authority ID type (ed25519 vs sr25519) instead of hard-coding assumptions per chain (e.g. Asset Hub vs others).

**Why it matters:** Wrong authority ID typing produces subtle, chain-specific failures in node tooling. Deriving the type from runtime metadata makes Omni-Node more correct and less error-prone for operators and integrators.

### Additional merged work (supporting)

Deprecation cleanup as part of [polkadot-sdk#11561](https://github.com/paritytech/polkadot-sdk/issues/11561), following review guidance to land **one removal per PR**:

- [polkadot-sdk#12146](https://github.com/paritytech/polkadot-sdk/pull/12146) — removes `WeightMeter::defensive_saturating_accrue` (use `consume`)
- [polkadot-sdk#12145](https://github.com/paritytech/polkadot-sdk/pull/12145) — removes `polkadot_runtime_common::NegativeImbalance` (use `fungible::Credit`)
- [polkadot-sdk#12131](https://github.com/paritytech/polkadot-sdk/pull/12131) — removes `parachains_common::ToStakingPot` (use `ResolveTo`)
- [polkadot-sdk#12169](https://github.com/paritytech/polkadot-sdk/pull/12169) — removes `frame_support::EnsureOneOf` (use `EitherOfDiverse`)
- [polkadot-sdk#12158](https://github.com/paritytech/polkadot-sdk/pull/12158) — removes deprecated `sp_core` hashing re-exports (use `sp_crypto_hashing`)

Further merged removals under #11561 may land separately; see open PRs below.

### Ongoing work

I have further [open PRs in polkadot-sdk](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AKanasjnr+is%3Aopen) and [polkadot-fellows/runtimes](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3AKanasjnr+is%3Aopen), including more deprecation removals for #11561.

### Commitment

I intend to continue contributing to core `polkadot-sdk` and Fellowship runtimes, including #11561 and other in-flight work. I will increase participation in Fellowship channels and RFC discussion as my rank allows.

[All merged polkadot-sdk PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AKanasjnr+is%3Amerged).

## Voting record

N/A — Candidate; not yet eligible for Fellowship referenda voting activity thresholds.


| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments  |
| ----- | ------------------- | -------------------- | -------------------------- | --------- |
| I     | 90%                 | N/A                  | N/A                        | Candidate |
| II    | 80%                 | N/A                  |                            |           |
| III   | 70%                 | 100%                 |                            |           |
| IV    | 60%                 | 90%                  |                            |           |
| V     | 50%                 | 80%                  |                            |           |
| VI    | 40%                 | 70%                  |                            |           |


## Misc

- Question(s): 
- Concern(s):
- Comment(s):

