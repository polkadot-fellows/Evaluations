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

I am Robert van Eerdewijk (0xRVE), a Fellowship Candidate inducted on 2026-04-21, seeking promotion to Dan 1. My work has been focused fully on Polkadot, specifically on pallet-revive: Polkadot's EVM-compatible smart-contract execution layer.

My contributions are concentrated in a coherent, high-value area: **bringing EVM-contract compatibility to pallet-revive**, building the precompile bridge that exposes core Substrate pallets to Solidity contracts, and fixing correctness and security issues in the surrounding execution and metering code. Since December 2025 I have landed ~31 PRs into `paritytech/polkadot-sdk`.

### Three clear examples of modest-but-substantial contributions

1. **New precompiles exposing core pallets to Solidity.**
   - vesting precompile [#11398](https://github.com/paritytech/polkadot-sdk/pull/11398), with `vestedTransfer` follow-up [#11630](https://github.com/paritytech/polkadot-sdk/pull/11630)
   - asset-conversion / Asset Hub DEX precompile [#11590](https://github.com/paritytech/polkadot-sdk/pull/11590), plus pool management [#11690](https://github.com/paritytech/polkadot-sdk/pull/11690) and `getReserves` [#11817](https://github.com/paritytech/polkadot-sdk/pull/11817)
   - `ForeignAssetIdExtractor` for the assets precompile [#10869](https://github.com/paritytech/polkadot-sdk/pull/10869)
   - ERC-20 feature support on the assets precompile: EIP-2612 permit (gasless approvals) [#11044](https://github.com/paritytech/polkadot-sdk/pull/11044) and `approve` semantics [#11279](https://github.com/paritytech/polkadot-sdk/pull/11279)

2. **Identifying and correcting non-trivial issues in core execution code.** Both were subtle metering bugs in a security-sensitive pallet.
   - storage-deposit refunds in nested contract calls [#10920](https://github.com/paritytech/polkadot-sdk/pull/10920)
   - execution tracer reporting zero gas for plain transfers [#12069](https://github.com/paritytech/polkadot-sdk/pull/12069)

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
