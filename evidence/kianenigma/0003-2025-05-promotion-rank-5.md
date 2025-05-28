# Argument-0003: Promotion to Rank 5

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/05/10)                                                             |
| **Submitted by**| Kian Paimani - `kianenigma`                                                                        |


## Member details

- Matrix username: @kianenigma
- Polkadot address: `1eTPAR2TuqLyidmPT9rMmuycHVm9s9czu78sePqg2KHMDrE`
- Current rank: 4
- Date of initial induction: seeding
- Date of last report: [22/05/2024](https://github.com/polkadot-fellows/Evaluations/pull/28)
- Area(s) of Expertise/Interest: 
    - FRAME
    - Staking / NPoS
    - JAM

## Reporting period

- Start date: 2024/12
- End date: 2025/05


## Argument

### Overview 
During this evaluation period, the scope of my managerial responsibilities in Parity has been slightly reduced, and is shifting more towards engineering. This is aligned with my aptitude and role in the "core" fellowship as well. This further encouraged me to recognize that I already meet the time requirement to **ask for a promotion to Rank V**.

I have spent the last few months materializing the transition of Polkadot's NPoS system into the Polkadot Hub (a _parachain_, rather than the relay-chain), the design for which I have scoped since early 2022. Beyond that, I have continued my participation in PBA, meetups and Accelerator programs to speak about Polkadot. Finally, I am still gladly participating in the development of GrayMatter, a JAM client in Elixir, developed by [JamBrains](https://x.com/jam_brains).

### Records / Links
* [Original design](https://www.youtube.com/watch?v=qVd9lAudynY) of the multi-block NPoS for parachain, currently being implemented in Polkadot Hub.
* Noteworthy code contributions (please note the commit history as well, as some PRs are not opened by me directly): [1](https://github.com/paritytech/polkadot-sdk/pull/7282), [2](https://github.com/paritytech/polkadot-sdk/pull/7782), [3](https://github.com/paritytech/polkadot-sdk/pull/8127)
* [Design of the precompile interface](https://github.com/paritytech/polkadot-sdk/pull/8389) for Solidity contracts interacting with staking.
* [Specification of the new multi-block+asyncronous staking system](https://github.com/paritytech/polkadot-sdk/pull/8313), inspired by the Parachain's implementor's guide.
* The list of my public talks and blog posts in [my website](https://blog.kianenigma.com/). Please see the ones dated after my last retention date.

### Promotion Specific
Here I articulate how I see myself fulfilling some of the manifesto requirements specific to rank V that are not present in Rank IV. I presume the rest is self-evident, and I would be happy to discuss them further if requested.

> Play a primary role in ideating, designing, and formalizing or prototyping a major component.

I have been the primary champion for [`try-runtime`](https://github.com/paritytech/try-runtime-cli)/[`try_state`](https://paritytech.github.io/polkadot-sdk/master/frame_support/traits/trait.Hooks.html#method.try_state) set of tools, used for many years across the Polkadot ecosystem (notably in the fellowship CI) for testing runtime migrations and the integrity of runtime's state, to this day.

> Usefully assisted in devising ("creating," "inventing," "incepting") three more major components.

* Multi-block staking system, [polkadot-staking-miner](https://github.com/paritytech/polkadot-staking-miner)
* [Polkadot Omni Node](https://paritytech.github.io/polkadot-sdk/master/polkadot_sdk_docs/reference_docs/omni_node/index.html)
* FRAME's ability to express [default configurations for Pallets](https://paritytech.github.io/polkadot-sdk/master/frame_support/pallet_macros/attr.config.html#optional-with_default)

> Be able to speak with technical authority on all levels of the Polkadot protocol (past, present, and future).

I have specifically tried to form holistic stories around Polkadot's entire history in a number of my talks, for example my [recap of the blockchain scalability](https://blog.kianenigma.com/blockchain-reimagined/presentation-tum/), and the [roundup of Polkadot-SDK's development in 2024](https://blog.kianenigma.com/posts/tech/polkadot-sdk-2024/). 

### Acknowledgment

Similar to my previous argument, I would like to acknowledge other fellowship members who contribute to the above alongside me on the above outcomes, most notably: 

* Ankan and Tsvetomir, Rank I and II respectively, on the staking project.
  * Joe, Rank III, for standing up for the difficult task of managing the overall migration of majority of Polkaodt's subsystems to Polkadot Hub, including staking.
* Francisco and Oliver, Rank I and III respectively, on GrayMatter.

As the fellowship manifesto puts it: 

> Internally, they should be both helpful, tactful and well-spirited, understanding that Polkdaot is a team effort.

## Voting record

Please see https://collectives.subsquare.io/fellowship/members/1eTPAR2TuqLyidmPT9rMmuycHVm9s9czu78sePqg2KHMDrE, and note that from the date of my last retention (https://collectives.subsquare.io/fellowship/referenda/256), the participation rate is almost 100%, excluding wrong proposals and those that I am not eligible for.
