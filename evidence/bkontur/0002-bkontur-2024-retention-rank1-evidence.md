# Evidence-0002: Retention at to Rank 1

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2024/11/29) |
| **Submitted by**| Branislav Kontur                |


## Member details

- Matrix username: @branislav_kontur:parity.io
- Polkadot address: 1HFq3DbX4tqanTLAx2CAToWnHXg6LRLMzSD4JzYCzCQpw5E
- Current rank: 1
- Date of initial induction: 2024/05/03
- Date of last report: 2024/08/16
- Area(s) of Expertise/Interest: `Bridges, XCM, System Parachains, benchmarking, testing, integration`


## Reporting period

- Start date: 2024/08/17
- End date: 2024/11/29


## Evidence

This summary outlines my primary activities, contributions, and collaborations during the reporting period, with my main focus on two key areas.

The first area was related to bridges and permissionless lanes. I completed the implementation of permissionless lane support for bridges, which resulted in two significant pull requests ([PR 4949](https://github.com/paritytech/polkadot-sdk/pull/4949) and [PR 5649](https://github.com/paritytech/polkadot-sdk/pull/5649)). As a continuation of this work, I authored a [design and deployment document](https://hackmd.io/3ei1CQhnTBKHBXF3yi2IIg) outlining how to deploy permissionless lanes as part of the broader Bridges vision - related discussions on the Polkadot Forum, such as [options for using the Polkadot-Kusama bridge](https://forum.polkadot.network/t/dotsama-parachains-options-for-using-polkadot-kusama-bridge/10873/3) and [exposing builder-facing bridging components on Asset Hub](https://forum.polkadot.network/t/expose-builder-facing-bridging-components-on-asset-hub). I am currently implementing support for deploying bridge messaging pallets on the different chain than the bridge finality pallets as tracked in [Issue 5827](https://github.com/paritytech/polkadot-sdk/issues/5827).

The second area was my involvement in the XCMv5 agenda. Although I did not directly add new features to XCMv5, I dedicated considerable time to reviewing nearly all new XCMv5-related pull requests. During this process, I contributed several improvements and fixes, such as those in [PR 6467](https://github.com/paritytech/polkadot-sdk/pull/6467), [PR 6092](https://github.com/paritytech/polkadot-sdk/pull/6092), [PR 6383](https://github.com/paritytech/polkadot-sdk/pull/6383), and [PR 6579](https://github.com/paritytech/polkadot-sdk/pull/6579). While reviewing these changes, I identified and resolved a bug in pallet-xcm related to data inconsistencies and missing migrations. I addressed this issue in [PR 6148](https://github.com/paritytech/polkadot-sdk/pull/6148) and created a related tracking [issue](https://github.com/polkadot-fellows/runtimes/issues/492) for the Polkadot Fellows.
After XCMv5 was initially deployed on Westend, I investigated and identified a problem with XCMv5-to-XCMv4 conversion, which is documented in [Issue 6585](https://github.com/paritytech/polkadot-sdk/issues/6585).
I also proposed several future improvements for [pallet-xcm](https://github.com/paritytech/polkadot-sdk/issues/6188) and [pallet-assets](https://github.com/paritytech/polkadot-sdk/issues/5969).   
A full list of my contributions to the Polkadot SDK repository is available [here](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3A%40me+is%3Aclosed+closed%3A%3E2024-08-17).

Regarding tooling, I requested a feature for Zombienet to [pass JSON as a parameter](https://github.com/paritytech/zombienet/pull/1902), which has been implemented.

Additionally, I worked on several smaller contributions for the Polkadot Fellows. These include tasks such as [updating weights for runtime version 1.3.0](https://github.com/polkadot-fellows/runtimes/pull/433), [fixing benchmarks for Encointer](https://github.com/encointer/runtimes/pull/1), improving bridges testing [[1]](https://github.com/polkadot-fellows/runtimes/pull/452), [[2]](https://github.com/polkadot-fellows/runtimes/pull/435), and addressing CI issues like [clippy compliance](https://github.com/polkadot-fellows/runtimes/pull/489). I also reviewed various pull requests and collaborated on updates to align with SDK stable2409, contributing to related tasks such as [PR 7](https://github.com/pandres95/runtimes/pull/7).

During this period, I participated in a [retreat](https://x.com/_snowbridge/status/1834569673045852412) with the Snowfork team, where we collaboratively designed Snowbridge V2.

Lastly, I provided support to several external contributors addressing issues in the Polkadot SDK repository. For instance, I helped with [Issue 6079](https://github.com/paritytech/polkadot-sdk/issues/6079#issuecomment-2422194407), [Issue 6101](https://github.com/paritytech/polkadot-sdk/issues/6101), and an issue reported by the Integritee Network parachain team ([Issue 302](https://github.com/integritee-network/parachain/issues/302#issuecomment-2422619497)).

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity).  | - |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

