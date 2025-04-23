 # Argument-0005: Retention at Rank II

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2025/04/22 |
| **Submitted by** | skunert    |


## Member details

- Matrix username: `@sebastian:parity.io`
- Polkadot address: `1682A5hxfiS1Kn1jrUnMYv14T9EuEnsgnBbujGfYbeEbSK3w`
- Current rank: 2
- Date of initial induction: 2024/01/08
- Date of last report: 2025/01/30
- Area(s) of Expertise/Interest: `Cumulus Node`, `Substrate Node`, `Parachain Authoring`, `Weight`

## Reporting period

- Start date: 2025/01/30
- End date: 2025/04/30

## Argument

During this reporting period I worked primarily on two improvements to parachain authoring:

1. **Stabilization of the slot-based collator ([PR](https://github.com/paritytech/polkadot-sdk/pull/7569)):** I introduced the slot-based collator last year into cumulus as an alternative to the lookahead collator, which is used for asynchronous backing chains. The first version implemented in `polkadot-sdk` could author on multiple cores faster than 6s. However, this initial version relied entirely on slot times for timing. Consequently, parachain teams wanting 2s block times needed 2s slot durations. In the second iteration, I reworked the collator to support operating at slot times of 6s or larger while still maintaining a lower block cadence. This work is finished and part of the `stable-2503` release of polkadot-sdk.
   This provides the following benefits for parachains:
   - Improved censorship resistance through larger slot times. Smaller slots cause faster rotation through the author set, allowing a single author who doesn't announce blocks to potentially censor all authors in the coming 12s (due to relay chain block recovery time).
   - More dynamic adjustment of core numbers. With 6s slots and 3 cores, for example, we achieve a 2s per block cadence. If a parachain team needs to scale down, they can remove cores to dynamically produce fewer blocks without skipping authors as in the previous short-slot variant.
   - Groundwork for future optimizations that minimize wasted time on import operations by enabling back-to-back block authoring on a single collator.

2. **Parachain fork management ([issue](https://github.com/paritytech/polkadot-sdk/issues/7780), [PR](https://github.com/paritytech/polkadot-sdk/pull/8299)):** The lookahead collator previously produced blocks on all relay chain forks. With elastic-scaling and multiple cores, we no longer have enough time for this approach. Instead, we now select the current best block of the relay chain as our best block. The drawback is potential selection of a fork that may later be abandoned. While this should occur infrequently, when it does happen it creates a parachain fork, negatively affecting throughput and latency. I'm developing a solution that allows parachains to choose relay parents with a fixed offset. By avoiding tip-of-chain relay parents, we can assume that forks have already settled. This mechanism includes a runtime-side implementation to verify that malicious authors are unable to build at the tip. Authors are forced to supply a chain of descendants to the parachain runtime, which will prevent authoring at the tip. This work is currently at an advanced stage, but not yet finished.

Beyond these primary projects, I'm managing efforts to improve [omni-node functionality](https://github.com/orgs/paritytech/projects/157) and consult and review on the [fork-aware transactionpool](https://github.com/orgs/paritytech/projects/156/views/6?sliceBy%5BcolumnId%5D=Status&sliceBy%5Bvalue%5D=Todo).

Additionally, I provided code reviews on `polkadot-sdk` and the `runtimes` repository:
- Runtime PRs (4): [list](https://github.com/polkadot-fellows/runtimes/pulls?q=is:pr++reviewed-by:skunert+created:2025-01-30..2025-04-30+)
- polkadot-sdk PRs (41): [list](https://github.com/paritytech/polkadot-sdk/pulls?q=is:pr+reviewed-by:skunert+created:2025-01-30..2025-04-30+)

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
