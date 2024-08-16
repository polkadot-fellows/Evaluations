# Evidence-0001: Retention at Rank 1

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2024/08/16) |
| **Submitted by**| Branislav Kontur                |


## Member details

- Matrix username: @branislav_kontur:parity.io
- Polkadot address: 1HFq3DbX4tqanTLAx2CAToWnHXg6LRLMzSD4JzYCzCQpw5E
- Current rank: 1
- Date of initial induction: 2024/05/03
- Date of last report: N/A
- Area(s) of Expertise/Interest: `Bridges, XCM, System Parachains, benchmarking, testing, integration`


## Reporting period

- Start date: 2024/05/03
- End date: 2024/08/16


## Evidence

I am confident that I am a valuable member of the Fellowship, contributing to the continued operation and improvement of the Polkadot (Main) Network. To support this claim, please review the evidence below.

Over the past few months, my primary focus has been on the Bridges "permissionless lanes" for substrate-to-substrate bridging, a topic I have taken on (migrating it from the old bridges repository and updating it with the latest polkadot-sdk). I had to design and solve several crucial aspects, such as [backward compatibility for the relayer and support for new XCM version transitions](https://github.com/paritytech/parity-bridges-common/issues/2500#issuecomment-2260287166) since polkadot-fellows runtimes are enacted/upgraded asynchronously. Another interesting challenge was solving the migration for the hard-coded lane between the Polkadot and Kusama Asset Hubs.
For more details, you can check out this [pull request](https://github.com/paritytech/polkadot-sdk/pull/4949).

I also addressed a requested [issue](https://github.com/paritytech/polkadot-sdk/issues/4298) to add a new runtime API for LocationToAccount conversions and saw it through to completion ([deployed](https://github.com/polkadot-fellows/runtimes/pull/413) across all polkadot-fellows runtimes and in [PJS](https://github.com/polkadot-js/api/pull/5917)).

Since the polkadot-fellows release [1.2.0](https://github.com/polkadot-fellows/runtimes/issues/140), which I essentially managed, I "accidentally" became known as the "guy who can regenerate fresh weights," assisting with several PRs: [[1]](https://github.com/joepetrowski/runtimes/pull/2), [[2]](https://github.com/polkadot-fellows/runtimes/pull/343), [[3]](https://github.com/polkadot-fellows/runtimes/pull/433), [[4]](https://github.com/Snowfork/runtimes/pull/13). In many cases, I also had to fix other issues along the way.
Since the beginning of the polkadot-fellows repo, a CI pipeline for checking benchmark validity was missing (my [issue](https://github.com/polkadot-fellows/runtimes/issues/197)), so I finally managed to release the missing pieces (frame-omni-bencher) and build a [CI pipeline](https://github.com/polkadot-fellows/runtimes/pull/379).
I also contributed to designing the new bench bot [here](https://github.com/paritytech/product-engineering/issues/41#issuecomment-2149190196) for an [issue](https://github.com/polkadot-fellows/runtimes/issues/128).
Benchmarks are a important part of runtimes, so this helps ensure more stable and higher-quality pull requests.

Additionally, I assisted with various polkadot-sdk bumps for polkadot-fellows, such as: [[1]](https://github.com/polkadot-fellows/runtimes/pull/327), [[2]](https://github.com/polkadot-fellows/runtimes/pull/353), [[3]](https://github.com/polkadot-fellows/runtimes/pull/352), [[4]](https://github.com/polkadot-fellows/runtimes/pull/360).
I’m not only focused on my own tasks but also try to contribute whenever I find anything that can be improved. For example, I discovered an [issue](https://github.com/polkadot-fellows/runtimes/issues/396) with the CI and drove it to completion with this [PR](https://github.com/polkadot-fellows/runtimes/pull/397).

You can see all my contributions to the polkadot-sdk repo [here](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3A%40me+is%3Aclosed+closed%3A%3E2024-05-03) and for polkadot-fellows [here](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3A%40me+is%3Aclosed+closed%3A%3E2024-05-03).

Yes, I know that I am not very publicly active (e.g., on forums or social media) except for my first [blog post](https://forum.polkadot.network/t/polkadot-kusama-bridge/2971/59). However, I am active and assist other users with issues in Parity's internal Element as well as in the polkadot-sdk and polkadot-fellows repositories. For example, I have contributed to addressing the [[1 - HRMP problem]](https://github.com/paritytech/polkadot-sdk/issues/4705), the [[2 - CheckMetadataHash problem]](https://github.com/paritytech/polkadot-sdk/issues/4770), and the [[3 - XCM Barrier problem]](https://github.com/paritytech/polkadot-sdk/issues/4868).

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                           | Comments                                            |
|---|---|---|----------------------------------------------------------------------|-----------------------------------------------------|
|III|70%   |100%  |                                                                      |                                                     |
|I  |90%   |N/A   | I did not vote in two referenda where I was eligible to vote.   | I will try to increase my involvement in governance. |
|II |80%   |N/A   |                                                                      |                                                     |
|III|70%   |100%  |                                                                      |                                                     |
|IV |60%   |90%   |                                                                      |                                                     |
|V  |50%   |80%   |                                                                      |                                                     |
|VI |40%   |70%   |                                                                      |                                                     |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
