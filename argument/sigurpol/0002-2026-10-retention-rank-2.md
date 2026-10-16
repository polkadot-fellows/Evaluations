# Argument-0002: Retention at Rank II

|                  |                         |
| ---------------- | ----------------------- |
| **Report Date**  | 2026/10/16              |
| **Submitted by** | Paolo La Camera         |
| **Sponsored by** | Kian Paimani (Staking)  |


## Member details

- Matrix username: @paolo:parity.io
- Polkadot address: 15JDUd4QXoArDgwzkAFhSnFvV8LSwAXE7t1A5gpaGoEc5qDE
- Current rank: II
- Date of initial induction: 2026/01/26
- Date of last report: 2026/07/30
- Link to last report: [Argument-0001: Fast Promotion to Rank II](0001-2026-07-promotion-rank-2.md), approved by [referendum 592](https://collectives.subsquare.io/fellowship/referenda/592) on 2026/08/30
- [Subsystems](../../subsystems.md) developed/maintained: Staking (Delegate, Rank 2)
- Salary status: **Non-salaried**. I work full-time at Parity, so per the [Accountability](../../README.md#accountability) rules I have not drawn and will not draw a Fellowship salary. I have never registered for a salary cycle.


## Reporting period

- Start date: 2026/07/30
- End date: 2026/10/16


## Argument

I am asking to be retained at Rank II. I am still the lead developer for staking on Polkadot. Since my last report most of my time went into letting validators collate on system chains, for the upcoming metanode release. Next to that I kept working on the DAP integration, added new OpenGov tracks for the upcoming App integrations, and designed two upcoming features, operational payments to validators in dotUSD and vested self-stake incentives.

### 1. Validators collating on system chains

With the next metanode release, a configurable number of validators in the active set will also collate on system chains, starting from Asset Hub and People, alongside the invulnerables and bonded candidates we have today.

I am responsible for the runtime changes that let collators be selected from the validator set and be paid for that. Asset Hub staking announces each era's validator set to the system chains, and every validator that registered session keys there becomes a collator within a few blocks of the era starting ([#13332](https://github.com/paritytech/polkadot-sdk/pull/13332), merged). Validators register their keys there against a deposit ([runtimes#1310](https://github.com/polkadot-fellows/runtimes/pull/1310), [#13337](https://github.com/paritytech/polkadot-sdk/pull/13337)). Governance sets a cap on how many validators collate, the collators are drawn at random every era using relay chain randomness, and the cap can be raised or lowered over time ([#13420](https://github.com/paritytech/polkadot-sdk/pull/13420), merged).

Two more pieces are in review. One rewards validators for this work, as blocks they author on system chains earn era points with a weight per chain set by governance ([#13464](https://github.com/paritytech/polkadot-sdk/pull/13464)). The other one protects liveness: a validator that registers keys but doesn't run a collator leaves its slots empty, so after a configurable number of missed turns it gets dropped, and it comes back on its own later ([#13483](https://github.com/paritytech/polkadot-sdk/pull/13483)).

### 2. Designing what staking does next

As lead developer in staking, I have designed what we are building next.

- **Operational payments in dotUSD.** The DAP was built to fund network costs, and the next step is to pay validators in stablecoin to cover operational costs. I wrote the initial design and it's in development, starting with the DAP distributing arbitrary assets ([#13305](https://github.com/paritytech/polkadot-sdk/pull/13305)).
- **Vested self-stake incentives.** Today the validator self-stake incentive is paid in liquid DOT. I wrote the initial design to pay it through vesting schedules instead, and it is now in development ([#12210](https://github.com/paritytech/polkadot-sdk/pull/12210)).
- **Research on a smaller active set.** I modelled what happens to liveness, staking rewards and security if we reduce the active validator set, which is linked to cost reduction, boostrap of dotUSD and deployment of metanodes. To back it up staking-wise, I also ran election predictions with the staking miner at different size of validators against a live election, using self-stake overrides I added to `predict` for this ([staking-miner#1303](https://github.com/paritytech/polkadot-staking-miner/pull/1303)).
- I am fully engaged in modelling and discussing future of staking vs Individuality and stablecoin integration, more to come in due time in the forum and public channels.

### 3. Keeping DAP and elections correct in production

DAP is live on Polkadot, and most of the follow-up work is making sure every flow ends up there. Coretime revenue now goes to the DAP on Polkadot ([runtimes#1282](https://github.com/polkadot-fellows/runtimes/pull/1282)), and genesis presets fund its buffer correctly ([runtimes#1286](https://github.com/polkadot-fellows/runtimes/pull/1286)). I also fixed issues that came up after the rollout, like signed-phase reward payouts failing silently ([#13166](https://github.com/paritytech/polkadot-sdk/pull/13166)) and a treasury payout XCM aimed at the wrong pallet ([#13268](https://github.com/paritytech/polkadot-sdk/pull/13268)).

On elections I bounded the fee refund paid to the winning solution ([#12877](https://github.com/paritytech/polkadot-sdk/pull/12877)) and fixed encoding and arithmetic edge cases in the election code ([#13265](https://github.com/paritytech/polkadot-sdk/pull/13265), [#13269](https://github.com/paritytech/polkadot-sdk/pull/13269)).

I am still the only developer of the staking miner and I'm on call for it in production. When Paseo Asset Hub added a transaction extension that broke every solution submission, I put in a quick workaround ([staking-miner#1302](https://github.com/paritytech/polkadot-staking-miner/pull/1302)) and then the proper fix once subxt supported it ([staking-miner#1332](https://github.com/paritytech/polkadot-staking-miner/pull/1332)). I also added a metric so alerts can tell apart a miner that was outbid from one that is down ([staking-miner#1331](https://github.com/paritytech/polkadot-staking-miner/pull/1331)).

### 4. Fellowship runtimes and governance

The App integrations coming to mainnet (Individuality, dotUSD, Bulletin, statement store and others) bring many operational values that will need changing often and quickly once live, like storage quotas, onboarding batch sizes and anti-spam fees. None of them move funds, but Root is slow and handles one referendum at a time, so it is the wrong tool for this. I added a `technical_maintenance` track on Asset Hub Polkadot for this kind of tuning. Its origin can only reach the parameters the runtime explicitly gives it, which is why it can decide faster than Root. In the same PR I added a `prosperity_emergency` track with very limited powers, so governance can react quickly if something goes wrong with the Prosperity monetary mechanisms, for example by pausing minting ([runtimes#1236](https://github.com/polkadot-fellows/runtimes/pull/1236)). Then I wired `technical_maintenance` into People and Asset Hub for the parameters that need it ([runtimes#1269](https://github.com/polkadot-fellows/runtimes/pull/1269), [runtimes#1279](https://github.com/polkadot-fellows/runtimes/pull/1279)).

I also fixed the precompile weight paths that were blocking the 2.5 release ([runtimes#1280](https://github.com/polkadot-fellows/runtimes/pull/1280), [#13092](https://github.com/paritytech/polkadot-sdk/pull/13092)).

### 5. Reviews

I spent a good part of this period reviewing staking work from others providing guidance and full support, for example Stephen Lawrence's series routing dust, fees and Coretime revenue into the DAP across the relay and system chains ([runtimes#1287](https://github.com/polkadot-fellows/runtimes/pull/1287), [runtimes#1288](https://github.com/polkadot-fellows/runtimes/pull/1288), [runtimes#1289](https://github.com/polkadot-fellows/runtimes/pull/1289), [runtimes#1301](https://github.com/polkadot-fellows/runtimes/pull/1301), [runtimes#1319](https://github.com/polkadot-fellows/runtimes/pull/1319)), and his SDK changes to the signed-phase reward source and slash destination ([#12843](https://github.com/paritytech/polkadot-sdk/pull/12843)) and the accumulate-and-forward period ([#13153](https://github.com/paritytech/polkadot-sdk/pull/13153)). I also reviewed the election-provider migration to `#[pallet::authorize]` ([#13032](https://github.com/paritytech/polkadot-sdk/pull/13032), [#12978](https://github.com/paritytech/polkadot-sdk/pull/12978)) and the removal of the multi-phase election provider from the relay runtimes ([runtimes#1313](https://github.com/polkadot-fellows/runtimes/pull/1313)). Outside staking, I reviewed Ankan and Luka's AsseHub Migration v2 series (e.g. [runtimes#1285](https://github.com/polkadot-fellows/runtimes/pull/1285), [runtimes#1305](https://github.com/polkadot-fellows/runtimes/pull/1305), [runtimes#1321](https://github.com/polkadot-fellows/runtimes/pull/1321), [#13282](https://github.com/paritytech/polkadot-sdk/pull/13282), [#13475](https://github.com/paritytech/polkadot-sdk/pull/13475)).


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I was eligible to vote on 0 referenda. | I was a Candidate until my promotion on 2026/08/30 (block 9,609,343). From then to this report, no referendum was open on the Members or Proficient Members tracks, the only tracks open to Rank II. All referenda open in that window were on tracks requiring Rank III or above. |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Acknowledgements

Thanks to [kianenigma](https://collectives.subsquare.io/user/1eTPAR2TuqLyidmPT9rMmuycHVm9s9czu78sePqg2KHMDrE/fellowship) for sponsoring this work and for the design discussions behind validator collators, and to Ankan and Stephen Lawrence for the staking and DAP work I had the chance to review.
