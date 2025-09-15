# Argument-0005: Promotion to Rank 2

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2025/09/15) |
| **Submitted by**| Christian Langenbacher          |


## Member details

- Matrix username: `@clang:matrix.org`
- Polkadot address: `16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3`
- Current rank: `1`
- Date of initial induction: `2024/03/27`
- Date of last report: `2025/07/11`
- Area(s) of Expertise/Interest: `Parachain Builder, Runtime, Clients`


## Reporting period

- Start date: 2025/07/11
- End date: 2025/09/15

## Argument
Over the last 18 months, I have been continuing growing my knowledge about the Polkadot-SDK. As a core maintainer of three Ecosystem Projects, Encointer, Integritee, and Ajuna, I keep getting knowledge and hands-on experience with the Polkadot-SDK also outside the contributions that are considered valid for the fellowship.

First, I list the arguments for this reporting period, and then I will expand on the broader perspective, why I believe that I may climb up the rank ladder of the fellowship.

### XCM

#### Remote XCM V5 Transfer
I have [implemented an abstraction](https://github.com/paritytech/polkadot-sdk/pull/9173) to remotely execute asset transfers on behalf of some account's representation on another chain. This is a novel feature, which was made possible with XCM V5. It is useful for any pallet that needs flexible cross-chain fund management. Some treasuries have already been using a similar abstraction, but they were limited to a single account representation on the other chain. I have made this implementation more generic, and the treasuries simply call into my generic version.

#### XCM Docs
I have gotten a lot of experience with XCM in my ecosystem projects, e.g., [bridging TEER from Kusama to Polkadot](https://github.com/integritee-network/parachain/pull/325), [autoswap relay token for TEER in XCM execution](https://github.com/integritee-network/parachain/issues/329), [allowing Encointer to remotely spend treasuries' funds on Asset Hub](https://github.com/polkadot-fellows/runtimes/pull/679), and the implementation in the previous section. Hence, I thought I can return this growth in knowledge to the community by writing up some documentation. I have [added a comprehensive XCM example](https://github.com/paritytech/polkadot-sdk/pull/9609) showing how to configure a runtime to:
1. Have other chains register their native token as a foreign asset on a chain.
2. Set up asset conversion pools between those foreign tokens and the native token of the asset chain.
3. How to set up XCM to autoswap foreign assets for native assets to pay for XCM execution fees.
4. Finally, condensed the whole onchain flow into a nice to read test, showing exactly which dispatchables need to be called in which order, and what kind of events are to be expected.

### Requirements for promotion

1. How I formalized, implemented, or made an analytical improvement of "a major component of the protocol":
    * I would consider that the implementation of the XCM abstraction above falls into this category.
2. How I have published a "long-form semi-technical article"
   * I have [presented](https://www.youtube.com/watch?v=Thf23T_tvGc&t=3s) Encointer at Decoded Buenos Aires.
   * I have [presented](https://www.youtube.com/watch?v=MKJ0_eQQDX0) Integritee at the sub0 Asia in Bangkok.
   * I intend to go to Sub0 Buenos Aires in November and present there as well.
   * Lastly, I believe that the XCM docs example I have implemented above can be considered a long-form semi-technical article too.

Lastly, I would like to express my eagerness to be able to contribute more to the fellowship by having more budget available. ;)

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|----------------------|----------------------------|---|
|I  |90%   | N/A                  | No elligible referenda     |  |
|II |80%   | N/A                  |                            |  |
|III|70%   | 100%                 |                            |  |
|IV |60%   | 90%                  |                            |  |
|V  |50%   | 80%                  |                            |  |
|VI |40%   | 70%                  |                            |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
