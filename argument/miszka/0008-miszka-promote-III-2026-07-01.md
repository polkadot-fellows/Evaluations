# Argument-0008: Promotion to Rank 3

|                 |                                  |
| --------------- | -------------------------------- |
| **Report Date** | 2026/07/01                       |
| **Submitted by**| Michał Kucharczyk                |

## Member details

- Matrix username: `@michal:parity.io`
- Polkadot address: [14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo](https://collectives.statescan.io/#/accounts/14T9NGF7LdCY7SK2j6oNXmB9NqfKYyrxBChUvYRjtFdvZBMo)
- Current rank: 1
- Date of initial induction: 2024/06/02
- Date of last report: 2026/06/08
- Area(s) of Expertise/Interest: Substrate node, Transaction Pool, ChainSpec/GenesisConfig, State/Trie & PoV

## Reporting period

- Start date: 2024/06/02 (induction)
- End date: 2026/07/01

## Argument

### Summary

My work is on the Substrate node. I own two areas: the fork-aware transaction pool and the genesis/chain-spec subsystem. I also work across the rest of the node and review a lot of code.

This is a request for a fast-track promotion to Rank III. I joined the Fellowship in June 2024, but I have worked on Polkadot core development since 2022 and attended the first Polkadot Blockchain Academy (PBA) that year. My on-chain tenure is therefore shorter than my actual involvement, which is why I am asking to skip Rank II.

### Contribution — *"…a supporting role in the code-design and a primary role in the implementation of a major protocol component"*

I am the primary author of the **fork-aware transaction pool**, both its design and its implementation. It replaced the previous pool, which could not keep a correct transaction state across competing forks — a long-standing problem. I designed the new approach ([design](https://hackmd.io/@_FY3-hvwQZ6cX_4n8zYUNA/HJqUWj4_s)), implemented it ([#4639](https://github.com/paritytech/polkadot-sdk/pull/4639)), drove it to feature-completeness ([roadmap](https://github.com/orgs/paritytech/projects/156)), and it is now the **network default** ([#8838](https://github.com/paritytech/polkadot-sdk/pull/8838)). The transaction pool is within the Fellowship's scope: the Manifesto lists "the internals of all functional Polkadot node implementations".

Building on this, I also authored **`transactions/v2`**, a proposal for a new transaction-propagation protocol. It separates announcing a transaction from sending its full data, to reduce bandwidth. This is a design proposal and groundwork for a future RFC ([#8128](https://github.com/paritytech/polkadot-sdk/pull/8128)).

My second area is the **genesis and chain-spec** subsystem. This was part of the *native-runtime-free* effort started by bkchr ([#62](https://github.com/paritytech/polkadot-sdk/issues/62)): genesis used to be built by the native runtime that was compiled into each node. I owned the genesis part of this work. I built the foundation ([#1256](https://github.com/paritytech/polkadot-sdk/pull/1256)), designed how to decouple the node from runtime types ([#1984](https://github.com/paritytech/polkadot-sdk/issues/1984)), and implemented it ([#2714](https://github.com/paritytech/polkadot-sdk/pull/2714)). The idea is to separate *what* runtime authors use (named genesis presets) from *how* the node builds genesis underneath, so the node builds genesis from the runtime's wasm instead of native code. This decoupling was the prerequisite for **`polkadot-omni-node`**, the generic, runtime-agnostic parachain node the ecosystem now uses. This work is within scope under the Manifesto's "runtime and host APIs".

### Robustness under adversarial load — *"…must function adequately even with a modest minority of malicious users"*

The transaction pool is built to stay healthy under load, including adversarial load. When the pool is full, it keeps higher-priority transactions and drops lower-priority ones, so it does not get stuck. It also correctly rejects invalid transactions reported by the block builder.

### Comprehensive knowledge and maintenance — *"comprehensive knowledge of the overall priorities and tradeoffs"*

I work across the whole node, not only my two main areas ([authored PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Amichalkucharczyk)). I also reason about node-wide constraints. For example, the parachain PoV (proof-size) budget: I fixed a bug that spanned the runtime, the state machine, and the trie layers, where a block could go over the budget. The interface change is written up as [RFC-158](https://github.com/polkadot-fellows/RFCs/pull/158).

I support the transaction pool in production. I built its monitoring dashboards, and I am the person people come to for transaction and block-building problems. Often the problem is not the pool itself, but I can find where it really is, which needs knowledge of the whole stack.

I also review a lot of code across the stack ([reviews](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Amichalkucharczyk)).

### Knowledge sharing within the ecosystem — *"demonstrable presence of knowledge sharing within the ecosystem"*

I mentor other engineers: I onboarded a new team member into the transaction pool, and I mentored a teammate in node internals. I help external teams when they hit transaction-pool problems, and my code reviews are also a way to share knowledge.

### Advocacy outside the ecosystem — *"at least three published long-form semi-technical articles concerning Polkadot"*

I have written several semi-technical articles about Polkadot and Substrate — one forum post and five HackMD write-ups. They are listed under Publications below.

## Voting record

I have voted on 0 out of 0 referenda in which I was eligible to vote during this reporting period.

|  Ranks | Activity | Agreement | Member's voting activities |
|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote during this reporting period. |
|III|70%   |100%  |  |

## Publications

- [The fork-aware transaction pool (forum)](https://forum.polkadot.network/t/the-fork-aware-transaction-pool/10468)
- [Fork-aware transaction pool — design proposal](https://hackmd.io/@_FY3-hvwQZ6cX_4n8zYUNA/HJqUWj4_s)
- [Substrate Transaction Pool: A Closer Look](https://hackmd.io/@_FY3-hvwQZ6cX_4n8zYUNA/SyT1QuhnA)
- [Mortal Transactions in Substrate](https://hackmd.io/@_FY3-hvwQZ6cX_4n8zYUNA/HJR2-ErNlg)
- [Reliable Flamegraphs for Substrate-Based Binaries](https://hackmd.io/@_FY3-hvwQZ6cX_4n8zYUNA/Sk3rV8sClg)
- [Note: ordering NFT transactions with tags](https://hackmd.io/@_FY3-hvwQZ6cX_4n8zYUNA/r1ua_w8fye)
- [RFC-158: v2 of the `storage_proof_size` host function](https://github.com/polkadot-fellows/RFCs/pull/158)

## Misc

- Comment: I have contributed to Polkadot since 2022 and have been a Fellowship member since June 2024. My on-chain rank history has a gap: I was bumped to rank 0 in January 2025 when a retention period lapsed, and re-promoted to rank 1 in March 2025. This was a missed administrative deadline, not a break in my contributions, which have been continuous.
