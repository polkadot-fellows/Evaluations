# Argument-0006: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/05/06)                                                             |
| **Submitted by**| Alexandru Vasile                                                                            |


## Member details

- Matrix username: @lexnv:parity.io
- Polkadot address: 14Mjra9hNggCSLyVv3AmtvpjeyBhUMwiEEBXGFidu3ZWTEQN
- Current rank: I
- Date of initial induction: 2025/02/12
- Date of last report: 2026/02/02
- Area(s) of Expertise/Interest: `Substrate Node`, `Substrate RPC`, `FRAME`


## Reporting period

- Start date: 2026/02/02
- End date: 2026/05/06


## Argument

Over the recent months, my efforts have been focused on improving the reliability and observability of the Polkadot networking and syncing stack. I have investigated several edge-cases that degraded the block confidence metrics of parachains on both Kusama and Polkadot, and contributed multiple fixes to the syncing engine, the collator protocol, and the underlying litep2p networking library. This work has been crucial in ensuring the stability and performance of the network under the increased load from Elastic Scaling.

### Block Confidence Investigations

The lower block confidence observed on Polkadot Asset Hub (~96%) compared to Kusama (~99%) prompted a deep-dive into the validator-side and collator-side protocols, as well as the syncing pipeline. The investigation, tracked in [polkadot-sdk #11377](https://github.com/paritytech/polkadot-sdk/issues/11377), uncovered a number of issues affecting block fetching latency, sync recovery, and observability.

**Syncing engine fixes**

I identified and reported [polkadot-sdk #11916](https://github.com/paritytech/polkadot-sdk/issues/11916), where the syncing engine restarts after importing blocks from forks, due to the peer's `common` number not being decreased after a prior fork. The follow-up [polkadot-sdk #11917](https://github.com/paritytech/polkadot-sdk/pull/11917) forces peers into ancestry search regardless of whether the announcement is the peer's current best, ensuring forks do not silently lead to "block has unknown parent" errors and full sync engine restarts.

I also tracked down a vicious loop affecting non-archive collators with an unfilled block gap. [polkadot-sdk #11330](https://github.com/paritytech/polkadot-sdk/pull/11330) skips block execution when the gap sync has marked blocks as `StateAction::Skip`, preventing the cycle of failed imports, sync restarts and eventual peer banning that was unblocking Kusama YAP 3392. The complementary [polkadot-sdk #11332](https://github.com/paritytech/polkadot-sdk/pull/11332) closes missing body gaps in the database for non-archive nodes, preventing nodes from re-requesting the same gap blocks on every restart and wasting bandwidth.

**Collator protocol observability**

To support the block confidence investigation, I contributed two observability improvements to the collator protocol. [polkadot-sdk #11629](https://github.com/paritytech/polkadot-sdk/pull/11629) surfaces previously silent rejections of advertised collations (when validators lack slots or fail `can_second` checks), already deployed on validators and surfacing further issues such as [polkadot-sdk #11625](https://github.com/paritytech/polkadot-sdk/issues/11625). [polkadot-sdk #11600](https://github.com/paritytech/polkadot-sdk/pull/11600) fixes a blindspot in the `collation_fetch_latency` metric, whose 5s upper bound aggregated all high-latency events into a single bucket and obscured the true distribution of network delays.

### litep2p Contributions

I have remained a core contributor to litep2p, focusing on transport-layer reliability, WebRTC stability, and observability.

On the transport manager side, I exposed failed addresses to the transport manager so that dial outcomes can be reasoned about end-to-end ([litep2p #529](https://github.com/paritytech/litep2p/pull/529)), made `accept` asynchronous to close a race window between the service and the transport ([litep2p #525](https://github.com/paritytech/litep2p/pull/525)), and bounded both dial concurrency and the total dialing time so that misbehaving peers cannot stall the manager ([litep2p #538](https://github.com/paritytech/litep2p/pull/538)). I also changed the manager to prioritize public addresses when dialing, which improves connectivity for nodes behind NAT ([litep2p #530](https://github.com/paritytech/litep2p/pull/530)).

On the WebRTC side, I addressed three correctness and stability issues: ensuring the delay future is actually awaited ([litep2p #548](https://github.com/paritytech/litep2p/pull/548)), cleaning stale hashmap entries to avoid memory leaks ([litep2p #549](https://github.com/paritytech/litep2p/pull/549)), and hardening the transport layer so that non-STUN packets cannot panic it ([litep2p #550](https://github.com/paritytech/litep2p/pull/550)).

### Other work

Beyond these core projects, I continue to provide reviews for the Polkadot-SDK in my area of expertise, and to support the WebRTC implementation in litep2p so that the integration remains smooth and efficient for the broader ecosystem.


## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referendums available for my rank to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 
