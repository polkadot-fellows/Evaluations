# Argument-0007: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/08/09                                                                                  |
| **Submitted by**| Sergej Sakac                                                                                |


## Member details

- Matrix username: @sergej.sakac:parity.io
- Polkadot address: 126X27SbhrV19mBFawys3ovkyBS87SGfYwtwa8J2FjHrtbmA
- Current rank: II
- Date of initial induction: Seeding
- Date of last report: 2026/05/25
- Area(s) of Expertise/Interest: Polkadot runtime, Coretime, PSM, On-demand, XCM


## Reporting period

- Start date: 2026/05/26
- End date: 2026/08/09


## Argument

During this reporting period, my work was focused on pUSD, Coretime and AHMv2.

### pUSD

- **Multi-instance PSM**: Completed the rework of `pallet-psm` from a single, governance-seeded PSM into a multi-instance design where PSMs are created permissionlessly and managed by their own admins ([tracking issue](https://github.com/paritytech/polkadot-sdk/issues/12134)). Creation became permissionless with per-instance admins in [polkadot-sdk#12206](https://github.com/paritytech/polkadot-sdk/pull/12206), and the rework was completed in [polkadot-sdk#12245](https://github.com/paritytech/polkadot-sdk/pull/12245). Follow-ups currently in review: correcting the creation-deposit footprint ([polkadot-sdk#12811](https://github.com/paritytech/polkadot-sdk/pull/12811)), unifying the decimal-scaling logic ([polkadot-sdk#12842](https://github.com/paritytech/polkadot-sdk/pull/12842)), and multi-instance fungibles support in the PSM remote tests ([polkadot-sdk#11950](https://github.com/paritytech/polkadot-sdk/pull/11950)).
- **Broader pUSD work**: Beyond `pallet-psm`, I have been working on the pUSD project more generally.

### Coretime

- **Auto-renewal fix**: Found and fixed a live bug on Polkadot Coretime where `enable_auto_renew` could charge a task for an unrelated task's renewal: [polkadot-sdk#12750](https://github.com/paritytech/polkadot-sdk/pull/12750). Core assignments are rebuilt every region, so `PotentialRenewals` can hold records for the same core index belonging to different tasks, which `enable_auto_renew` didn't account for. This actually occurred on Polkadot, where task 3428 ended up [paying for task 2094's renewal](https://coretime-polkadot.subscan.io/event/4766580-87). The fix also cleans up the mismatched record currently on-chain.
- **RFC-17 implementation**: Continued working on the implementation of [RFC-17](https://github.com/polkadot-fellows/RFCs/blob/main/text/0017-coretime-market-redesign.md). The new `pallet-coretime-market`, implementing the `Market` trait with a clearing-price Dutch auction, is under review ([polkadot-sdk#11802](https://github.com/paritytech/polkadot-sdk/pull/11802)), and the `fp-coretime` primitives crate, extracting the shared market types and traits out of `pallet-broker`, was merged ([polkadot-sdk#11810](https://github.com/paritytech/polkadot-sdk/pull/11810)).

### AHMv2

- **On-demand ordering on the Coretime chain**: As part of removing user-facing functionality from the relay chain, I have been working on moving on-demand Coretime ordering from the relay chain to the Coretime chain ([polkadot-sdk#12715](https://github.com/paritytech/polkadot-sdk/issues/12715)).

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | No referenda available for my rank during this period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
