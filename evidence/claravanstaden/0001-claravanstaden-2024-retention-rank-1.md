# Evidence-0001: Retention at Rank 1

|                 |                |
| --------------- |----------------|
| **Report Date** | 2024/09/11     |
| **Submitted by**| claravanstaden |


## **Member details**

* Matrix username: @claravanstaden:matrix.org
* Polkadot address: 12aoZXwbUzsv3z5HF5HCrtEwBJYCeKne6rYsxFEKDZ86Wdv8
* Current rank: 1
* Date of initial induction: 2024/06/17
* Date of last report: N/A
* Area(s) of Expertise/Interest: Snowbridge

## **Reporting period**

* Start date: 2024/07/11
* End date: 2024/10/11

## **Evidence**

During the last two months, I focused on three major themes:

1. **Cost Reduction to run Snowbridge**: Reduced operational costs to alleviate Treasury pressure and enhance financial sustainability.
2. **Enablement of Snowbridge on Paseo**: To facilitate more stable integration testing for parachain teams.
3. **Preparation for Ethereum Hard-Fork (Electra)**: Ensure Snowbridge compatibility with the upcoming Electra upgrade.

### Snowbridge Paseo Setup

I collaborated with the Paseo team to deploy Snowbridge on the Paseo network:

* Set up BridgeHub on Paseo from scratch and applied Snowbridge updates with each release.
* Debugged issues and made fixes to ensure all tests in the runtime repository passed.
* Added integration testing to the runtime repository to identify issues before deployment.
* Set up all off-chain infrastructure required for Snowbridge on Paseo, including a Sepolia Lodestar node and off-chain relayers.

**PRs**:

* [Paseo Runtime Pull Request \#95](https://github.com/paseo-network/runtimes/pull/95)
* [Paseo Runtime Pull Request \#128](https://github.com/paseo-network/runtimes/pull/128)
* [Paseo Runtime Pull Request \#127](https://github.com/paseo-network/runtimes/pull/127) (contributed fixes to this PR)

**Current Status**: Awaiting deployment of BridgeHub 1.2.8 on Paseo. Snowbridge is deployed but currently unusable due to a regression introduced on AssetHub (upgrade from 1.2.5 to 1.2.6).

### BridgeHub Upgrade to 1.2.8

With the Ethereum Deneb hardfork, a major improvement was added that enabled syncing Ethereum headers selectively, instead of syncing all headers. This reduced the cost to run the bridge massively, from around $17,000 per month to around $1,700. I was responsible for getting this feature released as soon as possible after Snowbridge launched, to reduce pressure on the Treasury. The upgrade executed on August 5th without issues and has been stable since.

The reduced cost to relay Ethereum headers can be verified via the [Snowbridge Beacon Relayer Balance](https://bridgehub-polkadot.subscan.io/account/16DWunYRv2q29SMxqgrPGhob5az332hhLggSj2Rysk3g1rvk?tab=balance_history).

PR: [Polkadot SDK Pull Request \#4829](https://github.com/paritytech/polkadot-sdk/pull/4829)   
Referendum: [Polkadot Referenda \#1002](https://polkadot.polkassembly.io/referenda/1002)

### Snowbridge Ethereum Client Free Consensus Updates

To further reduce running costs, I completed a feature for free Ethereum consensus updates if the header is valid, new enough, and has not been imported before. This will be included in the upcoming `stable2409` Polkadot-SDK release.

PR: [Polkadot SDK Pull Request \#5201](https://github.com/paritytech/polkadot-sdk/pull/5201)

### Governance Commands to Halt Snowbridge

I contributed to our CLI tool to generate a preimage for halting the bridge in emergencies. This tool enables halting specific components, such as the Ethereum client or cross-chain transfers (from Ethereum to Polkadot or Polkadot to Ethereum), or the entire bridge.

PR: [Snowbridge Pull Request \#1248](https://github.com/Snowfork/snowbridge/pull/1248)  
Public Documentation: [Emergency Pause Documentation](https://app.gitbook.com/o/bDGMcdShFBeGc3v6VzHf/s/tC80IPpnYgEJmgOYIpqZ/operations/governance-and-operational-processes#id-1.-emergency-pause)  
Referendum: [Fellowship Referenda \#150](https://collectives.subsquare.io/fellowship/referenda/150)

### Ethereum Electra Upgrade (WIP)

The upcoming Ethereum Electra hard fork, expected in late 2024 or early 2025, will bring breaking changes to the Altair light client sync protocol. I am working on the necessary updates to the Snowbridge Ethereum light client to maintain compatibility.

**Altair Light Client Sync Protocol Changes**: [GitHub Link](https://github.com/ethereum/consensus-specs/blob/dev/specs/electra/light-client/sync-protocol.md)  
**Snowbridge Ethereum Client Changes PR**: [Polkadot SDK Pull Request \#178](https://github.com/Snowfork/polkadot-sdk/pull/178)  
**Companion Off-Chain Relayer Changes PR**: [Snowbridge Pull Request \#1283](https://github.com/Snowfork/snowbridge/pull/1283)

## **Voting record**

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
| ----- | ----- | ----- | ----- | ----- |
| I | 90% | N/A | There were no proposals that I have been eligible to vote for for my rank 1\. |  |
| II | 80% | N/A |  |  |
| III | 70% | 100% |  |  |
| IV | 60% | 90% |  |  |
| V | 50% | 80% |  |  |
| VI | 40% | 70% |  |  |



