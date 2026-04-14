# Argument-0007: Retention at Rank II

|                 |                  |
| --------------- |------------------|
| **Report Date** | 2026-03-19       |
| **Submitted by**| Clara van Staden |


## Member details

- Matrix username: @claravanstaden:matrix.org
- Polkadot address: 12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8
- Current rank: 2
- Date of initial induction:  2024/06/17
- Date of last report: 2025-12-07
- Area(s) of Expertise/Interest: Snowbridge, XCM, Asset Hub, Bridge Hub


## Reporting period

- Start date: 2025/12/07
- End date: 2026/03/19


## Argument

The key themes of the last 3 months have been operational efficiency and keeping Snowbridge secure. My contributions have spanned Snowbridge V2 off-chain work and parachain integration, relayer infrastructure optimization, security triage and active code review across the Snowbridge and Polkadot ecosystem,
as well as continuing to work on the Polkadot social recovery demo app, to expand my contributions outside of Snowbridge.

### Relayer Decentralization

A key initiative this period has been the [optimization of the Snowbridge relayer infrastructure](https://github.com/Snowfork/snowbridge/pull/1696). 
The main optimisation of this work has been to reduce the amount of compute required to run relayers, reducing the compute costs required by 4x.
This gain came from adding a relayer service that only downloads beacon states and computes proofs, optimistically. Another key enhancement was
removing the brittle relayer round-robin code, replaced with more aggressive checks of what is on-chain and improved strategies.
Supporting this effort, I Dockerized the relayer setup, with [updated docs](https://docs.snowbridge.network/resources/run-relayers) on how to deploy and run them.

### Snowbridge V2

Following the Snowbridge V2 launch in October 2025, I have been focused on stabilizing the V2 off-chain components and testing V2 integration with parachains ([Acala, Hydration](https://github.com/Snowfork/snowbridge/pull/1716)).

### Snowbridge dApp

Together with Vincent Geddes, we shipped multiple improvements including [V2 UI improvements](https://github.com/Snowfork/snowbridge-app/pull/194), [DOT as V2 fee](https://github.com/Snowfork/snowbridge-app/pull/206), [USD price display fixes](https://github.com/Snowfork/snowbridge-app/pull/204), [source and destination account fixes](https://github.com/Snowfork/snowbridge-app/pull/200), and [history display improvements](https://github.com/Snowfork/snowbridge-app/pull/198). These updates refined the overall user experience and makes the Snowbridge dApp comparable with widely used interfaces like Uniswap.

### Security

During this reporting period, I triaged 29 bug bounty reports on Hackenproof and [fixed one minor](https://github.com/paritytech/polkadot-sdk/pull/10793) issue as a result.

### Code Review and Ecosystem Stewardship

During this period, I reviewed over 60 PRs across the Snowbridge, polkadot-sdk, polkadot-fellows/runtimes, and Snowbridge indexer repositories.

### Polkadot Social Account Recovery

Outside of Snowbridge, I continued work on the [Polkadot Social Account Recovery](https://github.com/claravanstaden/polkadot-social-account-recovery) project, [migrating to PAPI and integrating view functions](https://github.com/claravanstaden/polkadot-social-account-recovery/pull/1), keeping the project aligned with the latest Polkadot tooling. I also did a couple of in-depth review rounds of the recovery pallet changes in the Polkadot SDK.

### Conclusion

This period has been focused on hardening Snowbridge's production infrastructure, extending V2 to more parachains, and driving relayer decentralization — all critical for the long-term sustainability and trustlessness of the bridge. I have also maintained an active review presence across the ecosystem. I believe these contributions are worthy of Rank II retention.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                               | Comments |
|-------|---------------------|----------------------|----------------------------------------------------------|----------|
| I     | 90%                 | N/A                  |                                                          |          |
| II    | 80%                 | N/A                  | There were no valid referenda I was eligible to vote on. |          |
| III   |70%   |100%  |                                                          |         |
| IV    |60%   |90%   |                                                          |         |
| V     |50%   |80%   |                                                          |         |
| VI    |40%   |70%   |                                                          |         |
