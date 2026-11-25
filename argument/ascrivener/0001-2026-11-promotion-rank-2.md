# Argument-0001: Promotion to Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/11/16                                                                                  |
| **Submitted by**| Adam Scrivener                                                                              |
| **Sponsored by**| Davide Galassi                                                                              |



## Member details

- Matrix username: @ascriv:matrix.org
- Polkadot address: 15zc2BWvq5wkrWBVnkv2PKKpFsW3oJbzgpoTZA6LTVc5Yt3z (verified on-chain identity)
- Current rank: 0 (Candidate)
- Date of initial induction: 2026/11/16 ([application 29](https://collectives.subsquare.io/fellowship/applications/29))
- Date of last report: N/A (first report)
- Link to last report: N/A
- [Subsystems](subsystems.md) developed/maintained: JAM block import and state transition; PVM; formal verification of JAM

## Reporting period

- Start date: 2025/02/01
- End date: 2026/11/16


## Argument

Fast promotion from Candidate to Rank II (Proficient Member) under the [JAM Implementer's Prize](https://jam.web3.foundation/rules), Rule 13: after an accepted milestone a team may nominate members for direct promotion. I am the sole member of team JAMZILLA, nominated to Rank II after Milestone 1.

**Summary**

I am the sole developer of Jamzilla, a Go implementation of JAM that completed Milestone 1 (IMPORTER) of the JAM Implementer's Prize. The Fellowship approved it on-chain in [referendum 645](https://collectives.subsquare.io/fellowship/referenda/645) (13 Aye, 0 Nay): "The Polkadot Technical Fellowship approves in full JAM Prize Milestone 1 for team JAMZILLA in category Go (Set A), address 15zc2BWvq5wkrWBVnkv2PKKpFsW3oJbzgpoTZA6LTVc5Yt3z …". Since then I have built jam-lean, an executable formal model of the Gray Paper, and connected it to the JAM conformance fuzzing process.

**1. Primary individual responsible for a major component**

The Manifesto asks for the "primary individual responsible for the formalisation, implementation or analytical improvement of a major component". I am that for two artifacts: Jamzilla (implementation) and jam-lean (formalisation).

**Jamzilla, a JAM implementation in Go.**

- I am its sole author. It is a complete block importer: the state transition (Safrole, disputes, reports and assurances, accumulation, preimages, authorizations, history, statistics), the PVM, state merklization and the codec. Rust cryptographic primitives (Bandersnatch, Ed25519) are linked in.
- Milestone 1 (IMPORTER), GP 0.7.2: [w3f/jam-milestone-delivery#24](https://github.com/w3f/jam-milestone-delivery/pull/24). It passes the state-transitioning conformance vectors; approved in [referendum 645](https://collectives.subsquare.io/fellowship/referenda/645).
- It is a registered target in the ecosystem's conformance fuzzing (jam-conformance/jam-fuzzing, image ghcr.io/ascrivener/jamzilla), reported under GP 0.7.2.
- Repository: ascrivener/jam (private; access offered to reviewers on request).

**jam-lean, an executable formal model of JAM in Lean 4** ([github.com/ascrivener/jam-lean](https://github.com/ascrivener/jam-lean)).

- Written only from Gray Paper v0.8.0. It covers all of Appendix A (PVM, host calls, gas model), the codec, hashes, host functions, Ψ_R, Ψ_A, Ψ_I and block import Υ with every section-level transition.
- Validated against the official vectors: 364/364 PVM programs, 44,860 block-cost checks, the GP 0.8.0 STF vectors and the block-import traces.
- Kernel-checked theorems about the octets that run on chain: the witness service's refine rejects bad payloads with an exact result (re-checked by an independent kernel, nanoda); the heap allocator of Parity's jam-bootstrap-service 0.1.29 refines a functional model that keeps a full heap invariant; and the first milestone of Bootstrap's refine. Summary: [docs/whats-proven.md](https://github.com/ascrivener/jam-lean/blob/main/docs/whats-proven.md).
- On peer review: the Manifesto asks for a peer-reviewed publication "or a good reason why not". No paper is published: every theorem is machine-checked, so a reviewer can re-run the checker instead of trusting a referee, and each statement with its assumptions is listed in whats-proven.md.

**Analytical improvement: conformance.** jam-lean runs as a target of the conformance fuzzer ([jam-lean-target](https://github.com/ascrivener/jam-lean-target)), as an executable reference for the Gray Paper, with all cryptography written in plain Lean. Its public findings ([docs/findings.md](https://github.com/ascrivener/jam-lean-target/blob/main/docs/findings.md)):

- two places where jam-lean itself departed from the paper, both fixed;
- the fuzzer and today's "0.8.0" implementations following some Gray Paper changes made after v0.8.0 (GP #533, #563), raised as [jam-fuzzing #220](https://github.com/jam-conformance/jam-fuzzing/issues/220);
- three PolkaVM behaviours that differ from GP v0.8.0, one reported ([polkavm#455](https://github.com/paritytech/polkavm/issues/455)) and two already known upstream (#429, #447).

It also publishes 1,408 PVM vectors and block vectors with GP v0.8.0 results, crafts signed test blocks, and supports the fuzzer's proposed refine extension.

**2. Long-form semi-technical article**

[Checking JAM against an executable Gray Paper](https://forum.polkadot.network/t/checking-jam-against-an-executable-gray-paper/19563), Polkadot Forum (Tech Talk), 2026-11-16. It covers why an executable model of the Gray Paper matters for JAM, what jam-lean proves about deployed service binaries, and how the model joins the conformance fuzzing process.

**3. Deep familiarity with a major area**

I have implemented the Gray Paper's state transition and PVM twice, independently: for execution in Go (Jamzilla) and as a formal model in Lean (jam-lean). Each disagreement jam-lean finds is traced to its Gray Paper section and equation.

**4. Availability**

I am committed to JAM through and beyond its launch, and will keep Jamzilla and jam-lean current as the Gray Paper evolves. I am reachable on Matrix (@ascriv:matrix.org) and GitHub (ascrivener).

**5. Scope**

JAM is Polkadot's next core protocol. A conformant implementation, and a formal model that checks implementations against the Gray Paper, serve the Polkadot (Main) Network's continued operation and improvement, which is the Manifesto's test for scope.

**References**

- [JAM Implementer's Prize rules](https://jam.web3.foundation/rules) (Rule 13)
- [Jamzilla M1 delivery](https://github.com/w3f/jam-milestone-delivery/pull/24)
- [Referendum 645: M1 interview approval JAMZILLA](https://collectives.subsquare.io/fellowship/referenda/645)
- [Induction application 29](https://collectives.subsquare.io/fellowship/applications/29)
- [jam-lean](https://github.com/ascrivener/jam-lean) and [whats-proven.md](https://github.com/ascrivener/jam-lean/blob/main/docs/whats-proven.md)
- [jam-lean-target](https://github.com/ascrivener/jam-lean-target) and [findings.md](https://github.com/ascrivener/jam-lean-target/blob/main/docs/findings.md)
- [Polkadot Fellowship Manifesto](https://github.com/polkadot-fellows/manifesto)


## Voting record

Not applicable: as a Candidate (rank 0) I have not been eligible to vote on Fellowship referenda.

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [x] Comment(s): Private Jamzilla repository (ascrivener/jam): access offered to reviewers on request.
