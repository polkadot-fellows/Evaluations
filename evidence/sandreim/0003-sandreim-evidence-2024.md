# Evidence-0003: Promotion to Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/11/26                                                                                  |
| **Submitted by**| Andrei Sandu                                                                                |

## Member details

- Matrix username: @sandreim:parity.io
- Polkadot address: 13QdJvnJgfoitjrxESwrCWTaLMN8KvXxufDUucXM6EWGuxqh
- Current rank: 2
- Date of initial induction: 2023/07/18
- Date of last report: N/A
- Area(s) of Expertise/Interest: Parachain Consensus, Elastic Scaling, Node performance engineering, observability and resilience, Stress and integration testing

## Reporting period

- Start date: 2023/07/18
- End date: 2024/11/26

## Evidence

During the reporting period I have played an important role in the design, development and deployment of a few major contributions to Polkadot which had signficant impact:

- better decentralization and security by increasing parachain validators from 200 to 500
- more blockspace by increasing the number of usable cores to 100
- lowering the latency and increasing maximum throughput of parachains with Elastic Scaling
- faster and lower cost parachain consensus protocol performance engineering with Subsystem Benchmarks

I've been an active paritcipant in OpenDev calls and in the [Polkadot forum](https://forum.polkadot.network/u/sandreim/activity), constantly giving updates on the progress of the implementation, testing and deployment.

I consider that this evidence, detailed in next section, is aligned both in quality and quantity with the Fellowship for a rank 3 promotion.

### Increasing number of validators and cores

This is a multi year project which is still on going. I have started this project by searching for bottlnecks
in the node protocols implementation, network stack and runtime. At the time Polkadot had 200 validators
and 40 cores. I lead the [project planning](https://github.com/paritytech/roadmap/issues/26),
development, testing and deployment of protocol changes to scale up to 500 validators and 100.

Major design and code contributions:

- **Assignment certificates v2**: Introduces a new kind of assignment certificate that batches multiple tranche0 in a single certificate/message: https://github.com/paritytech/polkadot-sdk/pull/1178

- **Approval voting re-design**:
  [new design](https://github.com/paritytech/polkadot-sdk/issues/1617) that would allow the
  approval voting subsystems to process messages in parallel. This design was further
  refined and has been fully implemented and proven by benchmark tests that approval voting is no
  longer a bottleneck at a scale of 1000 validators and 200 cores.

I've communicated with the ecosystem about scaling up plans in forum posts and Element chats:
[Kusama](https://forum.polkadot.network/t/update-parachain-validator-set-size-increase-on-kusama/8218),
[Polkadot](https://forum.polkadot.network/t/update-polkadot-validator-set-size-increase/8682)

### Parachain consensus performance benchmarks

I designed and implemented multiple modular components that are used to emulate the network
traffic and load found in large scale networks on local development machine. It performs stress
test of one ore more parachain consensus subsystems without the need to run the network of that
size. It collects granular CPU usage and network metrics and is an integral part of ongoing
scalability and performance optimization development and CI performance regression testing.

**Availability read benchmarks PR** https://github.com/paritytech/polkadot-sdk/pull/2528
**Availability write benchmarks PR** https://github.com/paritytech/polkadot-sdk/pull/2970

### Elastic scaling (MVP)

I played a major role in the design, development and testing of the first iteration(MVP) of
Elastic Scaling which is was deployed to Kusama and currently allows parachains to
use up to 3 cores per relay chain block. I had several signficant contributions to bootstrap
the node side and runtime implementation:

- [Introduce an assumed core index](https://github.com/paritytech/polkadot-sdk/pull/3229)
- [Runtime changes for backing multiple candidates ](https://github.com/paritytech/polkadot-sdk/pull/3231)
- [Benchbuilder improvements for elastic scaling](https://github.com/paritytech/polkadot-sdk/pull/3573)
- [Collator protocol support](https://github.com/paritytech/polkadot-sdk/pull/3795)
- [Statement distribution support](https://github.com/paritytech/polkadot-sdk/pull/3879)

### Elastic scaling (RFC103)

Initial design work: [Github](https://github.com/polkadot-fellows/RFCs/issues/92)

Authored [RFC 103](https://github.com/polkadot-fellows/RFCs/blob/main/text/0103-introduce-core-index-commitment.md) and lead it's [planning](https://github.com/orgs/paritytech/projects/119/views/25) and development.

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
