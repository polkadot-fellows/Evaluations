# Evidence-0001: Retention at Rank 1

|                  |                                 |
| ---------------- | ------------------------------- |
| **Report Date**  | Date of submission (2024/07/02) |
| **Submitted by** | Eclesio Melo Junior             |

## Member details

- Matrix username: @eclesiomelo:matrix.org
- Polkadot address: 14Ak9rrF6RKHHoLLRUYMnzcvvi1t8E1yAMa7tcmiwUfaqzYK
- Current rank: 1
- Date of initial induction: Seeding
- Date of last report: N/A
- Area(s) of Expertise/Interest: Alternative Client, Polkadot Spec, Network Syncronizathion, Consensus Layer, Virtual Machines

## Reporting period

- Start date: 2023/07/01
- End date: 2024/06/30

## Evidence

Hello everyone, My name is Eclesio and I have been a Gossamer Core Developer from almost 3 years. Since last year my challenge is to make Gossamer a stable node and make it sync to the Westend network tip. Along this path I was able to understand a lot of the Polkadot internals, how pallets works and are composed.

I've also written a long-form post explaining how Polkadot epochs works from the host point of view (there is a small explanation on how it works on the runtime side): https://hackmd.io/q5O1XJ2YRw2UbU-xHEpK5g

| Areas of Contribution      | Tasks                                                                                                                                                                   | Links                                             | Notes                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Gossamer BABE              | Fix a Timestamp must match CurrentSlot bug in the BABE pkg                                                                                                              | https://github.com/ChainSafe/gossamer/pull/3133   |                                                                                                                           |
| Block Verification         | Cache slots to data header decreases the equivocation check from 18s to 3s                                                                                              | https://github.com/ChainSafe/gossamer/pull/3364   |                                                                                                                           |
| Network Sync               | Fix Gossamer sync by changing a round and set id validation given that in Westend there are a lot of weird cases that lead to rounds being messed up in the same set id | https://github.com/ChainSafe/gossamer/pull/3167   |                                                                                                                           |
| Gossamer Runtime Layer     | Reduced the number of in memory runtime instances in Gossamer                                                                                                           | https://github.com/ChainSafe/gossamer/pull/3151   |                                                                                                                           |
| Trie Package               | Fixing the correct state trie V1 root hash calculation, allowing Gossamer to execute blocks when the new trie was introduced in the relay chain                         | https://github.com/ChainSafe/gossamer/pull/3739   |                                                                                                                           |
| Gossamer Runtime Layer     | Introduces nested transactions                                                                                                                                          | https://github.com/ChainSafe/gossamer/pull/3670   |                                                                                                                           |
| Gossamer Runtime Allocator | Refactored Gossamer Freeing Bump Heap Allocator                                                                                                                         | https://github.com/ChainSafe/gossamer/pull/3570   |                                                                                                                           |
| Gossamer Runtime Layer     | Doing the correct page type cast to uint32                                                                                                                              | https://github.com/ChainSafe/gossamer/pull/3588   | This task required a some investigations on Wazero Go library                                                             |
| Gossamer Runtime Layer     | panic while executing a block `wasm error: out of bounds memory access`                                                                                                 | https://github.com/ChainSafe/gossamer/issues/3774 | With this task we were able to introduce Compiled Runtime Cache that enables Gossamer to bootstrap a runtime quickly when |

## Additional Note

Contributed with Substrate by identifying a bug in the peer reputation management where spamming Grandpa: Neighbor message increases reputation - https://github.com/paritytech/substrate/issues/12191
