# Retention at Rank 3

|                  |                                 |
| ---------------- | ------------------------------- |
| **Report Date**  | Date of submission (2026/02/13) |
| **Submitted by** | Jan Bujak                       |

## Member details

- Matrix username: @jan:parity.io
- Polkadot address: 15tRXfXoZXkjScB3Awv8s2saPjaicKYAyL1WZ3JP5kycoG9n
- Current rank: 3
- Date of initial induction: seeding
- Date of last report: 2025/08/01
- Area(s) of Expertise/Interest: Substrate, virtual machines, WebAssembly, host <-> runtime interface, performance, JAM, compilers and toolchains

## Reporting period

- Start date: 2025-08-01
- End date: 2026-02-13

## Argument

As previously, I've spent most of my time working on [PolkaVM](https://github.com/paritytech/polkavm) and on things related to JAM.

Here are the major highlights:

- I've finished researching, designing and prototyping the new gas-cost model for JAM.
  - I wrote [a spec of the new gas-cost model to be included in the GP](https://github.com/gavofyork/graypaper/pull/508), which I expect to be merged soon.
  - I also authored several other simplifications/improvements to the PVM spec in the GP (these are included in the gas-cost model PR).
- I've authored over [100+ commits in PolkaVM](https://github.com/paritytech/polkavm/commits/master/) and cut 6 new releases.
  - Currently I'm the sole maintainer of PolkaVM, which has stopped being purely a research project for JAM, and has become an integral part of Polkadot,
    where it is being used (in production!) on the Polkadot Hub for `pallet-revive` smart contracts.

Going forward, I will continue my work on the PVM gas-cost model, which still lacks a mechanism for gas metering the memory paging mechanism
(which, as we've recently discovered, is necessary for security), and I will help get JAM to 1.0.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|--------|---------------------|----------------------|----------------------------|----------|
|   III  |        70%          |         100%         |        ~33/48 (68.75%)     |          |

My voting activity has improved by ~17% compared to the previous retention period.
