# Evaluations

This repository contains all the Evidences filed as part of the Retention and Promotion of members of the Polkadot Technical Fellowship. These Evidences have been submitted for the discussion and review of individual members' contributions and achievements, as well as for the Fellowship's on-chain bodies to signal approval or disapproval of.


## Scope

The Fellowship is about retaining protocol expertise from developers, but also ideators, designers, formalisers and research analysts.
According to the [Fellowship Manifesto](https://github.com/polkadot-fellows/manifesto/blob/0c3df46d76625980b8b48742cb86f4d8fa6dda8d/manifesto.pdf), members of the Polkadot Fellowship are responsible for *expertise on a technology (or a specific implementation of it) required and primarily used for the Polkadot (Main) Network to continue operating and improving*. 

Specifically, this expertise may cover contributions in the following areas:
 * the internals of all functional Polkadot node implementations;
 * cryptographic data-structures, algorithms, languages and APIs required for the continued upkeep of the Polkadot (Main) Network;
 * consensus algorithms concerning the Relay-chain (BABE \& GRANDPA);
 * trust-free bridges relying on said consensus algorithms (planned to be) utilised by system chains;
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

Evidences are scoped to the subset of these concerns which must be held consistent across all evaluations for Retention and Promotion.


## Significance

Evidences are a proof of work to indicate the Fellowship's commitment to implement and maintain designs and architectures for Polkadot (and its ecosystem???), as well as participate in discussion and social consensus according to open-source principles.

All members that are on standard allowance as per the [Fellowship Salaries](https://github.com/polkadot-fellows/RFCs/blob/main/text/0050-fellowship-salaries.md) must submit their Evidences once over a period of time (3 months for Rank I-II, 6 months for Rank III-VI) to avoid demotion to a lower rank. 


## Process

The process for submitting Evidences is open to all existing Fellowship members (i.e Rank I to IX). Anyone may provide comments on submitted Evidences.

To submit an Evidence, follow these steps:
  * Copy the `0000-evidence-template.md` file into the `evidence` folder and rename to match the title of your rank request
  * Fill out the Evidence template and open a PR.
  * Rename the file to correspond to the GitHub pull request number and update the "Evidence PR" field in the file.

The Fellowship will decide via an on-chain voting mechanism when to approve and reject Evidences. It does so by issuing an on-chain remark with the body `EVIDENCE_APPROVE(xxxx, h)` from the `Fellows` origin on the Polkadot Collectives blockchain, where xxxx is the number of the Evidence and h is the blake2-256 hash of the raw submission text. Once this remark has been made, the PR can be merged. This on-chain process is designed to be resilient to where the Evidences are hosted and in what format, so it can be migrated away from GitHub in the future. The Fellowship should not approve more than one Evidence with the same number.

The Fellowship may also decide to reject an Evidence by issuing a remark with the text `EVIDENCE_REJECT(xxxx, h)`. This is a formality to provide clarity on when PRs (or their analogue on non-GitHub platforms) may be closed. PRs may be closed by their author, as well. PRs may be closed when sufficiently stale, as well - after a period of 3 months without acceptance.


## Communication channels

The Fellowship is using Matrix for communication. Right now there exists two channels:

- [Polkadot Technical Fellowship Channel](https://matrix.to/#/#fellowship-members:parity.io): The channel for all Fellowship members to discuss. To get voice rights, you need to be part of the Fellowship. However, the channel is readable by anyone.
- [Polkadot Technical Fellowship - Open Channel](https://matrix.to/#/#fellowship-open-channel:parity.io): Open channel for anyone. Should be used to reach out to the Fellowship e.g. to request review or help on a topic.
