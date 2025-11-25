# Argument-0005: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/11/24                                                                                   |
| **Submitted by**| Daniel Shiposha                                                                             |


## Member details

- Matrix username: `@mrshiposha:matrix.org`
- Polkadot address: `14aC2hfNZTX4sMHPh47MjGB4Vr4rVYHZgBid54vRKrZVBZQY`
- Current rank: Rank I
- Date of initial induction: 2024/12/11
- Date of last report: 2025/08/25
- Area(s) of Expertise/Interest: XCM, NFT


## Reporting period

- Start date: 2025/09/29
- End date: 2025/12/20

## Argument

During the reporting period I focused my attention around XCM refactoring to make XCM more easily upgradable (without huge amount of copy-pasting) to new version**s**.
This activity should eventually resolve the corresponding issue https://github.com/paritytech/polkadot-sdk/issues/7095.

I initially started by picking up [the existing work done by Bryan Chen](https://github.com/paritytech/polkadot-sdk/pull/7123) and [tried](https://github.com/UniqueNetwork/polkadot-sdk/commit/bacb61bca1fdfa8432746bcf8e9a2b4e937c06f9) to finish it.
But it became clear that this approach demands a lot of changes accross all the Polkadot SDK.

So, I decided to find an alternative (but similar) approach to minimize the changes in the SDK and contain them purely within `polkadot/xcm`.

I came up with a proc-macro approach which should:
* help us generate most of the conversion logic automatically
* provide a clear instruction definition in one place
* maintain Bryan's idea of having instructions as individual structs so we can implement their execution logic separately (as well as test them that way)
  * the individual structs should also allow us to implement special conversions granularly, without implementing the trivial ones by hand
* provide good enough balance between clarity and automation

For details see [this gist](https://gist.github.com/mrshiposha/9454dab3362c5d56dc067e2c7730640d) with a commented example of how the usage of the `#[versioned]` proc-macro might look like.
You can see an early implementation draft here: https://github.com/UniqueNetwork/polkadot-sdk/tree/xcm-refactor.
Note that this is WIP and may change in the future.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   | There were no referenda I was eligible to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
