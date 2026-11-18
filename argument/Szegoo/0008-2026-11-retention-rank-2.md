# Argument-0008: Retention at Rank II

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/11/18                                                                                  |
| **Submitted by**| Sergej Sakac                                                                                |


## Member details

- Matrix username: @sergej.sakac:parity.io
- Polkadot address: 126X27SbhrV19mBFawys3ovkyBS87SGfYwtwa8J2FjHrtbmA
- Current rank: II
- Date of initial induction: Seeding
- Date of last report: 2026/08/09
- Link to last report: [Argument-0007](https://github.com/polkadot-fellows/Evaluations/pull/332)
- Area(s) of Expertise/Interest: Polkadot runtime, Coretime, PSM, Price Oracle, On-demand, XCM


## Reporting period

- Start date: 2026/08/10
- End date: 2026/11/18


## Argument

During this reporting period, my work was focused on pUSD, the price oracle and Coretime.

### pUSD

- **PSM on Asset Hub Polkadot**: Added the multi-instance PSM to the Asset Hub Polkadot runtime ([runtimes#1252](https://github.com/polkadot-fellows/runtimes/pull/1252)) together with remote tests ([runtimes#1254](https://github.com/polkadot-fellows/runtimes/pull/1254)), after backporting it to `stable2606` ([polkadot-sdk#12952](https://github.com/paritytech/polkadot-sdk/pull/12952)).
- **PSM fixes**: Corrected the creation-deposit footprint ([polkadot-sdk#12811](https://github.com/paritytech/polkadot-sdk/pull/12811)), rejected the `None` origin as a PSM admin ([polkadot-sdk#13256](https://github.com/paritytech/polkadot-sdk/pull/13256)), simplified PSM account handling ([polkadot-sdk#13626](https://github.com/paritytech/polkadot-sdk/pull/13626)), and removed the PSM reset migration from Asset Hub Westend ([polkadot-sdk#13137](https://github.com/paritytech/polkadot-sdk/pull/13137)).

### Price Oracle

- Contributed to the price oracle ([polkadot-sdk#13241](https://github.com/paritytech/polkadot-sdk/pull/13241)): per-market votes and pair quorum ([polkadot-sdk#13346](https://github.com/paritytech/polkadot-sdk/pull/13346)), governance-registered pairs and cross rates ([polkadot-sdk#13393](https://github.com/paritytech/polkadot-sdk/pull/13393)), generic market pricing ([polkadot-sdk#13396](https://github.com/paritytech/polkadot-sdk/pull/13396)), exchange definitions ([polkadot-sdk#13249](https://github.com/paritytech/polkadot-sdk/pull/13249), [polkadot-sdk#13350](https://github.com/paritytech/polkadot-sdk/pull/13350)), logging ([polkadot-sdk#13555](https://github.com/paritytech/polkadot-sdk/pull/13555)) and metrics ([polkadot-sdk#13669](https://github.com/paritytech/polkadot-sdk/pull/13669)).

### Coretime

- **RFC-0175**: Authored [RFC-0175](https://github.com/polkadot-fellows/RFCs/pull/175), which proposes moving on-demand Coretime sales from the relay chain to the Coretime chain. A draft implementation is in [polkadot-sdk#12936](https://github.com/paritytech/polkadot-sdk/pull/12936).
- **Broker fixes**: The auto-renewal fix from the last report was merged ([polkadot-sdk#12750](https://github.com/paritytech/polkadot-sdk/pull/12750)). Fixed double counting of re-pooled regions in the instantaneous pool ([polkadot-sdk#13311](https://github.com/paritytech/polkadot-sdk/pull/13311)), with a follow-up in review ([polkadot-sdk#13712](https://github.com/paritytech/polkadot-sdk/pull/13712)).
- **Broker `sale_index` migration**: Added the `pallet-broker` v5 migration to Coretime Polkadot and Kusama ([runtimes#1357](https://github.com/polkadot-fellows/runtimes/pull/1357)).
- **RFC-17 implementation**: Continued addressing review feedback on `pallet-coretime-market` ([polkadot-sdk#11802](https://github.com/paritytech/polkadot-sdk/pull/11802)).

### Other fixes

- **`pallet-asset-conversion`**: Fixed users losing the remainder of their funds on a failed swap ([polkadot-sdk#13601](https://github.com/paritytech/polkadot-sdk/pull/13601)) and frozen or blocked pools being treated as usable ([polkadot-sdk#13598](https://github.com/paritytech/polkadot-sdk/pull/13598)).
- **`pallet-bounties`**: Payouts now only use spendable funds and no longer ignore failed transfers ([polkadot-sdk#13673](https://github.com/paritytech/polkadot-sdk/pull/13673)).
- **`pallet-staking-async`**: Only spendable funds are moved out of expired era pots ([polkadot-sdk#13690](https://github.com/paritytech/polkadot-sdk/pull/13690)).

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   | No referenda available for my rank during this period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
