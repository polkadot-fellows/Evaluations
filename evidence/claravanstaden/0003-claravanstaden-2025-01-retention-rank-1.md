# Argument-0003: Retention at Rank I

|                 |                  |
| --------------- |------------------|
| **Report Date** | 2025-03-31       |
| **Submitted by**| Clara van Staden |


## Member details

- Matrix username: @claravanstaden:matrix.org
- Polkadot address: 12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8
- Current rank: 1
- Date of initial induction:  2024/06/17
- Date of last report: 2024/12/12
- Area(s) of Expertise/Interest: Snowbridge, XCM, Asset Hub, Bridge Hub


## Reporting period

- Start date: 2024/12/12
- End date: 2025/03/31

## Argument
During this reporting period, my contributions were primarily focused on development, with some involvement in content creation as well.

On the development side, most of my work centered around building the new [Snowbridge V2 inbound queue](https://github.com/paritytech/polkadot-sdk/pull/7402). I was responsible for developing the BridgeHub side (creating the new pallet, writing unit and integration tests) and the off-chain side ([E2E tests, off-chain relayer](https://github.com/Snowfork/snowbridge/pull/1341)).

Another major focus was preparing the Snowbridge Ethereum client for the Electra upgrade. This included [updating the light client protocol](https://github.com/paritytech/polkadot-sdk/pull/7075), as well as updating all [off-chain infrastructure](https://github.com/Snowfork/snowbridge/pull/1283) (relayers, E2E tests) to support the new protocol. The Electra updates were deployed to Westend and the hardfork was successfully tested on [Westend-Sepolia on 5 March](https://bridgehub-westend.subscan.io/event?page=1&time_dimension=date&module=ethereumbeaconclient).

I found a [bug in a macro](https://github.com/paritytech/polkadot-sdk/pull/7913) used for asserting event fields, used throughout emulated tests. This bug could potentially mask issues in our test suite. I have fixed the bug and am busy updating the tests with the correct values.

On the content side, I made sure Snowbridge had a consistent voice on X. I wrote all the [Snowbridge X account posts](https://x.com/_snowbridge) over the past quarter, and also shared a longer [update on the Polkadot Forum](https://forum.polkadot.network/t/snowbridge-march-2025-update/12307) summarizing recent progress.

These contributions help ensure that Snowbridge — and by extension, Polkadot — is a secure, up-to-date, and user-friendly bridge for Ethereum interoperability. At the same time, increasing visibility through consistent communication helps educate the community and drive adoption.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities                                            | Comments |
|---|---|---|-----------------------------------------------------------------------|---|
|III|70%   |100%  | I have voted on 0 out of 1 referenda in which I was eligible to vote. |*I missed referenda https://collectives.subsquare.io/fellowship/referenda/301 but believe this is permissible since this referenda was invalid.* |
|I  |90%   |N/A   |                                                                       |  |
|II |80%   |N/A   |                                                                       |  |
|III|70%   |100%  |                                                                       |  |
|IV |60%   |90%   |                                                                       |  |
|V  |50%   |80%   |                                                                       |  |
|VI |40%   |70%   |                                                                       |  |
