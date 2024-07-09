# Evidence-0001: Promotion to Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/07/09                                                                                  |
| **Submitted by**| Andrei Sandu                                                                                |


## Member details

- Matrix username: @sandreim:parity.io
- Polkadot address: 13QdJvnJgfoitjrxESwrCWTaLMN8KvXxufDUucXM6EWGuxqh
- Current rank: 2
- Date of initial induction: 2023/07/18
- Date of last report: N/A
- Area(s) of Expertise/Interest: Parachain Consensus, Elastic Scaling, Nodes (scalability/performance, observability,resilience), Zombienet & integration testing



## Reporting period

- Start date: 2023/07/18
- End date: 2024/07/09


## Evidence

In the past year I have played a critical role and made major contributions in the following areas:
- Polkadot network scalability (more validators, more cores)
- increase parachain throughput and decrease latency with Elastic Scaling
- parachain consensus profiling and benchmarking (subsystem benchmarks)


### Network scalability (500 validators 100 cores)

**Planning and tracking**: I lead the project planning, development, testing and deployment of changes starting with 200 validators and 40 cores to currently proposed 500 validators and 100 cores on Kusama.  https://github.com/paritytech/roadmap/issues/26

**Assignment certificates v2**: Introduces a new kind of assignment certificate that batches multiple tranche0 in a single certificate/message: https://github.com/paritytech/polkadot-sdk/pull/1178

**Approval voting re-design**: I proposed a new design for the node aproval voting subsystems. This is expected to allow Polkadot to scale to 1kV and 200 cores in 2025 https://github.com/paritytech/polkadot-sdk/issues/1617

**Forum posts**
- Kusama scale up plan: https://forum.polkadot.network/t/update-parachain-validator-set-size-increase-on-kusama/8218
- Polkadot scale up plan: https://forum.polkadot.network/t/update-polkadot-validator-set-size-increase/8682


### Parachain consensus performance benchmarking 

I lead the design and development of the subsystem benchmarking initiative. This new development tool allows to recreate the network traffic and load found in large scale networks on your development machine. It performs stress test of one ore more parachain consensus subsystems without the need to run the network. It collects granular CPU usage and network metrics and is an integral part of ongoing scalability and performance optimization development and CI performance regression testing. 

**Availability read benchmarks PR** https://github.com/paritytech/polkadot-sdk/pull/2528
**Availability write benchmarks PR** https://github.com/paritytech/polkadot-sdk/pull/2970

### Elastic scaling

I played a major role in the design, development and testing of Elastic Scaling MVP. 

PRs bootstraping the node side and runtime changes: 
- Assume a CoreIndex for candidates: https://github.com/paritytech/polkadot-sdk/pull/3229
- Runtime changes for backing multiple candidates of same parachain:  https://github.com/paritytech/polkadot-sdk/pull/3231
- Benchbuilder improvements for elastic scaling: https://github.com/paritytech/polkadot-sdk/pull/3573
- Collator protocol support: https://github.com/paritytech/polkadot-sdk/pull/3795
- statement distribution support for multiple cores assigned to same parachain: https://github.com/paritytech/polkadot-sdk/pull/3879
- Introduce `candidates_pending_availability` runtime API: https://github.com/paritytech/polkadot-sdk/pull/4027

### Elastic scaling open collator set - CoreIndex commitments
Currently in the design stage, I have created two development plans discussed which one is best to follow in the current context: https://github.com/polkadot-fellows/RFCs/issues/92: 

1. Repurposing of `CandidateDescriptor` and `CandidateCommitments` fields: https://hackmd.io/xrzVVZ_qSZemEIVdEV8cpA
2. Introducing new versions for `CandidateDescriptor` and `CandidateCommitments`: https://hackmd.io/fWYvO8HQSFKjUlnpgwjcKw

### Runtime fixes

**CheckWeight signed extension**: Include extrinsic len as proof size https://github.com/paritytech/polkadot-sdk/pull/4765

### Support
- Active in [Polkadot OpenGov](https://polkadot.polkassembly.io/user/sandreim) and [Kusama OpenGov](https://kusama.polkassembly.io/user/sandreim).

### Evanghelism
- Participant on OpenDev calls,
- [Active in Polkadot forum](https://forum.polkadot.network/u/sandreim/activity).


