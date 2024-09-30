# Evidence-0001: Retention at Rank II

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2024/09/25) |
| **Submitted by**| Edward Mack                     |


## Member details

- Matrix username: @mackcom:matrix.org
- Polkadot address: 1ZYq7qWxvqC1rE4PKnTWwoVJYLtn99p9JM9cUn2WqbWr3Jt
- Current rank: 2
- Date of initial induction: Seeding
- Date of last report: NA
- Area(s) of Expertise/Interest: Gossamer node, parachain subsystems 


## Reporting period

- Start date: 2024/07/01
- End date: 2024/09/25


## Evidence
For the past three months my contributions to the Polkadot ecosystem has been implementing the parachain candidate validation subsystem for the Gossamer node.  The code that I have implemented focuses on the following areas of functionality:
- Implementing PVF pre-checking, the parachains' validation function (PVF) is used to validate state transitions of parachains, the pre-checking functionality confirms that this validation code is not malicious.  The implementation of this required an understanding of how to evaluate PVF blob and compile it so that it functions in our environment (Gossamer Node).  I utilized my understanding of the Gossamer Node's architecture along with consulting the Polkadot Parachain Host Implementers' Guide to design and build this subsystem.  The primary work involved in implementing this was contributed to the Gossamer repository in [ChainSafe PR 4205](https://github.com/ChainSafe/gossamer/pull/4205)
- Implementing functionality for handling candidate validation when all the validation data is provided exhaustively to the node.  This implementation involved researching and understanding the data necessary for conducting candidate validation, then utilizing the parachain's runtime function to validate that the provided validation data generates the expected result when processed by the validation function. The implementation for this was contributed to the Gossamer repository in [ChainSafe PR 4036](https://github.com/ChainSafe/gossamer/pull/4036)
- Implementing functionality for handling candidate validation with data from chain state.  This involves assembling validation data by querying the parachains' runtime API to request validation and chain state data.  I needed to understand where and how to assemble this data, then validate the data utilizing implementations that I had build for validation when data is provide exhaustively.  [ChainSafe PR 4067](https://github.com/ChainSafe/gossamer/pull/4067) is where the code for this implementation can be found.
- Along with these initiatives regarding candidate validation work was done to support those subsystems, including archetecting a structure for handling this functionality; [the PVF host](https://github.com/ChainSafe/gossamer/pull/4101), which forms the framework by which the candidate validation is handled.  

The above contributions provide functionality to the parachain subsystems of the Gossamer node, with the goal of creating a fully functional node to participate in the polkadot ecosystem.  By providing contribution to another node in the polkadot ecosystem we strengthen the resilency of the entire network.  Candidate validation is a primary function for a node participating in this network, being involved in implementing these systems has strengthened my understanding of the parachains and how they work with the relay chain.  I have shared this acquired knowledge by contributing to the open source Gossamer repository, and commenting on Github PRs and issues. 


## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                                                                                                                                                                                                                                                                               | Comments |
|---|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-|
|I  |90%   |N/A   |                                                                                                                                                                                                                                                                                                                          | |
|II |80%   |N/A   | I have voted on 0 out of 2 referenda in which I was eligible to vote (i.e 0 % voting activity).   | I intend to be more active regarding voting in the future. |
|III|70%   |100%  |                                                                                                                                                                                                                                                                                                                          | |
|IV |60%   |90%   |                                                                                                                                                                                                                                                                                                                          | |
|V  |50%   |80%   |                                                                                                                                                                                                                                                                                                                          | |
|VI |40%   |70%   |                                                                                                                                                                                                                                                                                                                          | |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

