# Argument-0001: Promotion to Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/01/13                                                             |
| **Submitted by**| Enoch                                                                        |


## Member details

- Matrix username: @runcomet
- Polkadot address: 14SRqZTC1d8rfxL8W1tBTnfUBPU23ACFVPzp61FyGf4ftUFg
- Current rank: Candidate
- Date of initial induction: [2025-10-30](https://collectives.statescan.io/#/extrinsics/7488182-2)
- Date of last report: N/A
- Area(s) of Expertise/Interest: FRAME, Node, Coretime, JAM


## Reporting period

- Start date: 2021/11/30 
- End date: 2025/01/13


## Argument
Hello, I'm Enoch(runcomet). A candidate seeking promotion, showcasing clear examples of modest but substantial contribution to protocol development that demonstrates both competence and thoughtful consideration of ecosystem needs.

### Configurable Number of Genesis Accounts
This configuration allows developers to specify both the [number of accounts and their balances](https://github.com/paritytech/polkadot-sdk/pull/6267) for benchmarking, enabling realistic performance testing, ensuring that benchmarks reflect real-world usage patterns. This update eliminates the need for managing enormous configuration files, reduces memory usage and maintains compatibility with existing tooling.

### Genesis Patch Support for Frame Omni-Bencher
Following the merge of dev-accounts, this [enhancement](https://github.com/paritytech/polkadot-sdk/pull/10735) to the benchmarking tooling enables developers create customized genesis states that simulates real-world network condiitions, such as stress testing with many accounts or complex initial configurations, without requiring modifications to the actual chain specifications.

Runtime developers can now benchmark their logic against tailored initial states, ensuring performance metrics account for the diverse conditions that may arise in prodocution networks.

### Migration of Core Pallets to Umbrella Crate
Migrated [pallet-asset-freezer](https://github.com/paritytech/polkadot-sdk/pull/6599) and [pallet-atomic-swap](https://github.com/paritytech/polkadot-sdk/pull/6601) to the new FRAME umbrella structure. This migration is an important step in the broader architectural evolution of FRAME, as it reduces code duplication, improves maintainability, and makes the codebase more understandable for new developers.

### Improved Warp Sync Logging
This enhancement significantly improves the user experience during warp synchronization by providing clear, actionable progress information. Previously, logs displayed irrelevant static data that gave no meaningful indication of progress. The [new implementation](https://github.com/paritytech/polkadot-sdk/pull/10196) removes this confusing noise and instead shows the count of successfully synced eras. This gives users a tangible sense of completion, transforming the logs from opaque technical details into a helpful progress indicator and making the entire warp sync process more transparent

### CrowdSourced Descision Deposit
Currently finalizing the [Crowdsourced Decision Deposit](https://github.com/paritytech/polkadot-sdk/pull/10715) feature by implementing its test coverage, benchmarking, and migration logic.

This feature improves governance accessibility and decentralization by allowing a referendum's decision deposit to be funded by multiple participants instead of a single entity.

This intelligent contribution management prioritizes the largest donations and refunds smaller excess ones, ensuring efficient capital allocation while encouraging participation from supporters of all means. By lowering the financial barrier to proposal sponsorship, it fosters greater innovation and diversity in governance, strengthening the ecosystem's resilience through more representative community involvement.

### Commitment
I am a full-stack developer who began contributing to the core code of the Polkadot ecosystem in 2021, with work in fundamental repositories like [Substrate](https://github.com/paritytech/substrate/pulls?q=is%3Apr+author%3AECJ222+is%3Aclosed+is%3Amerged) and [Polkadot](https://github.com/paritytech/polkadot/pulls/ECJ222). I have since expanded my contributions to Substrate-based ecosystems, such as [Darwinia](https://github.com/darwinia-network/darwinia/pull/953).

Having witnessed the technology's evolution, I am eager to participate more directly in the technical discussions and RFC processes that shape the platform's future. My early initiative on [RFC-0097](https://github.com/paritytech/polkadot-sdk/pull/7398) demonstrates this commitment.

My work has centered on improving user and developer experience. Moving forward, I aim to take on increasingly meaningful tasks that strengthen both the tools and the protocols underpinning Polkadot.

## Voting record
N/A, I am a candidate.

## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 


