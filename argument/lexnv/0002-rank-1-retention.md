# Argument-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/05/06)                                                             |
| **Submitted by**| Alexandru Vasile                                                                            |


## Member details

- Matrix username: @lexnv:parity.io
- Polkadot address: 14Mjra9hNggCSLyVv3AmtvpjeyBhUMwiEEBXGFidu3ZWTEQN
- Current rank: I
- Date of initial induction: 2025/02/12
- Date of last report: 2025/02/12
- Area(s) of Expertise/Interest: `Substrate Node`, `Substrate RPC`, `FRAME`


## Reporting period

- Start date: 2025/02/12
- End date: 2025/05/06


## Argument


Over the past few months, I have dedicated my efforts to enhancing the Litep2p networking stack.
My primary focus has been on improving its performance and robustness to ensure it is production-ready for deployment on the Polkadot network.

### Litep2p Network Backend: Stabilization and Performance Improvements

Litep2p is running [live in Kusama](https://github.com/paritytech/polkadot-sdk/pull/7866) and is set to be deployed on Polkadot soon.

From a performance standpoint, the release resolves a key issue in the notification protocol system, where protocols would fail to exit cleanly upon handle drop. This inefficiency previously caused unnecessary CPU load, but with the fix in place, CPU usage in scenarios such as minimal-relay-chains has dropped from **7% to an impressive 0.1%**. This type of gain reflects a clear optimization that directly benefits system performance in production environments.

The release also brings notable robustness improvements. Within the Kademlia protocol, the address store has been optimized by ranking entries based on dialing scores. This not only bounds memory consumption but also improves peer selection efficiency. Additionally, the responses to `FIND_NODE` requests have been limited to the protocol’s replication factor, which prevents overgrowth of the routing table and ensures tighter control over state size. These updates make the system more resilient to both churn and potential manipulation of the routing layer.

The identify codec has been enhanced to better handle malformed or unexpected messages during decoding. This ensures greater tolerance for protocol deviations and contributes to overall network stability. In the Bitswap protocol, the introduction of a write timeout when sending frames prevents indefinite stalls or hangs during data exchange—an important safeguard for maintaining protocol liveness under network variability or adversarial peers. For more details on the Litep2p release, please refer to the [release PR](https://github.com/paritytech/litep2p/pull/382).

### RPC Spec V2

I continued contributing to and maintaining the rpc-v2 specification. Notably, I resolved an issue in the transaction API that failed to properly handle chains launched with InstantSeal. This fix ensures correct transaction handling in such environments, improving the API’s robustness and reliability. You can find the details in [PR #8162](https://github.com/paritytech/polkadot-sdk/pull/8162).

Additionally, I kept the archive API aligned with the latest changes in the spec. See this [PR #7885](https://github.com/paritytech/polkadot-sdk/pull/7885) for more information.


### Substrate

I enhanced observability for the transaction APIs at the RPC level by introducing a range of [metrics](https://github.com/paritytech/polkadot-sdk/pull/8345).

To improve peer behavior enforcement, I ensured that misbehaviors in the notification protocols result in penalization—lowering peer reputation and eventually leading to disconnection. See [PR #7781](https://github.com/paritytech/polkadot-sdk/pull/7781) and [PR #7724](https://github.com/paritytech/polkadot-sdk/pull/7724) for implementation details.

I also continued efforts to expand our test coverage, particularly around verifying compatibility between our network backends, libp2p and litep2p.

### Other work:

Besides the mentioned topics, I'm providing reviews for my area of expertise in polkadot-sdk and RFCs.

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

