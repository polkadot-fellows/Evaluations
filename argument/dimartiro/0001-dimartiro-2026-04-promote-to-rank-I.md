# Argument-0001: Promotion to Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/04/16                                                                                  |
| **Submitted by**| Diego Romero                                                                                |


## Member details

- Matrix username: @dimartiro:matrix.org
- Polkadot address: 5FZGEDktFdfGuUjYAbdSdjwt67pXf4UQHcyiW9Wk4hrYvxvY
- Current rank: Candidate
- Date of initial induction: 2026/04/15
- Date of last report: N/A
- Area(s) of Expertise/Interest:
    - Substrate
    - Snowbridge
    - Developer Tooling
    - Clients (Gossamer)
    - JAM


## Reporting period

- Start date: 2023/03/20
- End date: 2026/04/16


## Argument

Hi everyone, I'm Diego Romero. I currently work at ChainSafe on Polkadot ecosystem infrastructure, contributing to [Gossamer](https://github.com/ChainSafe/gossamer) (an alternative Polkadot client implemented in Go) and to the JAM (Join-Accumulate Machine) implementation in Go. I am also a current participant of the Protocol Builders Program (PBP), which is deepening my grounding in the protocol internals I work on day-to-day. My contributions span protocol-level improvements, developer tooling, and client diversity — areas I believe are core to Polkadot's continued resilience and decentralisation.

Below are my most relevant contributions for this period:

### 1. Protocol & Bridge Improvements — Snowbridge

Contributions to Snowbridge on `polkadot-sdk`:

- **[Improve `inbound_queue::BenchmarkHelper` for more flexibility](https://github.com/paritytech/polkadot-sdk/pull/9627)** — Decoupled the `inbound_queue::BenchmarkHelper` from the mocks so it no longer hardcodes `register_token_message`, enabling any user to benchmark arbitrary custom messages.
- **[Add generic `AggregateMessageOrigin`](https://github.com/paritytech/polkadot-sdk/pull/8106)** — Generalised message origin handling, making the bridge logic more modular and easier to extend downstream.
- **[Rewards issue reported in Snowbridge V2](https://github.com/paritytech/polkadot-sdk/issues/8154)** — Identified a rewards-related issue affecting incentive distribution, contributing to the robustness of the bridge design.

These contributions strengthen a trust-free bridge that is explicitly in scope for the Fellowship, and directly impact protocol correctness and extensibility.

### 2. Developer Tooling — Forking Support in Foundry Polkadot

Contributions to [Foundry Polkadot](https://github.com/paritytech/foundry-polkadot) enabling a Foundry/Hardhat-like workflow for Substrate-based chains:

- PRs [#392](https://github.com/paritytech/foundry-polkadot/pull/392), [#426](https://github.com/paritytech/foundry-polkadot/pull/426), [#505](https://github.com/paritytech/foundry-polkadot/pull/505), [#508](https://github.com/paritytech/foundry-polkadot/pull/508)
- Implemented a lazy-loading backend that fetches remote state on demand, enabling local execution against real network state.
- Integrated RPC-based state retrieval, reducing the need for full state replication and fetching storage only when required.

**Impact:** Lowers the barrier for testing and debugging against live chains, bringing a developer-experience parity with mainstream EVM tooling to the Substrate/PolkaVM workflow.

### 3. Tooling, CI & Dependency Management — Zepter / polkadot-sdk

Contributions improving build reliability and maintenance of the `polkadot-sdk` codebase:

- **[Zepter duplicate-deps check in CI](https://github.com/paritytech/polkadot-sdk/pull/9809)** — Prevents dependency duplication across `Cargo.toml` sections at CI time.
- **[Remove unused dependencies](https://github.com/paritytech/polkadot-sdk/pull/9235)** — Reduces codebase complexity and potential attack surface.
- **[Deduplicate dependencies](https://github.com/paritytech/polkadot-sdk/pull/9233)** — Improves build times and binary size consistency.

These changes contribute to the long-term maintainability of the primary runtime implementation.

### 4. Client Diversity & Next-Gen Protocol Work

At ChainSafe, I contribute to:

- **[Gossamer](https://github.com/ChainSafe/gossamer)** — an alternative Polkadot host implementation in Go. Client diversity is critical for the decentralisation and resilience of the Polkadot Main Network.
- **JAM (Join-Accumulate Machine)** — contributing to the Go implementation of the next-generation Polkadot protocol.

This work is squarely within the Fellowship's scope: the internals of Polkadot node implementations and the protocol evolution that underpins them.

### Summary

My contributions focus on protocol-level improvements and developer experience:

- Improving Snowbridge correctness and extensibility
- Enabling realistic local development via forking in Foundry Polkadot
- Strengthening tooling and build reliability in `polkadot-sdk`
- Contributing to alternative client development (Gossamer) and future protocol evolution (JAM)


## Voting record

N/A — I am currently a Fellowship Candidate and do not yet have voting privileges.
