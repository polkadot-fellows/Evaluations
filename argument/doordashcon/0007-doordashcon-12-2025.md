# Argument-0007: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/12/27)                                                             |
| **Submitted by**| Jesse Chejieh                                                                        |


## Member details

- Matrix username: @doordashcon/:matrix.org
- Polkadot address: 12zsKEDVcHpKEWb99iFt3xrTCQQXZMu477nJQsTBBrof5k2h
- Current rank: II
- Date of initial induction: 2022/09/29
- Date of last report: 2025/06/20
- Area(s) of Expertise/Interest: FRAME


## Reporting period
- Start date: 2025/08/10
- End date: 2025/12/27

## Argument
During this reporting period I have made contributions to FRAME infrastructre, focusing on enhancing observability, improving treasury functionality and strengthening developer tooling.

### 1. Multi-Block Migration Observability and Tooling
Enhancing the [multi-block migration framework](https://github.com/paritytech/polkadot-sdk/pull/9461) with improved transparency and tooling support during runtime upgrades. This work enables external monitoring systems and developers to easily identify which parts of the chain’s storage are affected by a migration, reducing operational risk and improving the safety and observability of network upgrades. These improvements help teams coordinate upgrades more effectively and give the community greater confidence during migration processes.

### 2. Treasury Payout System Enhancement for Asset Categories
I am working on extending the [treasury pallet](https://github.com/paritytech/polkadot-sdk/pull/10381) to support spending from asset categories. This allows governance tracks to define spending policies in broader terms (e.g., b"USD*" rather than a single asset ID), making treasury management more flexible, future-proof, and easier to administer in multi-asset environments. This upgrade maintains full backward compatibility while paving the way for more sophisticated treasury operations as the ecosystem grows.

### 3. Transaction Chain Batching Implementation
[Transaction chain batching feature](https://github.com/paritytech/polkadot-sdk/pull/10234) addresses a longstanding request for transaction composition in FRAME. This feature enables the output of one transaction to serve as input for subsequesnt transactions within the same batch call.

By capturing specified event data into a dispatch context during event emission, these items become available for subsequent transactions in the chain. This extends the event parsing and expansion logic to handle the new capture semantics while maintaining full backward compatibility.

### Advocacy
Championing the shift from passive ledgers to self-executing protocols. The Task API has the potential to move operations from passive ledger execution to condition based automations in permissionless systems without compromising security, privacy or performance.
In a recent [forum post on autonomous operations](https://forum.polkadot.network/t/autonomous-operations/16466), I reiterated the bottlenecks in systems like the People Registry that require self executing logic to overcome them.

 ## Voting record
 |  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
 |---|---|---|---|---|
 |I  |90%   |N/A   |   |  |
 |II |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e undefined% voting activity). Out of xx referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus x times (i.e undefined% voting agreement). |  |
 |III|70%   |100%  |   |  |
 |IV |60%   |90%   |   |  |
 |V  |50%   |80%   |   |  |
 |VI |40%   |70%   |   |  |
