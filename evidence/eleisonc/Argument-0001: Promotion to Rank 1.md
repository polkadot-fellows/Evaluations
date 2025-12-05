# Argument-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/10/22                                                            |
| **Submitted by**|  Christopher Kalule                                                                        |


## Member details

- Matrix username: @eleisonc:matrix.org
- Polkadot address: 16JMzFbwMuLs8SooaTxiBZcd1e7HPUGchTBPtbDHk1Ubd9bT
- Current rank: 0
- Date of initial induction: 2025/10/20
- Date of last report:  N/A
- Area(s) of Expertise/Interest: Node SDK, Frame, Smart Contracts(Ink!v6), Bridges, Benchmarking, Governance.


## Reporting period

- Start date: 2024/11/18
- End date: 2025/10/21


## Argument
I bring 8+ years of full-stack engineering experience, now focused on Rust and blockchain development following 
completion of the [Let's Get Rusty Live certification program](https://drive.google.com/file/d/1yZ9f5L0ap5yOOTmN-8LvvCaO7xnen9a_/view) 
and  [PBA-X Wave #4](https://app.kajabi.com/certificates/d22ebcca). Currently serving as Developer Advocate for Polkadot
Africa (Uganda), I've been contributing to the Polkadot SDK since November 2024, focusing on runtime infrastructure, XCM
benchmarking infrastructure, and technical debt reduction.

My Fellowship application is driven by a thirst for deeper protocol-level and blockchain involvement and nothing beats 
contributing to the solution itself. This is about building confidence through genuine implementation experience, not 
just reading documentation. That hands-on knowledge naturally strengthens my ability to mentor when opportunities arise. 
My contributions since November have been recognized by the Polkadot SDK developers community with tips and encouragement, 
demonstrating this commitment.

PBA-X provided foundational knowledge in blockchain architecture, tokenomics, and game theory that goes beyond just 
Rust for blockchain. I immediately applied this at the [Polkadot Africa (Uganda) workshop for Sub0](https://x.com/KamalaImmac/status/1974558670303473682), 
where I mentored developers from blockchain fundamentals through building ink! v6 smart contracts. I want to deepen 
that expertise through active SDK contributions and it will be a pleasure working with the top engineers in the space.

**Key Contributions**

**Automated Omni Node testnet setup**
I automated chain spec generation by using pre-built CI integration, streamlining development workflows and improving ZombieNet compatibility. This automation reduces setup friction for developers working on parachain node implementations and testing. By having an already generated Chain Spec File whose runtime version matches with  that of  Polkadot-sdk.

PR: [Link](https://github.com/paritytech/polkadot-sdk/pull/6529)

**Removal of ElasticScalingMVP feature gates**
Collaborated with maintainers to remove outdated ElasticScalingMVP feature flag checks from backing and provisioner subsystems. Since elastic scaling became permanently enabled, these conditional checks were no longer necessary.

PR: [Link](https://github.com/paritytech/polkadot-sdk/issues/7211)

**Updated XCM benchmarking for system parachains**
Reconfigured XCM benchmarking configurations across Rococo and Westend system parachains (Asset Hub, Bridge Hub, Collectives, Coretime, and People) to support sibling parachain delivery instead of relay chain delivery.This update aligns benchmarks with the current architecture, where asset transfers and other cross-chain operations occur between parachains rather than via the relay chain. It ensures more accurate performance measurements and realistic test conditions for parachain developers. 
PR: [Link](https://github.com/paritytech/polkadot-sdk/pull/7321)


## Voting record
N/A, I am a candidate.


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

