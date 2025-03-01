# Evidence-0002: Retention at Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/03/01)                                                             |
| **Submitted by**| Alexander Theißen                                                                           |

## Member details

- Matrix username: @alex:parity.io
- Polkadot address: 15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1
- Current rank: III
- Date of initial induction: Seeding
- Date of last report: N/A
- Area(s) of Expertise/Interest: System Chain Pallets (Smart Contracts), PolkaVM, Virtual Machines, Host Functions

## Reporting period

- Start date: 2024/09/15
- End date: 2025/03/15

## Evidence

In the last reporting period, I started working on bringing Ethereum compatibility to AssetHub via PolkaVM. This included
[writing](https://github.com/paritytech/polkadot-sdk/pull/5293) the initial version of `pallet_revive`.

In this reporting period, my focus was on getting the pallet ready for deployment to production.

### API & Code Design

In this section, I list the design work. I also implemented those designs. Links can be found in the `Code Contribution`
section.

#### Defining the API Scope

Deploying a smart contract platform to production is tricky because we are dealing with immutable code. That means
all the APIs we expose need to be supported forever, similar to the host functions available to the Polkadot runtimes.

This means a lot of work went into deciding which APIs should be available to contracts in the first release and how to add
new functionality over time.

I broke down the functionality into multiple milestones, which will be deployed incrementally. It boils down to only launching with
the absolute minimal functionality: The initial API only includes APIs that directly correlate with EVM instructions.

Additional functionality unique to AssetHub will only be available as precompiles later. This also applies to core functionality of the
pallet if it has no correspondence on Ethereum. This keeps the API surface small and allows us to make more changes later. I summarized
the milestones in [this project board](https://github.com/orgs/paritytech/projects/29/views/1).

#### Address Mapping

We have to deal with the fact that AssetHub uses a different address format than Ethereum. There is some prior art by Acala and other
chains. I looked at their implementations and decided on a slightly different design that will eventually allow for what we call
"cross-signing": Signing Ethereum transactions with Polkadot keys and also signing Polkadot transactions with Ethereum keys.

#### Managing an Evolving PolkaVM

We are using PolkaVM to run contracts. PolkaVM is specified as part of the grey paper, but the spec is not yet finalized.
Most notably, the gas model is missing. To still launch into production, I needed to find ways to deal with an evolving PolkaVM.
I opted for adding very strict static validation on contract code upload to minimize the features contracts can use. We also explicitly
exclude any gas/weight-related numbers from the stability guarantees for contracts. Additionally, we version each uploaded code to
allow behavior changes later on.

### Code Contributions

My main code contributions are all related to the above design work.

#### Static Validation

To safely run contracts, I decided to statically validate all codes on upload. No further inspection is done
when the contract is run. This keeps the hot path of calling contracts fast and allows us to change the validation later
on without affecting existing contracts.

1) Ensure that contracts do not consume too much memory, either through code or data. This is important since the memory
available inside the runtime is very limited: https://github.com/paritytech/polkadot-sdk/pull/5726

2) Validate all instructions and limit the size of basic blocks. This is important since large basic blocks could make the
lazy interpreter vulnerable to DoS. It also allows us to add new instructions later without changing existing
code behavior: https://github.com/paritytech/polkadot-sdk/pull/5939

3) Validate all used host functions statically so we can add new functions later on without changing existing
code behavior: https://github.com/paritytech/polkadot-sdk/pull/6759

#### Address Mapping

I implemented our design of the address mapping that allows using both Polkadot and Ethereum addresses to interact
with `pallet_revive`: https://github.com/paritytech/polkadot-sdk/pull/6096

#### Assigning Safe Weights

In addition to the host functions, we also need to assign weights for uploading contracts and instruction execution. I did that
by generating runtime benchmarks using the PolkaVM text assembler.

1) The benchmark for code upload needs to generate PolkaVM bytecode of a specific size while also taking the maximum basic block
size into account: https://github.com/paritytech/polkadot-sdk/pull/7568

2) In the absence of a finalized gas model in PolkaVM, I opted for assuming the absolute worst case for each instruction: A cache unaligned load.
Please note that this overestimates the cost and will be rectified once we have a gas model: https://github.com/paritytech/polkadot-sdk/pull/7721

### Setting Up a Documentation Platform

I bootstrapped a documentation portal for smart contracts on AssetHub: https://github.com/paritytech/contract-docs

### Social Interaction

Apart from my duties of leading the smart contracts team, I am active on the Polkadot Discord to support
builders using Solidity smart contracts on Westend AssetHub.

## Voting Record

I have voted on [`115`](https://collectives.subsquare.io/user/15db5ksZgmhWE9U8MDq4wLKUdFivLVBybztWV8nmaJvv3NU1/votes) proposals
in total. These are `60` votes since the last report. To my best knowledge, that includes every referendum I could vote on.
I retained `100%` voting agreement.

Please keep in mind that, in the absence of better tooling, I derived these numbers by manually inspecting Subsquare.

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
