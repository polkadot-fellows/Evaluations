# Argument-0008: Retention at Rank II

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of submission (2026/03/29) |
| **Submitted by**| Branislav Kontur                |


## Member details

- Matrix username: @branislav_kontur:parity.io
- Polkadot address: 1HFq3DbX4tqanTLAx2CAToWnHXg6LRLMzSD4JzYCzCQpw5E
- Current rank: 2
- Date of initial induction: 2024/05/03
- Date of last report: 2026/01/03
- Area(s) of Expertise/Interest: `Bulletin, Bridges, XCM, System Parachains, governance, benchmarking, testing, integration, IPFS, Bitswap`


## Reporting period

- Start date: 2026/01/03
- End date: 2026/03/28

## Argument

This summary outlines my activities, contributions, and collaborations during the reporting period (January–March 2026).

### Bulletin Chain — Delivery

I continued leading the delivery of the **Bulletin Chain**, Polkadot's ephemeral storage chain designed to support Proof-of-Personhood (PoP) features and broader Web3 applications.

The Bulletin Chain originally started as a **solochain**. As the Polkadot SDK evolved, we decided to go with a **Polkadot parachain** design, which we also enabled through the PR adding parachain support [[1]](https://github.com/paritytech/polkadot-sdk/pull/10662). This transition allows Bulletin to benefit from Polkadot's shared security and cross-chain messaging capabilities, eliminating the need for a dedicated substrate-to-substrate bridge that was previously required for the solochain setup.

My role has been primarily focused on planning, coordination, design, improvement, and unblocking the team — which naturally results in fewer direct PRs but significant impact on delivery velocity. Key activities include:

- **Bulletin Polkadot parachain release**: Prepared the Bulletin for its first Polkadot mainnet release using a staged deployment plan — first onboarding an empty runtime to secure the parachain slot, then upgrading with the full Bulletin runtime via governance. I prepared the onboarding proposal [[2]](https://hackmd.io/@bkontur/SJWyQEdq-e), the Fellows runtime PR [[3]](https://github.com/polkadot-fellows/runtimes/pull/1120) with a tracking issue [[4]](https://github.com/polkadot-fellows/runtimes/issues/1119), coordinated the Fellows release process and publishing Bulletin crates.
- **Bulletin testnet deployments**: Coordinated deployment cycles for Westend and Paseo Bulletin networks.
- **Benchmarking and performance**: Conducted testing and benchmarking of Bulletin storage capabilities.
- **Bulletin UI**: Deployed the initial [Bulletin UI](https://paritytech.github.io/polkadot-bulletin-chain) and set directions for further UI development.

### IPFS / Bitswap / Smoldot

I continued deepening expertise in **IPFS/Bitswap**:

- Investigated and reported a >32MiB file transfer issue in litep2p [[5]](https://github.com/paritytech/litep2p/issues/514), proposed a solution, and handed it to Dmitry for implementation.
- Participated in the **Smoldot Bitswap RPC API** design together with Dmitry Markin and Basti, which resulted in the JSON-RPC spec PR [[6]](https://github.com/paritytech/json-rpc-interface-spec/pull/183), with a follow-up for `bitswap_stream` coming.

### Other Parity + Fellows Ecosystem Contributions

- Helped push the **Hyperbridge fix** through the Fellows release 2.0.7 pipeline [[7]](https://github.com/polkadot-fellows/runtimes/pull/1074), reviewing and facilitating the release.
- Ongoing PR reviews across polkadot-sdk, polkadot-bulletin-chain, and the Fellows runtimes repositories.
- Reviewing (and/or working on) numerous design documents including HOP protocol, data renewal, node syncing, and storage architecture proposals.

### Web3 Storage PoC

I helped stabilize and push the initial demo of the **Web3 Storage** proof-of-concept [[8]](https://github.com/paritytech/web3-storage) based on the storage design [[9]](https://github.com/paritytech/polkadot-sdk/pull/10731), — a user-facing decentralized storage solution. My contributions included setting up the storage provider infrastructure, fixing CI and integration issues, and identifying future changes needed beyond the PoC phase — such as storage provider architecture improvements and scalability concerns for the transition to production.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity).  |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

