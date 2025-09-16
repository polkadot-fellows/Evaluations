# Argument-0006: Promotion to Rank 2

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

- Start date: 2024/07/02
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
Through my ecosystem projects, I have gained significant hands-on experience with XCM. For reference (no need to if not interested), see [1](https://github.com/integritee-network/parachain/pull/325), [2](https://github.com/integritee-network/parachain/pull/341), [3](https://github.com/integritee-network/parachain/pull/344), and [4](https://github.com/integritee-network/parachain/pull/354), [5](https://github.com/polkadot-fellows/runtimes/pull/679).These contributions are not Fellowship-related, but they required me to work across nearly the entire XCM stack—a new domain for me in which I have learned a great deal. However...

Looking at the open tracking issues for XCM documentation - [1](https://github.com/paritytech/polkadot-sdk/issues/9431), [2](https://github.com/paritytech/polkadot-sdk/issues/5207) - it is clear that much work remains. XCM remains both highly abstract and complex, and it took me considerable time, along with extensive debugging, to fully grasp the details. To help reduce the learning curve for others, I authored a comprehensive [XCM example](https://github.com/paritytech/polkadot-sdk/pull/9609) that demonstrates how to:

* Allow other chains to register their native token as a foreign asset.
* Set up asset conversion pools between foreign tokens and the chain’s native token.
* Configure XCM to autoswap foreign assets into native assets for execution fees.
* Walk through the complete on-chain flow in a clear, test-driven example that shows the required dispatchables, call order, and expected events.

This contribution should make it easier for developers to understand and apply XCM, especially those interested in how Asset Hub handles foreign assets and fee payment in foreign tokens, as well as how parachain teams can integrate their own assets into Asset Hub.

### Add Genesis Presets for All Runtimes and update the genesis-presets mechanism
This work began with the seemingly simple task of implementing a CI job to [run the frame-omni-bencher-overhead command for all runtimes](https://github.com/paritytech/polkadot-sdk/pull/7459). This job is important to ensure that overhead benchmarking with the omni-bencher continues to function properly. However, while preparing the PR, I discovered that most runtimes did not yet implement genesis-dev-presets, which were required for the job to succeed.

For those unfamiliar: genesis presets define sensible defaults for development setups (e.g., assigning Alice as sudo). Rather than redundantly defining these defaults in the chain spec—as had been done previously—the new approach is to have the runtime itself provide these presets. This makes dev setups easier to manage, more consistent, and less error-prone.

Most integrations were straightforward, and I implemented them through a sequence of PRs: [coretimes](https://github.com/paritytech/polkadot-sdk/pull/7476), [rorocos](https://github.com/paritytech/polkadot-sdk/pull/7477), [glutton](https://github.com/paritytech/polkadot-sdk/pull/7481), [kitchensink-runtime](https://github.com/paritytech/polkadot-sdk/pull/7741), and [penpal and yap](https://github.com/paritytech/polkadot-sdk/pull/8426).

In some cases, however, deeper issues surfaced. The most significant was that genesis presets were static and could not be patched. As a result, the staging-node-cli still needed to call into the native runtime to configure a more sophisticated genesis setup. To address this, I implemented support for [patching genesis-presets](https://github.com/paritytech/polkadot-sdk/pull/8323). In the same PR, I also removed native runtime calls from the staging-node-cli.

This aligns with our broader architectural goal: eliminating native runtime dependencies on the node side in favor of an omni-node architecture that relies solely on the WASM blob. My work brought us one step closer to that vision.

I believe this contribution demonstrates my ability to take initiative, independently identify and solve problems, and proactively improve the architecture in ways that advance the long-term roadmap.

### Requirements for promotion

1. Formalizing, implementing, or analytically improving a major component of the protocol
    * I consider both, the generic XCM abstraction described above and the genesis presets journey to fall into this category.
2. Publishing a long-form semi-technical article
    * I [presented](https://www.youtube.com/watch?v=Thf23T_tvGc&t=3s) Encointer at _Decoded Buenos Aires_.
    * I [presented](https://www.youtube.com/watch?v=MKJ0_eQQDX0) Integritee's verifiable randomness oracle at the _sub0 Asia in Bangkok_.
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
