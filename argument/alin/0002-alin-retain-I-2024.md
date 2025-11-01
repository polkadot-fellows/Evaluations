# Evidence-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/10/01)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: I
- Date of initial induction: 2024-04-26
- Date of last report: 2024/06/21
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling


## Reporting period

- Start date: 2024/06/22
- End date: 2024/10/01


## Evidence

My contributions in these past months have been mostly centered around Elastic Scaling, along with other general endeavours
with bugfixing and refactoring across different components.

### Elastic Scaling and Coretime

I have identified a bug in the relay parent progression check done in the runtime and fixed it: https://github.com/paritytech/polkadot-sdk/pull/5113.
I made sure to perform the required backports of the PR to the fellowship repo so that the issue does not ever surface on production networks.

I identified the root-cause of [this issue](https://github.com/paritytech/polkadot-sdk/issues/4800#issuecomment-2182882971), which impacted
the backing rewards of validators for fork-producing parachains. The fix for this was a major redesign of the prospective-parachain subsystem,
which I successfully implemented and tested on private testnets: https://github.com/paritytech/polkadot-sdk/pull/4937. I believe the complexity
and impact of this change, together with the demonstrated autonomy is supportive of my eventual promotion to the IInd rank
(which is not yet possible due to the artificial 1-year waiting time between ranks).

I implemented the cumulus parts of [RFC103](https://github.com/polkadot-fellows/RFCs/pull/103), which enables having an untrusted collator
set when using elastic scaling:
- https://github.com/paritytech/polkadot-sdk/pull/5372
- https://github.com/paritytech/polkadot-sdk/pull/5888

I worked on removing the scheduling TTL from the relay chain runtime, which was preventing proper core-sharing between paras: https://github.com/paritytech/polkadot-sdk/pull/5461.
Doing this, I also refactored the runtime code and discovered an avenue for further improving the design of the scheduler module: https://github.com/paritytech/polkadot-sdk/issues/5529.

I opened the referendums for bumping `AsyncBackingParams.max_candidate_depth` to 6 (enabling the use of the elastic scaling MVP):
- https://kusama.subsquare.io/referenda/455
- https://kusama.subsquare.io/fellowship/referenda/87


### Root-causing and fixing other network issues

- Root-caused and reproduced relay chain node panic: https://github.com/paritytech/polkadot-sdk/issues/5421#issuecomment-2301509454
- Root-caused and fixed node memory leak: https://github.com/paritytech/polkadot-sdk/pull/5321

### Other contributions:
Polkadot-sdk reviews: https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aalindima

RFCs reviewed: https://github.com/polkadot-fellows/RFCs/pulls?q=is%3Apr+reviewed-by%3Aalindima+

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 1 referenda in which I was eligible to vote (i.e 0 % voting activity).   |I will make sure to pay closer attention to referendums that I am allowed to vote on.  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

