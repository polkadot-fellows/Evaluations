# Argument-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/05/07                                                             |
| **Submitted by**| Enoch                                                                        |


## Member details

- Matrix username: @runcomet:matrix.org
- Polkadot address: 14SRqZTC1d8rfxL8W1tBTnfUBPU23ACFVPzp61FyGf4ftUFg
- Current rank: I
- Date of initial induction: [2025-10-30](https://collectives.statescan.io/#/extrinsics/7488182-2)
- Date of last report: 2026/01/13
- Area(s) of Expertise/Interest: FRAME, Node, Coretime 


## Reporting period

- Start date: 2026/01/13
- End date: 2026/05/07


## Argument

During this reporting period I sustained technical contributions to the PolkadotSDK and the broder ecosystem, focusing on expanding coretime observability, governance ecosystem testing, technical design discussions and ensuring network reliability.

### Governance Testing: Whitelist Pallet Deferred Dispatch
Added full [E2E test coverage](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/595) for the `pallet-whitelist` deferred dispatch feature on both Polkadot and Kusama AssetHub. This feature is not yet merged upstream and required direct addition to generate custom WASM binaries. The resulting test suite validates both success and failure paths, ensuring this complex feature works correctly in production. 

This work was not only essential for validating the whitelist pallet but also demonstrates how to unblock testing efforts by pragmatically configuring live runtime environments, leaving behind a reusable pattern for others to follow.

### NFT Collection Identity: Origin to Collection ID Mapping
Introducing direct [origin to collection](https://github.com/paritytech/polkadot-sdk/pull/11212) mapping, eliminating the need to have wrapper pallets extract the ID and call `create_collection_with_id`. This feature will allow a collection to be created with an ID derived directly from the calling origin, solving a critical pain point for DAOs and other pallets that require a one to one mapping between an on-chain entity and a collection ID.

### Network Reliability: Import Queue Backpressure
On the networking front, I have taken ownership of adding [import queue backpressure](https://github.com/paritytech/polkadot-sdk/pull/11998), which addresses the unbounded growth of the block import channel between `BasicQueueHandle` and `BlockImportWorker` under heavy load. The goal is to propagate backpressure from the import queue all the way back to individual syncing strategies, so that nodes can slow down block requests from the network when they cannot import fast enough, improving stability and reliability under load.


## Voting record
|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |No referenda for my rank  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 


