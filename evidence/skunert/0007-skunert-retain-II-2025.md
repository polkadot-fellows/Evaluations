# Argument-0007: Retention at Rank II

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2025/07/22 |
| **Submitted by** | skunert    |

## Member details

- Matrix username: `@sebastian:parity.io`
- Polkadot address: `1682A5hxfiS1Kn1jrUnMYv14T9EuEnsgnBbujGfYbeEbSK3w`
- Current rank: 2
- Date of initial induction: 2024/01/08
- Date of last report: 2025/04/22
- Area(s) of Expertise/Interest: `Cumulus Node`, `Substrate Node`, `Parachain Authoring`, `Weight`

## Reporting period

- Start date: 2025/04/30
- End date: 2025/07/30

## Argument

During this reporting period, I worked primarily on finalizing parachain fork management. The work started before this reporting period, but the last bulk of the work happened in the first half of this one. I focused on improving abstractions, introducing additional documentation, and testing. The goal of the work is to give parachains a handle to configure their forkiness, with a trade-off on XCM latency. Parachain teams can configure their runtime to require the passing of relay parent descendants. This makes it impossible to author at the tip of the relay chain. Instead, they author with an offset, at which we expect forks to be resolved already. However, since authoring happens behind the tip, XCM messages also arrive with a delay of `relay_parent_offset * relay_chain_slot_duration` seconds ([issue](https://github.com/paritytech/polkadot-sdk/issues/7780), [PR](https://github.com/paritytech/polkadot-sdk/pull/8299)).

Other than that, I came back to exposing an `on_genesis` hook in the `Hooks` trait of frame. During integration of new features into polkadot-sdk, there is often a need to write integration tests with zombienet. These tests are a special scenario in that both the relay chain and the parachains start from genesis. Our relay chain runtimes currently have the limitation that parachain runtimes are only onboarded after one session. This means that:
- Developers have to wait for one session on their local machine to see blocks produced
- CI on various repositories idles for one session, waiting for blocks to be produced
- Flexibility in configured session length is low, since waiting time would increase even more with long sessions

The newly exposed `on_genesis` hook allows running initialization code on genesis, but after the individual pallets have fully initialized their storage. Before, uninitialized pallet storage was causing this waiting time. The changes are working, but integration with various pallets mocks needs to be finished ([PR](https://github.com/paritytech/polkadot-sdk/pull/7948)).

Beyond the code contributions, a lot of my time goes into code reviews, discussions, and guidance on `polkadot-sdk` and the `runtimes` repository:
- Runtime PRs (2): [list](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr++reviewed-by%3Askunert+created%3A2025-04-30..2025-07-30+)
- polkadot-sdk PRs (46): [list](https://github.com/paritytech/polkadot-sdk/pulls?q=is:pr+reviewed-by:skunert+created:2025-04-30..2025-07-30+)

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments                      |
| ----- | ------------------- | -------------------- | -------------------------- | ----------------------------- |
| III   | 70%                 | N/A                  |                            |                               |
| I     | 90%                 | N/A                  |                            | There was nothing to vote on. |
| II    | 80%                 | N/A                  |                            | There was nothing to vote on. |
| III   | 70%                 | N/A                  |                            |                               |
| IV    | 60%                 | N/A                  |                            |                               |
| V     | 50%                 | N/A                  |                            |                               |
| VI    | 40%                 | N/A                  |                            |                               |