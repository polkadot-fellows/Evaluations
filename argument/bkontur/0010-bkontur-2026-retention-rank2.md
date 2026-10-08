# Argument-0010: Retention at Rank II

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2026/09/24) |
| **Submitted by**| Branislav Kontur                |


## Member details

- Matrix username: @branislav_kontur:parity.io
- Polkadot address: 1HFq3DbX4tqanTLAx2CAToWnHXg6LRLMzSD4JzYCzCQpw5E
- Current rank: 2
- Date of initial induction: 2024/05/03
- Date of last report: 2026/06/23
- Link to last report: [Argument-0009 (PR #313)](https://github.com/polkadot-fellows/Evaluations/pull/313) ([referendum 563](https://collectives.subsquare.io/fellowship/referenda/563))
- Area(s) of Expertise/Interest: `Levity (Bulletin), Capacity (Web3 Storage), Bridges, XCM, System Parachains, governance, benchmarking, testing, integration, IPFS, Bitswap`


## Reporting period

- Start date: 2026/06/23
- End date: 2026/09/24

## Argument

This summary outlines my work during the reporting period (July–September 2026). The two main things are that **Levity Polkadot went live on Polkadot**, and that **Capacity** grew from a demo into a real implementation project that I help drive. I was on holiday for most of August.

### Levity (a.k.a Bulletin) Polkadot — live on Polkadot

Levity is now a working storage chain on Polkadot, not a prototype any more. Following the staged plan I prepared for onboarding it into the Fellows runtimes [[1]](https://github.com/polkadot-fellows/runtimes/issues/1119), we brought the Levity storage and HOP business into the runtime — pallets, runtime APIs and configuration [[2]](https://github.com/polkadot-fellows/runtimes/pull/1170) — thanks to the Levity team (Karol ([@karolk91](https://github.com/karolk91)), Cisco ([@franciscoaguirre](https://github.com/franciscoaguirre)), Rohit ([@rosarp](https://github.com/rosarp)), Anthony ([@antkve](https://github.com/antkve)), Andrii ([@dr333ws](https://github.com/dr333ws)), Rafal ([@RafalMirowski1](https://github.com/RafalMirowski1)), Naren ([@mudigal](https://github.com/mudigal))). It shipped in Fellows runtimes v2.4.0 [[3]](https://github.com/polkadot-fellows/runtimes/releases/tag/v2.4.0) and was enacted on Polkadot by fellowship referendum 603 [[4]](https://collectives.subsquare.io/fellowship/referenda/603), with Karol helping on the governance side with the referenda, and covering the discussions and setup with the Levity collators. Levity is part of the Products Platform infrastructure, for example for hosting SPAs for the DotNS machinery.

My own focus was mostly on coordinating the work behind it — preparing the plan, testing, creating issues [[5]](https://github.com/paritytech/polkadot-bulletin-chain/issues?q=is%3Aissue+author%3Abkontur+created%3A2026-06-23..2026-09-24) and doing reviews — and on the work around the runtime change rather than the change itself: setting up the release and the rest of the preparation [[6]](https://github.com/paritytech/polkadot-bulletin-chain/issues/718). The chain is live and ready, now waiting for the products to use it.

### Capacity (a.k.a Web3 Storage)

Capacity is the staked-provider storage system designed by Robert Klotzner ([@eskimor](https://github.com/eskimor)), where the chain is a credible threat instead of the hot path. I am one of the people pushing it forward [[7]](https://github.com/paritytech/web3-storage).

As with Levity, most of my time goes into moving the work forward rather than only writing code: keeping the design document and the code in sync [[8]](https://github.com/paritytech/web3-storage/pull/376), taking the resulting decisions back into the document [[9]](https://github.com/paritytech/web3-storage/pull/423), reporting the bugs I find on the way [[10]](https://github.com/paritytech/web3-storage/issues?q=is%3Aissue+author%3Abkontur+created%3A2026-06-23..2026-09-24), and doing my share of the implementation and the reviews [[11]](https://github.com/paritytech/web3-storage/pulls?q=is%3Apr+author%3Abkontur+created%3A2026-06-23..2026-09-24). Next to that I am doing research and investigation on what is needed to bring Capacity live and make it usable for the Products platform.

### Bridges

Together with Rohit ([@rosarp](https://github.com/rosarp)) I am the maintainer of the Polkadot<>Kusama bridge stack. It is in maintenance mode, but we recently improved the internal testing with zombienet-sdk [[12]](https://github.com/paritytech/parity-bridges-common/pulls?q=is%3Apr+zombienet+created%3A2026-06-23..2026-09-24), and those tests cover both our Polkadot SDK testnet runtimes and the latest Fellowship runtimes for the BridgeHubs and AssetHubs [[13]](https://github.com/paritytech/parity-bridges-common/pull/3299) [[14]](https://github.com/paritytech/parity-bridges-common/pull/3293) [[15]](https://github.com/paritytech/parity-bridges-common/pull/3276).

Looking ahead, I created issues about what JAM means for the bridges and for the parachain service [[16]](https://github.com/paritytech/polkadot-sdk/issues/12867) [[17]](https://github.com/paritytech/polkadot-sdk/issues/12734). We are also prototyping the use of a smoldot light client for the bridge relayers, where I identified the missing pieces around GRANDPA justifications [[18]](https://github.com/paritytech/parity-bridges-common/pull/3270) [[19]](https://github.com/paritytech/smoldot/issues/3288), and Rohit added a smoldot side-car for the zombienet tests [[20]](https://github.com/paritytech/parity-bridges-common/pull/3320).

### Reviews and helping others

I am a regular reviewer in the Levity [[21]](https://github.com/paritytech/polkadot-bulletin-chain/pulls?q=is%3Apr+reviewed-by%3Abkontur+updated%3A2026-06-23..2026-09-24), Polkadot SDK [[22]](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Abkontur+updated%3A2026-06-23..2026-09-24) and Fellows [[23]](https://github.com/search?q=org%3Apolkadot-fellows+is%3Apr+reviewed-by%3Abkontur+updated%3A2026-06-23..2026-09-24&type=pullrequests) repositories. I stayed the technical contact for Levity and Capacity across teams.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity).  | There were no referenda I could vote on during the reporting period. |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
