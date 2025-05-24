# Argument-0005: Promotion to Rank II

|                  |                            |
| ---------------- | -------------------------- |
| **Report Date**  | 2025/05/21                 |
| **Submitted by** | Pablo Andrés Dorado Suárez |

## Member Details

- **Matrix Username:** `@pandres95:bloque.team`
- **Polkadot Address:** `12gMhxHw8QjEwLQvnqsmMVY1z5gFa54vND74aMUbhhwN6mJR`
- **Current Rank:** 1
- **Date of Initial Induction:** [2023/11/12](https://collectives.subsquare.io/fellowship/referenda/38)
- **Date of Last Report:** [2025/04/29](https://github.com/polkadot-fellows/Evaluations/blob/main/evidence/pandres95/00004-2025-04-retain-rank-1.md)
- **Areas of Expertise:** Assets, Governance, Collectives, FRAME
- **Areas of Interest:** XCM, Bridges, Consensus

## Reporting Period

- **Start Date:** 2024/05/19
- **End Date:** 2025/05/20

## Argument

Since joining the Fellowship I have worked to make Polkadot easier to use and safer to upgrade. Below I explain the main things I built or helped ship over the past year and why they matter. All work lines up with the goals for Rank II in _Fellowship Manifesto § 6.3.1_.

### Assets Tooling

I contributed to push the boundaries of Assets, onto a full set of pallets that let parachains lock, hold and slowly release any non-native asset without writing custom code:

- **[`pallet-assets-freezer`](https://github.com/paritytech/polkadot-sdk/pull/3951)** freezes balances on assets accounts. Enables support for assets vesting.
- **[`pallet-assets-holder`](https://github.com/paritytech/polkadot-sdk/pull/4530)** adds an on-chain escrow. It powers staking rewards and pay-as-you-go services.
- **[`pallet-assets-vesting`](https://github.com/paritytech/polkadot-sdk/pull/7404)** (in review) provides a linear staking mechanism for assets accounts. Especially good for teams, grants and crowd-loans.

### Governance and Collective Tools

I **co-authored** (alongside @olanod) the Iterable Tracks, completing the proof-of-concept **[PSDK #2072](https://github.com/paritytech/polkadot-sdk/pull/2072)**, adjusting minor changes in the representing types, and later fixed a metadata bug **[PSDK #7671](https://github.com/paritytech/polkadot-sdk/pull/7671)** so dApps show tracks correctly.

I also **co-authored** (with @xlc) **[RFC 117 – Unbrick Collective](https://github.com/polkadot-fellows/RFCs/pull/117)**. This new collective would let the network restart a parachain that stops producing blocks. Discussion is paused hold until some conversations about changes derived from JAM are resolved, as well as the support for XCM cross-chain origins are ready.

### Runtime Upgrades

I helped ship three Fellowship runtime bumps:

- **[`stable2409-2`](https://github.com/polkadot-fellows/runtimes/pull/490)**
- **[`stable2409-4`](https://github.com/polkadot-fellows/runtimes/pull/568)**
- **[`stable2412-4`](https://github.com/polkadot-fellows/runtimes/pull/606)**

These upgrades moved chains to the SDK version `stable2412`. I also implemented a WFC that requested moving control of the Kusama Treasury “burn” to OpenGov **[runtimes #511](https://github.com/polkadot-fellows/runtimes/pull/511)**.

### Knowledge Sharing

I wrote **[“How to upgrade your runtime to the latest Polkadot-SDK (and not die trying)”](https://forum.polkadot.network/t/guide-how-to-upgrade-your-runtime-to-the-latest-version-of-polkadot-sdk-and-not-die-trying/13016)**. The guide walks parachain devs through common upgrade traps and fixes. I also review pull requests and discuss RFCs in Matrix frequently.

### Reflection

This year I moved from single-issue fixes to owning larger parts of the code that many chains rely on. I work independently, ship code that passes expert review and share what I learn. Moving to Rank II will let me take on bigger tasks—especially in consensus research and FRAME dev-experience—while staying accountable to the Fellowship.

## Voting Record

| Ranks | Activity | Agreement | My voting record | Notes |
|-------|----------|-----------|------------------|-------|
| I     | 90 %     | N/A       | N/A              | No Rank-I votes this year; counts as 100 % activity. |
| II    | 80 %     | N/A       | —                | —     |
| III   | 70 %     | 100 %     | —                | —     |
| IV    | 60 %     | 90 %      | —                | —     |
| V     | 50 %     | 80 %      | —                | —     |
| VI    | 40 %     | 70 %      | —                | —     |
