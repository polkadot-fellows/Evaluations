# Argument-0005: Promotion to Rank 2

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
This [Polkadot-SDK PR/#7457](https://github.com/paritytech/polkadot-sdk/pull/7459) ensures that the `omni-bencher overhead` command keeps working across all runtimes. A seemingly simple PR, yet it required the runtimes to implement `genesis-dev-presets`—which most of them lacked at the time of filing the PR. As a result, I also took on the work described in the next section.

### Add Genesis Presets for All Runtimes
Since the required genesis presets were missing, as mentioned above, I proactively took ownership of [Polkadot-SDK Issue/#5704](https://github.com/paritytech/polkadot-sdk/issues/5704) and implemented them for all remaining runtimes. Specifically:

- Coretime: [PR/#7476](https://github.com/paritytech/polkadot-sdk/pull/7476)
- Peoples: [PR/#7477](https://github.com/paritytech/polkadot-sdk/pull/7477)
- Glutton Westend: [PR/#7481](https://github.com/paritytech/polkadot-sdk/pull/7481)
- Kitchensink: [PR/#7741](https://github.com/paritytech/polkadot-sdk/pull/7741)

Most of the integration was straightforward, but in some cases, it uncovered issues:

- **Glutton Westend:** Broken extrinsics. The runtime lacks a `balances` pallet, causing the `CheckNonce` `TxExtension` to return an inexistent account error—even for the sudo account. After raising the issue, [bkchr](https://github.com/bkchr) himself quickly addressed it with [Polkadot SDK PR/#7838](https://github.com/paritytech/polkadot-sdk/pull/7838). This update makes the `CheckOnlySudo` `TxExtension` provide a tag, allowing us to remove `CheckNonce` from Glutton (since at least one extension must provide a tag for the transaction pool to identify transactions).

- **Immutability of Genesis Presets:** Currently, genesis presets are immutable, making them inflexible. To address this, we created [Polkadot SDK Issue/#7748](https://github.com/paritytech/polkadot-sdk/issues/7748), which proposes adding a mechanism to patch genesis presets. I plan to work on this next.

### Miscellaneous
- Discovered a bug caused by an implementation that didn’t follow the documentation ([Polkadot SDK Issue/#7845](https://github.com/paritytech/polkadot-sdk/issues/7845)). Fortunately, this hadn't affected anything yet, and I also fixed it in [Polkadot SDK PR/#7846](https://github.com/paritytech/polkadot-sdk/pull/7846).

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
