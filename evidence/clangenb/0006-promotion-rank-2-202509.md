# Argument-0005: Promotion to Rank 2

|                  |                                 |
|------------------|---------------------------------|
| **Report Date**  | Date of submission (2025/09/15) |
| **Submitted by** | Christian Langenbacher          |

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

Over the past 18 months, I have continued to deepen my knowledge of the Polkadot-SDK. As a core maintainer of three
ecosystem projects—Encointer, Integritee, and Ajuna—I have gained extensive hands-on experience with the SDK, not only
through contributions directly recognized by the Fellowship, but also through broader ecosystem work.

First, I will summarize the main arguments for this reporting period. Then, I will outline why I believe I am ready to
advance further within the Fellowship.

### XCM

#### Remote XCM V5 Transfer

I [implemented an abstraction](https://github.com/paritytech/polkadot-sdk/pull/9173) that enables remote execution of
asset transfers on behalf of an account’s representation on another chain. This feature, made possible with XCM V5, is
particularly useful for pallets that require flexible cross-chain fund management.

Previously, treasuries used similar a similar abstraction, but were limited to a single account representation on the
target chain. My implementation generalizes this pattern, allowing the current treasuries to simply call into the
generic version and no redundant code has been produced.

#### XCM Docs

Through my ecosystem projects, I have built significant experience with XCM, including:

* [Bridging TEER from Kusama to Polkadot](https://github.com/integritee-network/parachain/pull/325)
* [Autoswap relay tokens for TEER in XCM execution](https://github.com/integritee-network/parachain/issues/329)
* [Enabling Encointer to remotely spend treasury funds on Asset Hub](https://github.com/polkadot-fellows/runtimes/pull/679)
* The Remote XCM V5 Transfer implementation mentioned above

To share this knowledge with the community,
I [contributed a comprehensive XCM example](https://github.com/paritytech/polkadot-sdk/pull/9609).This documentation
demonstrates how to configure a runtime to:

* Allow other chains to register their native token as a foreign asset.
* Set up asset conversion pools between foreign tokens and the chain’s native token.
* Configure XCM to autoswap foreign assets into native assets for execution fees.
* Walk through the complete on-chain flow in a clear, test-driven example showing the required dispatchables, call
  order, and expected events.

### Requirements for promotion

1. Formalizing, implementing, or analytically improving a major component of the protocol
    * I consider the generic XCM abstraction described above to fall into this category.
2. Publishing a long-form semi-technical article
    * I [presented](https://www.youtube.com/watch?v=Thf23T_tvGc&t=3s) Encointer at _Decoded Buenos Aires_.
    * I [presented](https://www.youtube.com/watch?v=MKJ0_eQQDX0) Integritee at the _sub0 Asia in Bangkok_.
    * I plan to present again at _sub0 Buenos Aires_ in November.
    * Additionally, the XCM documentation example I authored serves as a long-form semi-technical contribution.

### Closing

I am eager to continue contributing at a higher level within the Fellowship, and believe that advancing in rank will
enable me to dedicate more time and resources to impactful work.

## Voting record

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|-------|---------------------|----------------------|----------------------------|----------|
| I     | 90%                 | N/A                  | No elligible referenda     |          |
| II    | 80%                 | N/A                  |                            |          |
| III   | 70%                 | 100%                 |                            |          |
| IV    | 60%                 | 90%                  |                            |          |
| V     | 50%                 | 80%                  |                            |          |
| VI    | 40%                 | 70%                  |                            |          |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
