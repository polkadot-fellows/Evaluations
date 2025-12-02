# Argument-0006: Retention at Rank I

|                 |                   |
| --------------- |-------------------|
| **Report Date** | 2025/10/22        |
| **Submitted by**| Damilare Akinlose |

---

## Member details

- **Matrix username**: `@dharjeezy/:matrix.org`
- **Polkadot address**: `12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW`
- **Current rank**: `1`
- **Date of initial induction**: `2024-04-29`
- **Date of last report**: `2025/07/23`
- **Area(s) of Expertise/Interest**: `FRAME/Runtime & Node`

---

## Reporting period

- **Start date**: 2025/07/23
- **End date**: 2025/10/22

---

## Argument

I am applying for Rank I retention.

During this period, my contributions have focused on enhancing the flexibility, reliability, and efficiency of both the Polkadot SDK runtime and the underlying `litep2p` networking stack. 
I have taken on issues that improve the developer experience, strengthen network resilience, and ensure the correctness of core pallets. 
My work demonstrates a commitment to delivering high-quality, impactful solutions across multiple domains of the ecosystem.

Below is a summary of my key contributions:

### Flexible & Developer-Focused

#### **Allow Specifying a Storage Deposit Payer for Calls**
To enhance the flexibility of transaction payments, I implemented a feature allowing a specified account—other than the transaction's origin—to pay for storage deposits. 
As detailed in [PR #9543](https://github.com/paritytech/polkadot-sdk/pull/9543), this change removes a significant limitation and enables more complex use cases where transaction costs can be sponsored or managed by a separate entity, improving the overall developer experience.
Though, this change was deeemed redundant based on the new updates to pallet revive.

#### **Expose Block Number Provider Name as a Constant**
I finished the implementation to expose the name of the `BlockNumberProvider` as a runtime constant. 
Tracked in [PR #9091](https://github.com/paritytech/polkadot-sdk/pull/9091), this feature is crucial for application developers who need to differentiate between a parachain's local block number and the Relay Chain's block number.

---

### Reliable & Resilient

#### **`proxy.removeProxies`: Emit Event on Clearing All Delegates**
I added an event for the `proxy.removeProxies` extrinsic, which calls `remove_all_proxy_delegates`. Previously, this action lacked an event, creating an observability gap that was inconsistent with `addProxy` and `removeProxy`.
As implemented in [PR #10073](https://github.com/paritytech/polkadot-sdk/pull/10073), an event is now emitted with the delegator's `AccountId`, ensuring this significant action is recorded on-chain and available for indexers.

#### **Introduce `try_state` Hook for Pallet-Alliance**
To bolster the integrity of `pallet-alliance`, I introduced a `try_state` hook to verify key storage invariants. This proactive measure, implemented in [PR #10000](https://github.com/paritytech/polkadot-sdk/pull/10000), helps ensure the pallet's state remains consistent and correct during runtime upgrades or state transitions, 
preventing potential bugs.

#### **`litep2p`: Implement Periodic Ping for Connection Liveness**
I continued with the challenging implementation to add periodic pings in `litep2p`, ensuring reliable detection of broken connections. The core difficulty, as discussed in [PR #416](https://github.com/paritytech/litep2p/pull/416), was adhering to the libp2p specification of using a single, long-lived substream without artificially keeping the connection alive. 
My solution involved introducing a stateful peer management system, and a commitment to spec-compliant solution.

---

### Efficient & Optimized

#### **`litep2p`: Optimize Propagation of Dial Failure Messages**
I improved the efficiency of the `TransportManager` by refining how `DialFailure` events are propagated. In [PR #443](https://github.com/paritytech/litep2p/pull/443), I modified the logic to send detailed address failure information **only** to the Kademlia protocol handler, which requires it for its address store. Other protocols now receive a more lightweight event, reducing unnecessary data propagation and improving the performance of the transport layer.

#### **`litep2p`: Optimize WebRTC Decoding Buffer**
I optimized the WebRTC transport by making the decoding buffer size configurable. This change, part of [PR #442](https://github.com/paritytech/litep2p/pull/442), allows node operators to set a sensible default while providing the flexibility to adjust it for different environments. This prevents over-allocation of memory and improves decoding efficiency.

---

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e undefined% voting activity). Out of xx referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus x times (i.e undefined% voting agreement).  |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

---

## Misc

- [ ] Question(s):
- [ ] Concern(s):
- [ ] Comment(s):