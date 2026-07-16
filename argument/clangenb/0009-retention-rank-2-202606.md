# Argument-0009: Retention at Rank 2

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2026/06/25) |
| **Submitted by**| Christian Langenbacher          |


## Member details

- Matrix username: `@clang:matrix.org`
- Polkadot address: `16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3`
- Current rank: `2`
- Date of initial induction: `2024/03/27`
- Date of last report: `2026/03/25`
- Link to last report: [0008 Retention at Rank II](https://collectives.subsquare.io/fellowship/members/16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3/evidences/8549237-3)
- Area(s) of Expertise/Interest: `Parachain Builder, Runtime, Clients`


## Reporting period

- Start date: 2026/03/25
- End date: 2026/06/25


## Argument

My argument primarily revolves around PRs and issues that I filed in the Polkadot SDK and
Runtimes repositories.

### Finalizing the Penpal Asset Management revamp

In my last report I described the in-progress revamp that establishes PEN as Penpal's
first-class native token while treating DOT as a foreign asset
([polkadot-sdk#10726](https://github.com/paritytech/polkadot-sdk/pull/10726)). 

Over this period I [brought](https://github.com/polkadot-fellows/runtimes/pull/1167) that work to completion
and propagated it into the Runtimes repository's integration tests: Each affected test
spans multiple chains (Asset Hub Westend/Rococo, Bridge Hub Westend/Rococo) and had to be
reviewed individually to ensure invariants and coverage were preserved. The changes mirror the
polkadot-sdk integration-test changes one-to-one, so no surprises were found: the original PSDK
design ported over cleanly and required no rework.

Insights from the above work inspired me to make a minor [refactoring PR](https://github.com/paritytech/polkadot-sdk/pull/12003)
to centralize some helper functions upstream, which was very swiftly followed up by bkontur to propagate them to the
Runtimes repository in the next release.

A minor issue was found after the first Asset Management revamp. The Penpal genesis presets failed to build in production due
to the ED not being respected (pre-existing bug). I [future-proofed](https://github.com/paritytech/polkadot-sdk/pull/11575) a fix by adding preset 
unit tests making sure that the genesis presets always build to prevent annoyances in production. 

### Triaging and reducing the Runtimes TODO backlog

The Runtimes repository carries a long-standing
[tracking issue for TODOs and leftovers](https://github.com/polkadot-fellows/runtimes/issues/696).
I picked this up and produced a
[full triage](https://github.com/polkadot-fellows/runtimes/issues/696#issuecomment-4787936619) of
every `TODO`/`FIXME` marker in the codebase: 56 markers in total, of which 21 carried no tracking
reference and 27 seemed actionable at first glance, showing the value of categorizing, triaging and
tracking them more systematically.

I went ahead and addressed some of those (PRs still pending merge) by simply switching to PSDK upstream code ([#1213](https://github.com/polkadot-fellows/runtimes/pull/1213), [#1214](https://github.com/polkadot-fellows/runtimes/pull/1214), [#1217](https://github.com/polkadot-fellows/runtimes/pull/1217)), and
investigating and fixing an old failing test [#1216](https://github.com/polkadot-fellows/runtimes/pull/1216).
 
I also proposed a lightweight CI check that requires every `TODO`/`FIXME` to carry a tracking-issue reference on the same line to prevent future build-up of hidden TODOs.

### Additional contributions

I remained involved in
[7 Polkadot SDK issues](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue%20involves%3Aclangenb%20updated%3A2026-03-25..2026-06-24)
and [7 Runtimes issues](https://github.com/polkadot-fellows/runtimes/issues?q=is%3Aissue%20involves%3Aclangenb%20updated%3A2026-03-25..2026-06-24)
over the period, and continued to assist community members with technical questions in the
Fellowship and ecosystem Element channels.

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|------|----------------------|----------------------|----------------------------|----------|
| I    | 90%                  | N/A                  |                            |          |
| II   | 80%                  | N/A                  | No eligible referenda      |          |
| III  | 70%                  | 100%                 |                            |          |
| IV   | 60%                  | 90%                  |                            |          |
| V    | 50%                  | 80%                  |                            |          |
| VI   | 40%                  | 70%                  |                            |          |


## Misc

- [ ] Question(s):
- [ ] Concern(s):
- [ ] Comment(s):
