# Retention at Rank 3

|                  |                                 |
| ---------------- | ------------------------------- |
| **Report Date**  | Date of submission (2025/01/06) |
| **Submitted by** | Jan Bujak                       |

## Member details

- Matrix username: @jan:parity.io
- Polkadot address: 15tRXfXoZXkjScB3Awv8s2saPjaicKYAyL1WZ3JP5kycoG9n
- Current rank: 3
- Date of initial induction: seeding
- Date of last report: 2024/05/09
- Area(s) of Expertise/Interest: Substrate, virtual machines, WebAssembly, host <-> runtime interface, performance, JAM, compilers and toolchains

## Reporting period

- Start date: 2024-05-10
- End date: 2025-01-06

## Evidence

Most of my time was spent working on [PolkaVM](https://github.com/paritytech/polkavm), which, while being one of many implementations
of PVM (as described in the [JAM Graypaper](https://graypaper.com)), is also the main vehicle for prototyping of any new additions
to the PVM spec before they end up in the Graypaper.

In total I've made 250+ new commits to the PolkaVM repository, totaling over 50k+ lines of code and 50+ PRs, with too many changes
to comprehensively list here; anyone interested in the gory details can take a look [at the list of commits](https://github.com/paritytech/polkavm/commits?author=koute)
and/or [the list of PRs](https://github.com/paritytech/polkavm/pulls?q=is%3Apr+author%3Akoute) I have made. My work has also directly
resulted in numerous changes to the PVM spec.

Here are some of the highlights:

- Prototype of 64-bit PVM support in PolkaVM, which we've then added to the Graypaper:
  - PRs in PolkaVM (there were many more, these are just a few major ones): https://github.com/paritytech/polkavm/pull/182 https://github.com/paritytech/polkavm/pull/206 https://github.com/paritytech/polkavm/pull/210
  - My HackMD describing the changes: https://hackmd.io/@hQTcJMiNR_K6HAoF_nY4qw/BkwgsG4Jye
  - Changes to the PVM spec: https://github.com/gavofyork/graypaper/pull/136
- Design work on the bit-manipulation instruction set extension based on RISC-V's `Zbb`
  - Implemented in this PR by Aman, which I've mentored and reviewed: https://github.com/paritytech/polkavm/pull/204
  - My HackMD describing the changes: https://hackmd.io/@koute/SJxTlrxN1g
  - Changes to the PVM spec: https://github.com/gavofyork/graypaper/pull/176
- Dynamic page faulting-related research and implementation (this is necessary to support inner PVMs in JAM)
  - Based on this experience this resulted in some changes to the inner PVM hostcalls in JAM, e.g. https://github.com/gavofyork/graypaper/pull/135/commits/21e264d72c2f353892fe69adc54eeb98f05611b7
- Prepared the initial set of [PVM test vectors](https://github.com/w3f/jamtestvectors/pull/3)
- Many toolchain improvements, culminating in being able to finally write and build Rust programs targeting PolkaVM/PVM using a fully upstream rustc, instead of having to use a custom fork.

I have also been closely collaborating with the Smart Contracts team within Parity to help [bring Smart Contracts to the Asset Hub](https://forum.polkadot.network/t/contracts-on-assethub-roadmap/9513)
on Polkadot, where PolkaVM will be used as the VM of choice. This work is currently still in-progress, with the first prototype already deployed on Westend.

I have also consulted on the [PolkaVM parachains runtimes MVP](https://github.com/paritytech/polkadot-sdk/pull/6704), although I haven't directly contributed code to that effort in `polkadot-sdk`.

Finally, I have hosted a guest talk during the Polkadot Blockchain Academy in Singapore regarding PolkaVM and PVM.

In the next six months I plan to continue to focus on PolkaVM, help get the PVM spec finalized for JAM 1.0, and support the Smart Contracts team.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|--------|---------------------|----------------------|----------------------------|----------|
|   III  |        70%          |         100%         |       ~40/100 (40%)        |          |

I admit my voting record activity is not as high as it should be; I will make a conscious effort to do better and vote more often.
