# Argument-0001: Fast Promotion to Rank II

|                 |               |
| --------------- | ------------- |
| **Report Date** | 2026/09/15    |
| **Submitted by**| Daniel Cukier |


## Member details

- Matrix username: `@danicuki:matrix.org`
- Polkadot address: `127XreSJZW91qLc91hwepYZ9pBfuNveqDERv9KDrm2oQf4Lu`
- Current rank: `0` (Candidate)
- Date of initial induction: 2025/12/29
- Date of last report: N/A
- Link to last report: N/A [induction application](https://collectives.subsquare.io/fellowship/applications/13)
- Area(s) of Expertise/Interest:
    - `JAM` (Graypaper semantics, state transition function)
    - `JAM block structure and extrinsics`
    - `JAM codec and state serialisation`
    - `PVM` (64-bit RISC-V, host functions)
    - `Node architecture` (BEAM/OTP, storage, RPC, conformance/fuzzer target)


## Reporting period

- Start date: 2024/06/28 (first Jamixir commit)
- End date: 2026/09/15


## Argument

I am requesting a fast promotion from Candidate directly to Rank II under **Rule 13 of the JAM Implementer's Prize**: "Following the accepted completion of each milestone, teams may nominate one Fellowship candidate/member to be promoted directly to rank III and (optionally) a second candidate/member to rank II". This is the Jamixir team's Rank II nomination; the team's Rank III nomination is submitted separately.

The Fellowship accepted Jamixir's Milestone 1 in full in [Referendum #604](https://collectives.subsquare.io/fellowship/referenda/604), executed on 2026/09/07: *"The Polkadot Technical Fellowship approves in full JAM Prize Milestone 1 for team JAMIXIR in category Elixir (Set D)"*. Before that, the implementation passed the W3F fuzzing benchmark (ten consecutive 100k-step runs, 2026/03/02), Parity's conformance test suite, and the combined M1 / Fellowship interview held in the last week of August 2026.

Rule 13 settles the timing. The rest of this argument addresses the Rank II requirements of the Manifesto (§6.3 and §6.3.1) on their merits.

### 1. Responsible for the implementation of major components of the JAM protocol (§6.3.1)

[Jamixir](https://github.com/jamixir/jamixir) is an independent, clean-room implementation of JAM in Elixir, written by a team of two. It is a functional implementation of the protocol: it imports blocks, executes the full state transition function, runs a PVM, and authors and propagates blocks in a six-node network. The Elixir codebase is about 23,000 lines, plus a Rust PVM used for performance. The repository is private for clean-room reasons while the Prize is running; under Rule 26 of the JAM Prize, W3F and Fellowship members are invited to it upon request, and I will add any reviewer who asks.

Over the reporting period I authored **819 of the repository's 1,541 commits** (53%, +57k / −27k lines). Within that, I was the primary author of the following components, which together form the block-import and state-transition core validated by Milestone 1:

- **Block, header and extrinsics** (`lib/block`): block and header structures; the assurances, guarantees, disputes, preimages, tickets, work-packages and work-package-bundles, including their validation rules.
- **State transition** (`lib/system`): the state model and the transitions for Safrole, accumulation, the authorizer pool, entropy pool, judgements, privileged services, recent history, service accounts, validator statistics, header seals and deferred transfers and data-availability logic.
- **Codec and state serialisation** (`lib/codec`): the JAM encoder/decoder, state Merklisation and serialisation, JSON test-vector codec and erasure coding.
- **Node, storage, RPC and the conformance/fuzzer target** (`lib/node.ex`, `lib/node_state_server.ex`, `lib/storage`, `lib/rpc`, `lib/fuzzer`): the runnable node and the binary target used by W3F and Parity to evaluate M1.

**Expert review and validation.** All code went through review within the team, and the implementation was subjected to external expert evaluation at three levels: the [W3F fuzzer against reference traces](https://github.com/w3f/jam-milestone-delivery/pull/23), including a two-week cycle in February 2026 in which we diagnosed and fixed gas accounting, timeouts, a missing database table in clean environments and memory pressure within hours of each report; Parity's conformance suite; and the Fellowship interview, in which we defended the codebase and the Graypaper in detail. [Referendum #604](https://collectives.subsquare.io/fellowship/referenda/604) records the outcome.

### 2. At least one published long-form semi-technical article concerning Polkadot (§6.3.1)

- **"Ensuring JAM Development Sustainability: Is It Time for a Dedicated JAM Bounty Program?"**, [Polkadot Forum, 2025/12/10](https://forum.polkadot.network/t/ensuring-jam-development-sustainability-is-it-time-for-a-dedicated-jam-bounty-program/16229). A long-form analysis of the economics of the JAM client ecosystem, the gap between protocol implementation and ecosystem readiness, and a concrete proposal for a JAM working group. It generated a substantive discussion with Fellowship members and W3F.
- [Work Package Execution Flow in Polkadot JAM](https://hackmd.io/Wcvrnx4BRj2KOpmnQ77tUw). A technical walkthrough of a work package from end user to finalised state: builders, guarantors, auditors, accumulation and GRANDPA finalisation, with the JAMNP-S protocols involved at each step.
- Technical threads with wide reach, each explaining one JAM mechanism: 
  - [EVM vs PVM](https://x.com/danicuki/status/1892240092871250159) (2025/02/19 72k views)
  - [erasure coding and data availability](https://x.com/danicuki/status/1903833622496383412) (9k views)
  - [GRANDPA and JAM](https://x.com/danicuki/status/1907866626495754599) 
  - [JAM super thread on RISC-V PVM, RingVRF, ELVES, Safrole, erasure coding, QUIC and in-core parallelism](https://x.com/danicuki/status/1909315806824964277) (2025/04/07 21k views)
  - [why 39+ teams can implement the same protocol without sharing code](https://x.com/danicuki/status/1938653720515895704) (9k views)

### 3. Knowledge of the protocol, and knowledge acquisition and sharing (§6.3)

The Manifesto expects a Rank II member to be "a core part of the team", deeply familiar with at least one major area, "making reasonable suggestions" rather than asking questions whose answers are easy to discover, and sharing knowledge.

- **Contributions to the protocol specification itself:** [15 accepted commits to the Graypaper](https://github.com/gavofyork/graypaper/commits?author=danicuki), correcting inconsistencies and refining definitions found while translating the formalism into executable code.
- **Talks and tutorials:** 
  - [Is Polkadot JAM the End of Smart Contracts as We Know Them?](https://youtube.com/live/rSB8NeYvw78), Hong Kong, 2026/02/07 
  - [I Ran DOOM on the Polkadot JAM Blockchain, on my laptop, full tutorial](https://www.youtube.com/watch?v=riyYJo-CKWE)
  - [Implementing the JAM Protocol with Elixir: A Developer Perspective](https://www.youtube.com/watch?v=-MqxfxljeKE)
  - [Polkadot JAM: Unlocking Complex Blockchain with Elixir](https://www.youtube.com/watch?v=UM3GgzNihN4)
  - [JAM Implementers profile #4](https://www.youtube.com/watch?v=gKrWeXKorEM).
- **Community and cross-implementation alignment:** co-organised the JAM implementers' sessions at JAM0 Bangkok (November 2024) and organised the JAM Experience in Lisbon (May 2025, about 100 participants, an implementers' day plus a public day); active in the public implementers' channel on semantics, determinism and specification interpretation.

### 4. Availability and readiness to be a maintainer (§6.3, §4.5.3)

The February 2026 fuzzing cycle on PR #23 is the concrete record: each failure report from the evaluators was answered with a diagnosis, a fix, a rebuilt release and a SHA-256 checksum within hours, over two weeks, until the target passed. The same cadence applied to each Graypaper version bump (0.6.0, 0.6.4, 0.7.2) during 2025. I have been working on JAM as my primary focus since June 2024, and I intend to keep Jamixir current through the remaining milestones and to take part in the Fellowship's JAM-related review and specification work.

### 5. Advocacy for Polkadot outside the ecosystem

Beyond the technical material above, I have argued publicly for Polkadot's design and economics to a general crypto audience: 
 - [BTC is money, DOT is infrastructure](https://x.com/danicuki/status/1916185958128427479) 20k views
 - [Blockchains aren't computers, JAM changes that](https://x.com/danicuki/status/1923497508342210619)
 - [A Comparison of JAM with Cardano Hydra](https://x.com/danicuki/status/1927453816372232393) - 25k views

### 6. Why this belongs in the Fellowship's scope

JAM is the protocol the Fellowship is judging and ratifying as Polkadot's next iteration, and the JAM Prize rules make the Fellowship the judge of each milestone and the destination of the fast-track. Jamixir is one of the independent implementations that the Prize was created to produce, and the work above is protocol-implementation work in the sense of Manifesto §2.3.1 ("the internals of all functional Polkadot node implementations").

### Conclusion

Rule 13 grants the team a Rank II nomination on the accepted completion of M1, recorded in [Referendum #604](https://collectives.subsquare.io/fellowship/referenda/604). On the Manifesto's own terms, I was the primary author of the block, state-transition and codec layers of a functional JAM implementation that passed W3F, Parity and Fellowship evaluation, I have contributed corrections to the protocol's formalisation, and I have published and presented on it extensively. I respectfully request fast promotion to Rank II.

### References

- Jamixir repository (private, access on request under Rule 26): https://github.com/jamixir/jamixir
- Jamixir organisation and releases used for evaluation: https://github.com/jamixir, https://github.com/jamixir/jamixir-releases
- M1 delivery PR and fuzzing record: https://github.com/w3f/jam-milestone-delivery/pull/23
- Fellowship [Referendum #604](https://collectives.subsquare.io/fellowship/referenda/604) (M1 approval)
- JAM Prize rules (Rules 13 and 26): https://jam.web3.foundation/rules
- Graypaper commits: https://github.com/gavofyork/graypaper/commits?author=danicuki
- Induction application: https://collectives.subsquare.io/fellowship/applications/13


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | N/A: as a Candidate (rank 0) I have not been eligible to vote on any referendum. | |
|II |80%   |N/A   |   | |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 
- [ ] Concern(s): 
- [ ] Comment(s): 
