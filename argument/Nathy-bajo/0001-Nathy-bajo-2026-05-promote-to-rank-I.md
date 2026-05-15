# Argument-0001: Promotion to Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/05/15                                                                                  |
| **Submitted by**| Nathaniel Bajo                                                                              |


## Member details

- Matrix username: @nathanielbajo:matrix.org
- Polkadot address: 1HXh7kCk2Z9Er4TpqF7TPX6ivSnJTECesp44RP7jnP7RCeL
- Current rank: Candidate
- Date of initial induction: 2026/03/12 ([extrinsic](https://collectives.statescan.io/#/extrinsics/8415862-2))
- Date of last report: N/A
- Area(s) of Expertise/Interest:
    - FRAME / Runtime
    - XCM
    - Node & RPC infrastructure
    - JSON-RPC interface
    - Release engineering


## Reporting period

- Start date: 2025/02/01
- End date: 2026/05/15


## Argument

Hi everyone, I'm Nathaniel Bajo. I'm a full-stack Rust engineer with a background in embedded systems, permissionless architectures, and web security. Outside of my contributions to the Polkadot SDK and the fellowship runtimes, I build personal projects on Polkadot infrastructure, including ink!-based smart contracts and tooling that exercises the runtime, XCM, and JSON-RPC surfaces of the SDK. My contributions during this reporting period span the runtime (FRAME pallets and runtime APIs), the XCM layer, node-level RPC infrastructure, the JSON-RPC specification, and the fellowship runtimes' release engineering.

Below are my most relevant contributions for this period:

### 1. Runtime APIs & Pallet Governance (FRAME)

- **[Add `ProxyApi` runtime API to the Proxy pallet (#7320, merged)](https://github.com/paritytech/polkadot-sdk/pull/7320)**: Introduced a runtime API exposing `check_permissions` (does a `RuntimeCall` pass a `ProxyType`'s `InstanceFilter`?) and `is_superset` (does one `ProxyType` strictly contain another?), enabling off-chain clients and wallets to verify proxy call permissions and proxy-type hierarchies without re-implementing filter logic.
- **[`paras`: add freeze/unfreeze parachain functionality (#11106)](https://github.com/paritytech/polkadot-sdk/pull/11106)**: Implemented root-only extrinsics that fully halt a parachain (no block production, no relay-chain messaging) until explicitly unfrozen, giving governance a precise circuit-breaker for misbehaving paras.
- **[`pallet-broker`: extrinsic to reset base price (#7293)](https://github.com/paritytech/polkadot-sdk/pull/7293)**: Added an administrative extrinsic that lets governance/sudo reset the minimum/base price for coretime sales without a runtime upgrade, part of the broader coretime admin tooling.

### 2. Cross-Chain (XCM)

- **[Generic account converter for external ecosystems (#7313, merged)](https://github.com/paritytech/polkadot-sdk/pull/7313)**: Added `ExternalConsensusLocationsConverterFor`, a unifying converter that handles external global-consensus locations (and their child locations) while remaining backward-compatible with `GlobalConsensusParachainConvertsFor` and `EthereumLocationsConverterFor`. Reduces duplication across XCM configurations for bridged/external ecosystems.

### 3. Node & RPC Infrastructure

- **[`pallet-revive-eth-rpc`: SubstrateClientT trait + Asset Hub embedded RPC (#11297)](https://github.com/paritytech/polkadot-sdk/pull/11297)**: Scoped this work myself by opening the tracking issue [#11221](https://github.com/paritytech/polkadot-sdk/issues/11221), then integrated `pallet-revive`'s ETH RPC server directly into the Asset Hub Omni node. Introduced a `SubstrateClientT` abstraction so `EthRpcServerImpl` is generic over its backend, with a new `NativeSubstrateClient` providing an in-process path (no `subxt` dependency on the hot path) while preserving the `SubxtClient` path for the standalone binary. Registered behind an opt-in `revive-rpc` feature in `polkadot-omni-node-lib`. Removal of the standalone `revive-dev-node` binary will be done in a follow-up PR.
- **[Fix inconsistent BABE fork-choice via shared block-weight storage (#7550)](https://github.com/paritytech/polkadot-sdk/pull/7550)**: Introduced `SharedBlockWeightStorage`, a thread-safe in-memory cache that makes block weights immediately visible across concurrent import operations, addressing a fork-choice consistency issue that surfaced under parallel imports.
- **[`archive_unstable_transactionReceipt` (json-rpc-interface-spec #182)](https://github.com/paritytech/json-rpc-interface-spec/pull/182)**: Identified the gap and opened the spec issue [#181](https://github.com/paritytech/json-rpc-interface-spec/issues/181) myself, then specified and proposed a stateless RPC method for transaction-receipt lookup that lets light clients locate transactions without downloading full blocks. Targets the JSON-RPC v2 spec used by light clients across the ecosystem.

### 4. Release Engineering & Maintenance (Fellowship Runtimes)

- **[Verify runtime WASM size against thresholds (runtimes #1177)](https://github.com/polkadot-fellows/runtimes/pull/1177)**: Added a release-workflow gate that warns at 80% and blocks publication at 95% of each runtime's configured compressed-WASM size limit, opening a tracking issue summarising any breaches. Helps prevent surprise breaches of on-chain size limits at release time.
- **[Align runtimes (runtimes #1175)](https://github.com/polkadot-fellows/runtimes/pull/1175)**: Aligned all system-parachain runtimes on shared `system_parachains_constants` for `TransactionByteFee`, migrated `MaxFreezes` to `VariantCountOf<RuntimeFreezeReason>`, and cleaned up legacy `# Substrate` / `# Polkadot` / `# Cumulus` delimiter comments in crate manifests. Reduces drift between system-chain configurations.

### Summary

I'm genuinely passionate about building on Polkadot and want to keep deepening my contributions across the entire ecosystem. I'd like to continue this work at Rank I and take on more review responsibility.

Other ongoing contributions can be tracked via my open PRs on `polkadot-sdk`: [is:pr is:open author:Nathy-bajo](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+is%3Aopen+Nathy-bajo+).


## Voting record

N/A.


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
