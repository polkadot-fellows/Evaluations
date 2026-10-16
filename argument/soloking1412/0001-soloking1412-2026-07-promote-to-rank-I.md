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

- Start date: 2024/06 (graduated Polkadot Blockchain Academy, Wave 5)
- End date: 2026/07/14


## Argument

My serious engagement with core Polkadot technology began in June 2024, when I graduated from Wave 5 of the Polkadot Blockchain Academy — the intensive program on Substrate, FRAME and the internals of the Polkadot protocol. That training is the grounding for the contributions described here. I also work professionally as a smart-contract security auditor, with more than fifteen confirmed findings across Sherlock, Code4rena, Cantina and Immunefi, and as a multi-chain protocol developer.

I have brought that EVM and adversarial-analysis experience to bear on a single Polkadot component: `pallet-revive` and its Ethereum JSON-RPC server, `pallet-revive-eth-rpc`, in `polkadot-sdk`. This is the layer that lets the existing Ethereum ecosystem — wallets, libraries, indexers and block explorers — interact with the Polkadot Hub without modification.

The problem I have set out to solve is strategically important for the network. `pallet-revive` only delivers its value if its JSON-RPC surface behaves exactly as Ethereum tooling expects, which in practice means behaving as go-ethereum, the de-facto reference implementation. Where it diverges, real tools break — and, worse, they often break silently, receiving plausible-but-wrong answers rather than errors.

Over this period I found that the interface diverged in numerous places: it returned incorrect fee data, dropped valid log results, accepted malformed input without complaint, and omitted a standard method entirely. My work has been a sustained effort to close these gaps and to formalise the compatibility guarantee so that it cannot silently regress, making the Polkadot Hub a dependable home for Ethereum applications.

I address each Rank I requirement from Section 6.2.1 of the Manifesto in turn below.

**"Three clear examples of a modest but substantial contribution to protocol development."** I have contributed seven such fixes to `paritytech/polkadot-sdk`, each found independently and each reviewed by Parity maintainers.

The first to be merged corrected `eth_feeHistory`. Its cache stored priority-fee rewards at half-percentile resolution, but the lookup rounded requests to whole percentiles, so fee-estimation tooling silently received the wrong values ([#12470, merged](https://github.com/paritytech/polkadot-sdk/pull/12470)).

A second, since approved by a maintainer, made `eth_getLogs` accept the `finalized`, `safe` and `pending` block tags that the rest of the server already honoured. At the maintainer's suggestion I extended it to unify three divergent copies of block-tag resolution into one canonical routine ([#12474](https://github.com/paritytech/polkadot-sdk/pull/12474)).

Four further contributions harden log filtering and fee history. They make empty and `null` topic positions behave as go-ethereum's wildcards while enforcing its rule that a filter of length *N* only matches logs with at least *N* topics ([#12479](https://github.com/paritytech/polkadot-sdk/pull/12479), [#12483](https://github.com/paritytech/polkadot-sdk/pull/12483)). They validate `eth_feeHistory` percentiles rather than silently approximating malformed input ([#12547](https://github.com/paritytech/polkadot-sdk/pull/12547)). And they bring the `eth_subscribe` log filter into line with the same semantics ([#12626](https://github.com/paritytech/polkadot-sdk/pull/12626)).

In every case the fix replaced a silently-wrong result — the most dangerous outcome for downstream software — with correct, specified behaviour. This is precisely the Manifesto's own example of a modest-but-substantial contribution: "identifying and correcting a non-trivial issue in protocol code."

**"Actively been involved in the design of a component ... reasonably intended for future deployment ... at the standard expected of a PRP," and "substantially assisted in the analysis, or authoring of formalisation or implementation of a protocol component."** To address the pattern behind these fixes rather than only their symptoms, I authored [RFC-0172](https://github.com/polkadot-fellows/RFCs/pull/172), a proposed Ethereum JSON-RPC compatibility standard for `pallet-revive`. It adopts the Ethereum `execution-apis` specification and go-ethereum as the normative conformance target, specifies the few places where Substrate and Ethereum genuinely differ — block-tag-to-GRANDPA-finality mapping, EIP-1474 error codes, log-filter edge cases, and how `pallet-revive`'s two-dimensional `Weight` and refundable storage deposit fold into a single gas figure — and mandates a CI conformance suite so the guarantee is enforced automatically.

The RFC is under Fellowship review and is intended for deployment as the component's standard. It also reflects collaboration: it began as a competing idea from another contributor, [@Nathy-bajo](https://github.com/Nathy-bajo), who chose to join me as co-author rather than open a rival proposal.

On the implementation side, I delivered a complete, previously-absent standard method, [`eth_getBlockReceipts` (#12636)](https://github.com/paritytech/polkadot-sdk/pull/12636). It returns every receipt in a block in a single call, which indexers and explorers depend upon, and its absence had been a concrete obstacle to running that tooling against Polkadot.

My analysis also extended into the review process. When a reviewer proposed a one-line change for the subscription length rule, I recognised that it would have introduced a regression — the filter's internal representation collapsed explicit `null` positions and unspecified ones — and implemented the correct, deeper fix instead.

**"Should be able to list all key goals, principles and tenets of Polkadot's overall philosophy."** Polkadot's central aim is decentralisation: removing single points of control or failure, and minimising trust through cryptographic and crypto-economic guarantees rather than intermediaries. Its security is shared — parachains inherit the Relay Chain's validator set — and it is designed to remain correct even with a Byzantine minority.

Polkadot scales through heterogeneous sharding, running many specialised chains in parallel, and connects them with Cross-Consensus Messaging (XCM). Participation is open and permissionless, secured by staking and steered by decentralised on-chain governance. Underlying all of this is the Web3 goal of user sovereignty and credible neutrality — minimising the need to trust powerful third parties.

As a member I commit to the Fellowship's four tenets: to sincerely uphold the interests of Polkadot; to respect its philosophy and principles; to respect the Fellowship's procedures, norms and voting conventions; and to respect my fellow members and the wider community.

Beyond these explicit requirements, the rank's primary qualities are present throughout this work. It reflects mastery of one major component — the whole of `pallet-revive`'s Ethereum JSON-RPC layer, from receipt extraction and log-filter query construction to the fee-history cache, block-tag mapping, subscription filtering and gas metering — built on the broad understanding of Substrate I gained at the Blockchain Academy.

Every contribution was found, scoped and delivered without assignment or direction. This demonstrates the independence of mind and the capacity to work unaided that the rank requires.

My security-auditing background serves the expectation that a candidate appreciates that a system must function even with a modest minority of malicious users. Several of the fixes above close paths where malformed or adversarial requests previously yielded silently-wrong results.

Throughout, I have maintained a pattern of availability and knowledge-sharing — publishing an RFC, engaging with maintainer reviews across many rounds, and turning a would-be competitor into a collaborator.

The ongoing impact of this work is to advance one of Polkadot's current priorities: making the Polkadot Hub a credible, frictionless home for the existing Ethereum developer ecosystem. Each fix lets real, unmodified tooling work correctly against Polkadot; the new method unblocks indexers and explorers; and the RFC, once its conformance suite lands, will keep the interface correct as both ecosystems evolve.

At Rank I, I intend to continue this campaign — shipping the conformance suite, extending coverage to further methods, and taking on review responsibility for others' `pallet-revive` work. My current and future contributions can be followed through my [open pull requests on `polkadot-sdk`](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Asoloking1412).


## Voting record

N/A.


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
