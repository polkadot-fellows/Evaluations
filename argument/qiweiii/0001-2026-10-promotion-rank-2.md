# Argument-0001: Fast Promotion to Rank II

|                 |               |
| --------------- | ------------- |
| **Report Date** | 2026/10/28    |
| **Submitted by**| Qiwei Yang    |


## Member details

- Matrix username: `@qiwei:matrix.org`
- Polkadot address: `5Ckhx3Ww6Dc75ccjEYnQmmopA3W4nJ7C8rz9HeEbft673rSu`
- Current rank: N/A
- Date of initial induction: N/A
- Date of last report: N/A
- Link to last report: N/A
- Subsystems developed/maintained: JAM clients (boka)
- Area(s) of Expertise/Interest:
    - `JAM` (PVM: interpreter, memory model, gas, host-calls, authorization, refinement and accumulation)
    - `JAM state transition function` (Safrole, accumulation, disputes, state Merklization)
    - `Gray Paper semantics` (implemented 0.5.0 through 0.7.2; currently implementing 0.8.0)
    - `Swift` (PVM interpreter, toolchains, release engineering)


## Reporting period

- Start date: 2024/06/17 (first merged boka commit, PR #19)
- End date: 2026/10/28


## Argument

I am requesting fast promotion to Rank II as the boka team's nominee under **Rule 13 of the JAM Implementer's Prize**, which allows a team to nominate a Rank II candidate following an accepted milestone, with the usual time requirements waived.

boka's Milestone 1 was delivered at [jam-milestone-delivery PR #27](https://github.com/w3f/jam-milestone-delivery/pull/27). The Fellowship approved boka's M1 interview through [referendum #643](https://collectives.subsquare.io/fellowship/referenda/643), which has now executed. The following addresses the Rank II requirements of the Manifesto.

### 1. Primary implementation of major components of the JAM protocol

[boka](https://github.com/open-web3-stack/boka) is a clean-room implementation of JAM in Swift built on the Gray Paper and the public implementers' channel only. It is a functional implementation of the protocol: it imports blocks, executes the full state transition function, and runs a PVM, validated through fuzzing and conformance testing for Milestone 1. I implemented boka's PVM and major state-transition components, and maintained conformance across Gray Paper upgrades.

My implementation and integration work included:

- **The PVM.** The complete instruction set in PRs [#70](https://github.com/open-web3-stack/boka/pull/70), [#75](https://github.com/open-web3-stack/boka/pull/75), [#80](https://github.com/open-web3-stack/boka/pull/80), [#84](https://github.com/open-web3-stack/boka/pull/84), [#91](https://github.com/open-web3-stack/boka/pull/91); standard program initialization and the memory-zone model [#101](https://github.com/open-web3-stack/boka/pull/101); interpreter performance and memory optimization [#109](https://github.com/open-web3-stack/boka/pull/109), [#160](https://github.com/open-web3-stack/boka/pull/160); the memory-model refactor [#257](https://github.com/open-web3-stack/boka/pull/257); and saturating gas and balance arithmetic [#135](https://github.com/open-web3-stack/boka/pull/135).
- **PVM invocation contexts and host calls.** Authorization and the host-call framework [#114](https://github.com/open-web3-stack/boka/pull/114); refinement [#237](https://github.com/open-web3-stack/boka/pull/237); accumulation and its host calls [#132](https://github.com/open-web3-stack/boka/pull/132); general host calls [#118](https://github.com/open-web3-stack/boka/pull/118); host-call updates for later Gray Paper versions [#215](https://github.com/open-web3-stack/boka/pull/215); the `log` host call [#264](https://github.com/open-web3-stack/boka/pull/264); and PVM conformance fixes and tests [#269](https://github.com/open-web3-stack/boka/pull/269), [#271](https://github.com/open-web3-stack/boka/pull/271). I also implemented the on-transfer invocation used in earlier Gray Paper versions [#118](https://github.com/open-web3-stack/boka/pull/118).
- **State-transition components.** Safrole [#44](https://github.com/open-web3-stack/boka/pull/44); judgements, disputes and verdicts [#61](https://github.com/open-web3-stack/boka/pull/61); state Merklization and trie test vectors [#60](https://github.com/open-web3-stack/boka/pull/60) and general Merklization constants [#254](https://github.com/open-web3-stack/boka/pull/254); ordered accumulation [#222](https://github.com/open-web3-stack/boka/pull/222) and its conformance [#311](https://github.com/open-web3-stack/boka/pull/311); accumulation test suites [#301](https://github.com/open-web3-stack/boka/pull/301); community STF tests [#304](https://github.com/open-web3-stack/boka/pull/304); assurance handling [#306](https://github.com/open-web3-stack/boka/pull/306); and parallel accumulation [#361](https://github.com/open-web3-stack/boka/pull/361).
- **Cryptographic library integration and erasure coding.** Blake2 integration [#22](https://github.com/open-web3-stack/boka/pull/22); Ed25519 integration [#23](https://github.com/open-web3-stack/boka/pull/23) and conformance fixes [#373](https://github.com/open-web3-stack/boka/pull/373); BLS bindings [#29](https://github.com/open-web3-stack/boka/pull/29) and library integration [#174](https://github.com/open-web3-stack/boka/pull/174); Bandersnatch bindings and integration [#33](https://github.com/open-web3-stack/boka/pull/33); and erasure-coding integration and updates [#53](https://github.com/open-web3-stack/boka/pull/53), [#326](https://github.com/open-web3-stack/boka/pull/326), [#338](https://github.com/open-web3-stack/boka/pull/338).
- **Node engineering and conformance maintenance.** Protocol fuzzing and fixes [#340](https://github.com/open-web3-stack/boka/pull/340), [#350](https://github.com/open-web3-stack/boka/pull/350), [#368](https://github.com/open-web3-stack/boka/pull/368); Gray Paper upgrades and conformance maintenance from 0.5.0 through 0.7.2, including [#228](https://github.com/open-web3-stack/boka/pull/228), [#334](https://github.com/open-web3-stack/boka/pull/334), [#376](https://github.com/open-web3-stack/boka/pull/376); state-handling performance [#364](https://github.com/open-web3-stack/boka/pull/364); and release-build hardening [#355](https://github.com/open-web3-stack/boka/pull/355), [#360](https://github.com/open-web3-stack/boka/pull/360).

**Code review.** These contributions went through team pull-request review.

### 2. Knowledge of the protocol, and knowledge acquisition and sharing

- **Gray Paper corrections.** Merged corrections to the protocol's formalisation: PVM invocation fixes [#130](https://github.com/gavofyork/graypaper/pull/130), standard-program initialization [#172](https://github.com/gavofyork/graypaper/pull/172), the leaf page function [#169](https://github.com/gavofyork/graypaper/pull/169), the `rot_32` register operand [#193](https://github.com/gavofyork/graypaper/pull/193), the refine context type [#244](https://github.com/gavofyork/graypaper/pull/244), outdated accounts definitions [#242](https://github.com/gavofyork/graypaper/pull/242), and ordering the accumulation output log θ before state assignment in the transition function [#477](https://github.com/gavofyork/graypaper/pull/477).
- **[JAM 3D](https://qiweiii.github.io/jam-3d/)** ([source](https://github.com/qiweiii/jam-3d)): a small interactive project to help explain JAM's cores, work packages, blocks and state transition. It includes short walkthroughs and links to the Gray Paper for further reading.
- **Ongoing protocol work**: I am currently implementing Gray Paper 0.8.0 (including the revised gas model) and Milestone 2 functionality in boka, keeping the implementation current through the remaining prize milestones.

### 3. Availability and readiness to be a maintainer

During fuzz testing and Gray Paper upgrades from 0.5.0 to 0.7.2, I diagnosed and fixed failures in the state trie, host-calls, accumulation ordering and release builds until the suites passed. I have worked on boka since June 2024 and intend to carry it through Milestones 2-5 and into maintenance.

### 4. Why this belongs in the Fellowship's scope

This application is based on my JAM protocol implementation work in boka and the team's Rank II nomination under JAM Prize Rule 13, following the Fellowship's M1 interview approval. The contributions above cover protocol implementation, conformance maintenance and corrections to the Gray Paper.

### References

- Milestone 1 delivery: https://github.com/w3f/jam-milestone-delivery/pull/27
- My boka pull requests: https://github.com/open-web3-stack/boka/pulls?q=is%3Apr+author%3Aqiweiii
- My Gray Paper pull requests: https://github.com/gavofyork/graypaper/pulls?q=is%3Apr+author%3Aqiweiii
- Fellowship M1 interview approval: https://collectives.subsquare.io/fellowship/referenda/643
- JAM 3D visual guide: https://qiweiii.github.io/jam-3d
- JAM Prize rules: https://jam.web3.foundation/rules


## Voting record

N/A — I have not yet been inducted into the Fellowship and have not been eligible to vote.
