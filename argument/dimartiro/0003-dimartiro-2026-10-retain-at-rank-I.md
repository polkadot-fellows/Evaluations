# Argument-0003: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/10/15                                                                                  |
| **Submitted by**| Diego Romero                                                                                |
| **Sponsored by**| Name of the assignee(s)                                                                     |


## Member details

- Matrix username: @dimartiro:matrix.org
- Polkadot address: 5FZGEDktFdfGuUjYAbdSdjwt67pXf4UQHcyiW9Wk4hrYvxvY
- Current rank: I
- Date of initial induction: 2026/04/15
- Date of last report: 2026/07/09
- Link to last report: [Argument-0002: Retention at Rank I](https://github.com/polkadot-fellows/Evaluations/blob/main/argument/dimartiro/0002-dimartiro-2026-07-retain-at-rank-I.md)
- [Subsystems](../../subsystems.md) developed/maintained:
    - Nodes (Networking, Security)
    - Revive (Smart Contracts, EVM precompiles, compatibility)
    - JAM (Clients)


## Reporting period

- Start date: 2026/07/09
- End date: 2026/10/15


## Argument

During this reporting period most of my time again went into the Go implementation of JAM at ChainSafe. Upstream, I chose depth over breadth this time: rather than spreading across the stack as in my previous period, I concentrated on two subsystems, node networking and Revive, and worked through bugs, many of them filed by those subsystems' own maintainers and several open for one to two years. Eight of my upstream pull requests were merged during the period and two more are approved and awaiting merge. The merged ones include the three PolkaVM determinism fixes ([#395](https://github.com/paritytech/polkavm/pull/395), [#396](https://github.com/paritytech/polkavm/pull/396), [#397](https://github.com/paritytech/polkavm/pull/397)) and the Snowbridge outbound-queue-v2 state pruning ([#12211](https://github.com/paritytech/polkadot-sdk/pull/12211)) that were still pending review when I submitted my last argument.

Among the Rank I requirements, §6.2.1 of the Manifesto asks for:

> Three clear examples of a modest but substantial contribution to protocol development.

and gives "identifying and correcting a non-trivial issue in protocol code or formalisation" as an example of one. Most of the work below is of exactly that shape.

**Nodes: networking and sync.** Polkadot nodes ban peers whose reputation falls below a threshold, and the sync code charged a peer the same ban-grade penalty for answering "I don't have those blocks" as for sending an invalid block. The range we ask for is inferred from the peer's announced best block, not something the peer offered, so an empty answer is honest behaviour: a node running with `--blocks-pruning 256` simply no longer holds old bodies. Today three such answers ban an honest peer and, through the peer store, also tear down its GRANDPA and transaction substreams. I introduced a milder, dedicated penalty for empty responses, the same magnitude already chosen for the equivalent gap-sync case. The peer is still disconnected and the requested range is still freed, so sync behaviour is unchanged and only the unjustified ban goes away ([#13047](https://github.com/paritytech/polkadot-sdk/pull/13047), in review, closing [#6009](https://github.com/paritytech/polkadot-sdk/issues/6009), open since 2024). On the litep2p backend, which is now the default, each notification protocol's peerset never forgot a peer: every peer that ever offered a substream we rejected stayed in its map for the lifetime of the node. I bounded it to the reserved set plus the peers with a live substream, taking care not to drop disconnected reserved peers, which the peerset must keep in order to redial them ([#13123](https://github.com/paritytech/polkadot-sdk/pull/13123), in review, closing [#6219](https://github.com/paritytech/polkadot-sdk/issues/6219)). In litep2p itself I fixed a race reported in about 30% of Bitswap and Kademlia dials. In that race, `dial` reports a peer as already connected while `open_substream` still says it does not exist, because the connection event has not yet been delivered to the protocol ([litep2p#660](https://github.com/paritytech/litep2p/pull/660), in review, closing [litep2p#504](https://github.com/paritytech/litep2p/issues/504)). Finally, I moved the connected-peers metric out of `sc-network`, where both networking backends maintained a counter purely to publish it, into the sync engine that already tracks that number. The metric keeps its name, so existing dashboards and alerts are unaffected ([#12979](https://github.com/paritytech/polkadot-sdk/pull/12979), merged, approved by three node maintainers, closing [#5024](https://github.com/paritytech/polkadot-sdk/issues/5024)).

**Revive: pallet-revive.** `System.terminate` could report success while leaving the contract alive. The actual destruction runs at the end of the call stack, where failures are dropped by design, and it failed whenever the contract account carried a lock, a freeze or a foreign hold. A third party could cause this, for example by making a vested transfer to the contract. Making `terminate` revert in that case was not an option, because anyone could then block a contract's termination indefinitely with a cheap long-lived lock. I redesigned the teardown so that a successful `terminate` always means the contract is gone. The storage deposit is refunded before the payout so that it cannot end up covering the lock, each balance step runs in its own storage transaction and can fail on its own without aborting the teardown, and `SELFDESTRUCT` keeps its EIP-6780 semantics ([#13085](https://github.com/paritytech/polkadot-sdk/pull/13085), approved, fixing [#13017](https://github.com/paritytech/polkadot-sdk/issues/13017)).

**Revive: the resolc compiler.** In the experimental `newyork` pipeline, a contract whose runtime code was empty compiled into a function that returned instead of exiting. LLVM then legitimately removed the deploy/runtime dispatch, so calling the deployed contract would have run its constructor; the build only failed because the PolkaVM linker happened to trip an internal assertion afterwards. I made the pipeline terminate code blocks with the implicit EVM return, as the default pipeline already did, and verified that the default pipeline's output stays byte-identical across all 83 integration contracts ([revive#598](https://github.com/paritytech/revive/pull/598), merged). I also made `resolc` compile Yul objects that carry deploy code only, which `solc` accepts and `resolc` rejected with an LLVM verifier error. The fix is a single parser-level change that covers both IR pipelines ([revive#597](https://github.com/paritytech/revive/pull/597), merged, closing [revive#490](https://github.com/paritytech/revive/issues/490)). I turned the compiler panics from an SRLabs audit finding into proper diagnostics ([revive#600](https://github.com/paritytech/revive/pull/600), merged, addressing [revive#351](https://github.com/paritytech/revive/issues/351)). Lastly, a contract compiled with a large heap could link successfully and then be rejected by the pallet on upload. I exposed the pallet's own upload check as a public function ([#13300](https://github.com/paritytech/polkadot-sdk/pull/13300), approved) so that `resolc` can reach the same verdict at link time and report the measured value against the broken limit ([revive#599](https://github.com/paritytech/revive/pull/599), in review, closing [revive#96](https://github.com/paritytech/revive/issues/96)).

**Runtime benchmarking.** `benchmark pallet` could write a `proof_size` around 10^18 into a pallet's weight file when a benchmark touched storage without a `MaxEncodedLen` bound. Such a weight claims more proof size than any block can hold and silently corrupts block-weight accounting. I traced it to a rank-deficient regression for storage prefixes observed at a single component value. I fixed that root cause, made the overhead arithmetic saturate instead of wrapping, and made the CLI refuse to write a coefficient no real measurement can produce ([#13073](https://github.com/paritytech/polkadot-sdk/pull/13073), in review, fixing [#13066](https://github.com/paritytech/polkadot-sdk/issues/13066)).

**JAM: Go client (ChainSafe).** I continue to contribute to the Go implementation of JAM, the next-generation Polkadot protocol, which remains my main focus. An independent implementation built from the Graypaper exercises the specification and strengthens client diversity for JAM from day one. Our team will have its JAM Prize Milestone 1 interview on 2026/10/26.

Finally, §6.2 describes the qualities expected at this rank as "aspiration, knowledge-discovery, knowledge-sharing and active maintenance", together with "a broad understanding across the protocol". This period shows them through sustained, concentrated work in the subsystems I list above: finding non-trivial correctness issues in the node, the networking stack, the contracts pallet and its compiler, and fixing them in review with the maintainers who own those components.


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |N/A   |There were no referenda on the Members track, the only track open to Rank I, during the reporting period. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
