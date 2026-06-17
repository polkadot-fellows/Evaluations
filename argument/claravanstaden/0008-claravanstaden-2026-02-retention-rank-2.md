# Argument-0008: Retention at Rank II

|                 |                  |
| --------------- |------------------|
| **Report Date** | 2026-06-17       |
| **Submitted by**| Clara van Staden |


## Member details

- Matrix username: @claravanstaden:matrix.org
- Polkadot address: 12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8
- Current rank: 2
- Date of initial induction:  2024/06/17
- Date of last report: 2026-03-19
- Area(s) of Expertise/Interest: Snowbridge, XCM, Asset Hub, Bridge Hub


## Reporting period

- Start date: 2026/03/19
- End date: 2026/06/17


## Argument

The last few months I have been focused on mainly on Snowbridge security hardening, which seems fitting at a time where bridge hacks are at a high and AI tools become more proficient at surfacing security issues.

### Snowbridge Security Hardening

After a Snowbridge false security alarm in May, we realized that our processes in case of an emergency need improvement. We have a CLI tool to generate the halt bridge preimage, but we realized it is too slow and cumbersome in an emergency situation. I automated the halt bridge preimage and call submission, which is now
available on the Snowbridge dApp on a [dedicated page (Menu dropdown -> Governance)](https://github.com/Snowfork/snowbridge-app/pull/250). The Snowbridge SDK supports [generating this preimage](https://github.com/Snowfork/snowbridge/pull/1787). Additionally, I am working on an extension to verify the preimage bytes are valid and that it matches what has been tested against the [Polkadot Ecosystem tests](https://github.com/Snowfork/snowbridge/pull/1796), to prove it has not been tampered with. I also updated our [emergency procedure process](https://docs.snowbridge.network/resources/emergency-procedures) documentation, so that we have clear steps to follow in a high-stakes, emergency situation.

I also implemented a couple of security hardening improvements ([PR11856](https://github.com/paritytech/polkadot-sdk/pull/11856), [PR10793](https://github.com/paritytech/polkadot-sdk/pull/10793)) and in the on-chain code, surfaced through bug bountry reports, as well as fixed some bugs ([PR10952](https://github.com/paritytech/polkadot-sdk/pull/10952), [PR11919](https://github.com/paritytech/polkadot-sdk/pull/11919))

In the same vein, I have contributed two RFCs related to Snowbridge reactive and proactive security - one to implement a permissionless bridge halt ([RFC-0166: Snowbridge Emergency Pause](https://github.com/polkadot-fellows/RFCs/pull/166)), given a sizeable DOT deposit and one to implement a circuit breaker on unusual move of funds ([RFC-0167: Snowbridge Circuit Breaker
](https://github.com/polkadot-fellows/RFCs/pull/167)).

### Speculative Messaging

As part of a drive to work on Polkadot core protocol besides Snowbridge, I am going to contribute to the speculative messaging implementation. I have been attending design meetings and working through the spec with the Parity in preparation to contribute.

### Code Reviews

During this period I reviewed 40+ PRs across the ecosystem.

### Conclusion

In this period, I've focused more on ensuring what Polkadot has is secure, having seen first hand how damaging breaches can be to the ecosystem's reputation. I believe my contributions meet the requirement for sustaining rank II.

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
