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

One of the current pain points the ecosystem struggled with when I started working on this specific area was (and still is, partially) the lack of support of advanced capabilities for assets in the ecosystem. With the native DOT token you can (in addition to transfer) pay fees, vest, and stake, but also reserve it for voting, and even hold it for deposits. Clearly, in this scenario, assets (like the ones in Asset Hub) are treated as second-class citizens. Currently, the only _"advanced"_ capability assets have (other than transferring) is paying for fees. This is clearly insufficient, especially given the future prospect of having a Hub and chains that are able to configure its economics beyond a singular token.

To close this gap, I started by assessing the implementation state of `fungibles`, the set of traits that allowed achieving these capabilities. While regular inspection, mutation (issuing, burning), unbalances handling, and transferring were already implemented, two main traits were lacking formal implementation on `pallet-assets`: support for freezing and holding assets.

Freezing assets is a capability that enables use cases like voting using non-native assets, staking, and vesting. This led me to implement the **[`pallet-assets-freezer`](https://github.com/paritytech/polkadot-sdk/pull/3951)**, a pluggable component for `pallet-assets` that extends the its base functionality by implementing the freezing of balances.

In consequence, this implementation enabled the necessary support for implementing two additional components: [`pallets-asset-rewards`](https://github.com/paritytech/polkadot-sdk/pull/3926) (implemented by [@liamaharon](https://github.com/liamaharon), and already released), which allows (among others) incentivising the freezing (staking) of LP tokens, thus incentivising the usage of Asset Conversion, a key component in the Hub; but also **[`pallet-assets-vesting`](https://github.com/paritytech/polkadot-sdk/pull/7404)** (currently waiting for a secondary review), which provides a linear vesting mechanism for balances in assets accounts, analogous to the one existing in `pallet-vesting`. This is especially good for teams in the ecosystem (an example of this is vested acquisition of tokens in DAOs), grants and crowd-loans.

Holding assets is the ability that an external component has to withhold a balance, in such a way it can be burned (slashed) by the system. By designing, and implementing the **[`pallet-assets-holder`](https://github.com/paritytech/polkadot-sdk/pull/4530)** component, I aimed to close the final gap in the `fungibles` implementation, a process that also involved [a major refactor](https://github.com/paritytech/polkadot-sdk/pull/4530#discussion_r1708418726) of the balances model for Assets, since the previous model was not fully compliant with the [specification](https://paritytech.github.io/polkadot-sdk/master/frame_support/traits/tokens/fungible/index.html), a clear proof of an _analytical improvement of a major component of the protocol_.

Following to this _implementation_, now new case uses like depositing with assets are supported. Currently, I'm working on the preliminary design stage for an _implementation_ of the `Consideration` traits for `fungibles`, in such a way that, for example, sufficient assets might be eligible to be placed on hold for on-chain storage deposits, the same way it currently works with the native token.

### Governance and Collective Tools

I **co-authored** (alongside [@olanod](https://github.com/olanod)) the Iterable Tracks, completing the proof-of-concept **[PSDK #2072](https://github.com/paritytech/polkadot-sdk/pull/2072)**, adjusting minor changes in the representing types, and later fixed a metadata bug **[PSDK #7671](https://github.com/paritytech/polkadot-sdk/pull/7671)** so dApps show tracks correctly.

I also **co-authored** (with [@xlc](https://github.com/xlc)) **[RFC 117 – Unbrick Collective](https://github.com/polkadot-fellows/RFCs/pull/117)**. This new collective would let the network restart a parachain that stops producing blocks. Discussion is paused hold until some conversations about changes derived from JAM are resolved, as well as the support for XCM cross-chain origins are ready.

### Runtime Upgrades

One of the main responsibilities any Member of the Polkadot Technical Fellowship has (Manifesto, §2.3) is _any specific realisation of the Polkadot runtime_. This includes, but is not limited to the maintenance (realisation) of the _Polkadot business-logic_.

By choosing this task as part of my duties in the Fellowship, I achieved three main goals, all of them in line with the description of a Proficient Member (Manifesto §6.3):

- Demonstrate capacity to execute maintenance tasks: _"they should be demonstrating a readiness to be a network maintainer through increased levels of availability"_
- Evolving my contributions from an individual perspective, towards working alongside other members of the colective: _"communication/sharing is also very important"_, and
- Expanding my current understanding of the protocol as a whole, as well as the challenges involved on it: _"clear demonstration of knowledge of the protocol is crucial"_.

In consequence, during the last year, I have mainly contributed to the bumps of the Polkadot SDK in the runtimes for **[`stable2409-2`](https://github.com/polkadot-fellows/runtimes/pull/490)**, **[`stable2409-4`](https://github.com/polkadot-fellows/runtimes/pull/568)**, and **[`stable2412-4`](https://github.com/polkadot-fellows/runtimes/pull/606)**.

These upgrades moved chains to the SDK version `stable2412`, which enabled major functionality now live, like Async Backing, the Coretime auto-renew, or the transferring of Polkadot-native assets to Ethereum.

I also implemented a WFC that requested moving control of the Kusama Treasury “burn” to OpenGov **[runtimes #511](https://github.com/polkadot-fellows/runtimes/pull/511)**. This was a request from the Kusama Ecosystem, and while it's only current immediate effect is stopping the spreading of some percentage of the treasury _residuals_ instead of being burned to Kappa Sigma Mu, it also enables potential experiments, like funding teams in the community, or other related approaches, available for them via governance instead of by time-expensive runtime upgrades.

### Knowledge Sharing

I wrote **[“How to upgrade your runtime to the latest Polkadot-SDK (and not die trying)”](https://forum.polkadot.network/t/guide-how-to-upgrade-your-runtime-to-the-latest-version-of-polkadot-sdk-and-not-die-trying/13016)**. The guide walks parachain devs through common upgrade traps and fixes. I also review pull requests and discuss RFCs in Matrix frequently.

This guide solves one of the gratest painpoints for any team in the ecosystem, following the stabilization of the Polkadot SDK: what to have in mind when upgrading the SDK in a runtime they maintain. Since then, the article has had some positive feedback from members of the ecosystem.

Also, by including the section of `runtimes` maintenance, current and future members of the fellowship can take a prior look on how to perform these upgrades, as part of the aforementioned maintenance duties every Member should perform. This experience also contributes to the [ongoing discussion](https://github.com/polkadot-fellows/runtimes/issues/101#issuecomment-2911039576) regarding how to update the SDK on the runtime.

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
