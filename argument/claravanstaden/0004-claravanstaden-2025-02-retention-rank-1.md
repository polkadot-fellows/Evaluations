# Argument-0004: Retention at Rank I

|                 |                  |
| --------------- |------------------|
| **Report Date** | 2025-06-10       |
| **Submitted by**| Clara van Staden |


## Member details

- Matrix username: @claravanstaden:matrix.org
- Polkadot address: 12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8
- Current rank: 1
- Date of initial induction:  2024/06/17
- Date of last report: 2025-03-31
- Area(s) of Expertise/Interest: Snowbridge, XCM, Asset Hub, Bridge Hub

## Reporting period

- Start date: 2025/03/31
- End date: 2025/06/31

## Argument
During this reporting period, my contributions focused on three major development themes: Snowbridge V2, the Ethereum 
Electra upgrade, and ERC-20 token transfers to Kusama.

I was responsible for [addressing all issues](https://github.com/paritytech/polkadot-sdk/pull/8240) raised during the 
Snowbridge V2 audit. In addition, I implemented a new feature that allows users to [top up the reward](https://github.com/paritytech/polkadot-sdk/pull/8271) 
for their message if a relayer considers it unprofitable to relay. I'm currently working on [upgrading Polkadot and Kusama AssetHub from XCM v4 to v5](https://github.com/polkadot-fellows/runtimes/pull/753), a prerequisite for integrating the Snowbridge V2 pallets, which depend on XCM v5 functionality.

I also ensured a smooth transition for the Ethereum Electra hardfork, which went live on 7 May without any downtime or 
issues. Ahead of the upgrade, I submitted runtime upgrades for both [Polkadot BridgeHub](https://polkadot.polkassembly.io/referenda/1528) 
and [Kusama AssetHub](https://kusama.polkassembly.io/referenda/518), the latter to help the community resolve an unrelated issue.

In parallel, I worked on enabling ERC-20 transfers from Polkadot to Kusama. This included [registering ERC-20 
tokens as foreign assets on Kusama](https://polkadot.polkassembly.io/referenda/1498), writing [tests](https://github.com/polkadot-fellows/runtimes/pull/625) 
to validate transfer functionality, and building the supporting [API](https://github.com/Snowfork/snowbridge/pull/1463), 
[indexer](https://github.com/Snowfork/snowbridge-subsquid/pull/21), and [UI components](https://github.com/Snowfork/snowbridge-app/pull/94). 
This feature is now live in the [Snowbridge UI](https://app.snowbridge.network/kusama).

My core objective over the past three months has been to stabilize Snowbridge to ensure uninterrupted liquidity flow 
from Ethereum to Polkadot, secure and extend Snowbridge V2 (which brings new use cases and better UX to the Polkadot ecosystem), 
and enable ERC-20 bridging to Kusama to increase liquidity across the ecosystem.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                      | Comments |
|-------|---|---|-------------------------------------------------|---------|
| I     |90%   |N/A  | There were no referenda I was eligible to vote on. |         |
| II    |80%   |N/A   |                                                 |         |
| III   |70%   |100%  |                                                 |         |
| IV    |60%   |90%   |                                                 |         |
| V     |50%   |80%   |                                                 |         |
| VI    |40%   |70%   |                                                 |         |
