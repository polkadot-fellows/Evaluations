# Evidence-0003: Retention at Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/12/18)                                                             |
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

I have  bootstrapped an API service for Polkadot staking, that solves usability issues around staking on Polkadot. User rewards are now fetched instantly. This service will expand to validator performance, fast unstake checking, and validator / pool performance data, that will dramatically speed up workflows. This is a significant improvement over the current state of affairs, where node-only data fetching is becoming unviable as the staking system scales - e.g. 297 to 500 validators, now 30k+ nominators, etc, and where Subscan has strict throttle limits for free API usage that is becoming unviable for high user open source projects like staking dashboard.

Staking dashboard also crossed the milestone of being light client by default. This was necessary to not exhaust RPC connections with the latest JSON RPC spec.

Also in this period, I replaced PJS API with PAPI in the staking dashboard, and rolled out Wallet Connect support. 

More validators have been onboarded into the validator community data source.

#### Unbonding RFC implementation PR

- [RFC-0097 Implementation to Decrease Unbonding Time.](https://github.com/paritytech/polkadot-sdk/pull/5715/) 

Due to the pressing issues of the application side work, and the limited scope of a Rank 1 fellowship member, I have not made significant progress on the unbonding RFC. However, in this period I have:

- Communicated the progress of the unbonding RFC implementation to the community, explaining the progress made and next steps.
- Had internal meetings with other fellowship members discussing its progress and what needs to be done.
- Identified a deprecation and removal of old / duplicated unbonding logic.
- Continued to resolve conflicts and keep the PR up-to-date with the latest changes in the Polkadot-SDK codebase.

### Relevant PRs Staking Dashboard

The recent series of pull requests showcases significant progress and key improvements to the Polkadot Staking Dashboard. A major highlight is the introduction of enhanced staking functionalities, including abstracting LeavePool logic and utilizing pool points for unbonding and leaving pools. The transition from Subscan to the Staking API for fetching nominator rewards demonstrates a shift towards a more integrated and streamlined data flow. Moreover, the dashboard now provides a 100% validator commission prompt to improve user awareness and facilitate proactive decision-making.

On the architectural side, the migration to a monorepo structure and the introduction of modular packages such as ui-structure, assets, and types mark a foundational transformation aimed at improving scalability and maintainability. Refactoring efforts, including the removal of lodash dependencies, abstracting hooks like useSize, and transitioning to ESLint 9, have further optimized the codebase. Additionally, new features such as WalletConnect support, PJS Removal in favour of Polkadot API, proxy logic enhancements, and the inclusion of the Staking API GraphQL plugin emphasize a focus on expanding interoperability and modernizing the platform's core capabilities. Collectively, these updates signal a robust and forward-thinking evolution of the staking dashboard, setting the stage for enhanced functionality and user experience.

### PR List

#### Security 
- [feat: Add 100% validator commission prompt.](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2358) 

#### Nomination Pools
- [feat(refactor): Pool rewards to controller, pool types to types package](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2344) 
- [feat(fix): Abstract LeavePool, use as depositor unbond](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2370) 
- [feat: Use pool points for unbonding / leaving pool](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2369) 

#### Web Extensions / wallet support
- [feat: Wallet Connect support](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2276) 

#### Adapting to Pallet-side changes
- [feat: Disable dual staking](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2368) 
- [feat: Replace maxElectingVoters const with counterForNominators storage](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2319) 

#### Scalability and performance
- [feat: Init Staking API GraphQL Plugin, discontinue Binance Spot](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2332) 
- [feat: Nominator Rewards from Staking API, discontinue Subscan nominator rewards](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2365) 

#### Refactoring and modernization
- [feat: Init monorepo, app and ui-buttons packages](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2327) 
- [feat(refactor): Migrate to ESLint 9](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2342) 
- [feat(refactor): Add assets package, move svgs to package](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2361) 
- [feat(refactor): Rm useSize hook, lodash deps](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2341) 
- [feat(fix): Fix prettier organize imports, lint.](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2340) 
- [feat(refactor): Locales to package, fixes and structural improvements.](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2338) 
- [feat(fix): Ensure unclaimed payouts are ints](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2336) 
- [feat: init ui-structure, consts, styles packages, migrate Structure kit](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2330) 
- [feat(refactor): Use new Polkicon from @w3ux/polkicon](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2315) 
- [feat(refactor): Abstract useTimeleft](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2321) 
- [feat(refactor): Update withProviders from @w3ux/factories](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2314) 
- [feat(refactor): Use useOnResize, remove lodash.throttle.](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2313) 
- [feat(refactor): Generalise useSize hook](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2312) 

#### PJS -> Polkadot API migration
- [Polkadot API (PAPI) Integration PR](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2335) 
- [fix: Proxy support logic for Polkadot API](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2359) 

#### User experience
- [feat: Support options refresh with Discord and Mail](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2331) 

### Relevant PRs w3ux Library

The recent updates to the w3ux library reflect significant progress in expanding its utility and enhancing its core components. A notable addition is the inclusion of the useTimeleft and useSize hooks under the @w3ux/hooks package, which provide reusable functionality for developers managing responsive and time-sensitive components. The addition of the @w3ux/crypto package offers cryptographic utilities tailored for blockchain applications. Furthermore, the withProviders feature in the new @w3ux/factories package simplifies provider integration, promoting consistency and ease of use across the library.

Improvements to existing components also highlight the progress. The Polkicon component has been completely rewritten and enhanced under @w3ux/react-polkicon, now supporting additional customization through a fontSize prop and improved rendering semantics. Refactoring efforts, such as removing bignumber.js and obsolete utilities, streamlining the unit utilities, and updating Substrate bindings for the AccountId codec, demonstrate a commitment to optimizing the library for efficiency and modern usage with Polkadot API. Community and project-specific contributions, such as the addition of ProStakers.com to the community page and Frog nodes support in the staking dashboard, further emphasize the library's adaptability and focus on the blockchain ecosystem's evolving needs. Together, these updates solidify w3ux as a robust and versatile toolkit for Web3 developers.

### PR List

#### Community asset support
- [PR for including Frog nodes in the staking dashboard](https://github.com/w3ux/w3ux-library/pull/148) 
- [Addition of ProStakers.com validator in the community page](https://github.com/w3ux/w3ux-library/pull/147) 

#### Fixes
- [feat(fix): Initial active account formatting correctly](https://github.com/w3ux/w3ux-library/pull/146) 

#### Discontinued features
- [feat(refactor): Remove ChainSafe Snap](https://github.com/w3ux/w3ux-library/pull/145) 

#### Library enhancements
- [feat: Add useTimeleft hook and utils to @w3ux/hooks](https://github.com/w3ux/w3ux-library/pull/143) 
- [feat: add fontSize prop to Polkicon, div -> span](https://github.com/w3ux/w3ux-library/pull/141) 
- [feat: Rewrite and improve Polkicon - @w3ux/react-polkicon](https://github.com/w3ux/w3ux-library/pull/139) 
- [feat: Add @w3ux/crypto package](https://github.com/w3ux/w3ux-library/pull/138) 
- [feat: init factories package with withProviders](https://github.com/w3ux/w3ux-library/pull/137) 
- [feat: Add useOnResize hook](https://github.com/w3ux/w3ux-library/pull/136) 
- [feat: Add useSize hook to @w3ux/hooks](https://github.com/w3ux/w3ux-library/pull/134) 
- [feat(utils):unit fn enhancements + more tests](https://github.com/w3ux/w3ux-library/pull/133) 
- [feat(refactor): Removes bignumber.js as utils dependency, remove obsolete utils, enhance unit utils](https://github.com/w3ux/w3ux-library/pull/130) 

#### PJS -> Polkadot API migration
- [chore: substrate bindings for AccountId codec](https://github.com/w3ux/w3ux-library/pull/129) 

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | N/A  | No referenda for my rank |
|II |80%   |N/A   |   |  |
|III|70%   |N/A   |   |  |
|IV |60%   |N/A   |   |  |
|V  |50%   |N/A   |   |  |
|VI |40%   |N/A   |   |  |

## Misc

- [x] Comment(s): 

As the staking system continues to evolve, my focus has been on keeping the Staking Dashboard up-to-date and as user-friendly as possible. I'm particularly excited about the new API service I’ve bootstrapped, which I believe will bring significant improvements to the user experience—I'm excited to see how it’s received. 

Looking ahead to the AssetHub migration, I’m committed to maintaining a seamless and reliable experience throughout the migration process, ensuring that our current infrastructure remains stable and supports Polkadot users without disruption. This is an exciting time, and I’m optimistic about the future as we continue to build and refine our tools for the community.