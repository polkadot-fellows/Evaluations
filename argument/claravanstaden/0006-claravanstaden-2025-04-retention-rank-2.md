# Argument-0006: Retention Rank II

|                 |                  |
| --------------- |------------------|
| **Report Date** | 2025-12-07       |
| **Submitted by**| Clara van Staden |


## Member details

- Matrix username: @claravanstaden:matrix.org
- Polkadot address: 12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8
- Current rank: 1
- Date of initial induction:  2024/06/17
- Date of last report: 2025-09-01
- Area(s) of Expertise/Interest: Snowbridge, XCM, Asset Hub, Bridge Hub

## Reporting period

- Start date: 2025-09-07
- End date: 2025-12-07

## Argument

In the last 3 months, my work has spanned technical contributions, application support on Snowbridge, as well as an expanded focus on Polkadot initiatives outside of Snowbridge.

### Snowbridge V2

Snowbridge V2, which brings major cost savings to bridge users, was released on-chain around middle October. I worked on off-chain support for Snowbridge V2, including the [Snowbridge TypeScript SDK](https://github.com/Snowfork/snowbridge/pull/1630), and [supporting Snowbridge V2](https://github.com/Snowfork/snowbridge-app/pull/179) in the Snowbridge app. Snowbridge V2 will be enabled for Ethereum <> AssetHub routes in the next week, realizing significant cost savings for users: ~50% reduction for Ethereum to Polkadot transfers and a ~75% reduction for Polkadot to Ethereum transfers. I also added [developer documentation](https://docs.snowbridge.network/developers/snowbridge-v2) for Snowbridge V2, wrote the [Snowbridge V2 release announcement](https://forum.polkadot.network/t/snowbridge-v2-is-live/15844) on the Polkadot Forum and gave an [overview of Snowbridge V2](https://www.youtube.com/watch?v=pGv5CmQnyWU&t=736s) at the Polkadot Builders Party.

### Ethereum Fusaka Upgrade

I was responsible for Ethereum Fusaka support on Snowbridge. This covered [on-chain version support](https://github.com/paritytech/polkadot-sdk/pull/9938), [off-chain relayer support](https://github.com/Snowfork/snowbridge/pull/1592), coordinating a [runtime release](https://github.com/polkadot-fellows/runtimes/pull/1013) and the [Polkadot system chain runtime upgrade](https://polkadot.polkassembly.io/referenda/1797) referendums. The Snowbridge Ethereum client switched over seamless on 3 Dec 2025.

### Polkadot Social Account Recovery

In an effort to expand my contributions in the ecosystem outside of Snowbridge, I have collaborated with Oliver Tale-Yazdi to work on social account recovery on Polkadot. I have created a [basic UI](https://github.com/claravanstaden/polkadot-social-account-recovery) to [demonstrate the functionality](https://polkadot-social-account-rec-git-e33270-claras-projects-d244fdee.vercel.app?_vercel_share=vAAX8QFav59xNOZYLI2VvNH5OefYVJZp) (backend to be completed).

### Incident Response and Recovery

#### Runtime Upgrade Problems

For the first time in Snowbridge's history on Polkadot mainnet, we had our first incident.
A member of our team noticed failing transactions on BridgeHub and alerted our team. I immediately realized what happened (that BridgeHub was not upgraded, while AssetHub was). I uploaded the BridgeHub runtime wasm 5 minutes after we discovered the outage, minimizing affected transactions. While the incident was regrettable, I believe it demonstrated my commitment and knowledge to maintain a high availability service. I was also responsible
for the [root cause incident report](https://forum.polkadot.network/t/snowbridge-incident-report-polkadot-runtime-upgrade-1-7-1/15144) and the [referendum](https://polkadot.polkassembly.io/referenda/1765) to correct the affected transactions.

#### Polkadot AssetHub migration

The Snowbridge and bridges team were both under the impression that Snowbridge would not
be affected by the AssetHub migration. A day before the migration, I realized that this
might not be the case. After further investigation from our team, we saw that Snowbridge 
would be affected by the migration, enabling us to make the necessary provisions to ensure
no user transactions are affected ([notifying our users](https://x.com/_snowbridge/status/1985319627803836585), putting the Snowbridge UI under maintenance mode, and notifying all our partners to do the same). This again shows a proactive response from my side to 
ensure user funds are protected.

### Conclusion

I believe my contributions these last 3 months are worthy of Rank II retention, and hope
you will favourably view my application.

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
