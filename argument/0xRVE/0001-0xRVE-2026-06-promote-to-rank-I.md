# Argument-0001: Promotion to Rank 1

| | |
|---|---|
| **Report Date** | 2026/06/23 |
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

I am Robert van Eerdewijk (0xRVE), a Fellowship Candidate inducted on 2026-04-21. My work has been focused on polkadot-sdk, specifically on pallet-revive: Polkadot's EVM-compatible smart-contract execution layer.

My contributions are concentrated in a coherent, high-value area: **bringing EVM-contract compatibility to pallet-revive**, building the precompile bridge that exposes core Substrate pallets to Solidity contracts, and fixing correctness and security issues in the surrounding execution code. Since December 2025 I have landed over 30 PRs into `paritytech/polkadot-sdk`.

The requirements for Rank 1 in §6.2.1 of the Manifesto ask for three clear examples of a modest but substantial contribution to protocol development, alongside independence of work, involvement in the design of a component, and a working awareness of the protocol. The contributions below speak to each of these, and I have ordered them by significance.

### Three clear examples of modest-but-substantial contributions

1. **New precompiles exposing core pallets to Solidity.**
A major focus of mine has been EVM/Solidity compatibility for pallet-revive: making native Substrate functionality callable from Solidity contracts through precompiles. The most substantial of these is the asset-conversion precompile ([#11590](https://github.com/paritytech/polkadot-sdk/pull/11590)), which exposes the Asset Hub DEX to contracts and let the Web3 Summit ticket sale accept payment in any currency. I made foreign assets addressable from Solidity by adding a StorageMap to the assets precompile ([#10869](https://github.com/paritytech/polkadot-sdk/pull/10869)), and I brought vesting into reach of contracts with the vesting precompile ([#11398](https://github.com/paritytech/polkadot-sdk/pull/11398)), which lets a Solidity contract unlock vested DOT. I also extended the ERC-20 asset precompiles with EIP-2612 permit support ([#11044](https://github.com/paritytech/polkadot-sdk/pull/11044)), enabling gasless token approvals through signed messages, which required implementing EIP-712 signing as a prerequisite. While working on this I also fixed a bug in the existing ERC-20 assets precompile that returned an incorrect encoding to Solidity.
For the vesting and asset-conversion precompiles I designed the Solidity interfaces and the mapping from each contract call to its underlying pallet dispatch.


2. **Identifying and correcting non-trivial issues.** 
The pallet-assets precompile had been deviating from the ERC-20 specification by adding to an account's existing allowance instead of replacing it, which I corrected in [#11279](https://github.com/paritytech/polkadot-sdk/pull/11279). In [#10920](https://github.com/paritytech/polkadot-sdk/pull/10920) I fixed storage refunds being calculated incorrectly when a contract allocated storage, a bug that caused some refunds to be ignored and others to be double-refunded. And in [#12069](https://github.com/paritytech/polkadot-sdk/pull/12069) I fixed the pallet-revive tracer underreporting gas for some transactions, which had been causing indexers and explorers to report the wrong gas usage.


3. **Security hardening of pallet-revive.**
In [#11676](https://github.com/paritytech/polkadot-sdk/pull/11676) and [#11715](https://github.com/paritytech/polkadot-sdk/pull/11715) I fixed a bug where a malicious intermediary contract could act on the caller's assets. In [#12387](https://github.com/paritytech/polkadot-sdk/pull/12387) I fixed a bug where `tload` and `sload` were always charged a fixed storage cost regardless of the actual storage size, which would have let a malicious actor spam storage loads without paying proportionally.

### Knowledge sharing
Alongside my own contributions I regularly review pull requests from other contributors, which is where most of my knowledge-sharing happens. I have [reviewed over 50 PRs authored by others](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3A0xRVE+-author%3A0xRVE), mostly on the precompile and pallet-revive surface. This has both spread what I have learned about the EVM compatibility layer and deepened my understanding of parts of the pallet I did not write, and I would like to take on more review responsibility at Rank 1.




### Independence and component ownership

This work was carried out independently: investigating, designing, implementing, and seeing each change through expert code-review to merge by the pallet-revive maintainers. Together it represents sustained responsibility for the EVM precompile layer, a component reasonably important to pallet-revive's role as Polkadot's smart-contract execution environment.

### Broader context

Beyond the precompile work I have contributed to surrounding maintenance and tooling, including host-function cleanup, Solidity fixture migration, toolchain bumps, and benchmark consolidation, giving me working familiarity with pallet-revive as a whole and its place in Polkadot. 

That broader view is also why the project's direction matters to me. I genuinely value Polkadot's commitment to minimised trust and unstoppability, because they offer a technically feasible alternative to problems currently handled by slow and inefficient bureaucracy: rules anyone can verify and no one can quietly override. It is also why correctness and abuse-resistance in the execution layer matter to me, since the platform can only fill that role if its guarantees actually hold.


## Conclusion

I believe this meets the expectations for Rank 1: three clear modest-but-substantial contributions, active involvement in the design of a deployed protocol component, and substantial implementation work in a functional implementation of the protocol, carried out independently and to the standard expected by the maintainers who reviewed it.

## References

- Polkadot SDK PRs: https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3A0xRVE
- GitHub profile: https://github.com/0xRVE