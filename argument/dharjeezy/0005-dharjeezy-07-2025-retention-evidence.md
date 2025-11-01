# Argument-0005: Retention at Rank I

|                 |                   |
| --------------- |-------------------|
| **Report Date** | 2025/07/23        |
| **Submitted by**| Damilare Akinlose |

---

## Member details

- **Matrix username**: `@dharjeezy/:matrix.org`
- **Polkadot address**: `12GyGD3QhT4i2JJpNzvMf96sxxBLWymz4RdGCxRH5Rj5agKW`
- **Current rank**: `1`
- **Date of initial induction**: `2024-04-29`
- **Date of last report**: `2025/04/29`
- **Area(s) of Expertise/Interest**: `FRAME/Runtime & Node`

---

## Reporting period

- **Start date**: 2025/06/01
- **End date**: 2025/09/30

---

## Argument

I am applying for Rank I retention.

In this cycle, my focus has been on enhancing the Polkadot SDK's efficiency, reliability, and interoperability. I have delivered key improvements across various pallets and libraries, from optimizing storage operations and improving network resilience to enabling cross-system functionality and enhancing developer experience.

Below is a summary of my key contributions:

### Efficient & Performant

#### **EPMB / signed pallet: Lazy Deletion for Leaders**
I implemented support for the lazy deletion of leaders in the `pallet-election-provider-multi-phase`'s `signed` pallet. The previous `take_leader_with_data` function forced a full deletion of all associated data pages, which was inefficient. By introducing a `with_data: bool` flag, this [PR #9025](https://github.com/paritytech/polkadot-sdk/pull/9025) allows for the removal of a leader without immediately deleting all their submission data, significantly improving performance by deferring storage-intensive operations.

#### **Refactor pallet-bounties to V2 Benchmarking Syntax**
As part of the ongoing effort to modernize the SDK's codebase, I refactored `pallet-bounties` to use the new V2 benchmarking syntax. This contribution, tracked in [PR #8952](https://github.com/paritytech/polkadot-sdk/pull/8952), ensures the pallet's benchmarks are consistent with current standards, improving maintainability and accuracy.

---

### Reliable & Observable

#### **Add `poll_index` to Conviction Voting Events**
To improve the indexability of on-chain governance data, I added the `poll_index` field to the `Voted` and `VoteRemoved` events in `pallet-conviction-voting`. As detailed in [PR #8840](https://github.com/paritytech/polkadot-sdk/pull/8840), this change allows indexing services and developers to precisely track voter activity for specific referenda, which was previously not possible with 100% accuracy.

#### **litep2p: Periodic Ping for Connection Liveness**
I enhanced the `ping` mechanism in `litep2p` to send requests periodically, rather than just once upon connection. This implementation, found in [PR #416](https://github.com/paritytech/litep2p/pull/416), aligns with libp2p standards and provides a robust method for detecting broken or stale connections, improving overall network reliability without artificially keeping connections alive.

#### **litep2p: Improved Error Handling in WebRTC Noise Functions**
I finalized the work on improving error handling within the WebRTC-related Noise handshake functions in `litep2p`. This effort, completed in [PR #377](https://github.com/paritytech/litep2p/pull/377), replaces unchecked `unwrap()` calls and assumptions about message sizes with proper error propagation, preventing potential panics and making the implementation more resilient.

---

### Configurable & Extensible

#### **Port `remote-proxy` Pallet to Polkadot-SDK for Westend**
Addressing a critical need for teams building on parachains, I initiated the process to port the `remote-proxy` pallet to the Polkadot-SDK and enable it on Westend. As outlined in [PR #9088](https://github.com/paritytech/polkadot-sdk/pull/9088), this will allow proxy relationships to function across different systems, a vital feature for post-Asset Hub migration scenarios. This work unblocks projects that rely on proxies for seamless user experiences.

#### **Expose the `BlockNumberProvider` Used by Pallets**
To improve the developer experience, especially in a post-Asset Hub Migration world, I am working on a method to expose which `BlockNumberProvider` a pallet is configured to use. By exposing the provider's name in the metadata, [PR #9091](https://github.com/paritytech/polkadot-sdk/pull/9091) allows DApp developers to reliably distinguish between local and Relay Chain block numbers, preventing critical errors in applications that depend on timing.

#### **Security: Proof of Key Ownership**
I collaborated with other contributors on introducing a proper proof of key ownership for BLS keys in the runtime. This foundational work, detailed in the discussion for [PR #9258](https://github.com/paritytech/polkadot-sdk/pull/9258), is essential for generating and verifying secure proofs and will be revisited once prerequisite pull requests are merged.

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