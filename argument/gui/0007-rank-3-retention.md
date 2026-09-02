# Argument-0007: Retention at Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/08/28                                                                                  |
| **Submitted by**| Guillaume Thiolliere                                                                        |


## Member details

- Matrix username: @guillaume:parity.io
- Polkadot address: 13psJuWEjBuZGaFqXvFnLMC6ME8RVVfQAhtFhydYjW45oKgZ
- Current rank: III
- Date of initial induction: 2025/01/09
- Date of last report: 2026/02/03
- Link to last report: https://github.com/polkadot-fellows/Evaluations/pull/254
- Area(s) of Expertise/Interest:
  - polkadot business-logic (aka the 'runtime')
  - the internals of the frame pallet framework
  - runtime and host APIs


## Reporting period

- Start date: 2026/02/03
- End date: 2026/08/28


## Argument

During this period my main focus was on Individuality-SDK, which comprises the Coinage system and
the various pallets related to People and Lite-People: their recognition mechanism, and the
utilities and resources provided to them. The historical contributions to Individuality-SDK were
made in a private repository, but it is now entirely open source in
[individuality-community](https://github.com/paritytech/individuality-community).
I contributed to the development, the reviews and part of the specifications of many of its
components. Part of the work in Individuality-SDK is now being integrated into the fellowship
runtimes ([runtimes#1233](https://github.com/polkadot-fellows/runtimes/pull/1233)), and the rest may
be integrated in the future.

In parallel I made some contributions to Polkadot-SDK. I merged the support for multiple
versions of transaction extensions
([polkadot-sdk#7035](https://github.com/paritytech/polkadot-sdk/pull/7035)). This key piece allows
us to ship Individuality-SDK without breaking current signers, by only introducing a new version of
the transaction extension pipeline.
I am also currently designing the block-level batch proof validation scheme for Bandersnatch Ring
VRF proofs. Validating proofs in batch is faster, and ideally we would like to only verify a batch
of proofs in the PoV, but Polkadot-SDK lacks the primitives to be able to declare such logic.
I proposed a safe design that enables it, by introducing a flag to distinguish transaction
validation from transaction execution as part of the block
([polkadot-sdk#12651](https://github.com/paritytech/polkadot-sdk/pull/12651)).

I also made smaller contributions to the Polkadot People Chain: using the full 2s block time now
available since it has been moved to elastic scaling
([runtimes#1232](https://github.com/polkadot-fellows/runtimes/pull/1232)), generalizing fee
payment to accept more assets, and configuring XCM to accept more reserve assets.
([runtimes#1257](https://github.com/polkadot-fellows/runtimes/pull/1257),
[runtimes#1260](https://github.com/polkadot-fellows/runtimes/pull/1260), under review).

Other PRs and reviews:
* [PRs authored](https://github.com/search?q=author%3Agui1117+is%3Apr+repo%3Aparitytech%2Fpolkadot-sdk+repo%3Apolkadot-fellows%2Fruntimes+repo%3Aparitytech%2Findividuality-community+created%3A%3E2026-02-03&type=pullrequests),
* [PRs reviewed](https://github.com/search?q=reviewed-by%3Agui1117+-author%3Agui1117+is%3Apr+repo%3Aparitytech%2Fpolkadot-sdk+repo%3Apolkadot-fellows%2Fruntimes+repo%3Aparitytech%2Findividuality-community+updated%3A%3E2026-02-03&type=pullrequests).

## Voting record
|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  | 55% activity (30/55), 100% agreement (29/29) | I acknowledge this is not good. This is my first period at Rank III, and I will make sure to vote more actively going forward. |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
