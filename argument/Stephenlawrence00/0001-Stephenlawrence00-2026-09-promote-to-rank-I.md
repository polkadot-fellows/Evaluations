# Argument-0001: Promotion to Rank I

|                 |                |
| --------------- | -------------- |
| **Report Date** | 2026/09/17     |
| **Submitted by**| Stephen Lawrence |

---

## Member details

- **Matrix username**: `@stevenlawrence:matrix.org`
- **Polkadot address**: `16Xj1rSgNBtzHch3Jb9SfW7dK749s9WbCqKcwmZCFkR2pnai`
- **GitHub**: [`Stephenlawrence00`](https://github.com/Stephenlawrence00)
- **Current rank**: 0 (Candidate)
- **Date of initial induction**: 2026/09/16, via [application #26](https://collectives.subsquare.io/fellowship/applications/26)
- **Date of last report**: N/A
- **Link to last report**: N/A. This is my first Argument.
- **Area(s) of Expertise/Interest**:
    - FRAME / runtime development
    - Staking, elections and governance pallets
    - Token issuance accounting and the Asset Hub Migration
    - XCM
    - JAM

---

## Reporting period

- **Start date**: 2025/02/12
- **End date**: 2026/09/17

---

## Argument

I'm Stephen Lawrence. I build and operate complex software systems, and for the past year most of that time has gone into the Polkadot SDK and the fellowship runtimes. I came in through a Polkadot Africa SDK workshop, started on isolated feature work, and have since moved to the parts of the stack production runtimes depend on.

Most of what I do is find the places where the code quietly does the wrong thing, and fix them on both sides of the stack. A state snapshot that looks valid but was built from a lagging RPC provider. A dry run that actually delivers the messages it was only meant to simulate. A burn on a system chain that never moves the issuance figure Asset Hub tracks. None of these fail loudly, and most surface only in production or in the tooling used to verify an upgrade before it is enacted. That work runs across both repositories, because a fix usually needs a primitive in the SDK and a runtime willing to adopt it, and the issues I open are there to keep the two halves in step.

Below are my substantial works over this period.

---

### `polkadot-fellows/runtimes`

- [runtimes#1287](https://github.com/polkadot-fellows/runtimes/pull/1287) (merged): Bridge Hub, Coretime, People and Encointer Kusama route `DustRemoval` into a `pallet-accumulate-and-forward` account and teleport it to Asset Hub to be burned there, so a burn on a system chain moves the `TotalIssuance` figure Asset Hub actually tracks.
- [runtimes#1289](https://github.com/polkadot-fellows/runtimes/pull/1289) (merged): the Kusama relay accumulates the dust it used to burn locally and teleports it to Asset Hub. I also inventoried the relay's remaining post-AHM sinks and established they are dormant or non-burning, so the change closes the problem rather than half of it.
- [runtimes#1288](https://github.com/polkadot-fellows/runtimes/pull/1288) (merged): `DustRemoval` on Asset Hub Polkadot resolves into the DAP staging account rather than burning, so dust is deactivated like every other Polkadot sink. Carries tests for the recursion question raised in [#12130](https://github.com/paritytech/polkadot-sdk/issues/12130).
- [runtimes#1234](https://github.com/polkadot-fellows/runtimes/pull/1234) (merged): `pallet-remote-proxy` silently dropped the newest relay storage root, so proofs anchored at recent relay blocks failed with `UnknownProofAnchorBlock`. Fixed by skipping duplicate `BlockToRoot` entries for the same relay parent and evicting the oldest entry rather than the newest when the bounded vector fills. Reported in [#1230](https://github.com/polkadot-fellows/runtimes/issues/1230).
- [runtimes#1301](https://github.com/polkadot-fellows/runtimes/pull/1301) (approved): collapses Coretime Kusama's two teleport-and-burn paths into one and closes a real leak. `py/ctbrn` is swept to zero daily with `Preservation::Expendable`, so sub-ED dust arriving while it sits empty is burned outright, because `can_deposit` refuses a deposit that would leave an account below ED.

### `paritytech/polkadot-sdk`

- [#12843](https://github.com/paritytech/polkadot-sdk/pull/12843) (merged): adds `type RewardSource` (pay rewards from a pot account instead of minting) and `type Slash` (route slashed deposits to a handler instead of burning) to `pallet-election-provider-multi-block::signed::Config`, so the signed phase stops silently minting and burning and `TotalIssuance` stays reconcilable with the DAP emission curve on Asset Hub. Reported in [#12813](https://github.com/paritytech/polkadot-sdk/issues/12813). The shape of the API owes a lot to [@sigurpol](https://github.com/sigurpol), who pushed for the reward payment to be recoverable rather than silently skipped, for the no-op reactivation to be opt-in rather than the default, and for keeping DAP and EPMB free of a dependency on each other.
- [#13153](https://github.com/paritytech/polkadot-sdk/pull/13153) (merged): `pallet-accumulate-and-forward`'s `on_idle` now records the block of the last forwarding attempt and forwards once `now - last >= TransferPeriod`, instead of requiring an exact multiple of `TransferPeriod`, which a parachain reading the relay chain block number can miss indefinitely, leaving accumulated funds forwarded never. Reported in [#13149](https://github.com/paritytech/polkadot-sdk/issues/13149).
- [#12268](https://github.com/paritytech/polkadot-sdk/pull/12268) (merged): `remote-ext` treated per-item RPC errors as empty values, so a lagging provider produced a snapshot that looked valid and was quietly wrong. Such errors now fail the batch, the computed storage root is verified against the block header before a snapshot is cached, and providers lacking the target block are excluded up front. This is the tooling used to dry-run runtime upgrades, so a silently corrupt snapshot is a bad failure mode. Reported in [#12264](https://github.com/paritytech/polkadot-sdk/issues/12264).
- [#12807](https://github.com/paritytech/polkadot-sdk/pull/12807) (merged): wraps `pallet-xcm`'s `dry_run_call` and `dry_run_xcm` in a rolled-back storage transaction so simulated XCM execution never mutates caller state. Before this, dry-run outbound messages were silently delivered via `process_messages()`, meaning emulator tests asserted against a world the dry run had already changed. Reported in [#11486](https://github.com/paritytech/polkadot-sdk/issues/11486).
- [#12710](https://github.com/paritytech/polkadot-sdk/pull/12710) (approved): adds `try_state` invariant checks to `pallet-proxy`, and gives it a storage version plus a `MigrateV0ToV1` migration that sorts the delegate list in every `Proxies` entry so lookups can rely on the ordering. Wired into the `Migrations` tuple of five Westend runtimes.
- [#11080](https://github.com/paritytech/polkadot-sdk/pull/11080) (approved): ensures broker parachain reachability in the coretime benchmarks, which otherwise assume a route that isn't configured.
- [#11758](https://github.com/paritytech/polkadot-sdk/pull/11758) (approved): refactors the `frame-benchmarking` pallet backend.
- [#10901](https://github.com/paritytech/polkadot-sdk/pull/10901) (approved): marks `SystemWeightInfo` and `ExtensionsWeightInfo` as `#[pallet::no_default]` and removes their `()` defaults from the `frame-system` default configs, so a runtime can no longer silently inherit the Substrate reference weights and must set its own explicitly. Reported in [#10758](https://github.com/paritytech/polkadot-sdk/issues/10758).
- [#12900](https://github.com/paritytech/polkadot-sdk/pull/12900) (approved): removes `FreezeIdentifier` and `MaxFreezes` from `pallet_balances` in favour of `RuntimeFreezeReason`.

---

## Honourable mentions

- [#11756](https://github.com/paritytech/polkadot-sdk/pull/11756) (open): removes the parathread lifecycle from `ParaLifecycle`, leaving `Onboarding`, `Parachain` and `OffboardingParachain`, so every registered para onboards directly as a `Parachain`. This reflects the coretime model, where holding a lease is no longer a property of the para itself. Reported in [#3402](https://github.com/paritytech/polkadot-sdk/issues/3402).
- [#11748](https://github.com/paritytech/polkadot-sdk/pull/11748) (open): makes `decl_runtime_apis!` generate parameters bounded by `EncodeLike<T>`, so any type producing the same SCALE bytes as `T` can be passed in its place, adds `where Self: Sized` for dyn compatibility, and updates `mock_impl_runtime_apis!` to decode generic arguments back to concrete types. Reported in [#5951](https://github.com/paritytech/polkadot-sdk/issues/5951).

---

## Issues authored

I try to scope work before writing it, and to track the operational consequences of my own changes rather than leaving them for someone else to discover.

- [runtimes#1290](https://github.com/polkadot-fellows/runtimes/issues/1290) (open): part of the [runtimes#1283](https://github.com/polkadot-fellows/runtimes/issues/1283) workstream opened by [@sigurpol](https://github.com/sigurpol), and a follow-up to #1287 that identified the sub-ED dust leak described above. I am implementing it in #1301.
- [runtimes#1239](https://github.com/polkadot-fellows/runtimes/issues/1239) (open): scopes the runtime-side half of my SDK change #12843, wiring `pallet-election-provider-multi-block`'s Slash and RewardSource to DAP on Polkadot Asset Hub once this repo bumps past it, with the config mirrored from Westend Asset Hub.
- [#13127](https://github.com/paritytech/polkadot-sdk/issues/13127) (open): scoped from a suggestion by [@Ank4n](https://github.com/Ank4n) in review on #12843. DAP already owns deactivate-on-inflow, so reactivate-on-outflow belongs there too, with the signed-phase pot registered as an absolute capped recipient. I am implementing it in [#13173](https://github.com/paritytech/polkadot-sdk/pull/13173).
- [runtimes#1298](https://github.com/polkadot-fellows/runtimes/issues/1298) (open): scopes the runtime-side follow-through for my migration in #12710, adding `pallet-proxy`'s `MigrateV0ToV1` to the Asset Hub Polkadot and Kusama `Unreleased` tuples, and records the crate pin that blocks it until an SDK release carries the migration.
- [#13244](https://github.com/paritytech/polkadot-sdk/issues/13244) (open): scopes the cleanup half of that same migration, deleting `MigrateV0ToV1` from the five Westend runtimes once each is at storage version 1 and the tuple entry is only a version read on every future upgrade.

---

## Other ongoing work

### FRAME state invariants (`try_state`)

A systematic pass adding `try_state` invariant checks to pallets that had none, so state corruption is caught in `try-runtime` upgrade checks rather than in production. Led by [`pallet-proxy` (#12710)](https://github.com/paritytech/polkadot-sdk/pull/12710), listed above as approved, with the same treatment for:

[`pallet-preimage` (#12716)](https://github.com/paritytech/polkadot-sdk/pull/12716) · [`pallet-identity` (#12713)](https://github.com/paritytech/polkadot-sdk/pull/12713) · [`pallet-vesting` (#12712)](https://github.com/paritytech/polkadot-sdk/pull/12712) · [`pallet-multisig` (#12711)](https://github.com/paritytech/polkadot-sdk/pull/12711) · [`pallet-scheduler` (#12426)](https://github.com/paritytech/polkadot-sdk/pull/12426) · [`pallet-whitelist` (#12425)](https://github.com/paritytech/polkadot-sdk/pull/12425) · [`pallet-salary` (#12424)](https://github.com/paritytech/polkadot-sdk/pull/12424)

Full record: [merged SDK PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AStephenlawrence00+is%3Amerged) · [merged runtimes PRs](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3AStephenlawrence00+is%3Amerged) · [all PRs](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3AStephenlawrence00) · [issues authored](https://github.com/search?q=author%3AStephenlawrence00+is%3Aissue&type=issues)

---

## Summary

My work is concentrated where the Fellowship's responsibility actually sits: the runtimes Polkadot and Kusama run, the FRAME pallets underneath them, and the tooling used to verify an upgrade before it is enacted. The issuance workstream in particular required carrying one problem across two repositories and several releases, writing the SDK primitive, using it in the runtime, and tracking the cleanup afterwards. That is the kind of end-to-end ownership I would like to keep doing as a Member.

At Rank I, I intend to carry the issuance and AHM work through to completion, keep expanding `try_state` coverage across FRAME, and take on review responsibility in the areas I now know well.

---

## Voting record

N/A. I am a Candidate seeking promotion and have no voting history yet. Per the Manifesto there is no minimum period of service for Candidates seeking to become Members, and no activity or agreement thresholds apply at Rank 0.

| Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
| 0 | N/A | N/A | N/A | Candidate, so no voting rights or obligations. |
| I | 90% | N/A | N/A | Thresholds apply from Rank I onward; I will meet them once promoted. |

---

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s): I was inducted as a Candidate on 2026/09/16 via [application #26](https://collectives.subsquare.io/fellowship/applications/26). Per the Manifesto there is no minimum period of service for Candidates seeking to become Members.
