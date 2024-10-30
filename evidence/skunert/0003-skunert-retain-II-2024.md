# Evidence-0003: Retention at Rank II

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2024/10/28 |
| **Submitted by** | skunert    |


## Member details

- Matrix username: `@sebastian:parity.io`
- Polkadot address: `1682A5hxfiS1Kn1jrUnMYv14T9EuEnsgnBbujGfYbeEbSK3w`
- Current rank: 2
- Date of initial induction: 2024/01/08
- Date of last report: 2024/07/29
- Area(s) of Expertise/Interest: `Cumulus Node`, `Substrate Node`, `Parachain Authoring`, `Weight`


## Reporting period

- Start date: 2024/08/24
- End date: 2024/10/24


## Evidence

### Proof weight hardening

During this reporting period I focused on the hardening of our proof weight system. Earlier this year we identified two issues with the way we handle proof size weight:

1. [#5229](https://github.com/paritytech/polkadot-sdk/issues/5229): Since PoV-reclaim only monitors `SignedExtensions` post-dispatch hook, it was missing trie accesses that occured in pre-dispatch hooks. Together with unbenchmarked extrinsic base  weights on parachains, this can lead to an underestimation of proof weight.
2. [#6020](https://github.com/paritytech/polkadot-sdk/issues/6020): Both our benchmarking code and PoV-reclaim do currently not account for storage accesses that happen during the storage root calculation in `finalize_block`.

I worked on a quick fix to alleviate the impact of #5229 ([#5281](https://github.com/paritytech/polkadot-sdk/pull/5281), [#5257](https://github.com/paritytech/polkadot-sdk/pull/5257)). However, proper hardening of the proof weight includes multiple steps, one of which is to integrate overhead benchmarking into the `frame-omni-bencher` in polkadot-sdk. Before, benchmarking block overhead and extrinsic base weight was not supported for parachains at all. I worked on identifying the requirements and came up with the design in [#5303](https://github.com/paritytech/polkadot-sdk/issues/5303). Then I implemented the proposed changes, leading to [#5891](https://github.com/paritytech/polkadot-sdk/pull/5891).

### Slot-based collator

Another workstream has been the continuation of the slot-based collator improvements [#6066](https://github.com/paritytech/polkadot-sdk/pull/6066). The MVP is in place and works for elastic scaling chains which want to produce blocks at fixed intervals, with one block per slot.
However, the slot-based collator should aim to fully replace our existing collator implementations with the following improvements:

- Simplified modification of block production timings and conditions
- Introduction of a slot-based collator variant that is behaviour-compatible with the lookahead collator.
- Implementation of multi-block authoring support per parachain slot

Work on this has started but is not yet presentable.

### Support

I invested time in supportive work:

- Sparred with Michal on the fork-aware transaction pool and spent a significant amount of time on its review [#4639](https://github.com/paritytech/polkadot-sdk/pull/4639)
- Reviewed fellowship RFC [#103](https://github.com/polkadot-fellows/RFCs/pull/103)
- Reviewed runtime PRs (3) [list](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr++reviewed-by%3Askunert+created%3A2024-07-30..2024-10-30+)
- Reviewed polkadot-sdk PRs (69) [list](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Askunert+created%3A2024-07-30..2024-10-30+)

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
