# Evidence-0001: Promotion to Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/02/12)                                                             |
| **Submitted by**| Alexandru Vasile                                                                            |


## Member details

- Matrix username: @lexnv:parity.io
- Polkadot address: 14Mjra9hNggCSLyVv3AmtvpjeyBhUMwiEEBXGFidu3ZWTEQN
- Current rank: 0
- Date of initial induction: 2025/02/12
- Date of last report: N/A
- Area(s) of Expertise/Interest: `Substrate Node`, `Substrate RPC`, `FRAME`


## Reporting period

- Start date: 2023/02/12
- End date: 2025/02/12


## Evidence

### Litep2p Network Backend

[Litep2p](https://github.com/paritytech/litep2p) is a highly optimized alternative to libp2p, designed for greater efficiency. Its architecture significantly reduces CPU consumption—by approximately **50% compared to libp2p**—while improving request-response performance, connection stability, and authority discovery. Specifically, Litep2p reduces authority discovery times from 10 minutes (in libp2p) to under 2 minutes. Additionally, the latest Yamux performance patch has improved notification message handling by 20%, further surpassing libp2p by 3%.

To drive community engagement, I have consistently provided insights into Litep2p in the [Polkadot forum](https://forum.polkadot.network/t/litep2p-network-backend-updates/9973/4). The project's progress and my contributions toward improving Litep2p’s robustness can be tracked in [this milestone](https://github.com/paritytech/litep2p/issues/140). Implementing Litep2p required a deep understanding of the Substrate-based chain networking stack and has led to multiple improvements across Substrate, including fixes for libp2p. My substrate contribution can be tracked via [@lexnv/PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Alexnv) and [@lexnv/issues](https://github.com/paritytech/polkadot-sdk/issues?q=is%3Aissue%20author%3Alexnv%20).

We are currently rolling out Litep2p in **Kusama** before enabling it on Polkadot. The deployment process can be tracked in this [issue](https://github.com/paritytech/polkadot-sdk/issues/7076).

### Metadata V15 & V16

Chain metadata plays a crucial role in facilitating interactions with the blockchain, especially for tools like Subxt, PAPI, and Polkadot-JS.
For Metadata V15, my most significant contribution was adding runtime API types, allowing nodes to expose runtime information that can be leveraged by tools to generate strongly typed APIs. This version also introduced support for querying multiple runtime versions. The progress can be tracked in [substrate/#12939](https://github.com/paritytech/substrate/issues/12939).


However, Metadata V15 still required improvements to eliminate hardcoded configurations across different chains. To address this, I led the development of **Metadata V16**, which introduces:
 - Deprecation information
 - A new transaction extension type
 - Associated types for runtime configuration traits
 - Numerous other refinements

Progress can be tracked in [polkadot-sdk/#4520](https://github.com/paritytech/polkadot-sdk/issues/4520).
Forum post updates can be tracked in [Polkadot forum](https://forum.polkadot.network/t/upcoming-metadata-v16-features-to-include-in-v16/8153).

### RPC Spec V2

The [RPC Spec V2](https://github.com/paritytech/json-rpc-interface-spec) was introduced to enhance compatibility between light clients and Substrate-based chains while providing a more structured API experience.

**ChainHead API**: A more efficient alternative to the legacy API, designed for developers needing real-time chain tip data. It operates as a subscription-based model, pinning blocks in memory until they are no longer needed. This API enables querying runtime state, storage, and more.

**Archive API**: Available only on archive nodes, this API enhances the experience for chain indexer developers. It functions similarly to the ChainHead API but allows querying historical blocks.

**Transaction API**: A new alternative to the legacy transaction submission implementation, aiming to bridge the gap between light clients and Substrate chains.

The body of work for the RPC Spec V2 can be followed in this [issue](https://github.com/paritytech/polkadot-sdk/issues/1516).

### Subp2p Explorer

I created [subp2p-explorer](https://github.com/lexnv/subp2p-explorer), a powerful debugging tool for Substrate-based blockchain networks. It enables users to:

- Discover all network participants of any Substrate-based chain, with geolocation support.
- Identify all authority records along with their respective authority details.
- Support both litep2p and libp2p, ensuring compatibility across different networking protocols.

Subp2p-Explorer is also integrated into other Web3 Projects like [Polkawatch](https://polkawatch.app/) and Parity tools like [polkadot-introspector/whois](https://github.com/paritytech/polkadot-introspector/blob/9640620532bcbf2e688cc521e8afd5c3c26ed9ef/whois/README.md), making it a valuable resource for network analysis and debugging.



## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

