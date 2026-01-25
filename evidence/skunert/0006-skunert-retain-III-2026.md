# Argument-0006: Retention at Rank III

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2026/01/25 |
| **Submitted by** | skunert    |


## Member details

- Matrix username: `@sebastian:parity.io`
- Polkadot address: `1682A5hxfiS1Kn1jrUnMYv14T9EuEnsgnBbujGfYbeEbSK3w`
- Current rank: 3
- Date of initial induction: 2024/01/08
- Date of last report: 2025/04/22
- Area(s) of Expertise/Interest: `Cumulus Node`, `Substrate Node`, `Parachain Authoring`, `Weight`


## Reporting period

- Start date: 2025/07/25
- End date: 2026/01/25


## Argument

During this reporting period my contributions were less in code, but more in support and advisory of various projects.

### Node Contributions

I invested effort into improving the omni-node tooling used for testing and development. These changes were mostly improving compatibility of the integrated dev-mode of the omni-node implementation.
It is now compatible again with the latest elastic scaling configurations which include a relay parent offset. [#9885](https://github.com/paritytech/polkadot-sdk/pull/9885), [#10755](https://github.com/paritytech/polkadot-sdk/pull/10755), [#10807](https://github.com/paritytech/polkadot-sdk/pull/10807)

I fixed a memory leak where blocks were unnecessarily pinned on the relay chain during syncing. This led to large memory consumption. We now free the blocks immediately which reduces memory consumption during sync by more than 80% in my experiments. [#10333](https://github.com/paritytech/polkadot-sdk/pull/10333)

I improved Substrate block pruning to exclude blocks which have justifications. The longer chains run, the longer it takes to fully sync them. To avoid longer and longer sync times, warp sync is the recommended approach. However, warp sync needs warp proofs from other peers in the network. Before my PR, nodes with pruning would also prune Grandpa justifications and could not serve warp proofs. Now, they keep blocks with justifications. [#10893](https://github.com/paritytech/polkadot-sdk/pull/10893)

### System Chain Contributions

I enabled the PoV-reclaim mechanism on the Polkadot and Kusama system chains. This mechanism allows better utilization of PoV space. After transactions are executed, overbenchmarked proof weight will be reimbursed. This is important
for effective execution of contracts. They can be large and multiple executions of the same contract should not contribute to the proof size multiple times. [PR#941](https://github.com/polkadot-fellows/runtimes/pull/941), [PR#1047](https://github.com/polkadot-fellows/runtimes/pull/1047)

### JAM Development

Towards the end of 2025 I started to investigate how we can onboard additional contributors to Parity's JAM implementation. To get a feeling for the project, I contributed to the user-experience of the tools in the JAM repository. In addition, I am
currently working on an improvement to the redistribution of tickets on ticket proxies, this is work in progress. [#888](https://github.com/paritytech/polkajam/pull/888), [#881](https://github.com/paritytech/polkajam/pull/881), [Safrole Ticket Issue WIP](https://github.com/paritytech/polkajam/issues/283)

### Advisory & Support

I lead the Node-SDK team at Parity, which means that I am involved in many node-related projects, onboarding and guiding new and long-standing contributors. Examples:
- Anvil Dev Node: I supported and advised on the Anvil node project, led by fellowship member @alindima
- NOMT Integration: Supported and coordinated work from contributor @gmiotti to bring NOMT storage format to the polkadot-sdk
- PoV Reclaim accuracy fix: Weekly sparring and advising with fellowship member @michalkucharczyk about fixing [#6020](https://github.com/paritytech/polkadot-sdk/issues/6020)

### Code Reviews

I provided extensive code reviews across repositories:
- polkadot-sdk PRs (96): [list](https://github.com/paritytech/polkadot-sdk/pulls?q=is:pr+reviewed-by:skunert+created:2025-07-25..2026-01-25)
- Runtime PRs (11): [list](https://github.com/polkadot-fellows/runtimes/pulls?q=is:pr+reviewed-by:skunert+created:2025-07-25..2026-01-25)


## Voting record

*Provide your voting record in relation to required thresholds for your rank.*

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
| ----- | ------------------- | -------------------- | -------------------------- | -------- |
| I     | 90%                 | N/A                  |                            |          |
| II    | 80%                 | N/A                  |                            |          |
| III   | 70%                 | 100%                 |   85.11%                   |          |
| IV    | 60%                 | 90%                  |                            |          |
| V     | 50%                 | 80%                  |                            |          |
| VI    | 40%                 | 70%                  |                            |          |
