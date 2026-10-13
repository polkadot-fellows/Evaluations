# Argument-0002: Retention at Rank II

|                  |                   |
| ---------------- | ----------------- |
| **Report Date**  | 2026/09/25        |
| **Submitted by** | Josep M Sobrepere |

## Member details

- Matrix username: @josepot:matrix.org
- Polkadot address: 15roJ4ZrgrZam5BQWJgiGHpgp7ShFQBRNLq6qUfiNqXDZjMK
- Current rank: Rank 2 (Proficient)
- Date of initial induction: 2026/06/09 (Candidate; promoted to Rank II via [Argument-0001](0001-josepot-promotion-rank-2.md))
- Date of last report: 2026/06/09
- Area(s) of Expertise/Interest: Standard RPCs (new JSON-RPC spec), light clients, transaction/extrinsic format design, developer-facing protocol APIs, runtime upgrade tooling.

## Reporting period

- Start date: 2026/06/09
- End date: 2026/09/25

## Argument

I am applying for retention at **Rank II: Proficient Member**. This is my first period as a member, and I used it to move from ecosystem tooling towards changes to the protocol itself: two Fellowship RFCs, one reference implementation of one of them in `polkadot-sdk`, a `pallet-utility` fix, and continued work on Polkadot-API (PAPI), the application-layer implementation of the standard JSON-RPC API.

### 1. Two RFCs in `polkadot-fellows/RFCs`

Both RFCs come from problems I hit while implementing transaction tracking in PAPI, and both target the boundary between runtime, node and light client.

**[RFC-0173: Prevent Transaction Replay After Account Reaping via `CheckCreatedAtHeight`](https://github.com/polkadot-fellows/RFCs/pull/173)** (opened 2026/07/01)

- *Problem:* when an account is reaped its nonce resets to 0. If it is re-funded, any previously signed transaction can be replayed. That includes immortal transactions and mortal ones inside their window. A dishonest block author can also replay a transaction inside the same block. As a result, a transaction hash is not a safe unique identifier, which complicates every inclusion-tracking API.
- *Proposal:* a per-account `created_at_height`, exposed via a runtime API (`AccountCreatedAtHeightApi`), and a `CheckCreatedAtHeight` transaction extension that carries it as an implicit (signed but not encoded) value. The extrinsic size does not grow, and previously signed transactions become permanently invalid if the account lifecycle changes.
- *Review:* the RFC received substantive feedback from 8+ participants ([discussion](https://github.com/polkadot-fellows/RFCs/pull/173)): offline-signer impact, unsigned extrinsics such as `Timestamp::set` not getting unique hashes (@voliva), storage placement options (@Kanasjnr, @PolkadotDom), and its overlap with [polkadot-fellows/runtimes#248](https://github.com/polkadot-fellows/runtimes/issues/248) (@bkchr). I revised it on 2026/07/02 in response: I defined the runtime API so the RFC no longer depends on a storage implementation, restructured the storage options (A/B/C) as implementation considerations, and clarified the limits of the tx-hash uniqueness guarantee. The RFC is still open.
- *Downstream interest:* @Nathy-bajo cited it as a prerequisite for hash-based transaction lookup in [json-rpc-interface-spec#182](https://github.com/paritytech/json-rpc-interface-spec/pull/182).

**[RFC-0174: Light client extrinsics-trie inclusion proof request](https://github.com/polkadot-fellows/RFCs/pull/174)** (opened 2026/07/13)

- *Problem:* a light client can only learn whether its transaction was included by downloading whole block bodies, which is wasteful bandwidth as blocks grow. This was first raised in [RFCs#19](https://github.com/polkadot-fellows/RFCs/issues/19) in 2023 and was blocked on the extrinsics trie using `state_version` 0.
- *Proposal:* [RFC-0042](https://github.com/polkadot-fellows/RFCs/blob/main/text/0042-extrinsics-state-version.md) already moved Polkadot and its system chains to `state_version` 1, which unblocked this. The RFC adds a light-client request that returns every leaf of a block's extrinsics trie, either verbatim or as a hash when the value is 33 bytes or more. The light client recomputes `extrinsics_root` and checks it against the header. That gives trustless inclusion and non-inclusion proofs, plus the extrinsic index, with no body download and no change to the runtime.
- *Review:* approved by @skunert ("Downloading the blocks just to send API consumers their transaction events for example is pure bandwidth waste") and @carlosala. Their review comments (reimplementing `ordered_trie_root` with mixed value/hash leaves, the response size limit, keeping it decoupled from RFC-0009) were resolved in the text.

### 2. Reference implementation in `polkadot-sdk`

- **[polkadot-sdk#12644: Serve light-client extrinsics-trie inclusion proof requests (RFC-0174)](https://github.com/paritytech/polkadot-sdk/pull/12644).** This is the full-node side of RFC-0174 in `sc-network-light`: new `RemoteReadExtrinsicsRequest`/`Response` messages and the protocol name bump `/light/2` to `/light/3`, with the older names kept as fallbacks. The PR also covers the design decisions the RFC leaves open. The trie `state_version` is recovered by recomputing the root from the body, so the handler still works after state pruning. The response has an all-or-nothing 16 MiB cap. Unknown, pruned or mismatching blocks are answered with an absent field, never an error. Tests include unit, handler-level, and an end-to-end `sc-network-test` where a peer verifies inclusion over a real libp2p `/light/3` substream without requesting the block body. The PR has approvals from @skunert, @bkchr, @ggwpez, @rockbmb and @sigurpol. It is intentionally held until RFC-0174 is merged.
- **[polkadot-sdk#12534: `pallet-utility`: fix dispatch class of empty `batch`/`batch_all`/`force_batch`](https://github.com/paritytech/polkadot-sdk/pull/12534)** (merged 2026/07/03). The dispatch-class fold started from an `Operational` accumulator, so an empty batch was classified `Operational` instead of `Normal`. This is a correctness fix in FRAME with a regression test.

### 3. Polkadot-API (PAPI)

I continued as technical lead of [PAPI](https://github.com/polkadot-api/polkadot-api). This period saw the [3.0.0 (2026/08/18)](https://github.com/polkadot-api/polkadot-api/releases) and [3.1.0 (2026/09/01)](https://github.com/polkadot-api/polkadot-api/releases) releases, following the 2.1.x/2.2.x line. My own merged PRs:

- [#1408](https://github.com/polkadot-api/polkadot-api/pull/1408) and [#1418](https://github.com/polkadot-api/polkadot-api/pull/1418): custom signed-extension support in `getPjsTxHelper` and `getTxHelper` (`tx-utils`). This is the practical counterpart of my `createTransaction` RFC ([polkadot-js/api#6213](https://github.com/polkadot-js/api/issues/6213)), so signers can handle chain-specific extensions.
- [#1426](https://github.com/polkadot-api/polkadot-api/pull/1426): performance improvement for `getValues` in the client, after a user report ([#1420](https://github.com/polkadot-api/polkadot-api/issues/1420)).

I also reviewed and gave feedback on the team's and community's PRs, including the v3 release candidates ([#1411](https://github.com/polkadot-api/polkadot-api/pull/1411), [#1413](https://github.com/polkadot-api/polkadot-api/pull/1413), [#1430](https://github.com/polkadot-api/polkadot-api/pull/1430)), the rename of the signer packages to `tx-creator` ([#1412](https://github.com/polkadot-api/polkadot-api/pull/1412)), the `tx-utils` mortality fix ([#1403](https://github.com/polkadot-api/polkadot-api/pull/1403)), and the known-chains update ([#1402](https://github.com/polkadot-api/polkadot-api/pull/1402)).

### 4. Community engagement

I answered technical questions on the RFCs above and on ecosystem issues, for example [PAPI#1436](https://github.com/polkadot-api/polkadot-api/issues/1436) and [PAPI#1434](https://github.com/polkadot-api/polkadot-api/issues/1434), and contributed to discussions in [polkadot-fellows/runtimes#1233](https://github.com/polkadot-fellows/runtimes/pull/1233) and [json-rpc-interface-spec#185](https://github.com/paritytech/json-rpc-interface-spec/pull/185).

### Relation to the Rank II requirements

I take my Rank II justification from [Argument-0001](0001-josepot-promotion-rank-2.md). During this period I kept meeting it in these ways:

- **Primary individual responsible for the formalisation, implementation, or analytical improvement of a major component:** I continued to lead PAPI, and I am the sole author and implementer of RFC-0173, RFC-0174 and the RFC-0174 SDK implementation.
- **Participation in Fellowship processes:** I proposed two RFCs through the Fellowship's RFC process, revised them following public review, and shipped the reference implementation for one of them.
- **Engagement with Polkadot's technical direction:** both RFCs address gaps I found through PAPI and light-client work, and both are in the Manifesto's scope (standard RPCs, light-client sync, transaction format, runtime and node APIs).

## Voting record

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments              |
| ----- | ------------------- | -------------------- | -------------------------- | --------------------- |
| I     | 90%                 | N/A                  | N/A                        | No eligible referenda |
| II    | 80%                 | N/A                  | 0 of 0 (100%)              | No eligible referenda |
| III   | 70%                 | 100%                 |                            | N/A                   |
| IV    | 60%                 | 90%                  |                            | N/A                   |
| V     | 50%                 | 80%                  |                            | N/A                   |
| VI    | 40%                 | 70%                  |                            | N/A                   |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s): RFC-0173 is still open and under discussion. I am happy to address further feedback or a change of direction (for example towards the approach in runtimes#248) before it is finalised.
