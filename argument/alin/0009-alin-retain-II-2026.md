# Argument-0009: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/04/15)                                                             |
| **Submitted by**| Alin Dima                                                                                   |


## Member details

- Matrix username: `@alin:parity.io`
- Polkadot address: `148f8D1P4CP2tV8JuaVHzEXQQgj3jBxEg3k9qZydPzkJjbQG`
- Current rank: II
- Date of initial induction: 2024-04-26
- Date of last report: 2026/01/16
- Area(s) of Expertise/Interest: Parachains consensus, Elastic Scaling, Availability, Collator Protocol


## Reporting period

- Start date: 2026/01/16
- End date: 2026/04/15

## Argument

During this reporting period I have mainly focused on improving block confidence and low latency of parachain blocks. I have contributed across research, coordination, reviews and implementation.

### Research cross-session backing and availability

I have conducted deep research and proposed designs for improving cross-session block confidence, targeting availability and backing.
At the moment, parablocks that are pending availability are dropped when a session change occurs. Similarly, parablocks built on relay parents from a previous session are no longer eligible for backing in a new session. Both limitations are predictable reasons for periodic regressions in parachain block confidence.

I authored two design documents: [Cross-session availability](https://hackmd.io/NKUWBZC7Q8ipvg1FYibRzQ) and [Cross-session backing](https://hackmd.io/IIpnCvYXRtOhmcz-8luNhg),
which have been reviewed within the low-latency working group (which includes several fellows).

Initially, these two avenues were seen as low-hanging fruits, but my research and designs informed key planning and prioritisation decisions. We instead converged on implementing resubmissions as a solution (something which was already part of the low-latency roadmap). 

### Allowing older relay parents for parachain candidates

The core novelty introduced by the [low-latency design](https://github.com/paritytech/polkadot-sdk/pull/11413) is the decoupling between the relay parent of the parachain block (relay chain block which provides the execution context) and the scheduling parent (relay chain block which provides the scheduling and backing context).

In order to achieve perfect block confidence, a v3 candidate descriptor was introduced.
I contributed heavily to the implementation and review of v3 descriptor support.
I authored the runtime API support in [PR #11231](https://github.com/paritytech/polkadot-sdk/pull/11231), which introduces the `max_relay_parent_session_age` runtime API and host configuration field, determining how old a relay parent of a candidate can be.

I wrote the entire relay chain runtime support in [PR #11328](https://github.com/paritytech/polkadot-sdk/pull/11328), implementing the on-chain backing checks that admit candidates built on older relay parents and adding a runtime API for querying the needed information of historical relay parents for candidate validation.

I added support for older relay parents in prospective-parachains, the main subsystem responsible for coordinating backing work on the relay chain in [PR #11772](https://github.com/paritytech/polkadot-sdk/pull/11772), which also fixes a bug identified in statement-distribution handling of v3 candidates.

Beyond the relay-chain implementation, I led the root-cause investigation into the cumulus-side problems preventing older relay parents from working end-to-end. In a [detailed review on the v3 cumulus PR #10742](https://github.com/paritytech/polkadot-sdk/pull/10742#pullrequestreview-4043127470), I identified three distinct bugs in the collator parent-search logic — an `ancestry_lookback` mismatch when v3 is enabled, a missing best-hash parameter that causes attempts to fork already finalized blocks, and a session-boundary lag in `find_deepest_valid_parent` requiring scheduling-parent state to be tracked through the block-import path — and proposed (temporary) fixes in a [reference implementation commit](https://github.com/paritytech/polkadot-sdk/commit/a681cae1de94e3409a87b02de561deae6ee8e0ab). This investigation unblocked further cumulus work and was neccessary for end to end testing of v3 candidates with older relay parents.

Beyond these contributions, I have [conducted numerous reviews](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aalindima) and participated actively in design discussions. I am now leading the low-latency effort within Parity.

### Live incident response and post-mortem

On 2026-03-23, immediately following the 2.1.1 runtime upgrade enactment at 12:37 UTC, 5 of the 37 active parachains stalled block production. I led the full incident response: investigation, root-cause analysis, coordination with the affected parachain teams on patch backporting, and the [public postmortem](https://forum.polkadot.network/t/partial-polkadot-parachains-stall-on-runtime-upgrade-2-1-1-postmortem/17387).

The root cause was a SCALE codec compatibility violation in the deprecated `backing_state` runtime API: a stale data structure had been removed during cleanup and replaced with a non-backward-compatible variant, breaking collators on releases older than `stable2407`.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II  |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referenda available on the [Members](https://collectives.subsquare.io/fellowship/tracks/1) or [Proficient Members](https://collectives.subsquare.io/fellowship/tracks/2) tracks during this reporting period. |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
