# Argument-0002: Retention at Rank II

|                  |              |
| ---------------- | ------------ |
| **Report Date**  | 2026/09/25   |
| **Submitted by** | Victor Oliva |

## Member details

- Matrix username: @voliva:matrix.org
- Polkadot address: 16JGzEsi8gcySKjpmxHVrkLTHdFHodRepEz8n244gNZpr9J
- Current rank: Rank 2 (Proficient)
- Date of initial induction: 2026/06/09
- Date of last report: 2026/06/09
- Area(s) of Expertise/Interest:

  - Developer tooling
  - Runtime and node API ergonomics
  - FRAME pallet UX

## Reporting period

- Start date: 2026/06/09
- End date: 2026/09/25

## Argument

I am applying for retention at **Rank II: Proficient Member**. During this period, I continued work in the two areas: a direct contribution to `pallet-referenda` in Polkadot SDK, and Forklift, a local forking tool.

### Polkadot SDK: `pallet-referenda`

I continued preparing [polkadot-sdk#11524](https://github.com/paritytech/polkadot-sdk/pull/11524), **[referenda] Add `slash_submission_deposit` extrinsic**, which is now ready for merging.

This has kept me engaged with FRAME extrinsic design, API compatibility, weights, and the review process for a production SDK change.

### Forklift

I continued leading development of [Forklift](https://github.com/polkadot-api/forklift), a local fork-aware testing tool for Polkadot applications and tooling. I merged seven PRs during this period:

- [#1](https://github.com/polkadot-api/forklift/pull/1), [#2](https://github.com/polkadot-api/forklift/pull/2), and [#3](https://github.com/polkadot-api/forklift/pull/3) improved correctness of runtime calls and block creation. This includes supporting mock signature host to all runtime calls, changes on best block handling, and preventing invalid block/finalization states when creating or skipping blocks.
- [#4](https://github.com/polkadot-api/forklift/pull/4) and [#9](https://github.com/polkadot-api/forklift/pull/9) fixes a few issues found while adding new test scenarios in PAPI: `dev_` RPC errors are propagated, `chainHead_v1_follow` state is cleaned up on disconnect, and operations are cleaned up before emitting completion events.
- [#10](https://github.com/polkadot-api/forklift/pull/10) fixed a crash triggered by Hydration HRMP messages, added configurable logging, and optimised block production by pre-loading the next block.
- [#11](https://github.com/polkadot-api/forklift/pull/11) based on external feedback, adds CORS preflight checks so that it can be used from a browser..

Forklift is deliberately focused on cases that are difficult to reproduce with a single linear chain: competing heads, finalization changes, `chainHead` subscriptions, queued messages, and RPC operation lifecycles.

Together, this work demonstrates continued, hands-on contribution to Polkadot SDK and the reliability of ecosystem developer tooling. I therefore request retention at Rank II.

### References

- [polkadot-sdk#11524 — `slash_submission_deposit`](https://github.com/paritytech/polkadot-sdk/pull/11524)
- [Forklift merged pull requests](https://github.com/polkadot-api/forklift/pulls?q=is%3Apr+state%3Aclosed)

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments              |
| ----- | ------------------- | -------------------- | -------------------------- | --------------------- |
| I     | 90%                 | N/A                  | N/A                        | No eligible referenda |
| II    | 80%                 | N/A                  | 0 of 0 (100%)              | No eligible referenda |
| III   | 70%                 | 100%                 |                            | N/A                   |
| IV    | 60%                 | 90%                  |                            | N/A                   |
| V     | 50%                 | 80%                  |                            | N/A                   |
| VI    | 40%                 | 70%                  |                            | N/A                   |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
