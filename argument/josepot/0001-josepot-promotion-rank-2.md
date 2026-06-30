# Argument-0001: Promotion to Rank II

|                 |                                                                             |
| --------------- | --------------------------------------------------------------------------- |
| **Report Date** | 2026/06/09                                                                  |
| **Submitted by**| Josep M Sobrepere                                                           |


## Member details

- Matrix username: @josepot:matrix.org
- Polkadot address: 15roJ4ZrgrZam5BQWJgiGHpgp7ShFQBRNLq6qUfiNqXDZjMK
- Current rank: Candidate (0)
- Date of initial induction: 2026/06/09
- Date of last report: N/A
- Area(s) of Expertise/Interest: Standard RPCs (new JSON-RPC spec), light-clients, developer-facing protocol APIs, transaction/extrinsic format design, runtime upgrade tooling.


## Reporting period

- Start date: 2021/09/01
- End date: 2026/06/09


## Argument

I am requesting a fast-track promotion directly from Candidate to Rank II. My contributions since joining the Polkadot ecosystem in September 2021 clearly satisfy the requirements for Rank II as stated in Section 6 of the Manifesto. I considered requesting Rank III, but prefer to begin at Rank II and earn a promotion to Rank III through demonstrated Fellowship participation in the coming months.

---

### Rank I criteria (exceeded)

**Three clear examples of a substantial contribution to protocol development:**

1. **Polkadot-API (PAPI)**: I am the primary author and technical lead of [PAPI](https://github.com/polkadot-api/polkadot-api), the recommended successor to polkadot.js. PAPI is a full implementation of the new JSON-RPC specification for the application layer: it is how the vast majority of modern dApps and wallets interact with Polkadot today. It has shipped 118+ releases across 4+ years of active development and is continuously funded by the Polkadot Treasury (6 approved referenda, each with near-unanimous support: [#467](https://polkadot.subsquare.io/referenda/467), [#695](https://polkadot.subsquare.io/referenda/695), [#1103](https://polkadot.subsquare.io/referenda/1103), [#1462](https://polkadot.subsquare.io/referenda/1462), [#1856](https://polkadot.subsquare.io/referenda/1856), [#1874](https://polkadot.subsquare.io/referenda/1874)).

2. **JSON-RPC interface spec contributions**: As the primary implementer of the new JSON-RPC spec, I have contributed fixes and design proposals directly to [paritytech/json-rpc-interface-spec](https://github.com/paritytech/json-rpc-interface-spec): the `transaction:searched` event ([#80](https://github.com/paritytech/json-rpc-interface-spec/pull/80)), explicit `finalized` guarantees ([#76](https://github.com/paritytech/json-rpc-interface-spec/pull/76)), the `inaccessible` event fix ([#65](https://github.com/paritytech/json-rpc-interface-spec/pull/65)), `rpc_methods` return value ([#129](https://github.com/paritytech/json-rpc-interface-spec/pull/129)), and multiple design RFCs including batching storage requests ([#47](https://github.com/paritytech/json-rpc-interface-spec/issues/47), [#48](https://github.com/paritytech/json-rpc-interface-spec/issues/48)) and `stop` event semantics ([#86](https://github.com/paritytech/json-rpc-interface-spec/issues/86)).

3. **`createTransaction` RFC**: I authored a detailed RFC ([polkadot-js/api#6213](https://github.com/polkadot-js/api/issues/6213), [forum post](https://forum.polkadot.network/t/toward-an-interoperable-transaction-interface-introducing-createtransaction/15060)) proposing a new, forward-compatible signer interface to replace `signPayload`. The core problem: `signPayload` predates Metadata V14, cannot handle custom extensions, and has broken nearly every dApp each time a signed extension has changed. The `createTransaction` interface passes full metadata and an explicit extension list, making it resilient to protocol evolution and compatible with Extrinsic V5. This RFC is driving the ecosystem-wide migration of the wallet/dApp signing boundary.

**Involvement in designing components at publication standards:**

I co-designed (with Victor Oliva) PAPI's fine-grained runtime compatibility system: the insight that metadata determines dApp compatibility, not raw SCALE encoding, and formalised it in a public technical deep-dive ([PAPI and Runtime Upgrades, June 2025](https://forum.polkadot.network/t/papi-and-runtime-upgrades-making-dapps-truly-resilient/13178)). The companion tool [diff.papi.how](https://diff.papi.how) is now used by runtime teams during upgrade reviews.

I designed the `PolkadotProvider` interface ([forum post, October 2023](https://forum.polkadot.network/t/polkadot-provider-api-a-common-interface-for-building-decentralized-applications/4128)): the standard interface decoupling dApp development from polkadot.js internals, which led directly to `@polkadot-api/light-client-extension-helpers` and transformed the `@substrate/connect` extension to comply with the new standard.

**Knowledge of Polkadot's key goals, principles and tenets:**

I graduated **with distinction** from the Polkadot Blockchain Academy, Cohort V (Singapore, May–June 2024): [graduation NFT](https://assethub-polkadot.subscan.io/nft_item?collection_id=171&address=15roJ4ZrgrZam5BQWJgiGHpgp7ShFQBRNLq6qUfiNqXDZjMK). For the following two PBA cohorts: **Cohort VI (Lucerne)** and **Cohort VII (Bali)**, my team and I **designed the dApps track curriculum from scratch** and served as its **primary instructors**.

---

### Rank II criteria

**Primary individual responsible for the formalisation, implementation, or analytical improvement of a major component:**

PAPI constitutes the application-layer implementation of Polkadot's standard JSON-RPC API, the primary interface through which the network is consumed by modern dApps, tools, and wallets. I am the primary author, architect, and technical lead. The work includes:

- Full TypeScript implementation of the `chainHead`, `transaction`, and `archive` JSON-RPC namespaces
- A metadata-driven type system that generates strongly typed, chain-agnostic descriptors from on-chain metadata
- Recovery from `stop` events, runtime upgrade handling, and compatibility checking
- A modular provider system enabling light-client (smoldot) and WebSocket backends interchangeably
- Performance benchmarks and integration tests.

**`@polkadot-api/check-runtime`, required gate in the Fellowship's CI:**

The Manifesto explicitly lists "user-interface code required to practically execute upgrades to the Polkadot (Main) Network" as in scope. My `@polkadot-api/check-runtime` CLI ([announcement](https://forum.polkadot.network/t/introducing-polkadot-api-check-runtime-quick-checks-for-runtime-upgrades-library-cli/15225)) is integrated as a **required check** in the `polkadot-fellows/runtimes` CI pipeline: the [`check-runtimes` job](https://github.com/polkadot-fellows/runtimes/blob/main/.github/workflows/test.yml) runs `npx @polkadot-api/check-runtime@latest problems` against every runtime WASM artifact before a PR can be merged. It is listed as a required dependency of the CI gate, no runtime upgrade to the Polkadot (Main) Network can be merged without passing this check.

**Contributions to `polkadot-fellows/runtimes` and `polkadot-sdk`:**

Beyond tooling, I have contributed directly to the Fellowship's runtimes and to the Polkadot SDK:

- [polkadot-fellows/runtimes#1117](https://github.com/polkadot-fellows/runtimes/pull/1117): Replaced the generic `ExtrinsicBaseWeight` constant with chain-specific values in fee calculation modules. A subtle but impactful correctness fix: the mismatch between the constant in use and the actual value in `System.BlockWeights.per_class_normal.base_extrinsic` caused fee calculation tools to silently produce wrong results. Merged March 2024.
- [paritytech/polkadot-sdk#7959](https://github.com/paritytech/polkadot-sdk/pull/7959): Treasury: reset `payout.expire_at` on each valid payout attempt, fixing an edge case in Treasury payout expiry logic.

I also contributed several fixes and improvements to smoldot (the light client itself): TypeScript type definition fixes that unblocked downstream type safety ([#1710](https://github.com/paritytech/smoldot/pull/1710)), browser error handling ([#2171](https://github.com/paritytech/smoldot/pull/2171)), and error naming ([#2019](https://github.com/paritytech/smoldot/pull/2019)).

The breadth and continuity of this work are evidenced by six consecutive Treasury referenda spanning from February 2024 to February 2027, each passed with near-unanimous community support.

**At least one published long-form semi-technical article concerning Polkadot:**

I have published extensively on the Polkadot Forum, including several substantial technical pieces:

- [Toward an Interoperable Transaction Interface: Introducing `createTransaction`](https://forum.polkadot.network/t/toward-an-interoperable-transaction-interface-introducing-createtransaction/15060): Protocol-level RFC for the transaction-creators interface, explaining the failures of `signPayload` and the design of its replacement.
- [New JSON-RPC API Q4 2024 Update](https://forum.polkadot.network/t/new-json-rpc-api-q4-2024-update/10541): Ecosystem-wide compliance audit identifying 13 non-compliant parachains and proposing remediation paths.
- [Can pallet-revive help improve Polkadot's UX?](https://forum.polkadot.network/t/can-pallet-revive-help-improve-polkadots-ux/12923): Technical analysis of the precompile approach and its impedance mismatch with Polkadot's evolving pallet model.
- [PAPI and Runtime Upgrades: Making dApps Truly Resilient](https://forum.polkadot.network/t/papi-and-runtime-upgrades-making-dapps-truly-resilient/13178): Deep technical analysis of metadata-driven compatibility checking and the runtime upgrade resilience problem.
- [Why Polkadot-API](https://forum.polkadot.network/t/why-polkadot-api/15468): Architectural rationale: tight coupling and leaky abstractions in the existing ecosystem, and how PAPI's composable design addresses them. Includes performance benchmarks.

Additional quarterly progress and technical updates: [Q4 2023](https://forum.polkadot.network/t/polkadot-api-2023-q4-update/5318), [Q1 2024](https://forum.polkadot.network/t/polkadot-api-2024-q1-update/7462), [Q2 2024](https://forum.polkadot.network/t/polkadot-api-2024-2nd-update/9673), [Q1 2025](https://forum.polkadot.network/t/polkadot-api-2025-q1-update/11906), [JSON-RPC Q3 2025](https://forum.polkadot.network/t/new-json-rpc-api-q3-2025-update-introducing-legacy-provider-and-moar/14394).

I also presented at **Polkadot Decoded 2024** in Brussels: [*Build a Modern dApp with Polkadot-API*](https://www.youtube.com/watch?v=fj63gYJmuIk).

---

### On the choice of Rank II over Rank III

The depth and longevity of my contributions, the ecosystem-wide impact of PAPI, and my work shaping the JSON-RPC specification would justify a Rank III argument. However, I prefer to begin my Fellowship membership at Rank II, participate actively in technical discussions over the coming months, and demonstrate through that participation that I am ready for Rank III. I believe earning promotion through Fellowship engagement is more appropriate than requesting it upfront.


## Voting record

As a newly inducted Candidate, I have not yet been eligible to vote in any Fellowship referenda.

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | N/A — inducted as Candidate on 2026/06/09 | |
|II |80%   |N/A   | | |
|III|70%   |100%  | | |
|IV |60%   |90%   | | |
|V  |50%   |80%   | | |
|VI |40%   |70%   | | |


## Misc

- [ ] I am open to any questions from Fellowship members about the scope or depth of the contributions described above.
