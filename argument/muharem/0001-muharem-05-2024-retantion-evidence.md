# Evidence-0001: Retention at Rank 2

|                 |              |
| --------------- | ------------ |
| **Report Date** | 2024/05/04   |
| **Submitted by**| Muharem      |


## Member details

- Matrix username: `@muharem:parity.io`
- Polkadot address: `12HWjfYxi7xt7EvpTxUis7JoNWF7YCqa19JXmuiwizfwJZY2`
- Current rank: `2`
- Date of initial induction: `2023/11/11`
- Date of last report: `2023/11/11`
- Area(s) of Expertise/Interest: `System Parachains, FRAME, XCM`


## Reporting period

- Start date: 2024/01/01
- End date: 2024/05/04


## Evidence

In this letter I would like to share what I have been working on since my last report and what I think is relevant to the Polkadot Fellowship Program.

The liquidity pool and XCM fee trader utilizing it for fee payments in non-native assets were rolled out to the Polkadot Asset Hub (runtimes [1.2.0](https://github.com/polkadot-fellows/runtimes/releases/tag/v1.2.0)). Main cross-chain use cases were tested, and all issues raised by auditors are closed ([pr1](https://github.com/paritytech/polkadot-sdk/pull/3250), [pr2](https://github.com/paritytech/polkadot-sdk/pull/3251), [pr3](https://github.com/paritytech/polkadot-sdk/pull/3275)). Work to get new features adopted has been initiated. Moving forward, I am supporting Liam to get pool rewards implemented and rolled out ([issue](https://github.com/paritytech/polkadot-sdk/issues/3149), [pr](https://github.com/paritytech/polkadot-sdk/pull/3926)). 

The Treasury’s multi-asset spend feature has released to the network (runtimes [1.1.0](https://github.com/polkadot-fellows/runtimes/releases/tag/v1.1.0)), main use cases tested, and documentation was provided. We have seen some initial tries made by community members ([blog post](https://forum.polkadot.network/t/multi-asset-treasury-and-milestone-based-spends/6780)). I have been exploring ways in which we can use liquidity pools mentioned above and the new treasury spend to diversify the treasure assets in a trustless way with OpenGov ([pr](https://github.com/paritytech/polkadot-sdk/pull/2939)). This drove the introduction of a new feature to the scheduler pallet that lets a user set a retry policy for scheduled tasks ([issue](https://github.com/paritytech/polkadot-sdk/issues/3014), [pr](https://github.com/paritytech/polkadot-sdk/pull/3060)). The first sub-treasury was onboarded for the Fellowship Collective ([pr](https://github.com/polkadot-fellows/runtimes/pull/109)). 

The Ambassador Program I had mentioned in my last report has been reshaped and approved by the stakeholders ([referendum](https://polkadot.polkassembly.io/referenda/487)). Therefore, I have raised a pull request with the new on-chain implementation on the Collectives Parachain ([pr](https://github.com/polkadot-fellows/runtimes/pull/291)). 

With a goal of implementing meta transactions, I've delved deeply into our transaction model, its implementation, and new contracts and implementation from Extrinsic Horizon ([issue](https://github.com/paritytech/polkadot-sdk/issues/2415)). As a result, an RFC for meta transactions implementation was created with a few proposals and implementation drafts to get feedback from stakeholders, including the clients’ owners ([issue](https://github.com/paritytech/polkadot-sdk/issues/4123), [draft1](https://github.com/paritytech/polkadot-sdk/pull/3712), [draft2](https://github.com/paritytech/polkadot-sdk/pull/4122)).

Furthermore, I’ve been consistently supporting the work in the runtimes repository with PRs review and the work to get the new releases for Polkadot. Additionally, I have been consistently participating in monthly Fellowship calls. I am happy to see how the program is progressing and wish to retain my current rank and continue the work.