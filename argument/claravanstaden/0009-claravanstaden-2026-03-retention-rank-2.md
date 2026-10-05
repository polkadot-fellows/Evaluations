# Argument-0009: Retention at Rank II

|                  | Clara van Staden |
| ---------------- | ---------------- |
| **Report date**  | 2026-09-16       |
| **Submitted by** | Clara van Staden |

## Member details

* **Matrix username:** @claravanstaden:matrix.org
* **Polkadot address:** 12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8
* **Current rank:** II
* **Date of initial induction:** 2024-06-17
* **Date of last report:** 2026-06-17
* **Areas of expertise and interest:** Snowbridge, XCM, Asset Hub, Bridge Hub

## Reporting period

* **Start date:** 2026-06-17
* **End date:** 2026-09-16

## Argument

During this reporting period, my focus shifted from primarily hands-on software development towards protocol specifications, design reviews, and broadening my knowledge of the Polkadot protocol. Alongside this work, I continued contributing to Snowbridge and cross-ecosystem bridge tooling.

### RFCs

I completed the remaining changes requested during the review of [RFC-0166: Snowbridge Emergency Pause](https://github.com/polkadot-fellows/RFCs/pull/166), including clarifying how the pause applies to the Ethereum-to-Polkadot direction, which does not pass through the Message Queue pallet. The RFC subsequently passed an [on-chain vote](https://collectives.subsquare.io/fellowship/referenda/605) and was merged.

I also made substantial revisions to [RFC-0167: Snowbridge Circuit Breaker](https://github.com/polkadot-fellows/RFCs/pull/167) in response to review feedback. The design was changed from tracking net flows to tracking gross flows, and from enforcing a fixed hard cap to using a refilling circuit-breaker model. These changes make the mechanism better suited to limiting abnormal bridge activity without unnecessarily constraining normal usage.

### Polkadot–Kusama bridge support

Following a community request, I added end-to-end support for Polkadot–Kusama transfers to the Snowbridge dApp, including updating the SDK to use the new bridge interfaces ([snowbridge-app#270](https://github.com/Snowfork/snowbridge-app/pull/270), [#271](https://github.com/Snowfork/snowbridge-app/pull/271)). I also completed the required indexer support and hardened it to safely handle transfers submitted through third-party UIs with XCM layouts outside Snowbridge’s control ([snowbridge-subsquid#125](https://github.com/Snowfork/snowbridge-subsquid/pull/125), [#133](https://github.com/Snowfork/snowbridge-subsquid/pull/133)).

### Emergency governance tooling

I completed the verification workflow for Snowbridge’s emergency halt and resume calls. The preimages are now tested through the Polkadot Ecosystem Tests, and the dApp verifies its generated preimages against recent reference bytes ([snowbridge-app#260](https://github.com/Snowfork/snowbridge-app/pull/260), [#267](https://github.com/Snowfork/snowbridge-app/pull/267)). This provides assurance that emergency governance calls are current and correctly encoded.

### Ethereum Gloas hard fork

I reviewed the implementation of support for the upcoming [Ethereum Gloas hard fork](https://github.com/paritytech/polkadot-sdk/pull/13122), with particular attention to its implications for Snowbridge and the Ethereum light client.

### Speculative Messaging

I participated in the ongoing design of the Speculative Messaging protocol by attending design meetings and reviewing the proof-of-concept implementation and associated design documents. This work has helped me develop a deeper understanding of the proposed protocol and contribute feedback as the design evolves.

### Conclusion

Although this reporting period included less hands-on development than previous quarters, I continued to make substantive contributions across protocol design, Fellowship RFCs, cross-ecosystem bridge support, emergency governance tooling, and technical review.

My work on the Snowbridge emergency-pause and circuit-breaker RFCs helped move operational safety mechanisms towards adoption, while my implementation work completed and hardened end-to-end Polkadot–Kusama bridge support. At the same time, my involvement in Speculative Messaging and the Gloas review has broadened my contribution beyond Snowbridge implementation work into protocol design and review.

I believe these contributions demonstrate continued active participation at Rank II and support my retention at this rank.

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
