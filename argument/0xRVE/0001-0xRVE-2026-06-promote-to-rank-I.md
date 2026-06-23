# Argument-0001: Promotion to Rank 1

| | |
|---|---|
| **Report Date** | 2026/06/10 |
| **Submitted by** | Robert van Eerdewijk |

## Member details

- Matrix username: @robert.vaneerdewijk:parity.io
- Polkadot address: 1TFKfeyB7ATV7Amy9tqppDSySHKQZDPr39shpuC4vnVPSin
- Current rank: Rank 0 (Candidate)
- Date of initial induction: 2026-04-21
- Area(s) of Expertise/Interest: pallet-revive, EVM precompiles, pallet-assets, Ethereum-compatibility (eth-rpc)

## Reporting period

- Start date: 2025/12/01
- End date: 2026/06/10

## Argument

I am applying for promotion to Rank 1, I Dan: Humble Member. I believe the scope and consistency of my merged contributions to `polkadot-sdk` justify it.

### Background

I am Robert van Eerdewijk (0xRVE), a Fellowship Candidate inducted on 2026-04-21, seeking promotion to Dan 1. My work has been focused on polkadot-sdk, specifically on pallet-revive: Polkadot's EVM-compatible smart-contract execution layer.

My contributions are concentrated in a coherent, high-value area: **bringing EVM-contract compatibility to pallet-revive**, building the precompile bridge that exposes core Substrate pallets to Solidity contracts, and fixing correctness and security issues in the surrounding execution and metering code. Since December 2025 I have landed over 30 PRs into `paritytech/polkadot-sdk`.

The requirements for Rank I in §6.2.1 of the Manifesto ask for three clear examples of a modest but substantial contribution to protocol development, alongside independence of work, involvement in the design of a component, and a working awareness of the protocol. The contributions below speak to each of these, and I have ordered them by significance.

### Three clear examples of modest-but-substantial contributions

1. **New precompiles exposing core pallets to Solidity.**
A major focus of mine has been EVM/Solidity compatibility for pallet-revive: making native Substrate functionality callable from Solidity contracts through precompiles. The most substantial of these is the asset-conversion precompile ([#11590](https://github.com/paritytech/polkadot-sdk/pull/11590)), which exposes the Asset Hub DEX to contracts and let the Web3 Summit ticket sale accept payment in any currency. I made foreign assets addressable from Solidity by adding a StorageMap to the assets precompile ([#10869](https://github.com/paritytech/polkadot-sdk/pull/10869)), and I brought vesting into reach of contracts with the vesting precompile ([#11398](https://github.com/paritytech/polkadot-sdk/pull/11398)), which lets a Solidity contract unlock vested DOT. I also extended the ERC-20 asset precompiles with EIP-2612 permit support ([#11044](https://github.com/paritytech/polkadot-sdk/pull/11044)), enabling gasless token approvals through signed messages, which required implementing EIP-712 signing as a prerequisite. While working on this I also fixed a bug in the existing ERC-20 assets precompile that returned an incorrect encoding to Solidity.


2. **Identifying and correcting non-trivial issues in core execution code.** 
The pallet-assets precompile had been deviating from the ERC-20 specification by adding to an account's existing allowance instead of replacing it, which I corrected in [#11279](https://github.com/paritytech/polkadot-sdk/pull/11279). In [#10920](https://github.com/paritytech/polkadot-sdk/pull/10920) I fixed storage refunds being calculated incorrectly when a contract allocated storage, a bug that caused some refunds to be ignored and others to be double-refunded. And in [#12069](https://github.com/paritytech/polkadot-sdk/pull/12069) I fixed the pallet-revive tracer underreporting gas for some transactions, which had been causing indexers and explorers to report the wrong gas usage.




3. **Security hardening of the precompile surface.**
   - rejected delegatecall into precompiles, closing a class of delegatecall-based attacks [#11715](https://github.com/paritytech/polkadot-sdk/pull/11715), [#11676](https://github.com/paritytech/polkadot-sdk/pull/11676)
   - corrected event-charging to bill by data length rather than topic count [#11912](https://github.com/paritytech/polkadot-sdk/pull/11912)

### Independence and component ownership

This work was carried out independently: investigating, designing, implementing, and seeing each change through expert code-review to merge by the pallet-revive maintainers. Together it represents sustained responsibility for the EVM precompile layer, a component reasonably important to pallet-revive's role as Polkadot's smart-contract execution environment.

### Broader context

Beyond the precompile work I have contributed to surrounding maintenance and tooling, including host-function cleanup, Solidity fixture migration, toolchain bumps, and benchmark consolidation, giving me working familiarity with pallet-revive as a whole and its place in the Polkadot Ethereum-compatibility stack (eth-rpc, runtime integration). I am comfortable discussing Polkadot's core philosophy and the tradeoffs of a decentralised, unstoppable network as they bear on this work.

## Conclusion

I believe this meets the expectations for Rank 1: three clear modest-but-substantial contributions, active involvement in the design of a deployed protocol component, and substantial implementation work in a functional implementation of the protocol, carried out independently and to the standard expected by the maintainers who reviewed it.

## References

- Polkadot SDK PRs: https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3A0xRVE
- GitHub profile: https://github.com/0xRVE