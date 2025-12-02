# Argument-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/07/27                                                                                  |
| **Submitted by**| Ludovic Domingues                                                                           |


## Member details

- Matrix username: @krayt78:matrix.org
- Polkadot address: 14AgwoPjcRiEEJgjfHmvAqkjdERCG26WEvQUoGLuBzcXKMS2
- Current rank: Candidate
- Date of initial induction: 2024-06-18
- Date of last report: N/A
- Area(s) of Expertise/Interest: 
    - FRAME
    - Runtime


## Reporting period

- Start date: 2024-06-18
- End date: 2025-07-01


## Argument
Hi Everyone ! I am Ludo, ex game dev, web3 dev for 4 years in the EVM ecosystem, i joined polkadot through the PBA-5 Singapore in 2024 where i was inducted as a candidate by Shawn.
Since then, I have been contributing to the Polkadot SDK. I am now working at PBA as the technical program specialist. 
Below are my most relevant and impactful contributions:

### 1. Improving Security & Economic Soundness: Session Key Deposit

In [PR #7953](https://github.com/paritytech/polkadot-sdk/pull/7953), I implemented an optional deposit mechanism for setting session keys. This tackled a long-standing concern (raised as early as 2021) around the lack of economic cost for key spamming, which only required the Existential Deposit. My solution enables chains using `pallet-session` to configure a deposit via `Hold`, improving spam prevention and aligning with the ecosystem’s values of economic rationality and protection against misuse. This contribution responds directly to an issue open in the [☂️ AHM-Kusama] Tracking Issue for Staking ([#8764](https://github.com/paritytech/polkadot-sdk/issues/8764)) and is now available for parachains and system chains to adopt.

### 2. Ensuring Runtime Correctness: Validator Nomination Sanity

While collaborating on the async-staking pallet, I discovered that users could nominate non-existent validators without error. This silent failure could lead to user confusion and misconfigured nominations. I corrected this behavior in [PR #8436](https://github.com/paritytech/polkadot-sdk/pull/8436), ensuring the runtime returns an error when a validator does not exist. In doing so, I also had to update multiple unit tests that unintentionally relied on broken logic, with guidance from Kian and Paolo. This change strengthens the integrity of the staking system and improves the developer and user experience across the ecosystem.

### 3. Ecosystem-Wide Benchmarking Refactors: FRAME Benchmarking V2

To help drive adoption of FRAME Benchmarking V2 (an initiative led by Oliver to modernize benchmarking syntax) I contributed refactors to 10+ pallets (e.g., [#6564](https://github.com/paritytech/polkadot-sdk/pull/6564), [#6612](https://github.com/paritytech/polkadot-sdk/pull/6612)). These contributions brought legacy code up to date with the new syntax, improving readability, consistency, and maintainability across the runtime.

### 4. Refactoring Bloated Pallets: Long-Term Maintainability

At Shawn’s suggestion and following an observation by Xiliang, I took on the task of modularizing large pallets that had grown unwieldy (e.g., over 1000 LOC). I broke down key modules such as `staking` and `session` into logical subcomponents ([#6746](https://github.com/paritytech/polkadot-sdk/pull/6746), [#6780](https://github.com/paritytech/polkadot-sdk/pull/6780)), improving overall code clarity and easing onboarding for future contributors. This work aligns with the Fellowship’s expectations around insightful refactoring and technical stewardship.

### 5. DX-Focused Architecture Work: Umbrella Crate Migration

In support of developer ergonomics, I helped migrate several pallets to the new `polkadot-sdk-frame` umbrella crate, ensuring unified prelude/type exports and simplifying imports for downstream users ([#6925](https://github.com/paritytech/polkadot-sdk/pull/6925), [#8285](https://github.com/paritytech/polkadot-sdk/pull/8285)). This effort was crucial in making FRAME more accessible to newcomers and reducing friction in SDK usage.

## Voting record

None, I am currently a Fellowship Candidate and do not yet have voting privileges.