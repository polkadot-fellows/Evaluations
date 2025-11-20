# Evaluations

This repository contains all the Arguments filed as part of the Retention and Promotion of members of the Polkadot Technical Fellowship. These Arguments have been submitted for the discussion and review of individual members' contributions and achievements, as well as for the Fellowship's on-chain bodies to signal approval or disapproval of.

More information about Membership management can be found on the [Polkadot Technical Fellowship Dashboard](https://polkadot-fellows.xyz/#/membership).

## History

Arguments used to be called simply "Evidence" and you may sometimes see this defunct term used. It was deprecated in favour of "Arguments", since people misconstrued their responsibilities regarding this information and tended to simply submit a list of code changes.

## Scope

The Fellowship is about retaining protocol expertise from developers, but also ideators, designers, formalisers and research analysts.
According to Section 4 of the [Fellowship Manifesto](https://github.com/polkadot-fellows/manifesto/blob/0c3df46d76625980b8b48742cb86f4d8fa6dda8d/manifesto.pdf), members of the Polkadot Fellowship are responsible for *expertise on a technology (or a specific implementation of it) required and primarily used for the Polkadot (Main) Network to continue operating and improving*. 

Specifically, this expertise may cover contributions in the following areas:
 * the internals of all functional Polkadot node implementations;
 * cryptographic data-structures, algorithms, languages and APIs required for the continued upkeep of the Polkadot (Main) Network;
 * consensus algorithms concerning the Relay-chain (BABE, BEEFY, GRANDPA, SASSAFRAS);
 * trust-free bridges relying on said consensus algorithms utilised by system chains;
 * parachain consensus;
 * cross-chain message passing (XCMP, HRMP, DMP \& UMP);
 * the Polkadot libp2p-based peer networking protocol;
 * the Polkadot topology strategies;
 * chain synchronisation strategies utilised by Polkadot;
 * the Polkadot business-logic (aka the 'runtime');
 * pallets utilised by the Polkadot (Main) Network and its system chains;
 * the internals of the frame pallet framework;
 * runtime and host APIs;
 * the XCM specification and realisation;
 * standard RPCs;
 * user-interface code required to practically execute upgrades to the Polkadot (Main) Network; and
 * code or technology required by, and utilised primarily for, any code or technology already included.

However, some technologies/code fall out of this scope, notably:
 * Rust language (required by realisations of the Polkadot Network, but not primarily used for them);
 * libp2p (required by the Polkadot Network but not primarily used for it);
 * ‘subxt‘ (useful tooling, but not required for Polkadot’s continued operation); and
 * ‘ink!’ (useful tooling, but not required for Polkadot’s continued operation).

Arguments are scoped to the subset of these concerns which must be held consistent across all evaluations for Retention and Promotion.


## Guidelines

Arguments may be made by members or candidates for the purpose of rank retention or promotion.

Arguments must directly address each of the Rank Requirements as stated in the Manifesto for the rank at which to be retained or at which to be promoted. If in doubt, copy and paste each requirement as stated in the Manifesto and write a short form answer, making links where necessary to demonstrate your activity. Ensure any proof is __specific__ to the Manifesto requirements and __substantial__. Irrelevant or insubstantial proofs may result in an early dismissal of the proposal.

The Argument is not a place to insert primary sources. No deep code review should be needed to evaluate the argument and its proofs. Pre-existing peer reviews (whether code or academic writing), accepted answers on Q&A sites, presentation at high-quality conferences or publication in high-quality media may be used to help understand the depth and quality of the work.

Any reviewer should be able consume your entire argument, including any auxilliary proofs, within __10 minutes__. 


## Significance

All members seeking retentions or promotions will need to reflect on their voting record in relation to the thresholds for voting "activity" and voting "agreement" described in the Manifesto. 

All members (Ranks I-VI) must serve a minimum period of service of 12 months at their current rank before seeking promotion to a higher rank. There is no minimum period of service for Candidates seeking to become members.

Members seeking promotions for Rank III-VI are required to attend an **in-person interview** before their request can be moved to on-chain voting. The Fellowship Sub-Treasury can cover all costs incurred while attending these in-person evaluations. An evaluation checklist for promotions is available [here](https://docs.google.com/document/d/1ZucQ4V06rfNLIRV3ZIDHPwoN3Xa-ib671SNg8My4gao/edit?usp=sharing).

More information can be found in the [FAQ](faq.md).


## Timelines

Members should individually monitor the progress of their demotion and promotion periods on the [Core Fellowship UI](https://collectives.subsquare.io/fellowship/core) provided by Subsquare. Alternatively, members can check their individual status directly on the chain state via [Polkadot-JS](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fsys.ibp.network%2Fcollectives-polkadot#/chainstate).

Members can also add an ical feed for Fellowship-related data directly into their email client or their Google account using this link: **webcal://fellowship-calendar.kchr.de/?account=YOUR_ACCOUNT_ID**. The code for this widget can be found [here](https://github.com/bkchr/fellowship-ical). 

It is recommended that members submit their Argument for review (via GitHub) and on-chain (via Subsquare) as per the following deadlines:
- For retentions: no later than **30 days** prior to the end of the demotion period
- For promotions: no later than **40 days** prior to the end of the demotion period


## Process

The process for submitting Arguments is open to all existing Fellowship members (i.e. Rank I to IX). Anyone may provide comments on submitted Arguments.

To submit an Argument, follow these steps:
  * Fork the `Evaluations` repository.
  * Create a new folder in the `argument` folder and rename it to match your Github username.
  * Copy the `0000-argument-template.md` file into the new folder and rename it to match the title of your request.
  * Fill out the Argument template and open a PR.
  * Announce your Argument to the Fellowship and wait at least one week.
  * If there are no major pushbacks by the Fellowship, submit your Argument on-chain via the [Core Fellowship UI](https://collectives.subsquare.io/fellowship/core) provided by Subsquare.

Once the request has been approved via on-chain referendum, the PR can be merged. This on-chain process is designed to be resilient to where the Arguments are hosted and in what format, so it can be migrated away from GitHub in the future. The Fellowship should not approve more than one Argument with the same number. PRs may be closed by their author, when sufficiently stale, or after a period of 6 months without approval. 


## Communication channels

The Fellowship is using Matrix for communication. Right now there exists two channels:

- [Polkadot Technical Fellowship Channel](https://matrix.to/#/#fellowship-members:parity.io): The channel for all Fellowship members to discuss. To get voice rights, you need to be part of the Fellowship. However, the channel is readable by anyone.
- [Polkadot Technical Fellowship - Open Channel](https://matrix.to/#/#fellowship-open-channel:parity.io): Open channel for anyone. Should be used to reach out to the Fellowship e.g. to request review or help on a topic.
