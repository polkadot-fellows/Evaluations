# Retention at Rank 3

|                  |                                 |
| ---------------- | ------------------------------- |
| **Report Date**  | Date of submission (2025/08/01) |
| **Submitted by** | Jan Bujak                       |

## Member details

- Matrix username: @jan:parity.io
- Polkadot address: 15tRXfXoZXkjScB3Awv8s2saPjaicKYAyL1WZ3JP5kycoG9n
- Current rank: 3
- Date of initial induction: seeding
- Date of last report: 2025/01/06
- Area(s) of Expertise/Interest: Substrate, virtual machines, WebAssembly, host <-> runtime interface, performance, JAM, compilers and toolchains

## Reporting period

- Start date: 2025-01-06
- End date: 2025-08-01

## Evidence

Most of my time once again was spent working on [PolkaVM](https://github.com/paritytech/polkavm),
and on research and experiments related to the new gas cost model for JAM.

- I made 200+ new commits to the PolkaVM repository across 18 PRs, with numerous fixes and improvements to the VM and the toolchain.
  - I wrote [a gas benchmarking harness](https://github.com/paritytech/polkavm/pull/305) to aid in my work on the new gas cost model for JAM.
  - I ported [Quake to PolkaVM](https://github.com/paritytech/polkavm/pull/289), which was then ported by Ivan to JAM.
- I started an [SDK for CoreVM](https://github.com/paritytech/polkaports) and ported musl to CoreVM, which makes it possible
  to compile completely unmodified programs and run them on JAM's CoreVM.
- I wrote [a new memory allocator](https://github.com/koute/picoalloc) to be used in JAM services, and I've also made
  a PR to `polkatdot-sdk` to potentially [use it as a local allocator](https://github.com/paritytech/polkadot-sdk/pull/8992).
- I hosted a talk about writing recompilers for other JAM implementers during the JAM Experience 2025 in Lisbon.
- I wrote [benchmarks to compare PVM and our potential new gas cost model with EVM](https://github.com/koute/evm-benchmarks/).

Currently I'm still busy working on the new, better gas cost model for PVM and JAM, which I hope I'll be able to
make public in the near future, and get it merged into the Graypaper.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|--------|---------------------|----------------------|----------------------------|----------|
|   III  |        70%          |         100%         |        ~47/91 (51%)        |          |

Unfortunately my voting record activity is still not as high as it should be, but I've managed
to improve it by 11% compared to the previous reporting period.
