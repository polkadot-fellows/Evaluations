# Argument-0001: Fast Promotion to Rank II

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2026/06/09 |
| **Submitted by** | Carlo Sala |

## Member details

- Matrix username: @carlosala:matrix.org
- Polkadot address: 16JskuojL6mSp6HNcjiHYa9jqksWbLD8L9YGWU1ppiPWQ9sa
- Current rank: Candidate
- Date of initial induction: 2026/06/09
- Date of last report: N/A
- Area(s) of Expertise/Interest:
  - Runtime metadata and runtime/off-chain communication
  - Transaction construction, signing flows, and transaction extensions
  - Light-client-first application and tool development
  - JSON-RPC interfaces and client behavior
  - Developer tooling and SDK ergonomics
  - Coordination between SDK/runtime changes and downstream tooling

## Reporting period

- Start date: 2024/01/01
- End date: 2026/06/09

## Argument

I am requesting an exceptional fast promotion from Candidate to Rank II.

I believe Rank II is the right place for my current work because my contributions are not limited to isolated tooling or small fixes. They sit at the boundary between the Polkadot protocol and the software that must correctly interpret it: runtime metadata, transaction construction, signing payloads, signed extensions, and the developer-facing APIs needed to build against Polkadot SDK chains without relying on centralized assumptions.

The major component I am putting forward is narrower than Polkadot-API as a whole: it is Polkadot's metadata-hash and merkleized-metadata verification path for offline signers, centered on [RFC #78: Merkleized metadata](https://github.com/polkadot-fellows/RFCs/pull/78), `CheckMetadataHash`, and the client/signing code that makes this protocol interface usable by wallets, hardware signers, and light-client applications. This area determines whether off-chain software can verify what it is signing without trusting an opaque metadata blob or a centralized RPC provider. Metadata and signing are not optional developer convenience layers: they are the basis for wallets, light clients, offline signers, and applications to submit correct transactions to Polkadot SDK chains.

The evidence below covers the full chain from RFC work and implementation to SDK corrections, Extrinsic V5 review, Polkadot-API integration, and knowledge sharing.

### Protocol-interface responsibility

I have worked on this area across design, implementation, maintenance, and correction of chain-side behavior.

In the Fellowship RFC process, I was a co-author of [RFC #78: Merkleized metadata](https://github.com/polkadot-fellows/RFCs/pull/78). The goal of this work is to let offline signers verify only the metadata needed for a transaction rather than trusting an opaque full metadata blob. This is directly connected to the security of transaction signing and to the ability of users to interact with Polkadot with reduced trust in external infrastructure.

I also implemented and maintain [`@polkadot-api/merkleize-metadata`](https://github.com/polkadot-api/polkadot-api/tree/main/packages/merkleize-metadata), which provides the concrete TypeScript implementation for Merkleizing `frame_metadata` according to RFC #78 and producing proofs for extrinsics and extrinsic parts. This is the implementation and downstream integration path that makes the RFC model usable by application developers, wallets, and signers.

The metadata and offline-signing work combines formalisation, implementation, and analysis. RFC #78 defines the Merkleized metadata approach; the Polkadot-API package implements it for real metadata and extrinsic payloads; and [RFC issue #148](https://github.com/polkadot-fellows/RFCs/issues/148) continues the analysis for Metadata V16 and Extrinsic V5. This follow-up is important because metadata and extrinsic formats evolve, and offline signers must still have the information needed to decode, verify, and explain what is being signed.

I also reviewed the Extrinsic V5 specification work in [RFC #124](https://github.com/polkadot-fellows/RFCs/pull/124), which is closely related to the same signing and metadata boundary. My review [requested changes](https://github.com/polkadot-fellows/RFCs/pull/124#pullrequestreview-2382224554) and included comments on keeping the RFC at the specification layer rather than tying it too closely to the initial SDK implementation, clarifying the SCALE encoding as a vector rather than a fixed-size array, explaining the `Bare` and `General` extrinsic variant layout, avoiding premature specification of a particular `VerifySignature`-style extension, and clarifying how Metadata V15 and Metadata V16 expose extrinsic-version information. This review is not the central component claim, but it is additional evidence that I work directly on the protocol-interface details that clients, wallets, signers, and runtime authors must implement consistently.

I have also contributed directly to `polkadot-sdk` where the protocol implementation boundary needed correction:

1. I fixed `frame-metadata` so that extrinsic types are collected before pallet types ([`frame-metadata` #110](https://github.com/paritytech/frame-metadata/pull/110)) and metadata v15 is generated correctly in `polkadot-sdk` ([`polkadot-sdk` #10592](https://github.com/paritytech/polkadot-sdk/pull/10592)). This was done to make `CheckMetadataHash` support Metadata V16 in a backwards-compatible way: signers and clients can continue to verify the Metadata V15 hash expected by RFC #78 while newer metadata versions expose the richer extrinsic information needed by the evolving transaction format. Runtime metadata is the contract that off-chain clients, wallets, signers, and tools use to understand runtime calls, types, signed extensions, and chain behavior, so preserving deterministic metadata generation is necessary for correct and sound offline verification. The SDK fix was important enough to be backported across multiple release branches.
2. I fixed an XCM payment issue where delivery fees could be subtracted twice ([#7201](https://github.com/paritytech/polkadot-sdk/pull/7201)). Correct XCM fee accounting is required for reliable cross-chain message execution and downstream tooling that estimates or explains XCM costs.
3. I fixed asset conversion in XCMPayment APIs ([#7134](https://github.com/paritytech/polkadot-sdk/pull/7134)). These runtime APIs are part of the boundary between system-chain behavior and off-chain software, and incorrect conversion creates wrong results for applications and users.

These contributions show the same responsibility from multiple angles: participating in the interface design, implementing the proof machinery, maintaining the signer/client integration path, and correcting SDK behavior when the metadata interface is wrong or incomplete.

### Polkadot-API as supporting evidence

The central Rank II component in this application is not Polkadot-API itself. I include PAPI as supporting evidence because it is where many protocol interfaces become usable by downstream applications: metadata decoding, typed runtime calls, transaction construction, signer integration, light-client-compatible providers, and releases.

This work shows a repeated pattern of taking protocol changes from Polkadot SDK and Fellowship RFCs, understanding their effect on off-chain software, and implementing the client/signing behavior needed by wallets, applications, and light-client users. Examples include [Metadata V16 support](https://github.com/polkadot-api/polkadot-api/pull/1025), [Extrinsic V5 support](https://github.com/polkadot-api/polkadot-api/pull/777), and [Ledger signer support](https://github.com/polkadot-api/polkadot-api/pull/720).

### Polkadot philosophy

The parts of Polkadot's philosophy most relevant to my work are: decentralization of technical decision-making, reducing trusted intermediaries, empowering users to verify and interact with the network themselves, protocol correctness, transparent governance, security, resilience, and the ability for the network to evolve without relying on a single off-chain authority.

My focus on light-client-first APIs, metadata proofs, and signing correctness is aligned with those goals: users and applications should be able to understand and verify what they sign without depending on trusted RPC providers, opaque metadata blobs, or centralized application backends.

### Knowledge Sharing

I have also presented this work publicly at Polkadot ecosystem events:

- [Build a Modern Dapp with Polkadot-API](https://youtu.be/fj63gYJmuIk), Polkadot Decoded 2024.
- [Next Gen Devtools for Polkadot](https://youtu.be/aOyLhABWGOA), sub0 reset 2024.
- [Ignite your Dapp with PAPI](https://youtu.be/MUlCusQDv1w), sub0 2025.

I have also taught at the Polkadot Blockchain Academy campus editions in Lucerne and Bali, covering both Fundamentals and Off-Chain modules ([public activity summary](https://forum.polkadot.network/t/sponsorship-for-active-devs-and-community-members-during-polkadot-symbiosis-in-buenos-aires/14723/74)). This teaching work brought the same runtime metadata, JSON-RPC, transaction-construction, and application-development knowledge into a structured educational setting for Polkadot builders.

These talks and teaching activities are not a substitute for the Rank II article requirement, but they show a sustained pattern of knowledge-sharing around the same technical area I am asking the Fellowship to evaluate: metadata-aware, type-safe, light-client-friendly interaction with Polkadot, especially around transaction construction and signing correctness.

**Requirement: primary individual responsible for the formalisation, implementation, or analytical improvement of a major component of the protocol.**

For Rank II, the component I am putting forward is Polkadot's metadata-hash and merkleized-metadata verification path for offline signers. This component includes:

- Runtime metadata as the machine-readable description of calls, types, signed extensions, and runtime interfaces.
- `CheckMetadataHash` and merkleized metadata proofs for offline signers, as described in RFC #78.
- The downstream signer/client integration required for wallets and signers to build payloads and verify metadata consistently.
- The analytical follow-up needed as Metadata V16 and Extrinsic V5 change the assumptions made by the original RFC.

I do not claim to be the sole inventor of every part of RFC #78 or of Polkadot metadata. Bastian was the RFC author and the Polkadot SDK implementation owner. My Rank II claim is that I have been a primary owner of the off-chain verification half of this protocol mechanism: turning RFC #78 and `CheckMetadataHash` into deterministic metadata digest and proof generation that wallets, signers, light-client applications, and transaction builders can actually use. This is protocol-boundary work because a signed payload is only sound if the off-chain signer can verify the runtime calls, types, signed extensions, and extrinsic parts it is authorizing. [`@polkadot-api/merkleize-metadata`](https://github.com/polkadot-api/polkadot-api/tree/main/packages/merkleize-metadata), where I am the package author and maintainer, is the main implementation vehicle for that responsibility, not the component being claimed in isolation.

| Evidence                                                                                                                                                                                                                                                                                                                                                               | Status                                                       | My role                                                                  | Why this is protocol-boundary work                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [RFC #78: Merkleized metadata](https://github.com/polkadot-fellows/RFCs/pull/78)                                                                                                                                                                                                                                                                                       | Merged and labeled implemented                               | Co-author and reviewer in the RFC process                                | Defines how offline signers verify the metadata needed to understand a transaction                                                          |
| [`frame-metadata` #110](https://github.com/paritytech/frame-metadata/pull/110) and [`polkadot-sdk` #10592](https://github.com/paritytech/polkadot-sdk/pull/10592)                                                                                                                                                                                                      | Merged; the SDK fix was marked for multiple stable backports | Author                                                                   | Makes `CheckMetadataHash` work with Metadata V16 in a backwards-compatible way while preserving deterministic, sound metadata verification  |
| [RFC issue #148](https://github.com/polkadot-fellows/RFCs/issues/148)                                                                                                                                                                                                                                                                                                  | Open analytical follow-up                                    | Issue author and active participant                                      | Identifies how RFC #78 must adapt to Metadata V16 and Extrinsic V5 instead of letting signer behavior become underspecified                 |
| [RFC #124: Extrinsic v5 definition and specification](https://github.com/polkadot-fellows/RFCs/pull/124)                                                                                                                                                                                                                                                               | Open; review comments submitted                              | Reviewer; requested changes                                              | Strengthens the transaction-format specification that wallets, signers, metadata consumers, and runtime authors must implement consistently |
| [`@polkadot-api/merkleize-metadata` initial release](https://github.com/polkadot-api/polkadot-api/pull/541), [payload proof support](https://github.com/polkadot-api/polkadot-api/pull/555), and [metadata refinement](https://github.com/polkadot-api/polkadot-api/pull/714)                                                                                          | Merged and released through Polkadot-API                     | Primary author and maintainer                                            | Implements RFC #78 proof generation over real `frame_metadata` for downstream signers and clients                                           |
| [`ledger-signer` support](https://github.com/polkadot-api/polkadot-api/pull/720) and downstream questions about [constructing proofs](https://github.com/polkadot-api/polkadot-api/issues/953) and [side-loading metadata](https://github.com/polkadot-api/polkadot-api/issues/954)                                                                                       | Merged or publicly tracked                                   | Primary author for the signer package; maintainer for downstream support | Shows the metadata-proof path being exercised by signer and wallet-facing users, not only by internal tooling                               |

The implementation has been subject to public review through Polkadot-API maintenance, RFC discussion, and `polkadot-sdk` review. The SDK fixes listed above demonstrate that I also work at the protocol implementation boundary when chain-side metadata behavior needs correction for the off-chain verification path to remain correct.

**Requirement: at least one published long-form semi-technical article concerning Polkadot.**

I wrote a 39-page bachelor thesis, **User Account Access Graphs in Polkadot** (2024/06/25), available as a public PDF at <https://raw.githubusercontent.com/carlosala/user-account-access-graphs/main/main.pdf> and in the source repository at <https://github.com/carlosala/user-account-access-graphs>. It satisfies the long-form Polkadot writing requirement by applying a directed-hypergraph model to concrete Polkadot account and wallet security/recoverability scenarios. Although it is hosted in a GitHub repository rather than a magazine or blog, it is a public long-form semi-technical Polkadot work with a direct publication artifact.

### Scope

The Fellowship's evaluation scope includes runtime and host APIs, standard RPCs, user-interface code required to practically execute upgrades, and code or technology required by and primarily used for code or technology already included in scope.

My work is in scope primarily because runtime metadata, `CheckMetadataHash`, signing payloads, and transaction extensions form the protocol boundary that wallets, signers, light clients, and applications must implement correctly in order to use Polkadot without unnecessary trust. The strongest chain of evidence is runtime metadata -> RFC #78 -> offline signer verification -> SDK/frame-metadata correctness.

Polkadot-API is relevant here not as generic tooling, but as the implementation vehicle through which this metadata and signing-verification interface is made correct, type-safe, light-client-compatible, and usable by downstream developers. My broader PAPI maintenance, release, metadata, extrinsic, and signer work is supporting evidence of sustained protocol-interface responsibility. My XCM payment API fixes are also included as supporting protocol-boundary work, but the Rank II claim does not depend on aggregating every client or tooling contribution into one broad component.

## Voting record

N/A. I am currently a Fellowship Candidate and do not yet have voting privileges.

## Misc

- [ ] Question(s):
- [ ] Concern(s):
- [ ] Comment(s):
