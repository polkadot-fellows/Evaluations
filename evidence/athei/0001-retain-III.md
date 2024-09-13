# Evidence-0001: Retention at Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/08/26)                                                             |
| **Submitted by**| Alexander Theißen                                                                           |


## Member details

- Matrix username: @alex:parity.io
- Polkadot address: 15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1
- Current rank: III
- Date of initial induction: Seeding
- Date of last report: N/A
- Area(s) of Expertise/Interest: System Chain Pallets (Smart Contracts), WebAssembly, Virtual Machines, Host Functions


## Reporting period

- Start date: 2024/03/07
- End date: 2024/09/15


## Evidence

In this reporting period, my main focus is on making and executing a plan that brings Ethereum compatibility to Polkadot.
This is of significance because the adoption of new technology greatly benefits from backwards compatibility.

### API & Code Design

I needed to decide on how we would support Ethereum. Re-using frontier would be the quickest path but wouldn't improve enough
over existing Ethereum L2 solutions. It also wouldn't contribute to the Ethereum compatibility of JAM. This is why I designed
a system where YUL (solc intermediate representation) bytecode is recompiled to PolkaVM instead of executing
EVM bytecode like frontier does.

This plan consists of multiple new components. I commissioned and oversee the implementation of those components
and laid out the design on the Polkadot Forum [here](https://forum.polkadot.network/t/contracts-on-assethub-roadmap/9513).

### Code Contributions

I contributed two parts of that plan in this reporting period:

1) [The pallet](https://github.com/paritytech/polkadot-sdk/pull/5293) to be deployed to AssetHub that ties all components together.

2) [A set of host functions](https://github.com/paritytech/polkadot-sdk/pull/3520) that allows parachains to execute JIT-compiled
PolkaVM programs. However, we delayed this plan in order to wait for the PolkaVM spec. We will use an in-runtime PolkaVM interpreter
in our first iteration.

### Social Interaction

A big part of that plan was finding consensus on how to offer Smart Contract support in Polkadot.
Historically, Polkadot took the stance of leaving that functionality up to parachain builders.
In order to change course, I laid out a plan and found consensus among token holders for said plan:
https://polkadot.subsquare.io/referenda/885

## Voting record

I have voted on [`55`](https://collectives.subsquare.io/user/15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1/votes)
out of [`108`](https://collectives.subsquare.io/fellowship) referenda in which I was eligible to vote in this reporting period.

This constitutes `55%` voting activity. I retained `100%` voting agreement.

In the last two months, my voting activity was nearly `100%` and I am committed to keeping my activity above the
threshold in the next reporting period.

Please keep in mind that in the absence of better tooling, I derived those numbers by manually inspecting subsquare.

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
