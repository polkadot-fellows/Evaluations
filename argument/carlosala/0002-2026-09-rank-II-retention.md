# Argument-0002: Retention at Rank II

|                  |            |
| ---------------- | ---------- |
| **Report Date**  | 2026/09/25 |
| **Submitted by** | Carlo Sala |

## Member details

- Matrix username: @carlosala:matrix.org
- Polkadot address: 16JskuojL6mSp6HNcjiHYa9jqksWbLD8L9YGWU1ppiPWQ9sa
- Current rank: Proficient (II)
- Date of initial induction: 2026/06/09
- Date of last report: 2026/06/09
- Link to last report: [Fast Promotion to Rank II](0001-fast-promotion-rank-II.md)
- Area(s) of Expertise/Interest:
  - Runtime metadata and runtime/off-chain communication
  - Transaction construction, signing flows, and transaction extensions
  - Light-client-first application and tool development
  - JSON-RPC interfaces and client behavior
  - Developer tooling and SDK ergonomics
  - Coordination between SDK/runtime changes and downstream tooling

## Reporting period

- Start date: 2026/06/10
- End date: 2026/09/25

## Argument

I request retention at Rank II. Since my June report, I have continued working on the interfaces between Polkadot nodes, light clients, runtimes, and the applications that use them.

### Statement-store JSON-RPC

I authored the [statement-store JSON-RPC specification](https://github.com/paritytech/json-rpc-interface-spec/pull/185). It defines how clients submit statements and subscribe to them with topic filters, including how a client can add and remove filters on a subscription and identify matching notifications. The design works across full nodes and light clients. It was peer reviewed, approved, and merged, and the API is [integrated in Polkadot SDK](https://github.com/paritytech/polkadot-sdk/pull/11989).

I followed through with [SDK #12706](https://github.com/paritytech/polkadot-sdk/pull/12706), correcting input validation and error responses so the implementation matches the specification. Clients can therefore rely on the behavior the interface promises.

### Asset-conversion reserve correctness

In [SDK #12408](https://github.com/paritytech/polkadot-sdk/pull/12408), I fixed asset-conversion pool price and liquidity calculations that used the wrong balances for reserves. This produced incorrect quotes and could potentially become an attack vector. The fix uses full pool balances, consistent with swap execution.

### Polkadot-API transactions

I also worked on PAPI's transaction API support for General Extrinsic V5. With V5, authorization can be handled by transaction extensions instead of requiring a conventional account signature. The [TxCreator API](https://github.com/polkadot-api/polkadot-api/pull/1380) reflects this shift: applications create transactions through an interface that can support different authorization methods. During this period, I contributed [transaction-extension code generation](https://github.com/polkadot-api/polkadot-api/pull/1390), the [client export](https://github.com/polkadot-api/polkadot-api/pull/1394), and [signer support](https://github.com/polkadot-api/polkadot-api/pull/1409), connecting the new transaction model to generated types, applications, and existing signing flows.

This helps bring Polkadot closer to its vision of more flexible transaction authorization: runtimes can evolve their authorization rules, while wallets and applications have a practical way to construct and submit the resulting extrinsics. The client API is part of making that protocol change usable across the ecosystem.

These contributions continue the Rank II work described in my previous report: specifying interfaces, checking their implementations, and correcting protocol-facing behavior that downstream clients rely on.

## Voting record

| Rank | Activity threshold | Agreement threshold | Member's voting activity            | Comments                                                              |
| ---- | ------------------ | ------------------- | ----------------------------------- | --------------------------------------------------------------------- |
| II   | 80%                | N/A                 | 0 votes out of 0 eligible referenda | There were no referenda I could vote on during this reporting period. |

## Misc

- Questions: None.
- Concerns: None.
- Comments: None.
