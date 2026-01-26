# Argument-0008: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/01/16)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: II
- Date of initial induction: 2024-04-26
- Date of last report: 2025/10/20
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling, Availability, Collator Protocol


## Reporting period

- Start date: 2025/10/20
- End date: 2026/01/16


## Argument

During this reporting period, I continued leading the [`anvil-polkadot`](https://github.com/paritytech/foundry-polkadot/tree/master/crates/anvil-polkadot) project, a critical component for the launch of EVM-compatible smart contracts on Polkadot Hub. This highly customized Substrate node provides extensive Ethereum test RPCs, enabling smart contract developers to perform comprehensive automated and manual testing in an environment closely matching Polkadot Hub's production setup, while maintaining low overhead, high customizability and a familiar interface for existing EVM developers.

I led a cross-organizational team of six engineers (four from Parity and two from Chainsafe) to deliver a functional anvil clone built on `pallet-revive` and Substrate node components. This project serves as the foundation for all end-to-end test tooling for contract developers on Polkadot, significantly improving developer experience by allowing teams to validate their code using familiar tooling with minimal modifications to existing test suites.

Building on the design, development plan, and foundational prototype I authored in the previous reporting period, I continued leading prioritization and development efforts throughout this period. I provided substantial technical guidance and conducted numerous code reviews across the entire team. Additionally, I played a major role in testing and validating anvil against test suites, root-causing issues, and implementing fixes across both `pallet-revive` and `anvil-polkadot`.

Fixes and improvements in pallet-revive include [a fix for block pruning](https://github.com/paritytech/polkadot-sdk/pull/10175) on chain reversion, adding [support for bypassing EIP-3607](https://github.com/paritytech/polkadot-sdk/pull/10387).
Some of the more notable fixes done in anvil-polkadot in the reporting period include [fixing get/setStorage RPCs](https://github.com/paritytech/foundry-polkadot/pull/385) and support for [sending transactions from contract accounts](https://github.com/paritytech/foundry-polkadot/pull/423).

The project is now out of my stewardship and entering maintenance mode, having completed the majority of features we deemed critical for launch. I am remaining in a role of advisor and
occasional code reviewer but starting this month, I will now get back to my previous work on parachain consensus.
More specifically, ensuring the collator protocol revamp is merged and deployed (which I was the main author of) through guidance and reviews and beginning
working on improvements for parachain block confidence.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II  |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referendums available for my rank to vote on. |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

