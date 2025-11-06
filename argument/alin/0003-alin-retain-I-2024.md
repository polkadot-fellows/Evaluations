# Evidence-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/12/19)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: I
- Date of initial induction: 2024-04-26
- Date of last report: 2024/10/01
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling, Availability


## Reporting period

- Start date: 2024/10/01
- End date: 2024/12/19


## Evidence

My contributions in these past months have been mostly centered around Elastic Scaling.

### Elastic Scaling

I have continued the implementation of [RFC103](https://github.com/polkadot-fellows/RFCs/pull/103), which enables having an untrusted collator
set when using elastic scaling:
- creating v2 receipts on collation-generation: https://github.com/paritytech/polkadot-sdk/pull/5908
- refactoring and hardening the core index check: https://github.com/paritytech/polkadot-sdk/pull/6217
- validating the receipt version when fetching the collation: https://github.com/paritytech/polkadot-sdk/pull/6011
- adding e2e zombienet-sdk test that verifies elastic scaling works both with the old and new receipt versions: https://github.com/paritytech/polkadot-sdk/pull/6452
- successfully debugged 12 core elastic scaling which will enable 500ms block times: https://github.com/paritytech/polkadot-sdk/issues/6858 

I have also started updating the elastic scaling enablement guide for parachain teams (PR still open): https://github.com/paritytech/polkadot-sdk/pull/6739 

Another notable contribution is my involvement in the design discussions around [streamlined block production](https://github.com/paritytech/polkadot-sdk/issues/5190#issuecomment-2505949587)
I researched and proposed an alternative implementation idea which would achieve the desired result in a much shorter time
(thanks to the simpler design, despite it being less efficient). I successfully developed a PoC and tested it with gluttons and spammening parachains.
The code is available here: https://github.com/paritytech/polkadot-sdk/tree/alindima/post-state-poc

### Other contributions:

- Offering significant guidance and help on the collation fetching fairness PR: https://github.com/paritytech/polkadot-sdk/pull/4880
- I have started offering technical mentorship for a new hire inside Parity's parachains team (which I'm a part of)
- Fix a best backable chain reversion bug in prospective parachains: https://github.com/paritytech/polkadot-sdk/pull/6417
- Rewriting some of the flaky zombienet tests to zombienet-sdk: https://github.com/paritytech/polkadot-sdk/pull/6757

Polkadot-sdk reviews: https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aalindima

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity).   |There were no referendums available for my rank to vote on.  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

