# Argument-0001: Fast Promotion to Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/11/10                                                                                  |
| **Submitted by**| Rohit Sarpotdar                                                                             |
| **Sponsored by**| Branislav Kontur (bkontur), Adrian Catangiu (acatangiu)                                     |

## Member details

- Matrix username: @rohit:parity.io
- Polkadot address: [143KKEzwsyjmTAjjpk75mCM4DYopmXTM52s6Lnj8udvX9Pxf](https://polkadot.subsquare.io/user/143KKEzwsyjmTAjjpk75mCM4DYopmXTM52s6Lnj8udvX9Pxf/identity)
- Current rank: Rank 0 (Candidate)
- Date of initial induction: 2025/11/10
- Date of last report: N/A
- Link to last report: N/A
- [Subsystems](https://github.com/polkadot-fellows/Evaluations/blob/main/subsystems.md) developed/maintained: System chains (Bulletin Chain), Trustless bridges, Nodes (light clients, SDK)
- Area(s) of Expertise/Interest: Bulletin Chain, Web3 Storage, Bridges, smoldot, Polkadot SDK, JAM Gray Paper

## Reporting period

- Start date: 2025/02/04
- End date: 2026/11/12

## Argument

I am applying for a fast promotion to **Rank 2, II Dan: Proficient Member**. Since joining Parity in February 2025, all of my work has been on Polkadot core technology: first and still mainly the Polkadot↔Kusama bridge, then the Bulletin system chain, Web3 Storage and smoldot.

### Polkadot↔Kusama bridge: maintenance, testing and the path to light clients

My first area at Parity was **trustless bridges**, and the live Polkadot↔Kusama bridge is still where most of my maintenance work goes. I am the regular release engineer for the Bridge Hub runtimes that carry it. I have shipped ten runtime releases, from Bridge Hub Kusama 1.6.1 to Bridge Hub Polkadot 2.5.0 (for example [#3191](https://github.com/paritytech/parity-bridges-common/pull/3191) and [#3323](https://github.com/paritytech/parity-bridges-common/pull/3323)).

Most of my recent bridge work went into making **Fellowship runtime upgrades testable end to end**. The Polkadot↔Kusama asset-transfer test used to be a manual, shell-driven script in the Fellowship runtimes repository. I moved the bridge integration tests to Rust on `zombienet-sdk` ([parity-bridges-common #3276](https://github.com/paritytech/parity-bridges-common/pull/3276), [#3293](https://github.com/paritytech/parity-bridges-common/pull/3293)), then ported the Polkadot↔Kusama test itself ([#3299](https://github.com/paritytech/parity-bridges-common/pull/3299)). It spawns both relay chains with their Bridge Hubs and Asset Hubs, runs real relayers, and checks that DOT and KSM cross the bridge in both directions and that relayers are rewarded. The test now runs against the released Fellowship runtimes, and CI regenerates it on every new Fellowship release ([#3305](https://github.com/paritytech/parity-bridges-common/pull/3305)), so each runtime upgrade is exercised on a working bridge before it reaches the network. This has already paid off: after Asset Hub Polkadot 2.5.0 introduced a new transaction extension, the suite broke, and I traced it to subxt and fixed it ([#3330](https://github.com/paritytech/parity-bridges-common/pull/3330)). All of these were reviewed by bkontur.

Earlier bridge work laid the ground for this. I added bridging support to Asset Hub Westend and wrote the initial AssetHub bridging primitives ([polkadot-sdk #7831](https://github.com/paritytech/polkadot-sdk/pull/7831), [#8063](https://github.com/paritytech/polkadot-sdk/pull/8063)), the groundwork for bridging centred on AssetHub. I also strengthened the on-chain invariant checks of `pallet-xcm-bridge` and `pallet-xcm-bridge-hub` ([#8546](https://github.com/paritytech/polkadot-sdk/pull/8546), [#8615](https://github.com/paritytech/polkadot-sdk/pull/8615), reviewed by acatangiu, bkontur and serban300), which `try-runtime` uses to catch corrupted bridge state before a runtime upgrade reaches the network.

The next step is to let relayers run on **smoldot light clients** instead of full RPC nodes that someone has to operate ([parity-bridges-common #3270](https://github.com/paritytech/parity-bridges-common/issues/3270)). Dropping the RPC node also drops the operator you would otherwise have to trust. The light-client relayer needs GRANDPA finality justifications from smoldot ([smoldot #3363](https://github.com/paritytech/smoldot/pull/3363), merged after review by bkchr and skunert, and [#3369](https://github.com/paritytech/smoldot/pull/3369), in review), corresponding relay-client changes in polkadot-sdk ([#13150](https://github.com/paritytech/polkadot-sdk/pull/13150), [#13546](https://github.com/paritytech/polkadot-sdk/pull/13546), in review), and a smoldot side-car for the zombienet tests ([#3320](https://github.com/paritytech/parity-bridges-common/pull/3320), in progress).

### Bulletin Chain: data renewal

Bulletin Chain is a system chain that provides temporary storage for the Polkadot ecosystem. It keeps data only for a fixed retention period, after which the data expires. Without renewal, anyone who needs data to persist has to resubmit it themselves, which makes the chain impractical for most real uses. I contributed to the subsystem that addresses this.

I first implemented renewal by content hash and **automatic renewal** ([bulletin #313](https://github.com/paritytech/polkadot-bulletin-chain/pull/313)). Users renew data by its content hash instead of a fragile `(block, index)` position, and can opt in to auto-renewal, which a mandatory inherent processes every block. Renewing many items in one inherent exposed a bug two layers down in shared client code: `sc-client-db` silently kept only the last renewal for each extrinsic index. I traced the bug and fixed it upstream with a new `DbExtrinsic::MultiRenew` variant ([polkadot-sdk #11474](https://github.com/paritytech/polkadot-sdk/pull/11474), reviewed by bkontur, karolk91 and skunert). The fee model came next: renewals are feeless, paid from the user's storage authorization, charged once at registration and never twice ([#504](https://github.com/paritytech/polkadot-bulletin-chain/pull/504)). Auditing the `on_initialize` weight ensures renewal load cannot endanger block production ([#512](https://github.com/paritytech/polkadot-bulletin-chain/pull/512)).

As the feature grew, renewal logic was tangled into the transaction-storage pallet, which made both pallets harder to reason about. I proposed splitting renewal into a dedicated **`pallet-bulletin-data-renewal`**, secured team sign-off, and carried it out myself ([#571](https://github.com/paritytech/polkadot-bulletin-chain/pull/571), reviewed by franciscoaguirre and karolk91). The storage pallet now exposes a small public API and an `OnObsoleteTransactions` hook. The renewal pallet never touches its storage directly, so each invariant stays with the pallet that owns it, and a runtime can leave renewal out entirely ([#738](https://github.com/paritytech/polkadot-bulletin-chain/pull/738)). The split shipped with a storage migration and wiring for the westend and paseo runtimes.

Getting the pallet to release meant moving the chain to polkadot-sdk `stable2606` ([#662](https://github.com/paritytech/polkadot-bulletin-chain/pull/662)), on a node release that also fixes a storage leak when data is renewed twice and then pruned. I worked on the Fellowship pre-release preparation ([#718](https://github.com/paritytech/polkadot-bulletin-chain/issues/718)) and wired the renewal pallet into the Fellowship runtimes staging fork ([bkontur/runtimes #32](https://github.com/bkontur/runtimes/pull/32)). My most recent change, [#760](https://github.com/paritytech/polkadot-bulletin-chain/pull/760) (in review), fixes an accounting bug I found, where renewing the same content within its retention period counted its bytes twice.

### Web3 Storage and other contributions

On **Web3 Storage**, the storage protocol proposed to succeed Bulletin, I implemented the separation of bucket creation from provider assignment ([#446](https://github.com/paritytech/web3-storage/pull/446)). I then led the staged removal of two registry pallets, moving every client's metadata into the bucket itself ([#512](https://github.com/paritytech/web3-storage/pull/512), [#509](https://github.com/paritytech/web3-storage/pull/509)). Storage providers that leave the network needed a way out, so I proposed a graceful wind-down process ([#281](https://github.com/paritytech/web3-storage/issues/281)).

In 2026 I reviewed more than 65 pull requests by others on the bridges, Bulletin and Web3 Storage. I document what I build: the developer docs site for Web3 Storage ([#452](https://github.com/paritytech/web3-storage/pull/452)) and the Authorization & Incentives architecture document for Bulletin. I also wrote a semi-technical article on Bulletin's storage authorizations, which explains the renewal design to the wider community.

### Conclusion

Rank 2 asks for primary responsibility for implementing a major protocol component, reviewed by experts and included in a functional implementation, and a long-form semi-technical article (Manifesto §6.3.1). I believe my work meets these expectations. I have been the main person keeping the Polkadot↔Kusama bridge released and tested across Fellowship runtime upgrades, and I am taking it towards light-client relayers. On Bulletin Chain, I contributed much of the data-renewal work, from its first extrinsic and an upstream client-database fix to the pallet split I designed and its integration into the Fellowship runtimes, and I wrote a long-form article explaining that design. My Web3 Storage work, reviewing and documentation show a broad understanding of the protocol and the availability expected of a network maintainer.

### References

All my code contributions can be found through my GitHub profile (https://github.com/rosarp); the most important links are below.

- **Parity Bridges Common:** https://github.com/paritytech/parity-bridges-common/pulls?q=is%3Apr+author%3Arosarp+
- **Bulletin Chain:** https://github.com/paritytech/polkadot-bulletin-chain/pulls?q=is%3Apr+author%3Arosarp+
- **Polkadot SDK:** https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Arosarp+
- **smoldot:** https://github.com/paritytech/smoldot/pulls?q=is%3Apr+author%3Arosarp+
- **Web3 Storage:** https://github.com/paritytech/web3-storage/pulls?q=is%3Apr+author%3Arosarp+

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | N/A | As a Rank 0 Candidate, I was not eligible to vote on any referenda during the reporting period. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
