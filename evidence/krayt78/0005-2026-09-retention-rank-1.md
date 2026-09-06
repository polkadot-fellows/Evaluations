# Argument-0005: Retention at Rank I

|                  |                   |
| ---------------- | ----------------- |
| **Report Date**  | 2026-09-02        |
| **Submitted by** | Ludovic Domingues |

## Member details

- Matrix username: @krayt78:matrix.org
- Polkadot address: 14AgwoPjcRiEEJgjfHmvAqkjdERCG26WEvQUoGLuBzcXKMS2
- Current rank: Rank I (Humble Member)
- Date of initial induction: 2024-06-18
- Date of last report: 2026-05-28
- Link to last report: [0004-2026-05-retention-rank-1.md](https://github.com/polkadot-fellows/Evaluations/blob/main/evidence/krayt78/0004-2026-05-retention-rank-1.md)
- Area(s) of Expertise/Interest: 
    - FRAME
    - Runtime

## Reporting period

- Start date: 2026/05/28
- End date: 2026/09/01

---

## Argument

This period I shipped a governance fix to `pallet-identity`, opened a new precompile for `pallet-revive` that went through a first round of review, and spent some time on the NFT/Gaming initiative and reviewing other fellows' pallets. Details below, strongest first.

### `pallet-identity`: `remove_registrar` extrinsic (merged)

[#12263](https://github.com/paritytech/polkadot-sdk/pull/12263) - merged 2026-06-04, approved by @bkchr, @bkontur, @cirko33 and @sigurpol.

Once a registrar was added with `add_registrar` there was no way to remove it. Disabling a compromised or inactive registrar meant a full runtime upgrade carrying a bespoke storage migration, which is a weeks-long process for what should be a routine governance action. This PR adds `remove_registrar`, gated by the same `RegistrarOrigin` as `add_registrar`, with a new `RegistrarRemoved` event, benchmark and weights. It is purely additive: fresh call index, no storage migration, nothing renamed. People Chain can now handle this through governance alone.

### `pallet-revive`: `UncheckedRuntime` precompile (paused after first review round)

[#12457](https://github.com/paritytech/polkadot-sdk/pull/12457) - opened 2026-06-24, reviewed by @kianenigma, @ggwpez and @xermicus.

This picks up @kianenigma's exploratory `kiz-unstable-runtime-precompiles` branch and turns it into a proper PR. The precompile gives contracts two raw primitives against the host runtime: `dispatch(bytes)` to dispatch an arbitrary SCALE-encoded `RuntimeCall` as the calling contract's account, and `getStorage(bytes)` to read any storage item by its full key. The point is to let builders prototype contract-to-runtime integrations without waiting for a bespoke, stabilised precompile per pallet.

What went into it beyond the prototype:

- Feature-gated (`unchecked-precompiles`, off by default) and opt-in via `Config::Precompiles`, with a hazard table in the module docs explaining why it must never ship on a production runtime as-is.
- A `Contains<RuntimeCall>` filter attached to the dispatch origin so it stays in force through `batch` and `proxy`, plus a separate storage-key filter.
- A two-dimensional benchmark for `getStorage`, charging the worst case up front and refunding to the actual size, with proof size charged on every path including revert.
- Re-entrancy blocked through `run_guarded`, `BaseCallFilter` respected.

The review went through many exchanges. It was renamed from `UnstableRuntime` to `UncheckedRuntime` after @ggwpez's feedback, and the remaining open question from @kianenigma is how the weight handling compares with the XCM precompile. I put this PR on pause in July to focus on the NFT/Gaming initiative and the `pallet-scarcity` work described below. Depending on priorities I may pick it back up; what is left is answering that thread and rebasing.

### Reviewing other fellows' work

**`pallet-scarcity`** by @shawntabrizi - [#12730](https://github.com/paritytech/polkadot-sdk/pull/12730), merged.

I was part of the NFT/Gaming initiative that this pallet came out of, where I built a `PalletCollectibles` prototype exploring the same design space (ownership policies as contracts, collection ownership transfer, Root force-transfer for emergencies). That work lived in a private repository so I cannot link it, but it is why I was in a position to review the resulting pallet in depth.

**`pallet-treasury` `Currency` to `Fungible` migration** by @pandres95 - [#11109](https://github.com/paritytech/polkadot-sdk/pull/11109), open.

This is the same migration effort I have been contributing to on other pallets, so I reviewed it with that context.

### `Currency` to `fungible` migration PRs (parked)

The five PRs from my previous reports are still open and were up to date as of my last report. This migration is not a priority for the SDK right now and reviewer time keeps going elsewhere, so I am not putting more work into it. I am leaving the PRs as they are rather than closing them, so anyone who wants to pick the effort up has a ready starting point.

| Pallet           | PR                                                              | Status                              |
| ---------------- | --------------------------------------------------------------- | ----------------------------------- |
| pallet-lottery   | [#10045](https://github.com/paritytech/polkadot-sdk/pull/10045) | Approved, waiting for merge         |
| pallet-referenda | [#10701](https://github.com/paritytech/polkadot-sdk/pull/10701) | Waiting for a dependency            |
| pallet-preimage  | [#11066](https://github.com/paritytech/polkadot-sdk/pull/11066) | Needs review                        |
| pallet-multisig  | [#11064](https://github.com/paritytech/polkadot-sdk/pull/11064) | Needs review                        |
| pallet-indices   | [#9610](https://github.com/paritytech/polkadot-sdk/pull/9610)   | Needs review                        |

---

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | N/A  | No referenda on the Members track during the reporting period |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

