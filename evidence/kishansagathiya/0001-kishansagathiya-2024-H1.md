# Evidence-0001: Rentention at Rank I

|                 |                                 |
| --------------- |---------------------------------|
| **Report Date** | Date of Submission (2024/07/06) |
| **Submitted by**| Kishan Sagathiya                |


## Member details

- Matrix username: @kishanmsagathiya:matrix.org
- Polkadot address: 13DWAWRTVpkPwWdFDmtUfh73KeCWMiJqEV84xRwpg34EZt8Y
- Current rank: 1
- Date of initial induction:
- Date of last report: NA
- Area(s) of Expertise/Interest: Gossamer Node, Parachain Subsystems

## Reporting period

- Start date: 2022/11/25
- End date: 2024/07/06

## Evidence
My contributions to Polkadot Ecosystem has been primarily through my work in Gossamer.
At Gossamer, I lead, plan and contribute to the work of implementing the parachain protocol of Polkadot. In a nutshell, my contributions to Gossamer could be described as 
- Creating basis for parachain protocol (runtime imports, some missing host apis)
- Creating overseer
- Implementing Collator Protocol
- Implementing the Network Bridge
A significant part of my work at Gossamer is planning (creating issues) for parachain protocol and reviewing PRs

Below is my list of contributions

| Areas of Contribution                         | Tasks                  | Links                                                                 |Notes |
|-----------------------------------------------|------------------------|-----------------------------------------------------------------------|--|
| Gossamer Node, Parachains Protocol   |   Implemented extra parachain host runtime API calls (ParachainHost_persisted_validation_data, ParachainHost_validation_code)  | [ChainSafe PR 3237](https://github.com/ChainSafe/gossamer/pull/3237)  |  |
|  | Introduced parachain candidate validation | [ChainSafe PR 3249](https://github.com/ChainSafe/gossamer/pull/3249)  |  |
|  | feat(lib/runtime): add extra required runtime imports for parachain validation (`ext_default_child_storage_clear_prefix_version_2`, `ext_default_child_storage_root_version_2`, `ext_offchain_index_clear_version_1`) | [ChainSafe PR 3254](https://github.com/ChainSafe/gossamer/pull/3254)  |  |
|  |  chore(dot/network): added common request-response protocol  | [ChainSafe PR 3334](https://github.com/ChainSafe/gossamer/pull/3334)  |  |
|  |   feat(lib/parachain): added parachain service and registering protocols  | [ChainSafe PR 3277](https://github.com/ChainSafe/gossamer/pull/3277)  |  |
|  |move `lib/parachain` to `dot/parachain`| [ChainSafe PR 3429](https://github.com/ChainSafe/gossamer/pull/3429)  |  |
|  | chore(parachain): use wazero instead of wasmer | [ChainSafe PR 3462](https://github.com/ChainSafe/gossamer/pull/3462)  |  |
|  | added parachain related reputation values and reasons | [ChainSafe PR 3498](https://github.com/ChainSafe/gossamer/pull/3498)  |  |
|  |  feat(dot/parachain): added overseer signals  | [ChainSafe PR 3638](https://github.com/ChainSafe/gossamer/pull/3638)  |  |
| Gossamer, Parachains Protocol, Collator Protocol | collator protocol skeleton | [ChainSafe PR 3512](https://github.com/ChainSafe/gossamer/pull/3512)  |  |
|  |  feat(parachain/collator): handle Declare message received by a collator  | [ChainSafe PR 3529](https://github.com/ChainSafe/gossamer/pull/3529)  |  |
|  |  feat(parachain/collator): handle AdvertiseCollation message received by a collator | [ChainSafe PR 3535](https://github.com/ChainSafe/gossamer/pull/3535)  |  |
|  | feat(parachain/overseer): added message forwarding in overseer | [ChainSafe PR 3546](https://github.com/ChainSafe/gossamer/pull/3546)  |  |
|  | feat(parachain/collator): handle Seconded overseer message | [ChainSafe PR 3557](https://github.com/ChainSafe/gossamer/pull/3557)  |  |
|  |  feat(parachain/collator): handle backed overseer message | [ChainSafe PR 3559](https://github.com/ChainSafe/gossamer/pull/3559)  |  |
|  |  collator protocol collator side skeleton | [ChainSafe PR 3825](https://github.com/ChainSafe/gossamer/pull/3825)  |  |
|  |   emit network events and handle them in collator protocol  | [ChainSafe PR 3827](https://github.com/ChainSafe/gossamer/pull/3827)  |  
|  | handle active leaves update in collator protocol | [ChainSafe PR 3829](https://github.com/ChainSafe/gossamer/pull/3829)  |  
| Gossamer, Parachains Protocol, Network Bridge |   feat/parachain: network bridge skeleton | [ChainSafe PR 3885](https://github.com/ChainSafe/gossamer/pull/3885)  |  
| Gossamer Node, Miscellaneous  | feat(lib/babe): Submit BABE equivocation report  | [ChainSafe PR 2947 ](https://github.com/ChainSafe/gossamer/pull/2947) |  |
|     |  fix(blockstate): if blocktree fails to search a hash in memory, load it from disk  | [ChainSafe PR 3059](https://github.com/ChainSafe/gossamer/pull/3059)  |  |
|   |  fix(lib/grandpa): on verifying block justification, compare given block hash with finalised hash  | [ChainSafe PR 3081](https://github.com/ChainSafe/gossamer/pull/3081)  |  |
|  |  chore(types/digest): remove ChangesTrieRootDigest  | [ChainSafe PR 3082](https://github.com/ChainSafe/gossamer/pull/3082)  |  |
|     |  added Runtime Environment Updated digest   | [ChainSafe PR 3083](https://github.com/ChainSafe/gossamer/pull/3083)  |  |
|     |   Change GetBlockByNumber to GetBlocksByNumber and return multiple blocks    | [ChainSafe PR 3097](https://github.com/ChainSafe/gossamer/pull/3097)  |  |
|     |  fix(dot/state) : Retrieve the parent header in case of KeyNotFound | [ChainSafe PR 3119](https://github.com/ChainSafe/gossamer/pull/3119)  |  |
|     |  fix(dot/state): fix a bug in IsDescendantOf | [ChainSafe PR 3125](https://github.com/ChainSafe/gossamer/pull/3125)  |  |
|     |   (chore/runtime): don't use CoreVersion on creating an instance  | [ChainSafe PR 3233](https://github.com/ChainSafe/gossamer/pull/3233)  |  |
|     |   task(runtime): use just one runtime instance interface | [ChainSafe PR 3238](https://github.com/ChainSafe/gossamer/pull/3238)  |  |
|     | fix(dot): use tempDir in tests as base path to avoid creating dot/~ | [ChainSafe PR 3363](https://github.com/ChainSafe/gossamer/pull/3363)  |  |
| | fix: add a limit of number of bytes while scale decoding a slice | [ChainSafe PR 3733](https://github.com/ChainSafe/gossamer/pull/3733)  |  |