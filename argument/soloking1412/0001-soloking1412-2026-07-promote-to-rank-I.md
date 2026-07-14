# Argument-0001: Promotion to Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/07/14                                                                                  |
| **Submitted by**| Maheswaran Velmurugan                                                                        |


## Member details

- Matrix username: @solokingm:matrix.org
- Polkadot address: 15aifM2JnkGoZ5QixmFJLiK5rmpqBcdYuSCAPBK92VyMtAQh
- Current rank: Candidate
- Date of initial induction: 2026/06/18 ([Fellowship application #23](https://collectives.subsquare.io/fellowship/applications/23))
- Date of last report: N/A
- Area(s) of Expertise/Interest:
    - `pallet-revive` / PolkaVM — the Ethereum-compatibility (smart-contract) layer of the Polkadot Hub
    - Ethereum JSON-RPC interface & conformance
    - Smart-contract security auditing
    - Multi-chain / EVM development


## Reporting period

- Start date: 2026/06/24
- End date: 2026/07/14


## Argument

Hi everyone, I'm Maheswaran Velmurugan. I'm a **Polkadot Blockchain Academy (Wave 5, June 2024) graduate** and a practising smart-contract security auditor with 15+ confirmed findings across Sherlock, Code4rena, Cantina and Immunefi. Outside Polkadot I build production infrastructure across 8+ chains, solo and grant-funded (e.g. [Stylus-Toolkit](https://github.com/soloking1412/Stylus-Toolkit), an Arbitrum-grant CLI published to NPM, and [satoshi-yield](https://github.com/soloking1412/satoshi-yield), a Stacks-Foundation grant). I work in Rust and Solidity and have deep EVM experience, which I have applied directly to `pallet-revive`'s Ethereum layer.

Since my induction I have concentrated on a single core component — **`pallet-revive` and its Ethereum JSON-RPC server (`pallet-revive-eth-rpc`) in `polkadot-sdk`** — with the goal of making its Ethereum interface conform to the de-facto reference (go-ethereum) so that *unmodified* Ethereum tooling works against a Polkadot chain. My work spans self-found bug fixes, a maintainer-requested refactor, input-validation hardening, a complete new standard RPC method, and a co-authored RFC formalising the component's guarantee.

### 1. `pallet-revive` Ethereum JSON-RPC conformance (polkadot-sdk)

All of the below were found by me independently (no assigned issues) and reviewed by Parity maintainers:

- **[`eth_feeHistory`: correct reward-bucket resolution (#12470, merged)](https://github.com/paritytech/polkadot-sdk/pull/12470)**: the cache stores reward percentiles at half-percentile resolution, but the lookup rounded to whole percentiles, making half-point buckets unreachable and returning the wrong reward. Fixed with a pure `reward_bucket_index` helper + unit test.
- **[`eth_getLogs`: support `finalized`/`safe`/`pending` block tags (#12474, approved)](https://github.com/paritytech/polkadot-sdk/pull/12474)**: these standard tags were rejected in filter ranges though the rest of the server accepts them. On maintainer request I went further and centralised block-tag resolution into a single canonical resolver shared by `eth_getLogs` and `block_hash_for_tag`, removing three divergent copies of the logic.
- **[`eth_getLogs`: empty address/topic filter lists (#12479)](https://github.com/paritytech/polkadot-sdk/pull/12479)**: `[]` is a go-ethereum wildcard; it was treated as an always-false `IN ()` clause that silently returned zero logs. Now a wildcard, while still enforcing the topic-length rule.
- **[`eth_getLogs`: `null` topic positions (#12483)](https://github.com/paritytech/polkadot-sdk/pull/12483)**: added support for `null` ("match-any") topic positions with go-ethereum's rule that a filter of length `N` only matches logs with at least `N` topics.
- **[`eth_feeHistory`: validate reward percentiles (#12547)](https://github.com/paritytech/polkadot-sdk/pull/12547)**: percentiles are now validated (range `0..=100`, strictly increasing, count-capped) and empty-block requests return early, matching go-ethereum, instead of silently approximating malformed input.
- **[`eth_subscribe`: enforce log topic length (#12626)](https://github.com/paritytech/polkadot-sdk/pull/12626)**: brought the subscription log filter in line with the same length rule as `eth_getLogs`.

### 2. New RPC functionality: `eth_getBlockReceipts`

- **[`pallet-revive`: implement `eth_getBlockReceipts` (#12636)](https://github.com/paritytech/polkadot-sdk/pull/12636)**: implemented a **missing standard `execution-apis` method** end-to-end (trait, handler, client, provider, integration test). It returns every receipt in a block in a single call — a method indexers and block explorers depend on — extracting them in a single pass, and returning `null` for a non-existent block to match go-ethereum.

### 3. Component design — RFC-0172 (co-authored)

- **[RFC-0172: Ethereum JSON-RPC compatibility standard for `pallet-revive`](https://github.com/polkadot-fellows/RFCs/pull/172)**: adopts the Ethereum `execution-apis`/go-ethereum specification as a normative conformance target, standardises the points where Substrate and Ethereum genuinely diverge (block-tag→GRANDPA-finality mapping, EIP-1474 error codes, filter edge cases, and the gas↔`Weight`+storage-deposit fold), and mandates a CI conformance suite. It ties the fixes above into a single citable guarantee and is intended for future deployment as the component's standard. It began as a competing idea from another contributor, [@Nathy-bajo](https://github.com/Nathy-bajo), who chose to fold their work in as **co-author** rather than open a rival RFC.

### 4. Analysis, review and collaboration

- I discovered and diagnosed every divergence above myself, working alone and without direction.
- On #12626 a reviewer suggested a one-line fix; I identified that it would have caused a regression (the filter representation padded unspecified positions identically to explicit `null`s) and implemented the correct deeper fix instead.
- I have incorporated review feedback from Parity contributors (marian-radu, 0xOmarA, 0xRVE) across multiple rounds, and turned a would-be competing contributor into an RFC co-author — reflecting the Fellowship's collaborative norms.

### Meeting the Rank I requirements (Manifesto §6)

- **"Three clear examples of a modest but substantial contribution":** the seven PRs in §1–§2 (one merged, one approved).
- **Active involvement in designing a component intended for deployment:** RFC-0172 (§3).
- **Substantially assisted in analysis, formalisation or implementation of a protocol component:** authored all seven PRs and the RFC; implemented a new RPC method and a maintainer-requested refactor (§1–§3).
- **Mastery of at least one major component:** `pallet-revive`'s Ethereum JSON-RPC layer (receipt extraction, log/filter querying, fee-history cache, block-tag/finality mapping, subscription filtering, gas metering).
- **Independence, and ability to work alone and without direction:** every contribution was self-found and self-scoped.
- **Security consciousness — systems must function with a malicious minority:** my auditing background informs this; several fixes close paths where the server silently returned *wrong* results (mispriced fees, dropped logs, unenforced filter-length rules) that malformed or adversarial requests could exploit.
- **Listing Polkadot's key goals, principles and tenets:** decentralisation; minimised trust / credible neutrality; shared (pooled) security; heterogeneous sharding and specialisation; interoperability via XCM; Byzantine resilience; open, permissionless participation; stake-based economic security; decentralised on-chain governance; and the Web3 vision of user sovereignty. I commit to the four Fellowship tenets: sincerely upholding Polkadot's interests; respecting its philosophy and principles; respecting the Fellowship's procedures, norms and voting conventions; and respecting fellow Members and the wider community.

### Summary

I'm genuinely committed to `pallet-revive` and the Ethereum-compatibility layer of the Polkadot Hub, and I intend to keep landing conformance work, ship the RFC's CI conformance suite, and take on review responsibility. I'd be honoured to continue this work as a Rank I Member.

Ongoing contributions can be tracked via my open PRs on `polkadot-sdk`: [is:pr author:soloking1412](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Asoloking1412).


## Voting record

N/A.


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
