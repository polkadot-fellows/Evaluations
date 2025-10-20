# Argument-0007: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/10/20)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: II
- Date of initial induction: 2024-04-26
- Date of last report:  2025/07/09
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling, Availability, Collator Protocol


## Reporting period

- Start date: 2025/07/09
- End date: 2025/10/20


## Argument

My primary focus earlier this year was the design and implementation of the new collator protocol — the interface that facilitates communication between backing validators and collators. This protocol is a key upgrade to improve the reliability and resilience of the parachain backing process and ensure liveness, particularly in support of the Asset Hub migration.

During previous periods, I designed and implemented the majority of the components underpinning this protocol. In this current reporting period, I continued this effort by continuing the [main subsystem logic](https://github.com/paritytech/polkadot-sdk/pull/8541).
This is the final substantial component required to make the system functional and enable testing on live networks. Subsequently, we reprioritised in favour of a short-term solution to unblock the Asset Hub migration, implemented by @tdimitrov, for which I provided reviews and early guidance. I plan on offering additional support for the engineers that will continue my work on the collator protocol, which aims to be completed by the end of the year.

However, my focus at the moment and for most of the reporting period was a new strategic project for the launch of EVM-compatible smart contracts on asset hub.

I am leading a team of four engineers at Parity to implement an EVM-compatible test node built on Substrate — [`anvil-polkadot`](https://github.com/paritytech/foundry-polkadot/tree/master/crates/anvil-polkadot).
This project is modeled after the widespread Ethereum `anvil` test node, but using a Substrate node with EVM contract support via `pallet-revive`.

This effort is crucial to the developer experience for the upcoming Polkadot Hub, making it easy for smart contract teams to validate their code using familiar tooling.
I authored the project’s [design and development plan](https://github.com/paritytech/foundry-polkadot/issues/209), wrote the [initial prototype](https://github.com/paritytech/foundry-polkadot/pull/220) and implemented foundational features such as seamless arbitrary state injection into running chains (PR https://github.com/paritytech/foundry-polkadot/pull/296). I also provide ongoing technical support and reviews for the team.

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

