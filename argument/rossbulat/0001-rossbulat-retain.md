# Evidence-0001: Retention at Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/05/28                                                                                  |
| **Submitted by**| Ross Bulat                                                                                  |


## Member details

- Matrix username: @ross:parity.io
- Polkadot address: 1hYiMW8KSfUYChzCQSPGXvMSyKVqmyvMXqohjKr3oU5PCXF
- Current rank: 1
- Date of initial induction: 2024/03/18
- Date of last report: N/A
- Area(s) of Expertise/Interest: Pallets, Staking, Nomination Pools.


## Reporting period

- Start date: 2024/03/18
- End date: 2024/06/16


## Evidence

_Pallets utilised by the Polkadot (Main) Network and its system chains._

|  Areas of Contribution | Tasks  | Links   |Notes   |
|---|---|---|---|
|Polkadot SDK   | Maintenance of controller deprecation tracking | [Github Issue](https://github.com/paritytech/polkadot-sdk/issues/2500) | *Ongoing initiative.*  |
|Polkadot SDK   | Removal of controller account logic from polkadot-sdk | [Github PR](https://github.com/paritytech/polkadot-sdk/pull/4574) | *Ongoing initiative.* |
|Polkadot SDK | Identified & raised discussion around unlocking unclaimed nomination pool rewards | [Github Issue](https://github.com/paritytech/polkadot-sdk/issues/3398), [Polkadot Forum](https://forum.polkadot.network/t/nomination-pools-make-permissionless-withdrawing-the-default-claiming-permission/6766) | *Concluded.* |
|Polkadot SDK   | Allowed permissionless withdrawing by default for nomination pools | [Github PR](https://github.com/paritytech/polkadot-sdk/pull/3438) | *Merged.* |
| Roadmap/Vision   | Deployed new staking reward algorithm named "Average Reward Rate", fixing issues of outdated PJS based calculation | [Forum Post](https://forum.polkadot.network/t/new-average-reward-rate-calculations-for-staking/5599), [Staking Dashboard](https://staking.polkadot.network) | *Deployed.* |

_Code or technology required by, and utilised primarily for, any code or technology already included._

|  Areas of Contribution | Tasks  | Links   |Notes   |
|---|---|---|---|
| Toolng/Utilisation   | Developed and released Polkadot Staking Dashboard v1.4.4 | [Github PR](https://github.com/paritytech/polkadot-staking-dashboard/releases/tag/v1.4.4) | *Deployed.* |
| Toolng/Utilisation   | Developed and released Polkadot Staking Dashboard v1.4.3 | [Github PR](https://github.com/paritytech/polkadot-staking-dashboard/releases/tag/v1.4.3) | *Deployed.* |
| Toolng/Utilisation   | Developed and released Polkadot Staking Dashboard v1.4.2 | [Github PR](https://github.com/paritytech/polkadot-staking-dashboard/releases/tag/v1.4.2) | *Deployed.* |
| Toolng/Utilisation   | Developed and released Polkadot Staking Dashboard v1.4.1 | [Github PR](https://github.com/paritytech/polkadot-staking-dashboard/releases/tag/v1.4.1) | *Deployed.* |
| Toolng/Utilisation   | Developed and released Polkadot Staking Dashboard v1.4.0 | [Github PR](https://github.com/paritytech/polkadot-staking-dashboard/releases/tag/v1.4.0) | *Deployed.* |
| Toolng/Utilisation   | Developed and released Polkadot Staking Dashboard v1.3.1 | [Github PR](https://github.com/paritytech/polkadot-staking-dashboard/releases/tag/v1.3.1) | *Deployed.* |
| Toolng/Utilisation   | Developed and released Polkadot Staking Dashboard v1.3.0 | [Github PR](https://github.com/paritytech/polkadot-staking-dashboard/releases/tag/v1.3.0) | *Deployed.* |
| Toolng/Utilisation   | Developed and released Polkadot Staking Dashboard v1.2.1 | [Github PR](https://github.com/paritytech/polkadot-staking-dashboard/releases/tag/v1.2.1) | *Deployed.* |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [x] Comment(s): 

Polkadot SDK ativity was spent improving staking and nomination pool UX. Resolved an issue of exponential increase of unclaimed pool rewards, >160k DOT (and growing). Controller deprecation finish line is in sight, with the deprecation PR awaiting migrations, reviews & final polish before merge.

Staking dashboard was the first and only staking tool to support paged rewards on day 1 on all networks. Maintenance and critical features continue to roll out (e.g. 1-click pool joining) for users to use Polkadot's staking system with ease.

