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
- Date of last report: 28th May 2024
- Area(s) of Expertise/Interest: Pallets, staking, nomination pools, developer tools, pro-sumer applications.


## Reporting period

- Start date: 2024/07/15
- End date: 2024/10/15


## Evidence
This period has been spent on maintaining the [Staking Dashboard](http://staking.polkadot.cloud), developing an alternative to Polkadot JS Apps in the [Polkadot Developer Console](https://console.polkadot.cloud), and implementing [RFC 0097](https://polkadot-fellows.github.io/RFCs/approved/0097-unbonding_queue.html#rfc-0097-unbonding-queue) (unbonding queue).

I have given a [public presentation](https://x.com/rossbulat/status/1825967285896380659) on the issues around Polkadot JS Apps, and solutions in the Polkadot Developer Console, which has now been released in a public alpha. Community feedback has been solicited since this announcement.

I have also bootstrapped service platform [polkadot.cloud](http://polkadot.cloud), which now hosts the staking dashboard and developer console. This enabled W3F and Parity to migrate the source code of Staking Dashboard to a viable home.

I managed migrations of the staking dashboard and its source code away from the polkadot.network domain and paritytech Github organization respectively.

In this period I have learned a great deal about metadata and how UI can be derived from it. Developer Console does this in the same manner that the PJS Apps Developer tab has done. 

- I studied the structure of metadata in detail, understanding each section and how it describes the runtime.
- I studied and understood the 8 types exposed in metadata, ranging from variants, composites, compact, primitives, sequences, arrays, bit sequences and tuples, and how they recursively comprise storage item / extrinsic / constant signatures.
- I created a UI that describes storage items, constants, and extrinsics, that displays forms that enable these items to be interacted with - to query storage and to submit extrinsics for a runtime.
- Beyond this focus, Developer Console identifies the shortfalls of JS Apps and demonstrates tangible ways it can be improved (these are demonstrated in the presentation).
- I also studied RFC 0097 in detail and understand the unbonding queue mechanism, and how to implement this in the Polkadot SDK runtime.

My work is relevant for the specific Manifesto requirements:
- the Polkadot business-logic (aka the 'runtime');
- pallets utilized by the Polkadot (Main) Network and its system chains;
- runtime and host APIs
- user-interface code required to practically execute upgrades to the Polkadot (Main) Network

Polkadot SDK PRs:

- [RFC-0097 Implementation to Decrease Unbonding Time](https://github.com/paritytech/polkadot-sdk/pull/5449)
- [Remove staking controller account logic from pallets & runtimes](https://github.com/paritytech/polkadot-sdk/pull/5715)

Social:

- [Announcement presentation of Polkadot Developer Console initiative](https://x.com/rossbulat/status/1825967285896380659)
- Continue to engage with staking related activities.


Documentation / Education:

- Launched and open sourced Polkadot Cloud docs. [website](https://docs.polkadot.cloud/) / [source code](https://github.com/polkadot-cloud/docs).


Staking Dashboard PRs:
- [feat: Check if Polkadot app is at least generic version](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2191) 
- [feat(refactor): People chain on Polkadot - disable identities on Relay Chain](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2192)
- [feat(refactor): Abstract state bootstrapping & subscriptions from Api](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2193)
- [feat(refactor): Use merkelise-metadata for Ledger signing, discontinue metadata service](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2195)
- [feat(refactor): @substrate/connect updates](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2196)
- [feat(refactor): Remove pre-paged rewards deprecation logic](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2197)
- [feat: Activate People Chain and re-enable identities](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2198)
- [fix: people status on identity sync](https://github.com/polkadot-cloud/polkadot-staking-dashboard/pull/2236)


Developer Console:
- Launch of Public Alpha and positioning to be an eventual alternative to Polkadot JS Apps.
- Polkadot Developer Console [app](http://console.polkadot.cloud) / [source code](https://github.com/polkadot-cloud/polkadot-developer-console).

There are too many PRs / commits to list here, so the evidence instead points to the source code of Developer Console that was rapidly iterated leading up to its public alpha release, as well as the public presentation.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|   |   |   |   |   |

Out of the 1 **Member origin** referendum posted in this period that I was eligible to vote on, I did not vote on it as Snowbridge is currently outside of my area of expertise (referendum #150).

## Misc

- [x] Comment(s): 

This was a turbulant period involving migrations, setting up new platforms to host applications, and re-focusing my efforts around the fellowship, all the while battling an illness that spanned this period. Although I am happy with this evidence, it has been challenging period and I am looking forward to the next one being smoother.