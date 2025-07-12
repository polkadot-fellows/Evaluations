# Argument-0005: Retention at Rank 1

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2025/07/11) |
| **Submitted by**| Christian Langenbacher          |


## Member details

- Matrix username: `@clang:matrix.org`
- Polkadot address: `16YCL3UVpVWQLGW3p3Zx4k5WAEp9W1DwdDnxAbyAaPxVxnp3`
- Current rank: `1`
- Date of initial induction: `2024/03/27`
- Date of last report: `2025/04/03`
- Area(s) of Expertise/Interest: `Parachain Builder, Runtime, Clients`


## Reporting period

- Start date: 2025/04/03
- End date: 2025/07/11


## Argument
My argument mostly revolves around PRs and issues that I filed in the Polkadot-SDK repository, which will be elaborated below.

### Allow genesis-presets to be patched.
The genesis-preset provides sensible defaults for genesis configurations, but until now, it couldn't be modified—making — small adjustments impossible. I’ve implemented support for [patching genesis-presets](https://github.com/paritytech/polkadot-sdk/pull/8323), and in the same PR, removed native runtime calls from staging-node-cli. As a reminder, we're aiming to eliminate native runtime dependencies on the node side as we move towards an omni-node architecture that relies solely on the WASM blob.

### Add genesis-presets for the remaining runtimes in the polkadot-parachain-bin
We've already adopted genesis-presets in polkadot-parachain-bin, but some newer runtimes were still using the old approach—defining the full JSON on the node side. I’ve [migrated](https://github.com/paritytech/polkadot-sdk/pull/8426) penpal, rococo-parachain-runtime, and yet-another-parachain-runtime to the new paradigm.

### Add Remote XCM V5 transfer
For Encointer, I [implemented](https://github.com/paritytech/polkadot-sdk/pull/9173) a concept that allows a pallet managing multiple accounts on one chain to perform asset transfers on another chain—on behalf of those accounts—using the new DescendOrigin XCM instruction. Since this pattern is useful for any pallet that needs flexible cross-chain fund management, I [proposed upstreaming it](https://github.com/paritytech/polkadot-sdk/issues/9170) and have already started [working on it](https://github.com/paritytech/polkadot-sdk/pull/9173).

#### Related Work
The existing PayOverXCM type implements the Pay trait, but it has two limitations:
* It supports only a single, static sender per implementation. 
* It assumes remote execution is always UnpaidExecution.

My proposed implementation addresses both issues.


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
