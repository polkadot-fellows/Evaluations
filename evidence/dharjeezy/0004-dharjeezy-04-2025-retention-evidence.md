# Argument-0004: Retention at Rank I

|                 |                   |
| --------------- |-------------------|
| **Report Date** | 2025/04/29        |
| **Submitted by**| Damilare Akinlose |


## Member details

- Matrix username: `@dharjeezy/:matrix.org`
- Polkadot address: `12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW`
- Current rank: `1`
- Date of initial induction: `2024-04-29`
- Date of last report: `2025-01-13`
- Area(s) of Expertise/Interest: `FRAME/Runtime & Node`


## Reporting period

- Start date: 2025/01/31
- End date: 2025/05/31


## Argument

### 1. BlockNumberProvider for Pallet Election Provider Multiphase
To support the migration of pallets from the Relay Chain to Asset Hub, I extended the BlockNumberProvider pattern to [pallet-election-provider-multi-phase](https://github.com/paritytech/polkadot-sdk/pull/7515).
This ensures that the pallet can deterministically use either the system block number or an externally provided block number, 
simplifying state migration and preventing inconsistencies caused by block number discrepancies across chains.
Similar to previous work done on other pallets, this change introduces a configurable block number source, enabling runtime flexibility and ensuring a smooth migration path.

### 2. Add retracted event in fork aware transaction pool 
I worked on extending fatxpool to emit a [Retracted event](https://github.com/paritytech/polkadot-sdk/pull/8093) whenever the best chain is switched.
To approach this, I had discussions on the issue to clarify the correct behavior and studied the internals of the chain selection process during block import, particularly how the best block is determined via the SelectChain trait.
From the transaction pool’s perspective, a chain switch is detected when the tree_route field of a ChainEvent contains a non-empty retracted path.
Based on this understanding, I introduced Retracted event to be emitted whenever a retraction occurs.

### 3. Txpool: use tracing for structured logging
I refactored the transaction pool (txpool) to replace usage of the traditional log crate with the  [tracing crate](https://github.com/paritytech/polkadot-sdk/pull/8001), enabling structured and contextual logging.
This refactoring allows logs to carry richer metadata (such as fields and spans), improving debugging and monitoring capabilities.
I updated all logging statements to use tracing macros (info!, warn!, error!, etc.) while preserving the original log levels and message formats where applicable, ensuring compatibility and minimal disruption.
This change prepares the txpool for environments where structured telemetry and distributed tracing are important.

### 4. Fatxpool: use dyn instead of TransactionPoolWrapper
While working on fatxpool, I am currently exploring replacing the TransactionPoolWrapper pattern with a dynamic trait object  [(dyn FullClientTransactionPool)](https://github.com/paritytech/polkadot-sdk/issues/5489) to achieve a cleaner and more flexible abstraction.
After a brief discussion and deeper investigation, I found that although the dyn approach should simplify the structure conceptually, it would require significant refactoring across multiple modules because the transaction pool traits are heavily generic and involve associated types.
This will impact many files. I am continuing to explore ways to introduce this improvement in a more incremental and manageable way.

### 5. Staking: Full Unbonding Support
[The full unbonding support for validators/nominators in staking finally got merged in.](https://github.com/paritytech/polkadot-sdk/pull/3811)
This feature enables validators and nominators to get chilled and fully unbond their stake in a single operation, without requiring separate actions for chilling and unbonding.

### 6. Litep2p: Optimize RoutingTable::closest to Clone Only Necessary KademliaPeer Entries

In the litep2p library, I worked on [optimizing the RoutingTable::closest implementation](https://github.com/paritytech/litep2p/pull/326) to reduce unnecessary cloning of KademliaPeer entries.
Previously, `RoutingTable::closest` relied on `KBucket::closest_iter`, which cloned all peers within a bucket before selecting the closest nodes.
After reviewing the implementation, I identified that this could be optimized by sorting the entries in place, yielding references instead of cloning upfront, and cloning only the `KademliaPeer` instances that are actually returned by `RoutingTable::closest`.
This change reduces memory allocations and improves efficiency, especially when operating over large Kademlia buckets with many entries.

### 7. Litep2p: Improve Error Handling in WebRTC-Related Noise Functions
I am working on improving the [error handling in the WebRTC-related Noise handshake functions](https://github.com/paritytech/litep2p/pull/377) within the litep2p library.
Currently, these functions make unchecked assumptions about message sizes and contain multiple unwrap() calls, which could lead to panics or undefined behavior in edge cases.
The work done and to be done involves replacing these unchecked operations with proper error propagation and introducing well-defined error types.

I am humbly applying for Rank I retention


## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e undefined% voting activity). Out of xx referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus x times (i.e undefined% voting agreement).  |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s): 

