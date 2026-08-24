# Argument-0007: Retention at Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/06/23)                                                             |
| **Submitted by**| Adrian Catangiu                                                                        |


## Member details

- Matrix username: @adrian:parity.io
- Polkadot address: 121dd6J26VUnBZ8BqLGjANWkEAXSb9mWq1SB7LsS9QNTGFvz
- Current rank: III (Fellow)
- Date of initial induction: 2023/06/12
- Date of last report: 2025/12/09
- Area(s) of Expertise/Interest: System Chains, XCM, Trustless Bridges, BEEFY


## Reporting period

- Start date: 2026/01/01
- End date: 2026/06/30


## Argument

During this reporting period I have widened my focus and contributed in the design and delivery of new Polkadot system components such as Levity (Bulletin Chain), Celerity (Small Statement Store). I have also continued supporting XCM, Snowbridge and P<>K Bridge, as well as being an active reviewer for most big changes going in the Polkadot System Chains runtimes.

I authored a big change under the hood of XCM to properly handle imbalances across the stack during the execution of XCM programs. This was necessary to close the door on a whole class of security issues where total issuance invariants could be broken through clever use of XCM programs. I started this work December last year, but [finished and merged it March of this year](https://github.com/paritytech/polkadot-sdk/pull/10384). I also [helped integrating it to live chains](https://github.com/polkadot-fellows/runtimes/pull/1114) (April).

This year I also finished the [integration of support for non-teleportable Foreign Assets](https://github.com/polkadot-fellows/runtimes/pull/1085) in Polkadot Hub. This widens the support of assets on the Hub, making it more flexible to how foreign assets are managed by their creators and owners. This capability will, for example, allow Hydration to register Hollar on the Hub, while still maintaining the unique reserve and source of truth on their chain.

A smaller, but also important piece of work, was adding [support for Polkadot Technical Fellowship to operate on Kusama](https://github.com/polkadot-fellows/runtimes/pull/1100) over the P<>K bridge. For example, the latest Kusama upgrade was [whitelisted](https://collectives.subsquare.io/fellowship/referenda/544) through the better maintained Polkadot Fellowship (I also [added support to Fellowship tooling](https://github.com/joepetrowski/opengov-cli/pull/55) to make this easy).

I have also regularly run maintenance efforts on the Polkadot System Chains runtimes, for example [integrating many tests](https://github.com/polkadot-fellows/runtimes/pull/1105) that were missed during original integration of new features.

I am currently expanding my knowledge of Polkadot core protocols to also cover parts of staking, and I have been active in the design and implementation review of the new staking system and the introduction of the _Dynamic Allocation Pool_. Notable public examples of active involvement: [here](https://github.com/paritytech/polkadot-sdk/pull/11434) and [here](https://github.com/paritytech/polkadot-sdk/pull/11763).

Consistent reviewer for both [Fellowship runtimes](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr++reviewed-by%3Aacatangiu+created%3A2026-01-01..2026-06-30+) and [Polkadot-SDK](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr++reviewed-by%3Aacatangiu+created%3A2026-01-01..2026-06-30+).

As described in the beginning of this argument, as of late I have moved away from individual contributions and more into the design and coordination of new components. Two of these components have already landed on Polkadot (although most other components making use of them haven't done so yet): [Levity (Bulletin chain)](https://github.com/polkadot-fellows/runtimes/pull/1120) and [Celerity (SSS)](https://github.com/paritytech/polkadot-sdk/tree/master/substrate/client/statement-store).

At the 2026 Web3 Summit, I've presented the components under the hood of the upcoming Polkadot Developer Platform, and how they empower easy building and hosting of decentralized, private and human-centric Web3 products.

## Voting record

Based on [my membership page](https://collectives.subsquare.io/user/121dd6J26VUnBZ8BqLGjANWkEAXSb9mWq1SB7LsS9QNTGFvz/fellowship) on Subsquare Polkadot Fellowship dashboard, my participation rate in the last 6 months: `Participation Rate 88.16% Win Rate 100.00%`.

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  | 88.16% |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

