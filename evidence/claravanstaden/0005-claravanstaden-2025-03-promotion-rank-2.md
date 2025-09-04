# Argument-0005: Promotion to Rank II

|                 |                  |
| --------------- |------------------|
| **Report Date** | 2025-09-01       |
| **Submitted by**| Clara van Staden |


## Member details

- Matrix username: @claravanstaden:matrix.org
- Polkadot address: 12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8
- Current rank: 1
- Date of initial induction:  2024/06/17
- Date of last report: 2025-06-10
- Area(s) of Expertise/Interest: Snowbridge, XCM, Asset Hub, Bridge Hub

## Reporting period

- Start date: 2024/06/17
- End date: 2025/09/01

## Argument

Over the past year in the Polkadot Fellowship, I have consistently contributed to the Polkadot core ecosystem. I would 
therefore like to apply for promotion to Rank II. Weighing the requirements of Rank II responsibility against my 
contributions this last year, I believe have completed all the requirements.

I have been working on Polkadot full-time since 2021, authored an [article](https://medium.com/snowbridge/the-evolution-of-snowbridges-ethereum-light-client-an-engineering-journey-65e08db0825d) 
on the Ethereum client of Snowbridge, and contributed extensively to Snowbridge V2, where I am the primary author of the new [Inbound Queue V2 pallet](https://github.com/paritytech/polkadot-sdk/tree/master/bridges/snowbridge/pallets/inbound-queue-v2).

### Snowbridge V2

My primary contribution this year has been Snowbridge V2, which is part of the Polkadot SDK. I authored the [Inbound Queue V2](https://github.com/paritytech/polkadot-sdk/pull/7402), 
enabling users on Ethereum to send arbitrary XCM messages for execution on Polkadot. I also completed the off-chain
components required for Snowbridge V2 in the Ethereum -> Polkadot direction, including the [relayers](https://github.com/Snowfork/snowbridge/pull/1341) and [SDK](https://github.com/Snowfork/snowbridge/pull/1540).

I also implemented a 
[mechanism](https://github.com/paritytech/polkadot-sdk/pull/8271) allowing unprofitable messages to be topped up with a 
tip, ensuring they can still be relayed. Together, these features make Snowbridge V2 more flexible, cost-efficient, and 
open to a broader set of use cases.

### Ethereum Electra Upgrade

I independently managed the Ethereum Electra upgrade, which spanned 
[on-chain changes](https://github.com/paritytech/polkadot-sdk/pull/7075), [off-chain relayers, infrastructure](https://github.com/Snowfork/snowbridge/pull/1283), 
and the [referenda](https://polkadot.polkassembly.io/referenda/1528) required to upgrade Bridge Hub.

This effort also included liaising directly with Ethereum core developers to coordinate upgrade timing across Electra 
testnets and mainnet, ensuring sufficient time to pass the relevant Polkadot referendum before the hard fork. 
In addition, I have 
[actively advocated](https://ethereum-magicians.org/t/soliciting-stakeholder-feedback-on-glamsterdam-headliners/24885/3?u=claravan...) 
for Ethereum improvements that directly benefit Snowbridge.

### XCM Upgrade

I completed the [XCM v4 → v5 runtime upgrade](https://github.com/polkadot-fellows/runtimes/pull/753) across Polkadot and 
Kusama Asset Hub and Bridge Hub. This work will enable the 
ecosystem to adopt new XCM v5 capabilities.

### Polkadot ↔ Kusama Bridge

I delivered support for bridging ERC-20 tokens between Polkadot and Kusama. This included creating the [referendum](https://polkadot.polkassembly.io/referenda/1498) to 
register assets on Kusama Asset Hub, writing [integration tests](https://github.com/polkadot-fellows/runtimes/pull/625), 
building the [UI](https://github.com/Snowfork/snowbridge-app/pull/94) for token transfers, and enhancing the Snowbridge 
[indexer](https://github.com/Snowfork/snowbridge-subsquid/pull/21) service to track these transactions. This feature is live in the 
[Snowbridge UI](https://app.snowbridge.network/kusama).

### Ecosystem Integration

I have been recently working with NeuroWeb to [support bridging](https://github.com/Snowfork/snowbridge/pull/1552) of their TRAC token from Ethereum through Polkadot Asset 
Hub to their parachain.

### Community Outreach

Beyond engineering, I have also contributed to community visibility by managing the 
[Snowbridge account on X](https://x.com/_snowbridge), sharing updates, and engaging with the wider ecosystem.

### Conclusion

My work over the past year demonstrates both breadth and depth of technical expertise across the ecosystem. I have 
consistently taken ownership of critical tasks, maintained a high level of visibility and reliability, and contributed 
to the success of Polkadot’s cross-chain infrastructure.

I believe these contributions align strongly with the responsibilities of Rank II, and I respectfully request your 
consideration for promotion.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                               | Comments |
|-------|---|---|----------------------------------------------------------|---------|
| I     |90%   |N/A  | There were no valid referenda I was eligible to vote on. |         |
| II    |80%   |N/A   |                                                          |         |
| III   |70%   |100%  |                                                          |         |
| IV    |60%   |90%   |                                                          |         |
| V     |50%   |80%   |                                                          |         |
| VI    |40%   |70%   |                                                          |         |
