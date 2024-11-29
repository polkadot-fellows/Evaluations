# Evidence-0003: Promotion to Rank III

| | |
| --------------- | ------------------------------------------------------------------------------------------ |
| **Report Date** | 2024/11/29 |
| **Submitted by**| Andrei Sandu |

## Member details

- Matrix username: @sandreim:parity.io
- Polkadot address: 13QdJvnJgfoitjrxESwrCWTaLMN8KvXxufDUucXM6EWGuxqh
- Current rank: 2
- Date of initial induction: 2023/07/18
- Date of last report: N/A
- Area(s) of Expertise/Interest: Parachain Consensus, Node Performance Engineering, Observability,
Stress and integration testing

## Reporting period

- Start date: 2023/07/18
- End date: 2024/11/29

## Evidence

During the reporting period, I have played an important role in the design, development, and
deployment of a few major projects to Polkadot that had a significant impact:

- better decentralization and security by increasing parachain validators from 200 to 500
- more blockspace by increasing the number of usable cores to 100
- lowering the latency and increasing the maximum throughput of parachains with Elastic Scaling
- faster and lower cost parachain consensus protocol performance engineering with Subsystem Benchmarks

I've been an active participant in OpenDev calls and in the
[Polkadot forum](https://forum.polkadot.network/u/sandreim/activity), consistently giving updates
on the progress of the implementation, testing, and deployment of Elastic Scaling.

I consider that this evidence, detailed in the next section, is aligned both in quality and
quantity with the Fellowship for a rank 3 promotion.

### Increasing number of validators and cores

I started working on this project before being inducted into the fellowship.
That work consisted of load testing, benchmarking, and research to find parachain consensus
protocol and implementation bottlenecks on the node and runtime implementation. At the time
Polkadot had 200 validators and 40 cores.  I created the
[scalability roadmap](https://github.com/paritytech/roadmap/issues/26) which includes
multiple changes and ideas I contributed as improvements in major parachain consensus protocols:
availability, approval voting, and the overall node-side subsystem architecture.

Major design and code contributions:

- **[Assignment certificates v2](https://github.com/paritytech/polkadot-sdk/pull/1178)**:
This is an enhancement of the approval voting protocol aimed at reducing the usage
of network/CPU resources by a factor of up to 6 in perfect network conditions.

- **[Approval voting subsystem re-write](https://github.com/paritytech/polkadot-sdk/issues/1617)**:
Proposal of a simpler and scalable subsystem architecture. The two existing approval voting
subsystems are merged into a single one. The new subsystem introduces message processing parallelism
to make use of more CPU resources to handle the load at a scale of 1000 validators and
500 cores.

I've communicated with the ecosystem about scaling up plans in forum posts and Element chats:
[Kusama](https://forum.polkadot.network/t/update-parachain-validator-set-size-increase-on-kusama/8218),
[Polkadot](https://forum.polkadot.network/t/update-polkadot-validator-set-size-increase/8682)

### Parachain consensus performance benchmarks

My main motivation for building this was to replace the old ways of doing load testing by
running large networks. It was expensive and slow, producing huge amounts of data
that were very hard to analyze and reason about. The output of my work is a
[new tool](https://github.com/paritytech/polkadot-sdk/tree/master/polkadot/node/subsystem-bench)
which is required for the continuous improvement of the scalability and resilience of the parachain
consensus protocols and Polkadot.

I designed and implemented [multiple modular components](https://github.com/paritytech/polkadot-sdk/tree/master/polkadot/node/subsystem-bench#reusable-test-components) that are used to emulate the network
traffic and load found in large-scale networks on local development machines. It performs stress
tests of one or more parachain consensus subsystems without running a network. It collects granular
CPU usage and network metrics and is an integral part of ongoing scalability and performance
optimization development and CI performance regression testing.

**Subsytem benchmarks PRs**: [1](https://github.com/paritytech/polkadot-sdk/pull/2528), [2](https://github.com/paritytech/polkadot-sdk/pull/2970)

### Elastic scaling (MVP)

I played a major role in the design, development, and testing of the first iteration (MVP) of
Elastic Scaling, which was deployed to Kusama and currently allows parachains to
use up to 3 cores per relay chain block. I had several significant contributions to bootstrap
the node side and runtime implementation:

- [Introduce an assumed core index](https://github.com/paritytech/polkadot-sdk/pull/3229)
- [Runtime changes for backing multiple candidates ](https://github.com/paritytech/polkadot-sdk/pull/3231)
- [Benchbuilder improvements for elastic scaling](https://github.com/paritytech/polkadot-sdk/pull/3573)
- [Collator protocol support](https://github.com/paritytech/polkadot-sdk/pull/3795)
- [Statement distribution support](https://github.com/paritytech/polkadot-sdk/pull/3879)

### Elastic scaling (RFC103)

Played a primary role in initial design work: [Github](https://github.com/polkadot-fellows/RFCs/issues/92)

Authored [RFC 103](https://github.com/polkadot-fellows/RFCs/blob/main/text/0103-introduce-core-index-commitment.md)
and led the [planning](https://github.com/orgs/paritytech/projects/119/views/25) and
implementation in multiple parachain consensus protocol components.

Significant code contributions in both runtime and node side:

- [Introduce the new Polkadot primitives](https://github.com/paritytech/polkadot-sdk/issues/5044)
- [Node feature sanity checks](https://github.com/paritytech/polkadot-sdk/pull/5362)
- [Full Runtime implementation](https://github.com/paritytech/polkadot-sdk/pull/5423)
- [Bootstrap node implementation](https://github.com/paritytech/polkadot-sdk/pull/5679).
- [Candidate Validation](https://github.com/paritytech/polkadot-sdk/pull/5847)
- [Statement Distribution](https://github.com/paritytech/polkadot-sdk/pull/5883)

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 4 out of 21 referenda in which I was eligible to vote (19% voting activity) | I target to raise it to 80% at least for the next reporting period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
