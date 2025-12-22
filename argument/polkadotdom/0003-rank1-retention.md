# Argument-0003: Retention at Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/12/19                                                             |
| **Submitted by**| polka.dom                                                                        |


## Member details

- Matrix username: @polkadotdom:matrix.org
- Polkadot address: 1L66uQMKFnXKSZx9pCD5o56GvvP1i2Qns7CaS2AaKp9mnwc
- Current rank: 1
- Date of initial induction: [2025/05/06](https://collectives.statescan.io/#/extrinsics/6306997-2)
- Date of last report: [2025/09/25](https://github.com/polkadot-fellows/Evaluations/blob/d379fc31aee1ee53b3ca58f1bfa553940271b10a/evidence/polkadotdom/0002-rank1-retention.md)
- Area(s) of Expertise/Interest: FRAME, System Parachains


## Reporting period

- Start date: 2025/09/25
- End date: 2025/12/19

## Argument

### 'Hard Pressure' Issuance Model

This period I continued my work alongside Kian, Oliver, and Paolo to complete the new Hard Pressure issuance model enacted in [Ref 1710 - Hard Pressure Capped & Stepped Supply Schedule](https://polkadot.subsquare.io/referenda/1710). This involved addressing several security considerations that served to bolster the implementation. I am happy to report that by the time it was audited, SRLabs found no issues with the logic. Now merged, the new code is on its way to a runtime release.

This [new hard pressure system](https://github.com/polkadot-fellows/runtimes/pull/898) addresses community concerns around high inflation, and is of vital importance to our overall macro-economic strategy.

### RFC 150 - Voting While Delegating

Work has continued smoothly on [RFC-150](https://github.com/PolkadotDom/RFCs/blob/dom/voting-while-delegating/text/0150-voting-while-delegating.md), the OpenGov upgrade that would see voters retain their voting power while delegating. The RFC itself has been pushed to completion and has now been accepted by the fellows, marking a position of confidence in its necessity. Following that signal, I have completed the code itself, which is now [under review](https://github.com/paritytech/polkadot-sdk/pull/9026).

These mark the next steps in allowing for a more accurate plutocracy, the very backbone of Polkadot itself.

### Crowdsourced Decision Deposits

Following Basti's initial implementation, I completed the logic portion of our transition to crowdsourcable decision deposits. This involved guarding against several possible griefs that could wipe the current deposits or otherwise 'jab' at participants. I then passed the remaining work off to an eager candidate, runcomet.

With decision deposits increasing in accordance with [Ref 1701](https://polkadot.subsquare.io/referenda/1701), it will quickly become important to allow for multiple parties to back a referenda, lest smaller holders be pushed out of showcasing their voice.

### Community & Indirect work

During this period, I attended the annual Sub0 conference. While there I [presented](https://www.youtube.com/watch?v=yAYeV04-4sw) on how to best join the Technical Fellowship, and created and offered simple [material](https://docs.google.com/document/d/1Y8Q63hOgnNoeOfNG2IiwqdMB1tw56jm1OMAfJibDGMU/edit?usp=sharing) meant to help those along this path. Following the presentation, I joined Jay for an interview that I hope will spark some additional vigor within the community.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |No referenda to vote on  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
