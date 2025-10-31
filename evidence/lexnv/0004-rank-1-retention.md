# Argument-0004: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/10/31)                                                             |
| **Submitted by**| Alexandru Vasile                                                                            |


## Member details

- Matrix username: @lexnv:parity.io
- Polkadot address: 14Mjra9hNggCSLyVv3AmtvpjeyBhUMwiEEBXGFidu3ZWTEQN
- Current rank: I
- Date of initial induction: 2025/02/12
- Date of last report: 2025/02/12
- Area(s) of Expertise/Interest: `Substrate Node`, `Substrate RPC`, `FRAME`


## Reporting period

- Start date: 2025/07/31
- End date: 2025/10/31


## Argument

Over the recent months, I have focused my efforts on the Ethereum Block Storage implementation in Substrate's **Pallet Revive**. This is part of a company-wide effort to bring EVM smart contract support to Substrate. At the same time, I continued to offer support for **litep2p**, pending fixes and reviews on the WebRTC work.

### Ethereum Block Storage

I implemented an Ethereum-compatible block within [`pallet-revive`](https://github.com/paritytech/polkadot-sdk/tree/master/substrate/frame/revive) (the Substrate EVM pallet) to enable **full Ethereum block reconstruction**, including block hashes, transaction roots, and receipt roots, directly within the Substrate runtime.

The [**#PR 9418**](https://github.com/paritytech/polkadot-sdk/pull/9418) introduces a memory-efficient Ethereum block builder that constructs a full Ethereum block on-chain using only Substrate runtime data.

The implementation achieves a **low memory footprint**, avoiding pallet storage bloat and consuming **up to 90% less memory and storage**. This utilizes low-level semantics of RLP encoding to incrementally build the transaction and receipt roots, while keeping a maximum of 3 in-flight transactions.

The RPC layer has also been adjusted by Lukas and me to utilize the pallet changes.

For more details, the workload was monitored weekly in the following public document:  
[Weekly Progress Tracking](https://docs.google.com/document/d/177vFqRfVynYowTHd-hwQVfBnFtldVWmHfp8bSs9k6r0/edit?tab=t.0#heading=h.4pwww2fcxwtv)

### Litep2p Network Backend

I continued to monitor and support the [**litep2p**](https://github.com/paritytech/litep2p) crate. In doing so, I created a new release, **[litep2p v0.11.1](https://github.com/paritytech/litep2p/pull/461)**, which mitigates an edge case that causes nodes to panic on unexpected rust-yamux inbound connections — addressed in [**PR #445**](https://github.com/paritytech/litep2p/pull/445). I also submitted a fix in the upstream `rust-yamux` crate to ensure poisoned states are no longer polled: [**rust-yamux #211**](https://github.com/libp2p/rust-yamux/pull/211).

During this period, I’ve also been in contact with Tim from ChainSafe to provide feedback on their WebRTC work, which is progressing in the right direction: [**litep2p WebRTC PR #441**](https://github.com/paritytech/litep2p/pull/441).

### Other work:

Besides the mentioned topics, I'm providing reviews for my area of expertise in polkadot-sdk and RFCs.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referendums available for my rank to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

