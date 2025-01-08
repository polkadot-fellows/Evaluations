# Evidence-0002: Retention at Rank 1

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2024/10/15) |
| **Submitted by**| Christian Langenbacher           |


## Member details

- Matrix username: `@clang:matrix.org`
- Polkadot address: `16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3`
- Current rank: `1`
- Date of initial induction: `2024/03/27`
- Date of last report: `2024/10/15`
- Area(s) of Expertise/Interest: `Parachain Builder, Runtime, Clients`


## Reporting period

- Start date: 2024/10/15
- End date: 2025/01/08


## Evidence
My sole code contribution this time, was identifying, reproducing, and fixing a bug in the polkadot-sdk, which resulted in a build error under some circumstances due to an unhygenic widely-used macro, namely the `format_runtime_string!` macro, see the fix in [PR #5632](https://github.com/paritytech/polkadot-sdk/pull/5632). This bug has indeed affected some parachain teams, and was backported into both `stable2407` and `stable2409`.

I don't have any other hard evidence, but naturally, I have continued staying active in the ecosystem mostly as parachain a builder in Encointer, Integritee and Ajuna.



## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|----------------------|----------------------------|---|
|I  |90%   | N/A                  | No elligible referenda     |  |
|II |80%   | N/A                  |                            |  |
|III|70%   | 100%                 |                            |  |
|IV |60%   | 90%                  |                            |  |
|V  |50%   | 80%                  |                            |  |
|VI |40%   | 70%                  |                            |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s):

### General Activity in reporting period
* [Authored 8 PRs in the polkadot-sdk](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aclangenb+created%3A2024-10-15..2025-01-08+). Two of those PRs were closed, but this is because the umbrella issue was a bit chaotic and another PR for the same subtask was done **after** my PR had been opened. Unfortunately (for me), the other PRs have been merged first, see [comment](https://github.com/paritytech/polkadot-sdk/issues/6202#issuecomment-2506383064).
* [Involvement in 6 Fellowship issues](https://github.com/polkadot-fellows/runtimes/issues?q=is%3Aissue+involves%3Aclangenb+updated%3A2024-10-15..2025-01-08+).
* [Involvement in 6 Polakdot-sdk issues](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue+involves%3Aclangenb+updated%3A2024-10-15..2025-01-08+)
