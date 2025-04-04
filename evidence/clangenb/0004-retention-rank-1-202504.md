# Argument-0004: Retention at Rank 1

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2025/04/03) |
| **Submitted by**| Christian Langenbacher          |


## Member details

- Matrix username: `@clang:matrix.org`
- Polkadot address: `16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3`
- Current rank: `1`
- Date of initial induction: `2024/03/27`
- Date of last report: `2025/01/08`
- Area(s) of Expertise/Interest: `Parachain Builder, Runtime, Clients`


## Reporting period

- Start date: 2025/01/08
- End date: 2025/04/03


## Argument
My argument mostly revolves around PRs and issues that I filed in the Polkadot-SDK repository, which will be elaborated below.

### Run `frame-omni-bencher` Overhead in CI for All Runtimes
I implemented a CI job that [runs the `frame-omni-bencher-overhead` command for all runtimes](https://github.com/paritytech/polkadot-sdk/pull/7459). A seemingly simple PR, yet it required the runtimes to implement `genesis-dev-presets`—which most of them lacked at the time of filing the PR. As a result, I also took on the work described in the next section.

### Add Genesis Presets for All Runtimes
Since the required genesis presets were missing, as mentioned above, I proactively took ownership of the issue regarding [implementing genesis presets for all runtimes](https://github.com/paritytech/polkadot-sdk/issues/5704) and implemented them in a sequence of PRs.

For those who have never used them, these genesis presets are a set of sensible genesis values (e.g., setting Alice as sudo). However, instead of redundantly defining them in the chain-spec, as has been the case until now, the idea is that the runtime itself knows these sensible defaults for dev setups, making those dev setups easier to manage and use.

Hence, I went ahead and implemented the genesis presets for:
- [coretime-rococo and coretime-westend](https://github.com/paritytech/polkadot-sdk/pull/7476),
- [people-rococo and people-westend](https://github.com/paritytech/polkadot-sdk/pull/7477),
- [glutton-westend](https://github.com/paritytech/polkadot-sdk/pull/7481) (there is no Rococo variant),
- and the [kitchensink-runtime](https://github.com/paritytech/polkadot-sdk/pull/7741).

Most of the integration was straightforward, but in some cases, it uncovered issues:

- **Glutton Westend:** Broken extrinsics. The runtime lacks a `balances` pallet, causing the `CheckNonce` `TxExtension` to return a nonexistent account error—even for the sudo account. After raising the issue, [bkchr](https://github.com/bkchr) himself quickly addressed it by making the `CheckOnlySudo` `TxExtension` [provide a tag](https://github.com/paritytech/polkadot-sdk/pull/7838), allowing us to remove `CheckNonce` from Glutton (since at least one extension must provide a tag for the transaction pool to identify transactions).

- **Immutability of Genesis Presets:** Currently, genesis presets are immutable, making them inflexible. I intend to expand their functionality by [allowing them to be patched](https://github.com/paritytech/polkadot-sdk/issues/7748) as my next task.

### Miscellaneous
- I identified that the [`Incrementable` trait is not implemented according to the documentation](https://github.com/paritytech/polkadot-sdk/issues/7845), which caused saturation instead of returning `None`. This could, in theory, lead to new assets overwriting each other if `AssetId::MAX` were reached. Luckily, all chains are far from that limit. I also fixed this behavior by properly [returning `None` when the value would saturate](https://github.com/paritytech/polkadot-sdk/pull/7846).

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
