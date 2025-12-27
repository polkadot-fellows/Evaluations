# Argument-0005: Retention at Rank II

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

### 1. Enhancing Multi-Block Migration Observability and Tooling
I Implemented an enhancement to the multi-block migration framework that improves chain observability and developer experience. This [contribution](https://github.com/paritytech/polkadot-sdk/pull/9461) introduces the ability for multi-block migrations to declare which storage prefixes will be modified, enabling external tooling and monitoring systems to identify potentially affected state during migration execution.

Improvements include exposing migrating prefixes through the `migrating_prefixes()` method in the `SteppedMigrations` trait, which allows migrations to declare their storage impact. This work also introduced comprehensive status reporting via the view functions; `ongoing_status()`, `progress()`, `affected_prefixes()` and `status()` that provide real-time insights into migration state. 

These changes Provide runtime developers with neccessary visibility into migration progress and affected storage prefixes, ensuring consistency across all migration types, including single migrations and tuple collections, with thorough testing for various migration configurations and failure scenerios.


### 2. Treasury Payout System Enhancement for Asset Categories
I am working on enabling the [treasury pallet](https://github.com/paritytech/polkadot-sdk/pull/10381) `spend` from an asset category rather than just a specific `asset_kind`, This work extends `SpendAsset` to support a new `Category` variant, enabling tracks define spending in bytes(i.e. b"USD*") rather than specific asset IDs. 
It extends `PaymentState` to handle multiple payment executions and retry partial executions during payout, intorducing `PaymentExecution` for single and multiple payments to a single benefitiary during payouts and also `AssetCategoryManager` trait that provides category membership and balance checking during payouts, mainitaining backward compatibility with existing single `asset_kind` spending.  


### 3. Transaction Chain Batching Implementation
[Transaction chain batching feature](https://github.com/paritytech/polkadot-sdk/pull/10234) addresses a longstanding request for transaction composition in FRAME. This feature enables the output of one transaction to serve as input for subsequesnt transactions within the same batch call.

This implementaion introduces #[pallet::capture_for_chain_batch] *still workshoping the name*, that can be applied to event enums, along with field-level #[chain_batch(capture = "name")] attriibutes to specify which event fields should be captured for reuse.
This system automatically captures specified event data into a dipatch context during event deposition, making these items available for subsequent transactions in the chain. Making modifications to the procedural macro system, extending the event parsing and expansion logic to handle the new capture sematics while maintaining full backward compatibility.

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
