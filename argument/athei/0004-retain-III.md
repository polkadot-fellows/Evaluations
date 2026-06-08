# Argument-0004: Retention at Rank III

|                  |                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------- |
| **Report Date**  | 2026/05/20                                                                                  |
| **Submitted by** | Alexander Theißen                                                                           |

## Member details

- Matrix username: @alex:parity.io
- Polkadot address: 15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1
- Current rank: III
- Date of initial induction: Seeding
- Date of last report: 2025/11/05
- Area(s) of Expertise/Interest: System Chain Pallets (Smart Contracts), PolkaVM, Virtual Machines, Host Functions

## Reporting period

- Start date: 2025/09/15
- End date: 2026/05/20

## Argument

In this reporting period I worked on the PolkaVM JIT integration. The goal is a set of host
functions that let the runtime spawn and execute PolkaVM instances on the host. With this in place
we can switch `pallet_revive` from the in-runtime PolkaVM interpreter to JIT compiled execution
without any changes to the runtime/contract boundary.

In parallel I shipped `pallet_revive` on Polkadot AssetHub. This is the production launch on the
main relay, following the Kusama release from my previous reporting period.

The rest of my work continued as described in my [previous argument](https://github.com/polkadot-fellows/Evaluations/pull/217):
coaching new hires, Discord support for Solidity builders on Westend AssetHub, gas mapping
follow-ups and `pallet_revive` maintenance.

### API & Code Design

#### Virtualization host functions

Smart contracts on AssetHub launched with an in-runtime PolkaVM interpreter. That was the
pragmatic choice for the first release but it caps throughput. To enable JIT execution we need
to move PolkaVM out of the runtime. The runtime keeps control over which program to run and how
much gas to spend, but compilation and execution live on the host side behind a stable
host-function ABI.

I designed this as `sp-virtualization`. The runtime sees three concrete types: `Module`,
`Instance` and `Execution`. Their move semantics enforce the program lifecycle. For example,
calling memory access methods outside of a syscall is a compile error. The host side owns all
PolkaVM types behind a `VirtManagerBackend` trait. It is exposed to the runtime as an
externalities extension (`VirtManagerExt`) instead of being attached to the WASM executor.
Compilation has three entry points: `compile_from_bytes`, `compile_from_storage_key` (auto-load
on cache miss), and a pure `lookup`. The compiled-module cache lives on the extension instance.
This way cache hits and misses are deterministic against chain state instead of host process
history. The cache status is reported back to the runtime so weight can be charged.

The design also adds `PassFatPointerAndReadOption<T>` to `sp-runtime-interface`. This is needed
to pass `Option<&[u8]>` across the FFI without SCALE overhead. It uses `(ptr=0, len=0)` as the
`None` sentinel.

### Code Contributions

#### Add virtualization host functions

The initial PR that introduces `sp-virtualization`, exposes a virtualization manager from
`sc-executor-wasmtime`, and adds the `sp-wasm-interface` plumbing for host calls. I opened this
PR back in 2024 alongside the broader Ethereum on AssetHub roadmap. We held it back while we
decided to use an in-runtime interpreter for v1. It merged in this reporting period.

PR: [Add virtualization host functions](https://github.com/paritytech/polkadot-sdk/pull/3520)

#### Rework `sp-virtualization` API

A larger follow-up that applies what we learned from the first design. It introduces the
`Module`/`Instance`/`Execution` typestate API, splits the host-side ownership into a new
`sc-virtualization` crate, replaces numeric syscall IDs with string `SyscallSymbol`s, adds the
`compile_from_storage_key` and `lookup` cache entry points with cache status reporting, moves
the compiled-module cache onto a per-extension `VirtManagerExt`, and adds
`PassFatPointerAndReadOption<T>` to `sp-runtime-interface`. It removes about 1000 lines of
trait-based abstraction (`VirtT`, `MemoryT`, the old `Virtualization` trait in
`sp-wasm-interface`, `native.rs`, manual error wire encoding) in favour of concrete types.

PR: [Rework sp-virtualization API](https://github.com/paritytech/polkadot-sdk/pull/11767)

#### Releasing `pallet_revive` on Polkadot

Following the Kusama release in the previous reporting period, I added `pallet_revive` to
Polkadot AssetHub, unified `WeightToFee` across the system chains by moving the fee definition
into the constants crate, and cut the `2.0.5` Fellowship runtimes release.

PRs:
[Add pallet_revive to Polkadot AssetHub](https://github.com/polkadot-fellows/runtimes/pull/1050),
[Release `2.0.5`](https://github.com/polkadot-fellows/runtimes/pull/1054).

#### Ongoing `pallet_revive` and tooling work

Smaller PRs that continue work covered by my previous argument: gas mapping follow-ups, EVM
compatibility fixes, parameter tuning, the `stable2512` backport, runtime toolchain bumps and
supporting infrastructure.

`polkadot-sdk`:
[#9670](https://github.com/paritytech/polkadot-sdk/pull/9670),
[#9928](https://github.com/paritytech/polkadot-sdk/pull/9928),
[#9942](https://github.com/paritytech/polkadot-sdk/pull/9942),
[#9968](https://github.com/paritytech/polkadot-sdk/pull/9968),
[#10026](https://github.com/paritytech/polkadot-sdk/pull/10026),
[#10027](https://github.com/paritytech/polkadot-sdk/pull/10027),
[#10047](https://github.com/paritytech/polkadot-sdk/pull/10047),
[#10089](https://github.com/paritytech/polkadot-sdk/pull/10089),
[#10100](https://github.com/paritytech/polkadot-sdk/pull/10100),
[#10157](https://github.com/paritytech/polkadot-sdk/pull/10157),
[#10160](https://github.com/paritytech/polkadot-sdk/pull/10160),
[#10214](https://github.com/paritytech/polkadot-sdk/pull/10214),
[#10302](https://github.com/paritytech/polkadot-sdk/pull/10302),
[#10708](https://github.com/paritytech/polkadot-sdk/pull/10708),
[#10740](https://github.com/paritytech/polkadot-sdk/pull/10740),
[#10780](https://github.com/paritytech/polkadot-sdk/pull/10780),
[#10805](https://github.com/paritytech/polkadot-sdk/pull/10805),
[#10816](https://github.com/paritytech/polkadot-sdk/pull/10816),
[#11839](https://github.com/paritytech/polkadot-sdk/pull/11839),
[#11992](https://github.com/paritytech/polkadot-sdk/pull/11992).

Other:
[`contracts-boilerplate#17`](https://github.com/paritytech/contracts-boilerplate/pull/17),
[`TorstenStueber/polkadot-runtimes#1`](https://github.com/TorstenStueber/polkadot-runtimes/pull/1).

### Social Interaction

Engagement was the same as in the previous reporting period: coaching and onboarding co-workers
via in-depth code review, supporting Solidity builders on Westend AssetHub via the Polkadot
Discord, and leading the smart contracts team.

## Voting Record

Please keep in mind that, in the absence of better tooling, I derived these numbers by manually
inspecting Subsquare. I used the [slider on Subsquare](https://collectives.subsquare.io/user/15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1/fellowship)
to filter for the timespan covered by this report (#392 to #527).

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
| ----- | ------------------- | -------------------- | -------------------------- | -------- |
| III   | 70%                 | 100%                 | 78%                        |          |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
