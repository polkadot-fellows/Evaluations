# Evidence-0002: Retention at Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/09/21)                                                             |
| **Submitted by**| Ross Bulat                                                                        |


## Member details

- Matrix username: @rossbulat:matrix.org
- Polkadot address: 1hYiMW8KSfUYChzCQSPGXvMSyKVqmyvMXqohjKr3oU5PCXF
- Current rank: 1
- Date of initial induction: 6th December 2023
- Date of last report: 21st September 2024
- Area(s) of Expertise/Interest: Pallets, staking, nomination pools, developer tools, pro-sumer applications.


## Reporting period

- Start date: 2024/10/15
- End date: 2025/01/15


## Evidence
This period has been spent on maintaining the [Staking Dashboard](http://staking.polkadot.cloud) and surrounding tooling ensuring users can still stake on Polkadot.

In this period I have been studying abstraction of code and how to better formalise / organise packages for better maintainability. A range of refactors and upgrades have taken place to keep the codebase using latest packages, and simplifying syntax.

I have focused on user support and engagement, something that has been lacking in the past. Discord has been set up, and over 100 Polkadot users have joined and are communicating staking improvements and requests.

I have  bootstrapped an API service for Polkadot staking, that solves usability issues around staking on Polkadot. User rewards are now fetched instantly. This service will expand to validator performance, fast unstake checking, and validator / pool performance data, that will dramatically speed up workflows. This is a significant improvement over the current state of affairs, where node-only data fetching is becoming unviable as the staking system scales - e.g. 297 to 500 validators, now 30k+ nominators, etc.

Staking dashboard also crossed the milestone of being light client by default. This was necessary to not exhaust RPC connections with the latest JSON RPC spec.

Also in this period, I replaced PJS API with PAPI in the staking dashboard, and rolled out Wallet Connect support. 

More validators have been onboarded into the validator community data source.

PRs Staking Dashboard:
- [feat(fix): Abstract LeavePool, use as depositor unbond](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2370) 
- [feat: Use pool points for unbonding / leaving pool](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2369) 
- [feat: Disable dual staking](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2368) 
- [feat: Disable dual staking](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2365) 
- [feat: Nominator Rewards from Staking API, discontinue Subscan nominator rewards](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2365) 
- [feat(refactor): Add assets package, move svgs to package](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2361) 
- [fix: Proxy support logic for Polkadot API](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2359) 
- [feat: Add 100% validator commission prompt.](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2358) 
- [feat(refactor): Remove semi](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2356) 
- [feat(refactor): Pool rewards to controller, pool types to types package](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2344) 
- [feat(refactor): Migrate to ESLint 9](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2342) 
- [feat(refactor): Rm useSize hook, lodash deps](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2341) 
- [feat(fix): Fix prettier organize imports, lint.](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2340) 
- [feat(refactor): Locales to package, fixes and structural improvements.](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2338) 
- [feat: Refetch token price if online status is true](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2337) 
- [feat(fix): Ensure unclaimed payouts are ints](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2336) 
- [Polkadot API (PAPI) Integration PR](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2335) 
- [fix: theme Selectable buttons](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2334) 
- [feat: Init Staking API GraphQL Plugin, discontinue Binance Spot](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2332) 
- [feat: Support options refresh with Discord and Mail](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2331) 
- [feat: init ui-structure, consts, styles packages, migrate Structure kit](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2330) 
- [feat: Init monorepo, app and ui-buttons packages](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2327) 
- [feat(refactor): Abstract useTimeleft](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2321) 
- [feat(fix): Render timeleft on end time update](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2320) 
- [feat: Replace maxElectingVoters const with counterForNominators storage](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2319) 
- [feat(refactor): Use new Polkicon from @w3ux/polkicon](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2315) 
- [feat(refactor): Update withProviders from @w3ux/factories](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2314) 
- [feat(refactor): Use useOnResize, remove lodash.throttle.](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2313) 
- [feat(refactor): Generalise useSize hook](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2312) 
- [feat: Wallet Connect support](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2276) 

PRs w3ux Library:
- [PR for including Frog nodes in the staking dashboard](https://github.com/w3ux/w3ux-library/pull/148) 
- [Addition of ProStakers.com validator in the community page](https://github.com/w3ux/w3ux-library/pull/147) 
- [feat(fix): Initial active account formatting correctly](https://github.com/w3ux/w3ux-library/pull/146) 
- [feat(refactor): Remove ChainSafe Snap](https://github.com/w3ux/w3ux-library/pull/145) 
- [feat: add rmDecimals to utils, apply to planckToUnit](https://github.com/w3ux/w3ux-library/pull/144) 
- [feat: Add useTimeleft hook and utils to @w3ux/hooks](https://github.com/w3ux/w3ux-library/pull/143) 
- [feat(refactor): Misc utils improvements](https://github.com/w3ux/w3ux-library/pull/142) 
- [feat: add fontSize prop to Polkicon, div -> span](https://github.com/w3ux/w3ux-library/pull/141) 
- [feat: Rewrite and improve Polkicon - @w3ux/react-polkicon](https://github.com/w3ux/w3ux-library/pull/139) 
- [feat: Add @w3ux/crypto package](https://github.com/w3ux/w3ux-library/pull/138) 
- [feat: init factories package with withProviders](https://github.com/w3ux/w3ux-library/pull/137) 
- [feat: Add useOnResize hook](https://github.com/w3ux/w3ux-library/pull/136) 
- [feat: Add useSize hook to @w3ux/hooks](https://github.com/w3ux/w3ux-library/pull/134) 
- [feat(utils):unit fn enhancements + more tests](https://github.com/w3ux/w3ux-library/pull/133) 
- [feat(refactor): Removes bignumber.js as utils dependency, remove obsolete utils, enhance unit utils](https://github.com/w3ux/w3ux-library/pull/130) 
- [chore: substrate bindings for AccountId codec](https://github.com/w3ux/w3ux-library/pull/129) 
- [chore: substrate bindings for AccountId codec](https://github.com/w3ux/w3ux-library/pull/129) 


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |N/A   |   |  |
|IV |60%   |N/A   |   |  |
|V  |50%   |N/A   |   |  |
|VI |40%   |N/A   |   |  |

## Misc

- [x] Comment(s): 

With the staking system evolving rapidly, I have been focused on ensuring the Staking Dashboard is up to date and user-friendly. The API service I have bootstrapped will be a significant improvement for users, and I am excited to see how it will be received. I believe this period up to AssetHub migration should focus on maintaining usability, ensuring our current infrastructure is working as expected & does not break at the cost of alienating Polkadot users.