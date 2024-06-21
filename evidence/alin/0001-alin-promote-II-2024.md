# Evidence-0001: Promotion to Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/06/21)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: I
- Date of initial induction: 2024-04-26
- Date of last report: N/A
- Area(s) of Expertise/Interest: Parachains consensus


## Reporting period

- Start date: 2024/04/26
- End date: 2024/07/25


## Evidence for the reporting period

|  Areas of Contribution | Tasks  | Links   |Notes   |
|---|---|---|---|
|Polkadot   | Rewrite prospective-parachains subsystem for full elastic scaling throughput. Also refactor it with some simplifying assumptions in mind.   | [PR](https://github.com/paritytech/polkadot-sdk/pull/4035)  | Also conducted the neccessary testing on the Versi private testnet  |
|Cumulus   |  Remove prospective-parachains subsystem from collators, for improved performance | [PR](https://github.com/paritytech/polkadot-sdk/pull/4471)  |   |
|Cumulus    | pov-recovery: add elastic scaling support and comprehensive unit tests    |  [PR](https://github.com/paritytech/polkadot-sdk/pull/4733)  |  pov-recovery was previously lacking unit tests altogether |
|Polkadot   | Root-causing and fixing problems with core-sharing parachains and parachains producing blocks ahead of schedule  | Co-authored [PR](https://github.com/paritytech/polkadot-sdk/pull/4724)  |   |
|Documentation   | Elastic scaling MVP guide for parachains  | [PR](https://github.com/paritytech/polkadot-sdk/pull/4663)  | Not merged yet  |

Other contributions

- A couple of other smaller PRs: https://github.com/paritytech/polkadot-sdk/pull/3778 & https://github.com/paritytech/polkadot-sdk/pull/3874
- running elastic scaling tests on Versi private testnet
- Polkadot SDK reviews: https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aalindima

## Other evidence

Document for initial induction to rank I: https://hackmd.io/@k-1PToxXTnuLArMnC4ivmA/B1EsZduCp

Considering this is a proposal for promotion to rank II, I believe several work items from my initial
induction doc (for rank I) are supportive of rank II, especially:
- systematic availability recovery: [RFC#47](https://github.com/polkadot-fellows/RFCs/pull/47) and [PR](https://github.com/paritytech/polkadot-sdk/pull/1644)
- elastic scaling PRs: [runtime support](https://github.com/paritytech/polkadot-sdk/pull/3479) and others: [#3233](https://github.com/paritytech/polkadot-sdk/pull/3233), [#3160](https://github.com/paritytech/polkadot-sdk/pull/3160)
