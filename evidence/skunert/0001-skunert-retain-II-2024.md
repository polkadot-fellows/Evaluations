# Evidence-0001: Retention at Rank II

|                  |                  |
| ---------------- | ---------------- |
| **Report Date**  | 2024/05/03       |
| **Submitted by** | Sebastian Kunert |

## Member details

- Matrix username: `@sebastian:parity.io`
- Polkadot address: `1682A5hxfiS1Kn1jrUnMYv14T9EuEnsgnBbujGfYbeEbSK3w`
- Current rank: 2
- Date of initial induction: 2024/01/08
- Date of last report: N/A
- Area(s) of Expertise/Interest: `Cumulus Node`, `Substrate Node`

## Reporting period

- Start date: 2024/01/08
- End date: 2024/05/13

## Evidence

### Projects

Aside smaller contributions, I worked on the following projects:

- **PoV-Reclaim:**
  - **Description:** Allow parachains to make full use of their PoV-size by reclaiming storage weight that was overestimated due to worst-case benchmarking.
  - **PRs:** [Runtime Side](https://github.com/paritytech/polkadot-sdk/pull/3002), [Node Side](https://github.com/paritytech/polkadot-sdk/pull/1462), [Integration Guide](https://github.com/paritytech/polkadot-sdk/pull/4244)
  - **RFC:** [Introduce `storage_proof_size` host function](https://github.com/polkadot-fellows/RFCs/pull/43)
- **Pinning Improvements:**
  - **Description:** Revisited Substrate internal management of notification-based block pinning. Resolves issue where blocks were pinned too long.
  - **PRs:** [Introduce Notification Pinning Limit](https://github.com/paritytech/polkadot-sdk/pull/2935)
- **Parachain Authoring Overhaul:**
  - **Description:** Work in progress to prepare parachain nodes for upcoming elastic-scaling changes. This will make the parachain block authoring more flexible by introducing authoring on multiple cores and preparing future, more dynamic, authoring models.
  - **PRs:** [Refactor polkadot-parachain](https://github.com/paritytech/polkadot-sdk/pull/3511), [Prepare test infrastructure](https://github.com/paritytech/polkadot-sdk/pull/3568), [Introduce slot-based collator](https://github.com/paritytech/polkadot-sdk/pull/4097)

[Full PR List](https://github.com/paritytech/polkadot-sdk/pulls?q=+is%3Apr+author%3Askunert+)

### Talks

- Parachain Summit: PoV Reclaim & Elastic Scaling
