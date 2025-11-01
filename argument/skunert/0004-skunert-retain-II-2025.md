# Evidence-0004: Retention at Rank II

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2025/01/30 |
| **Submitted by** | skunert    |


## Member details

- Matrix username: `@sebastian:parity.io`
- Polkadot address: `1682A5hxfiS1Kn1jrUnMYv14T9EuEnsgnBbujGfYbeEbSK3w`
- Current rank: 2
- Date of initial induction: 2024/01/08
- Date of last report: 2024/10/28
- Area(s) of Expertise/Interest: `Cumulus Node`, `Substrate Node`, `Parachain Authoring`, `Weight`

## Reporting period

- Start date: 2024/10/30
- End date: 2025/01/30

## Evidence

I worked mostly on improvements to Cumulus and the stabilization of parachain authoring for elastic scaling. This includes the following work:

- Improvements in how parachains track the number of authored blocks per relay-chain block, the velocity of a parachain. This was previously tracked in parachain blocks. This was fine for asynchronous backing where the relay chain and parachain slot duration is the same. For elastic scaling parachains, we can make fewer assumptions about the slot duration, since blocks can be authored at any cadence. I implemented the change in [#6825](https://github.com/paritytech/polkadot-sdk/pull/6825) and [#7205](https://github.com/paritytech/polkadot-sdk/pull/7205).
- Unification of lookahead collator and slot-based collator codepaths. This is an attempt to unify the currently disjoint codepaths. The different implementations lead to an increased maintenance burden with no benefit. This is in progress and a draft of the refactoring is available at [#7326](https://github.com/paritytech/polkadot-sdk/pull/7326).
- Support for multiple parachain blocks in one AURA slot on elastic-scaling enabled chains. The goal is to have one author produce multiple blocks before yielding to the next collator. This gives other network participants more time to fetch blocks from the relay chain using the PoV-recovery mechanism. A prototype of this exists but is work in progress.

In addition, I am involved in the [fork-aware transaction pool project](https://github.com/orgs/paritytech/projects/156/views/6). This work includes multiple sparring meetings and discussions as well as prioritization of future issues. This also includes reviews of several non-trivial pull requests ([#6104](https://github.com/paritytech/polkadot-sdk/issues/6104), [#6405](https://github.com/paritytech/polkadot-sdk/issues/6405), [#6647](https://github.com/paritytech/polkadot-sdk/issues/6647), [#7316](https://github.com/paritytech/polkadot-sdk/issues/7316), [#7102](https://github.com/paritytech/polkadot-sdk/issues/7102)) and discussions about the design of the future transaction protocol. The new transaction pool will tackle problems that arose with the decreased block times with asynchronous backing and now elastic-scaling. The goal is to eliminate empty blocks, stuck transactions and deliver full throughput at all times.

I invested a significant amount of time in reviews:

- Reviewed runtime PRs (7) [list](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr++reviewed-by%3Askunert+created%3A2024-10-30..2025-01-30+)
- Reviewed polkadot-sdk PRs (41) [list](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Askunert+created%3A2024-10-30..2025-01-30+)

## Voting record

*Provide your voting record in relation to required thresholds for your rank.* 

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments                      |
| ----- | ------------------- | -------------------- | -------------------------- | ----------------------------- |
| III   | 70%                 | N/A                  |                            |                               |
| I     | 90%                 | N/A                  |                            | There was nothing to vote on. |
| II    | 80%                 | N/A                  |                            | There was nothing to vote on. |
| III   | 70%                 | N/A                  |                            |                               |
| IV    | 60%                 | N/A                  |                            |                               |
| V     | 50%                 | N/A                  |                            |                               |
| VI    | 40%                 | N/A                  |                            |                               |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
