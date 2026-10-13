# Argument-0004: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/09/22)                                                             |
| **Submitted by**| Rodrigo Quelhas                                                                             |


## Member details

- Matrix username: @romarq:matrix.org
- Polkadot address: 12fiMKJP9t3gTFpHEXGYtdbZzwQciCpUcVFRnVXU4JYQLWvA
- Current rank: I
- Date of initial induction: 2025/10/06
- Date of last report: 2026/06/08
- Link to last report: [Evaluations#300](https://github.com/polkadot-fellows/Evaluations/pull/300), decided in fellowship referendum [#556](https://collectives.subsquare.io/fellowship/referenda/556)
- Area(s) of Expertise/Interest: FRAME, Parachain Consensus


## Reporting period

- Start date: 2026/06/08
- End date: 2026/09/22


## Argument

The deprecation of `ValidateUnsigned` ([**PR #10150**](https://github.com/paritytech/polkadot-sdk/pull/10150)) merged during the previous period. A deprecation only pays off when the callers move, so this period I turned it into a migration across the SDK, landed two pieces of work that were still in flight at the last report, and followed the migration through to the client libraries that have to submit the transactions it changes.

### Migrating pallets to `#[pallet::authorize]`

[**PR #13032**](https://github.com/paritytech/polkadot-sdk/pull/13032) migrated `pallet-election-provider-multi-block` and merged on 2026/09/16. It is the first pallet of this wave to land, and it sets the pattern the rest follow: the validation logic moves unchanged into an authorize callback, `ensure_none` becomes `ensure_authorized`, the offchain worker builds an authorized transaction, and the runtime gains `frame_system::AuthorizeCall` in its extension pipeline.

Seven further migrations are open and awaiting review:

| PR | Pallet |
|---|---|
| [#12795](https://github.com/paritytech/polkadot-sdk/pull/12795) | `pallet-sassafras` |
| [#12973](https://github.com/paritytech/polkadot-sdk/pull/12973) | `pallet-babe` |
| [#12974](https://github.com/paritytech/polkadot-sdk/pull/12974) | `pallet-grandpa` |
| [#12975](https://github.com/paritytech/polkadot-sdk/pull/12975) | `pallet-beefy` |
| [#12978](https://github.com/paritytech/polkadot-sdk/pull/12978) | `pallet-election-provider-multi-phase` |
| [#13077](https://github.com/paritytech/polkadot-sdk/pull/13077) | `polkadot-runtime-parachains::disputes::slashing` |
| [#13243](https://github.com/paritytech/polkadot-sdk/pull/13243) | `polkadot-runtime-common::claims` |

`claims` ([#13243](https://github.com/paritytech/polkadot-sdk/pull/13243)) needed more than a mechanical conversion. It is the first migrated pallet whose transactions come from end users rather than from a node, and it is live on Polkadot and Kusama. The claims page runs on polkadot-js, which cannot submit a general transaction today, so a straight cut-over would have broken the claim flow on the day the fellows adopted it. The PR therefore keeps the deprecated path beside the new one, so both a bare and a general transaction stay valid and are validated by the same code. A follow-up removes the old path once the clients are ready, and before the SDK removes the attribute after April 2027.

### Following the migration through to the clients

A migrated call must be submitted as a general transaction (extrinsic v5, RFC-84) that carries no signature, because the pallet's own callback authorizes it. While preparing `claims` I checked the three main clients. [polkadot-js](https://github.com/polkadot-js/api) has no general path: an unsigned submission builds a bare extrinsic. [subxt](https://github.com/paritytech/subxt) reaches the general form only through its signing flow, and its unsigned constructor emits a bare extrinsic. [PAPI](https://github.com/polkadot-api/polkadot-api) can build one, because its v3 transaction creator needs no signer, but it ships no ready-made creator for this case.

I reported this to the client teams:

- [polkadot-js/api#6276](https://github.com/polkadot-js/api/issues/6276): submit a call as a general transaction with no signer, and select the form by validation.
- [polkadot-js/apps#12446](https://github.com/polkadot-js/apps/issues/12446): the claims page needs that path.
- [polkadot-api/polkadot-api#760](https://github.com/polkadot-api/polkadot-api/issues/760): the concrete use case the maintainer had asked for, and a defect report. PAPI's shipped transaction validity decoder stops at `BadSigner`, so `UnknownOrigin`, the variant a client needs for the fallback, decodes as an unknown error.

### Tooling and dependencies

The `subxt` bump from 0.44 to 0.50 ([**PR #12096**](https://github.com/paritytech/polkadot-sdk/pull/12096)) merged on 2026/07/15. It was parked at the last report, waiting on the upstream fix I contributed in [subxt#2236](https://github.com/paritytech/subxt/pull/2236). The bump refactors `pallet-revive-eth-rpc`, `frame-benchmarking-cli` and `polkadot-omni-node-lib` onto the block-anchored client API and the split error types.

The CI check for workspace dependency inheritance ([**PR #11422**](https://github.com/paritytech/polkadot-sdk/pull/11422)) merged on 2026/07/16. It keeps member crates from pinning their own versions of shared dependencies, which previously caused duplicate versions in the build graph.

### Carried over

Two contributions from earlier periods remain open and are kept current: the `pallet-mixnet` migration ([#11010](https://github.com/paritytech/polkadot-sdk/pull/11010)) and the multi-block migration that clears a storage prefix across blocks ([#10436](https://github.com/paritytech/polkadot-sdk/pull/10436)).


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100% voting activity). | 82 fellowship referenda were opened during this period. Every one of them was on a track that requires rank III or above to vote, so none was open to a Rank I member. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
