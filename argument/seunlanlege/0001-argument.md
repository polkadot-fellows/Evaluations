# Argument-0001: Promotion to Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/06/02                                                                                  |
| **Submitted by**| Seun Lanlege                                                                                |


## Member details

- Matrix username: @seunlanlege:matrix.org
- Polkadot address: 1333zsMafds2sKAr8nG3zwXTCHPYv2Nm6CRgakpu6YVGt7nM
- Current rank: `1`
- Date of initial induction: Seeding
- Date of last report: 2025/12/15 (Retention at Rank II, [#231](https://github.com/polkadot-fellows/Evaluations/pull/231))
- Area(s) of Expertise/Interest: Hyperbridge, BEEFY, trust-free bridges, BLS cryptography


## Reporting period

- Start date: 2024/06/01
- End date: 2026/06/02


## Context

I was demoted from Rank II to Rank I on 2026-06-01 by the Fellowship Secretary
after missing the Rank II retention defense window during the Hyperbridge
security incident response
([extrinsic](https://collectives.statescan.io/#/extrinsics/8993139-2)). The
work below is what I would have submitted in defense had I filed in time, and
the scope of what has shipped since my last successful retention is in my view
beyond Rank II. I am therefore requesting promotion directly to Rank III, to
be enacted via `fellowshipCore.promote_fast`, which the pallet explicitly
supports for out-of-band promotions
([`core-fellowship/src/lib.rs:531`](https://github.com/paritytech/polkadot-sdk/blob/master/substrate/frame/core-fellowship/src/lib.rs#L531)).


## Argument

### Primary/supporting role in formalising or implementing a major protocol component

**Hyperbridge — trust-free interoperability layer for Polkadot.** Hyperbridge is
a parachain that verifies BEEFY and GRANDPA consensus proofs to provide
trust-free cross-chain messaging — exactly the class of work the Manifesto
names in scope ("trust-free bridges relying on said consensus algorithms
utilised by system chains"). I have led the protocol's design and
implementation for over two years. Hyperbridge is deployed to Polkadot Hub
mainnet:
- Mainnet contract addresses (Polkadot Hub): https://docs.hyperbridge.network/developers/evm/contract-addresses/mainnet/#polkadot-hub

**BLS-BEEFY verifier circuit in gnark.** I led the implementation of a
BLS12-381 aggregated-public-key proof circuit in gnark, which will enable
succinct verification of Polkadot's BLS-BEEFY consensus proofs once that
upgrade is live. This unblocks one of the longest-standing dependencies for
practical Polkadot light clients on EVM chains.
- https://github.com/polytope-labs/gnark-apk-proofs

**Reporting a critical soundness bug in `paritytech/merkle-mountain-range`.**
As part of our internal audit following the Hyperbridge security incident, we
identified a soundness vulnerability in the MMR proof verification code: the
verifier could be tricked into accepting forged leaves sharing a duplicate
leaf index as verified. The consequences extend across the Polkadot stack —
BEEFY proof verification, any system-chain bridge that consumes MMR proofs,
and the [proposed XCMP design](https://forum.polkadot.network/t/xcmp-design-discussion/7328),
which was specified to use MMR proofs for inbound-message verification. We
reported it to Parity; the fix was authored by Bastian Köcher and merged as
[paritytech/merkle-mountain-range#10](https://github.com/paritytech/merkle-mountain-range/pull/10).
- Post-mortem (includes the vulnerability writeup): https://blog.hyperbridge.network/april-13-post-mortem/


### External advocacy & high-quality publication

The Polytope Labs research site collects our published work on Polkadot
consensus, bridging, and cryptographic research:
- https://research.polytope.technology

Conference talks and podcast / interview appearances on Polkadot and Hyperbridge:
- **ETHDenver** — https://www.youtube.com/watch?v=qp-aar9Wl0s
- **zkSummit (ZK10):** *zkCasper — An Accountable Light Client* —
  https://www.youtube.com/watch?v=tqkOU0FsN8I&t=739s
- **When Shift Happens — DROPS E20:** *This Security Issue Is Costing Crypto
  Users Millions of Dollars* — https://www.youtube.com/watch?v=m2yiVrxz1qw


### Ecosystem knowledge sharing

- Responsibly disclosing critical vulnerabilities to Parity and publishing
  post-mortems so the wider ecosystem can learn from them (most recently the
  MMR proof-verification soundness bug — see post-mortem linked above).
- Driving the public case for BLS-BEEFY as the next BEEFY consensus upgrade
  across research publications, podcasts, and conference talks.
- The Hyperbridge codebase, docs, and integration guides serve as a reference
  implementation for BEEFY/GRANDPA consensus verification on EVM and other
  ecosystems.


### Demonstrable ecosystem impact

**DeFi Singularity (pre-token-gateway incident).** Hyperbridge facilitated the
DeFi Singularity liquidity campaign, which moved DOT to where liquidity already
exists rather than waiting for liquidity to arrive on Polkadot:
- **$24.3M** in DOT purchased from Uniswap / PancakeSwap pools
- **10.66M DOT** total purchased
- **11,563** unique buyers
- **5.19M DOT** bridged across chains via Hyperbridge

Report: https://forum.polkadot.network/t/polkadot-defi-singularity-report/17388


### Philosophical defense of Polkadot

The core thesis of Polkadot — shared security, sovereign execution, and
trust-minimised interoperability via cryptographic proofs rather than
multisigs — is the design lineage Hyperbridge extends. The choice to build
Hyperbridge as a Polkadot parachain verifying BEEFY proofs (rather than as a
standalone multisig bridge or an optimistic system) is itself the position I
defend in public against alternative ecosystems.


### Time at Polkadot

Over six years contributing to the Polkadot stack — core developer at Parity
(parity-ethereum, substrate, polkadot), substrate-IBC work at Composable, and
two-plus years founding and leading Polytope Labs / Hyperbridge as my primary
life-focus.


## Voting record

At Ranks I and II, voting eligibility is restricted by `MinRankOfClass` to the
`Members` and `Proficients` tracks respectively; most Fellowship referenda
during this period were on higher tracks and therefore not votable at my rank.

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
| --- | --- | --- | --- | --- |
| I | 90% | N/A |  | Rank I can only vote on the `Members` track |
| II | 80% | N/A | N/A | Rank II adds the `Proficients` track; no eligible referenda during the reporting period |
| III | 70% | 100% |  |  |
| IV | 60% | 90% |  |  |
| V | 50% | 80% |  |  |
| VI | 40% | 70% |  |  |


## Misc

- [ ] Question(s):
  - Given the demotion was a missed-defense procedural lapse during the
    Hyperbridge incident response, I am requesting `promote_fast(_, 3)`
    rather than the conventional rank-by-rank path. I welcome the in-person
    interview required for Rank III promotion under the Evaluations process.

- [ ] Concern(s):

- [ ] Comment(s):
