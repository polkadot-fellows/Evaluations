# Argument-0001: Promotion to Rank II

|                  |              |
| ---------------- | ------------ |
| **Report Date**  | 2026/06/09   |
| **Submitted by** | Victor Oliva |

## Member details

- Matrix username: @voliva:matrix.org
- Polkadot address: 16JGzEsi8gcySKjpmxHVrkLTHdFHodRepEz8n244gNZpr9J
- Current rank: Rank 0 (Candidate)
- Date of initial induction: 2026/06/09
- Date of last report: N/A
- Area(s) of Expertise/Interest:

  - Developer tooling
  - Runtime and node API ergonomics
  - FRAME pallet UX

## Reporting period

- Start date: 2024/02/01
- End date: 2026/06/09

## Argument

I am applying for fast promotion to **Rank II: Proficient Member**. I believe this is justified by my sustained work on Polkadot as a core developer of Polkadot-API since February 2024, spanning more than two years of contribution, together with direct contributions to Polkadot SDK and related ecosystem projects.

My strongest evidence for Rank II is my ongoing ownership and development work in **Polkadot-API**, where I have contributed to the developer-facing infrastructure used to interact with Polkadot SDK-based chains. This work is directly relevant to runtime interaction, standard RPC usage, transaction construction, metadata/codegen, runtime compatibility, storage/event subscriptions, signer abstractions, and upgrade-safe client behaviour.

In May 2024, I attended the in-person Polkadot Blockchain Academy in Singapore, where I graduated with distinction from the protocol track: [PBA graduation certificate on Asset Hub Polkadot](https://assethub-polkadot.subscan.io/nft_item/171-20).

### Polkadot-API

Since February 2024, I have worked as a core developer of Polkadot-API.

During this time, I have opened [over 250 PRs](https://github.com/polkadot-api/polkadot-api/pulls?q=author%3Avoliva) in the repository, mainly covering development work, API design, maintenance, releases, issue triage, and ecosystem support. My biggest contributions have been in API design, runtime safety through the compatibility API, bundle-size improvements, CLI and codegen architecture and ink!/Revive contracts support.

Most important contributions:

- [Compatibility API](https://github.com/polkadot-api/polkadot-api/pull/549)

  I worked on Polkadot-API’s runtime compatibility layer, including static compatibility checks, generated-descriptor compatibility checks, reporting of compatibility changes and granular detection of changes across runtime updates. This helps applications handle runtime upgrades and metadata changes more safely.

- [Typed Signed Extensions](https://github.com/polkadot-api/polkadot-api/pull/1226)

  I implemented typed signed extensions support, improving type safety around transaction construction and making custom signed-extension handling more explicit for advanced users.

- Performance and size improvements: [#502](https://github.com/polkadot-api/polkadot-api/pull/502), [#504](https://github.com/polkadot-api/polkadot-api/pull/504), [#516](https://github.com/polkadot-api/polkadot-api/pull/516)

  I improved descriptor generation and loading by decoupling descriptor types from values, lazy-loading descriptor values, compacting generated descriptors, and reducing memory usage when updating multiple chains.

- [CLI refactor into new architecture](https://github.com/polkadot-api/polkadot-api/pull/304)

  I improved the CLI/codegen workflow substantially, including whitelisting, automatic codegen after chain changes, generating from the metadata of a specific block, and more robust CLI error handling.

- [Revive contract support](https://github.com/polkadot-api/polkadot-api/pull/717)

  I worked on typed contract support in Polkadot-API, including the ink-contracts package, TypeScript support for ink! and later Revive contract interactions, event decoding, nested storage queries, as well as Solidity support.

- [Event API redesign](https://github.com/polkadot-api/polkadot-api/pull/1267)

  I contributed to the event API and subscription layer, including a TypedAPI event interface redesign and `watchBest` event support.

- Meta-signers: [multisig signer](https://github.com/polkadot-api/polkadot-api/pull/880) and [proxy signer](https://github.com/polkadot-api/polkadot-api/pull/889)

  I contributed to signer infrastructure, including the multisig signer and proxy signer, which are higher-order signers that abstract away signing with a multisig or proxy account.

This is complemented by substantial maintenance work, including fixes, releases, issue triage, ecosystem support, and documentation, as well as initiating the development of the PAPI Console.

This work represents sustained ownership of a major developer-facing component, including API design, implementation, release work, compatibility maintenance, and support for downstream users.

### Polkadot SDK

I have also contributed directly to Polkadot SDK in areas related to contracts, RPC behaviour, and governance/runtime functionality.

- [[pallet-revive] add get_storage_var_key for variable-sized keys](https://github.com/paritytech/polkadot-sdk/pull/8274)

  This PR added support for retrieving storage variable keys for variable-sized keys in `pallet-revive`. The change supports contract developer tooling and is relevant to ink! v6 compatibility.

- [feat(revive): add contract instantiated event](https://github.com/paritytech/polkadot-sdk/pull/8789)

  This PR added an event for contract instantiation in `pallet-revive`, improving observability for contract lifecycle operations.

- [fix(rpc-spec-v2): best block not announced immediately after initialised](https://github.com/paritytech/polkadot-sdk/pull/10525)

  This PR fixed behaviour in `rpc-spec-v2` where the best block was not announced immediately after initialization. The fix improves RPC correctness and client-facing node behaviour.

- [[referenda] Add `slash_submission_deposit` extrinsic](https://github.com/paritytech/polkadot-sdk/pull/11524)

  This PR added a `slash_submission_deposit` extrinsic to `pallet-referenda`, contributing to governance/runtime functionality.

- [Treasury: update expire date on payout](https://github.com/paritytech/polkadot-sdk/pull/7959)

  I co-authored this PR, which updates treasury payout expiry logic so that expiry can be extended if the payout cannot be fulfilled.

Additionally, I have participated in issues and discussions, specifically in `pallet-revive` and foreign assets: [Polkadot SDK issues authored by me](https://github.com/paritytech/polkadot-sdk/issues?q=author%3Avoliva).

### Smoldot

My main Smoldot contribution was implementing [`state_getReadProof` support](https://github.com/paritytech/smoldot-archive/pull/2136).

This PR implemented the `state_getReadProof` RPC method in Smoldot. The motivation was to support storage-proof retrieval in Polkadot-API while preserving Smoldot/light-client compatibility. The implementation required working through proof retrieval, proof verification, multi-key proof handling, proof merging, and integration with Smoldot’s JSON-RPC and sync-service internals.

I have also opened issues that helped identify light-client correctness, performance, and developer-experience issues:

- [Starting smoldot with databaseContent takes longer than without it](https://github.com/paritytech/smoldot-archive/issues/2134)

  Reported a startup-performance issue where initializing Smoldot with an up-to-date `databaseContent` was slower than starting without it.

- [Repeated `operationInaccessible` on call `TaggedTransactionQueue_validate_transaction` for `System.apply_authorized_upgrade`](https://github.com/paritytech/smoldot-archive/issues/2089)

  Reported an issue where Polkadot-API transaction validation could get stuck around `operationInaccessible` responses when validating a large unsigned runtime-upgrade transaction through `TaggedTransactionQueue_validate_transaction`.

- [[JS] unable to import subpackages (`smoldot/worker`, `smoldot/bytecode`, etc.) with parcel](https://github.com/paritytech/smoldot-archive/issues/1923)

  Reported JS packaging issues affecting downstream bundlers and followed up with the package metadata fix in PR #1924.

- [Subscribing to a chain after it has been added for a while results in broken parent references](https://github.com/paritytech/smoldot-archive/issues/1788)

  Reported a `chainHead_v1_followEvent` correctness issue where `newBlock` events could be emitted with unmatched `parentBlockHash` if a chain had been added but left idle before subscribing.

- [`chainHead_unstable_follow` withRuntime=false emits `stop` shortly after `initialized`](https://github.com/paritytech/smoldot-archive/issues/1665)

  Reported a `chainHead_unstable_follow` issue where subscriptions with `withRuntime = false` stopped shortly after initialization.

### Acala Chopsticks

My Chopsticks contributions focused mainly on implementing and hardening support for the JSON-RPC interface spec, including `chainHead_v1`, `transaction_v1`, `chainSpec_v1`, and storage-query APIs used by modern Polkadot clients and tooling. The most important contributions are:

- [JSON RPC interface spec: chainHead_v1](https://github.com/AcalaNetwork/chopsticks/pull/813)

  Implemented support for the `chainHead_v1` JSON-RPC interface in Chopsticks. This improved Chopsticks compatibility with clients expecting the newer RPC interface spec.

- [feat: add transaction_v1 group of functions](https://github.com/AcalaNetwork/chopsticks/pull/819)

  Added the `transaction_v1` group of JSON-RPC functions, improving transaction submission compatibility with tooling that uses the modern RPC interface.

- [feat: add chainSpec_v1 group of functions](https://github.com/AcalaNetwork/chopsticks/pull/820)

  Added the `chainSpec_v1` group of JSON-RPC functions, improving chain-spec access through the newer RPC interface.

- [feat(chainHead_v1): operationWaitingForContinue and chainHead_v1_continue](https://github.com/AcalaNetwork/chopsticks/pull/838)

  Extended the `chainHead_v1` implementation with `operationWaitingForContinue` and `chainHead_v1_continue`, bringing Chopsticks closer to the expected behavior of the RPC interface spec.

- [feat: add support for chainHead_v1_storage hash queries](https://github.com/AcalaNetwork/chopsticks/pull/921)

  Added support for hash queries in `chainHead_v1_storage`, improving storage-query compatibility for clients using the new RPC interface.

Overall, these Chopsticks contributions improved compatibility between Chopsticks and modern Polkadot client tooling, particularly Polkadot-API. They are relevant to testing, simulation, and development workflows for Substrate/Polkadot-based chains.

### PolkaHub

I also led the development of [PolkaHub](https://github.com/polkadot-api/polkahub), a library designed to unify signers and wallets behind a single interface so they can be integrated more easily into applications.

PolkaHub supports predefined components as well as external components through plugins and composition. This work is relevant to wallet interoperability, signer UX, and application-level integration with Polkadot accounts and transactions.

### Forklift

As introduced in the [Polkadot Forum](https://forum.polkadot.network/t/forklift-a-tool-to-test-reorgs-locally/17589), I also led the development of Forklift: a Chopsticks-like tool designed to create local testing scenarios with multiple forks and chain heads.

Forklift allows tooling developers to test reorg-sensitive scenarios that were not possible with previous solutions such as Zombienet or Chopsticks. This is relevant to client correctness, `chainHead` behavior, fork handling, and testing tooling for applications that need to behave correctly under chain reorganization conditions.

### Published technical articles

I have published technical posts concerning Polkadot developer tooling, Revive contracts, signer UX, and light-client-based applications:

- [[Revive] Solidity contracts using a Polkadot signer](https://forum.polkadot.network/t/revive-solidity-contracts-using-a-polkadot-signer/14960)

  This post explains how to interact with Solidity contracts on Revive using Polkadot tooling. It covers the boundary between ABI-encoded contract data and SCALE-encoded runtime calls, `Revive.instantiate_with_code`, runtime API calls for gas and storage deposit estimation, and PAPI-based querying/submission flows.

- [[PAPI] Stateless Multisig Tool](https://forum.polkadot.network/t/papi-stateless-multisig-tool/12782)

  This post introduces a stateless multisig tool built with PAPI. It explains how the tool avoids indexer dependency by relying on on-chain data and URL parameters, how it coordinates multisig operations, and how PAPI can be used to build light-client-friendly tooling for practical governance and account-management workflows.

### Polkadot Blockchain Academy Instructor

I was an instructor at the Polkadot Blockchain Academy editions in Luzern and Bali in 2025, teaching new developers how to build applications and contribute effectively to the Polkadot ecosystem. This has also led to many new developers joining the ecosystem.

### Additional ecosystem background

I completed the Polkadot Blockchain Academy protocol track in [Singapore 2024 with distinction](https://assethub-polkadot.subscan.io/nft_item/171-20), where I learned about the development of Polkadot SDK.

Additionally, I have given technical talks at ecosystem events:

- Parachain Summit 2024: technical talk on the Compatibility API, including the challenge of circular references in metadata types.
- sub0 reset 2024: [Next Gen Devtools for Polkadot](https://youtu.be/aOyLhABWGOA?si=rlbB9KBpE8xhD7ro&t=349), introducing the PAPI Console to the ecosystem.

### Basis for Rank II promotion

I believe this application meets the expected standard for **Rank II** promotion. My contributions show sustained ownership of Polkadot developer tooling through Polkadot-API, direct merged contributions to Polkadot SDK, related work across Smoldot and Chopsticks, and published semi-technical material concerning Polkadot.

The basis for this request is not isolated PR activity. It is continued responsibility for tooling that developers use to interact with Polkadot, including API design, runtime compatibility, code generation, contracts support, signer infrastructure, client correctness, releases, and ecosystem support.

For the Rank II requirement of being primarily responsible for the implementation or analytical improvement of a major protocol component, my argument is based on sustained ownership of Polkadot-API’s protocol-facing interaction layer with Polkadot SDK-based chains.

This work is not generic application tooling. It sits at the boundary between applications and the Polkadot protocol, and depends directly on runtime metadata, standard RPC behaviour, transaction validity, storage proofs, signed extensions, runtime upgrades, `chainHead` behaviour, and client correctness. My related contributions to Polkadot SDK, Smoldot, and Chopsticks further show that I have improved underlying protocol-facing interfaces rather than only consuming them.

I intend to continue expanding my contributions to core Polkadot SDK work, especially around developer tooling and FRAME pallet developer experience.

### References

- **GitHub profile:** https://github.com/voliva
- **Polkadot-API PRs:** https://github.com/polkadot-api/polkadot-api/pulls?q=author%3Avoliva
- **Polkadot SDK PRs:** https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Avoliva
- **Polkadot SDK issues:** https://github.com/paritytech/polkadot-sdk/issues?q=author%3Avoliva
- **Smoldot PRs:** https://github.com/paritytech/smoldot-archive/pulls?q=author%3Avoliva
- **Smoldot issues:** https://github.com/paritytech/smoldot-archive/issues?q=is%3Aissue+author%3Avoliva
- **Chopsticks PRs:** https://github.com/AcalaNetwork/chopsticks/pulls?q=is%3Apr+author%3Avoliva
- **Chopsticks issues:** https://github.com/AcalaNetwork/chopsticks/issues?q=is%3Aissue+author%3Avoliva
- **Published articles:** https://forum.polkadot.network/u/voliva/activity/topics
- **PBA certificate:** https://assethub-polkadot.subscan.io/nft_item/171-20

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments                                                                                        |
| ----- | ------------------- | -------------------- | -------------------------- | ----------------------------------------------------------------------------------------------- |
| I     | 90%                 | N/A                  | N/A                        | As a Rank 0 Candidate, I was not eligible to vote on any referenda during the reporting period. |
| II    | 80%                 | N/A                  |                            | Target rank.                                                                                    |
| III   | 70%                 | 100%                 |                            | N/A                                                                                             |
| IV    | 60%                 | 90%                  |                            | N/A                                                                                             |
| V     | 50%                 | 80%                  |                            | N/A                                                                                             |
| VI    | 40%                 | 70%                  |                            | N/A                                                                                             |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
