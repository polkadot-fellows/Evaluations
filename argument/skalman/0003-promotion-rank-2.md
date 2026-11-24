# Argument-0003: Fast Promotion to Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/11/24                                                                                  |
| **Submitted by**| Skalman🐢                                                                                   |


## Member details

- Matrix username: @skalman:matrix.org
- Polkadot address: 13zbXMsJgQbMkrjai3JUaQmVERZHKLNt42xaGjqJq7mBasDk
- Current rank: 0 (dempoted from Rank I)
- Date of initial induction: 2023/10/30
- Date of last report: 2026/03/20 (Argument-0002)
- Area(s) of Expertise/Interest: Cryptographic research and implementation

## Reporting period

- Start date: 2023/10/30
- End date: 2026/11/24


## Preamble: Request for fast promotion

I was inducted into the Fellowship at Rank I on 2023/10/30 and served continuously at that rank for approximately three years. During that period, I submitted two retention arguments (Argument-0001 and Argument-0002) which were approved by the Fellowship. I missed the deadline for the July 2026 retention argument, which unfortunately fell due during my vacation, and was consequently demoted to Rank 0.

My technical contributions to Polkadot have been continuous during the past three years, and I was eligible for promotion to Rank II before I missed the retention deadline. As such, I hope that it merits a fast promotion to Rank II. The body of work I have produced over the last three years already satisfies the Rank II requirements set out in Section 6 of the Manifesto, as detailed below.

Fellowship members have invited me to serve as a delegate on the **Cryptography (Applied)** subsystem in the newly adopted subsystem/delegate structure (https://github.com/polkadot-fellows/Evaluations/pull/354), which further motivates this application.

## Argument

My work during this period has been centred on bringing advanced cryptographic protocols — most notably BLS signatures and Ring-based proof systems — into Polkadot as a core protocol capability. Below I address each Rank II requirement from the Manifesto directly.

### Requirement 1: Primary individual responsible for the formalisation, implementation or analytical improvement of a major component of the protocol

I have been the primary individual responsible for the implementation of **BLS signature support in Polkadot**, a cryptographic component intended to improve BEEFY's efficiency trustlessly bridging Polkadot to other chains and enable aDKG-based protocols (unbiasable random beacon, encrypt-to-the-future). This work is a direct match for the Manifesto's scope item on "cryptographic data-structures, algorithms, languages and APIs required for the continued upkeep of the Polkadot (Main) Network" and "trust-free bridges relying on said consensus algorithms".

Primary implementation work (subject to expert code-review and merged into the functional Polkadot implementation):

- Initial introduction of a BLS crypto scheme into Substrate / polkadot-sdk, in collaboration with @davxy, enabling BEEFY to handle BLS alongside ECDSA:
  - https://github.com/paritytech/substrate/pull/13618
  - https://github.com/paritytech/polkadot-sdk/pull/1705
  - https://github.com/paritytech/polkadot-sdk/pull/1816
  - https://github.com/paritytech/polkadot-sdk/pull/1739 (Rogue-key-attack-safe proof of possession, merged)

- Redesign and re-implementation of proof-of-possession in the Substrate cryptography module to be resistant to multiple attack vectors, and follow-up work with @bkchr to update runtime generation and verification of proof-of-possession across runtimes authored after the original code (AssetHub and test runtimes):
  - https://github.com/paritytech/polkadot-sdk/pull/9471
  - https://github.com/paritytech/polkadot-sdk/pull/9949
  - https://github.com/paritytech/polkadot-sdk/pull/10002
  - https://github.com/paritytech/polkadot-sdk/pull/10033
  - https://github.com/paritytech/polkadot-sdk/pull/11369

Draft PR enabling Westend validators to include BLS keys in their session keys (pending approval), together with the host-call changes required by the final RFC 156 design:
  - https://github.com/paritytech/polkadot-sdk/pull/11149

I am the **principal maintainer** of the `w3f-bls` library — the BLS library used by Polkadot's BLS signature implementation — and have been responsible for its sustained improvement over the whole three-year period:

- Implementation of the fast BLS variant described in Web3 Foundation's paper: https://github.com/w3f/bls/pull/66
- Implementation and benchmarking of Chaum–Pedersen signatures on a third sister curve and various other optimisation, and benchmarking of double- vs triple-nugget BLS; and resolving all pertinent issues raised by the auditor: 
  - https://github.com/w3f/bls/compare/master...skalman--cp-on-sister-curve, 
  - https://github.com/paritytech/bls/pull/81, 
  - https://github.com/w3f/bls/pull/57, 
  - https://github.com/w3f/bls/pull/86 (Addressing audits findings)

Enabling cryptographic work in the broader Arkworks ecosystem (required for the BLS and Ring Proof stacks to work on Polkadot's curves and missing upstream prior to my contribution): hash-to-curve for all curves used in Polkadot:

- https://github.com/arkworks-rs/algebra/pull/343
- https://github.com/arkworks-rs/algebra/pull/659
- https://github.com/w3f/arkworks-curves/pull/11
- https://github.com/arkworks-rs/curves/pull/138

Formalisation and analytical improvement work supporting the same component:

- Research on space-efficient representations of finite field elements, yielding ~3× proof-size reduction in SNARKs used in W3F protocols: https://github.com/w3f/algebraic-torus

### Requirement 2: At least one published long-form semi-technical article concerning Polkadot

- Co-author / implementer of the fast BLS flavour designed by Web3 Foundation, written up as a preprint on IACR ePrint: https://eprint.iacr.org/2022/1611

- I authored a long-form, step-by-step educational walkthrough of Web3Sum / APK proofs — intended specifically to make this piece of Polkadot's bridging cryptography accessible to other researchers and ecosystem developers:

- "APK Proofs by Hand and Sage", Web3 Foundation blog: https://medium.com/web3foundation/apk-proofs-by-hand-and-sage-3f5feb3fcca4

- Authored a technical article presenting formal proofs of soundness, correctness, and zero-knowledge for the Ring Proof construction, drafted for subsequent publication: https://hackmd.io/gtws4XBzQgGJMKKWX8XYEQ

## Additional contributions

The following sections cover further contributions of mine to Polkadot.

### Specification, standards and review work

- Early contributions to the Polkadot Specification:
  - https://github.com/w3f/polkadot-spec/graphs/contributors
- RFC 156 (BLS host functions): review, discussion, and modifications so BLS could be moved into production, including the follow-up code changes required by the final design:
  - https://github.com/polkadot-fellows/RFCs/pull/156
  - https://github.com/paritytech/polkadot-sdk/pull/11369

### Ring Proof / Ring VRF
- Collaborated on batched verification of multiple ring proofs: https://github.com/paritytech/ring-proof/pull/72
- Implemented the prover for the `w3f-ring-vrf-snark` crate (SNARK-verifying VRF used by `verifiable`) on the `skalman--snarkified-ring-vrf` development branch: https://github.com/paritytech/ring-proof/tree/skalman--snarkified-ring-vrf
- Implemented the Twisted-Edwards "powers of two multiples" / doubling gadget for the `w3f-ring-proof` crate. The gadget was originally proposed in https://github.com/paritytech/ring-proof/pull/36 (closed) and subsequently re-landed as https://github.com/paritytech/ring-proof/pull/49.

### Knowledge sharing and ecosystem engagement

- Developed the ZK module of the Polkadot Blockchain Academy (PBA) curriculum, and taught the cryptography module at PBA Hong Kong and PBA Singapore.
- Mentored a PBA alumnus submitting a grant for a Web3Sum-based bridge prototype, and reviewed grants on JAM cryptography and ZK cryptography on Polkadot:
  - https://github.com/PolkadotOpenSourceGrants/apply/pull/46#issuecomment-3529911905
  - https://github.com/w3f/Grants-Program/pull/2603/files
  - https://github.com/PolkadotOpenSourceGrants/delivery/pull/8

### Time-of-service

Although I am currently at Rank 0 as a consequence of a missed retention deadline, I have been working on core Polkadot cryptography continuously as my primary professional focus for well over five years (as a research scientist at Web3 Foundation) and served approximately three unbroken years at Rank I. This substantially exceeds the Manifesto's indicative "~1 year" expectation of service at Rank I prior to promotion to Rank II.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | After reporting a voting record at Rank I became mandatory, there was no referendum in which I was eligible to vote. | |
|II |80%   |N/A   | N/A — not yet at this rank. | |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc
- I acknowledge that the missed July 2026 retention argument was my own oversight. I would like the Fellowship to weigh this against the fact that my technical output has continued uninterrupted, that my prior two retention arguments were approved, and that the body of work above arguably meets the Rank II bar.
