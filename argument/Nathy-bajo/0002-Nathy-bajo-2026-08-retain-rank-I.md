# Argument-0002: Retention at Rank I

|                 |                |
| --------------- | -------------- |
| **Report Date** | 2026/08/31     |
| **Submitted by**| Nathaniel Bajo |

---

## Member details

- **Matrix username**: `@nathanielbajo:matrix.org`
- **Polkadot address**: `1HXh7kCk2Z9Er4TpqF7TPX6ivSnJTECesp44RP7jnP7RCeL`
- **Current rank**: `1`
- **Date of initial induction**: `2026/03/12` ([extrinsic](https://collectives.statescan.io/#/extrinsics/8415862-2))
- **Date of last report**: `2026/05/15`
- **Link to last report**: [Evaluations#285](https://github.com/polkadot-fellows/Evaluations/pull/285), approved by [referendum 545](https://collectives.subsquare.io/fellowship/referenda/545) and executed on 2026/06/20
- **Area(s) of Expertise/Interest**:
    - FRAME / Runtime
    - `pallet-revive` and EVM compatibility
    - Node & RPC infrastructure
    - XCM
    - Release engineering (fellowship runtimes)

---

## Reporting period

- **Start date**: 2026/05/16
- **End date**: 2026/08/31

---

## Argument

I'm applying for Rank I retention.

Most of my time since the promotion has gone into `pallet-revive`, reading the EVM implementation against the Ethereum spec and `revm` and fixing what doesn't match. The rest went to the fellowship runtimes, clearing out finished migrations and closing gaps the Asset Hub Migration left behind. Much of what landed started as an issue I opened and diagnosed myself.

---

### Correctness and security fixes

#### Re-entrant `CREATE2` could deploy two contracts to one address

A contract isn't written to `AccountInfoOf` until its constructor frame pops, and the `is_contract` check in `ContractInfo::new` is the only thing standing between that and a duplicate deployment. Re-entrancy is on by default, so a factory could call `CREATE2` twice with the same salt and code inside one transaction and see the address as empty both times. Two constructors then ran for one account, which permanently leaked a consumer reference and the code refcount and orphaned the second contract's storage deposit. EIP-684 exists to stop exactly this.

Reported in [#12639](https://github.com/paritytech/polkadot-sdk/issues/12639), fixed in [#12645](https://github.com/paritytech/polkadot-sdk/pull/12645) (merged 2026/07/20) by rejecting a nested instantiate whose target is already being constructed by an ancestor frame.

#### `EXTCODECOPY` trapped instead of zero filling

`EXTCODECOPY` converted `code_offset` with `as_usize_or_halt`, so an offset too large for a `usize` halted with `OutOfGas` where Ethereum returns zeros. The sibling copy opcodes already used `as_usize_saturated`, so this was an isolated slip that produced a different state root.

Reported in [#12643](https://github.com/paritytech/polkadot-sdk/issues/12643), fixed in [#12650](https://github.com/paritytech/polkadot-sdk/pull/12650) (merged 2026/08/14).

#### Session keys could be registered on both relays for free

`pallet_session` sets `type KeyDeposit = ()` on both relays, so `set_keys` reserved nothing and anyone could create `SessionKeys` entries at no cost. I reported it in [runtimes#1200](https://github.com/polkadot-fellows/runtimes/issues/1200) and proposed wiring up the deposit.

Thanks to [@sigurpol](https://github.com/sigurpol), who pushed back with a better fix. Post AHM the key lifecycle already lives on Asset Hub and is forwarded to the relay through `ah_client::set_keys_from_ah`, and the relay extrinsics had only been left open to give validators time to move across, so the right answer was to close them rather than price them. I reworked the PR to that approach: [runtimes#1212](https://github.com/polkadot-fellows/runtimes/pull/1212) (merged 2026/06/29) disables `set_keys` and `purge_keys` on both relays through `PostAhmFilter`, with tests asserting each is rejected with `CallFiltered`. sigurpol also picked up the validator communication and documentation side, and @Ank4n raised the staged rollout, Kusama first and Polkadot shortly after.

---

### Ethereum compatibility (`pallet-revive` eth-rpc)

Three fixes so Ethereum tooling works against Asset Hub without special casing.

#### EIP-1474 error codes

Every non `ClientError` variant collapsed into a blanket `-32600 Invalid Request`. [#11887](https://github.com/paritytech/polkadot-sdk/pull/11887) (merged 2026/06/29) maps `ConversionError` to `-32602` and the execution time variants to `-32000`, which is what Geth and Nethermind do. Reported in [#11886](https://github.com/paritytech/polkadot-sdk/issues/11886).

#### `eth_estimate_gas` on plain transfers

Every call ran a full binary search of dry runs, including EOA to EOA transfers that always cost 21,000. [#11890](https://github.com/paritytech/polkadot-sdk/pull/11890) (merged 2026/06/26) returns the fixed cost when there's no calldata, no code at the destination, and no access list, authorization list, blob payload or state overrides. Reported in [#11888](https://github.com/paritytech/polkadot-sdk/issues/11888).

#### `SubmittedTransaction::gas()` panic

It unwrapped an `Option<U256>` that is legitimately `None` for legacy payloads, and it was reachable from the published crate through an ungated `pub mod example`. [#12220](https://github.com/paritytech/polkadot-sdk/pull/12220) (merged 2026/07/03) returns `Option<U256>` instead. Reported in [#11889](https://github.com/paritytech/polkadot-sdk/issues/11889).

---

### Release engineering and runtime maintenance

- [runtimes#1189](https://github.com/polkadot-fellows/runtimes/pull/1189) (merged 2026/08/28): removed the finished `pallet-state-trie-migration` from the Polkadot relay and both Asset Hubs, and purged its leftover storage with a `RemovePallet` migration.
- [runtimes#1182](https://github.com/polkadot-fellows/runtimes/pull/1182) (merged 2026/07/20): Asset Hub Kusama and Polkadot now use their own benchmarked `pallet-revive` weights instead of the kitchensink fallback. This was open at my last report.
- [runtimes#1177](https://github.com/polkadot-fellows/runtimes/pull/1177) (merged 2026/06/08): releases now warn at 80% and block at 95% of each runtime's compressed WASM limit.

---

### Governance and treasury tooling

- [runtimes#1188](https://github.com/polkadot-fellows/runtimes/pull/1188) (merged 2026/06/23): deploys `pallet-parameters` on Collectives Polkadot so governance can maintain an allow-list of accounts, such as the Parity tip bot, that may open Fellowship referenda without holding a rank.
- [#11045](https://github.com/paritytech/polkadot-sdk/pull/11045) (merged 2026/07/22): a permissionless `reclaim_bounty_funds` that returns funds stranded in closed bounty accounts to the treasury, free on success and paid on a no-op so it can't be griefed.

---

### In progress: serving the ETH RPC from inside the node

This is the biggest thread I have open and it carries into the next period. The ETH RPC runs as its own binary talking to the node over `subxt`, which is a hop and an extra moving part that doesn't need to exist. I scoped it in [#11221](https://github.com/paritytech/polkadot-sdk/issues/11221).

My first attempt, [#11297](https://github.com/paritytech/polkadot-sdk/pull/11297), made the RPC server generic over its backend behind a `SubstrateClientT` trait. Review turned up a smaller path: `subxt`'s `Backend` is sealed but `RpcClientT` isn't. I agreed the change of direction with the `pallet-revive` team and opened [#12760](https://github.com/paritytech/polkadot-sdk/pull/12760) as the POC, keeping #11297 open as the record of how we got there.

#12760 dispatches JSON-RPC into the node's in-memory `RpcModule` rather than over a loopback WebSocket, behind an off by default feature. Running it against an Asset Hub Westend dev chain turned up three wiring bugs, all fixed: two nested `block_on` calls and a Prometheus registration panic. Review since then tightened subscription cleanup, so dropping one now calls `unsub` the way a real transport does.

The design works. I'm writing it up with the `pallet-revive` team to take to the node team.

---

### Issue discovery

Beyond direct code contributions, I actively identify and document gaps, edge cases, and improvements across the ecosystem to guide future work and lower the contribution barrier. This reporting period I opened a number of issues, particularly around `pallet-revive`, many of which I am now implementing myself: [#12648](https://github.com/paritytech/polkadot-sdk/pull/12648), [#12445](https://github.com/paritytech/polkadot-sdk/pull/12445) and [#12352](https://github.com/paritytech/polkadot-sdk/pull/12352) are all open PRs against my own issues.

Some of the currently open issues I authored can be found here:

- [`polkadot-sdk` issues (open, author: Nathy-bajo)](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue+state%3Aopen+author%3ANathy-bajo)
- [`runtimes` issues (open, author: Nathy-bajo)](https://github.com/polkadot-fellows/runtimes/issues?q=is%3Aissue+state%3Aopen+author%3ANathy-bajo)

---

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 0 referenda in which I was eligible to vote.  |   |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

---

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
