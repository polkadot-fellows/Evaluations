# Argument-0006: Promotion to Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/05/25                                                                                  |
| **Submitted by**| Sergej Sakac                                                                                |


## Member details

- Matrix username: @sergej.sakac:parity.io
- Polkadot address: 126X27SbhrV19mBFawys3ovkyBS87SGfYwtwa8J2FjHrtbmA
- Current rank: I
- Date of initial induction: Seeding
- Date of last report: 2026/03/13
- Area(s) of Expertise/Interest: Polkadot runtime, Coretime, PSM, On-demand, XCM


## Reporting period

- Start date: 2024/02/16
- End date: 2026/05/25


## Argument

Since being seeded into the Fellowship at Rank I, my work has concentrated on two areas of the Polkadot protocol: the Agile Coretime model and its associated runtime pallets, and more recently the Peg Stability Module (PSM). Alongside this protocol work, I have for two years been leading RegionX, the user-facing tooling for Coretime in the ecosystem. The work below is what I am putting forward in support of promotion from Rank I to Rank II.



### Coretime protocol: pallet-broker and the RFC-17 redesign

I have contributed to `pallet-broker` and the surrounding Coretime code regularly since its introduction. Over the reporting period this covers both foundational pieces of Agile Coretime that are live on Polkadot today, and the in-progress redesign of the Coretime market.

On the foundational side, the most substantial pieces were the end-to-end implementation of Coretime auto-renew ([#4424](https://github.com/paritytech/polkadot-sdk/pull/4424)) and the implementation of on-demand credits from [RFC-1](https://github.com/polkadot-fellows/RFCs/blob/main/text/0001-agile-coretime.md) ([#5990](https://github.com/paritytech/polkadot-sdk/pull/5990)). Both are now part of the production Coretime pipeline. I also built the runtime-side machinery for XCM Coretime region transfers ([#3455](https://github.com/paritytech/polkadot-sdk/pull/3455)) that makes regions transferable across system chains, and added a sale-price runtime API on `pallet-broker`.

I authored [RFC PR #44: Rent-Based Registration Model](https://github.com/polkadot-fellows/RFCs/pull/44), proposing a sustainable on-demand parachain registration scheme based on a smaller initial deposit plus periodic rent and a hibernation stage. Although the RFC was eventually closed, the design discussion it kicked off informed subsequent thinking on para-lifecycle economics.

**Current focus, RFC-17 Coretime market redesign:**

One of my main current workstreams is the implementation of [RFC-17](https://github.com/polkadot-fellows/RFCs/blob/main/text/0017-coretime-market-redesign.md) (authored by Jonas Gehrlein), which redesigns the Coretime sale logic. The core piece is the new `pallet-coretime-market`, implementing the RFC-17 `Market` trait with a Dutch auction and a uniform clearing-price mechanism ([#11802](https://github.com/paritytech/polkadot-sdk/pull/11802)). Alongside this, I am pulling shared market types and traits out of `pallet-broker` into a new primitives crate, `fp-coretime` ([#11810](https://github.com/paritytech/polkadot-sdk/pull/11810)).


### RegionX

Outside of the SDK, I have for two years been leading RegionX. The [RegionX Hub](https://hub.regionx.tech/) is its primary application, used by teams across the ecosystem to interact with Agile Coretime.

### Other runtime contributions

Earlier polkadot-sdk work outside of Coretime includes runtime code-blob validation at the parachain registrar, which catches broken or malformed code at scheduling time rather than at activation ([#3232](https://github.com/paritytech/polkadot-sdk/pull/3232)), and permissioned contract deployment in `pallet-contracts` that lets the runtime configure which origins are allowed to deploy contracts ([#3377](https://github.com/paritytech/polkadot-sdk/pull/3377)).


### Peg Stability Module (PSM)

More recently I have also been contributing to the new Peg Stability Module (PSM), working on both the integration into the runtime and feature additions on the pallet itself.

The first major piece was integrating `pallet-psm` into Westend Asset Hub with pUSD as the stablecoin and remote integration tests ([#11529](https://github.com/paritytech/polkadot-sdk/pull/11529)). Alongside the integration I added the `MonetaryGuard` governance track that acts as the PSM circuit-breaker ([#11736](https://github.com/paritytech/polkadot-sdk/pull/11736)), and reworked the `InitializePsm` migration into an idempotent variant that can be safely re-applied. A further change allows the Emergency origin to adjust PSM max debt directly, without going through a full governance cycle ([#12012](https://github.com/paritytech/polkadot-sdk/pull/12012)). Smaller supporting cleanups around `UnionOf` metadata traits and PSM `AssetId` bounds also went in.

The main in-progress workstream is the multi-instance refactor of `pallet-psm`. The tracking issue lays out the roadmap to a permissionless `create_psm` end-state ([#12134](https://github.com/paritytech/polkadot-sdk/issues/12134)). The first PR moves per-instance config out of `Config` into a storage map as a behaviour-preserving first step ([#12088](https://github.com/paritytech/polkadot-sdk/pull/12088)), and a follow-up extends the pallet to support multiple PSMs in a single runtime, each with its own reserve account, debt ceiling, and circuit breaker ([#12174](https://github.com/paritytech/polkadot-sdk/pull/12174)). Alongside this I am extending the PSM remote tests for multi-instance fungibles and adding pUSD teleport support to People chain Westend.


### Design discussions, writing, and talks

- Earlier long-form forum writing on Coretime: [Building a Coretime Marketplace](https://forum.polkadot.network/t/building-a-coretime-marketplace/6661).
- Gave a talk on Coretime at Polkadot Decoded 2024 in Brussels.

## Conclusion

I have been contributing to Substrate and polkadot-sdk for several years, with work spanning the parachain registrar, Coretime, contracts pallet, and more recently PSM. I am asking the Fellowship to consider promoting me from Rank I to Rank II on the basis of this work.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | No referenda available for my rank during this period | |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
