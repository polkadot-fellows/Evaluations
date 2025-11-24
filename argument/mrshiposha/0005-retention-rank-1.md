# Argument-0005: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2025/11/24                                                                                   |
| **Submitted by**| Daniel Shiposha                                                                             |


## Member details

- Matrix username: `@mrshiposha:matrix.org`
- Polkadot address: `14aC2hfNZTX4sMHPh47MjGB4Vr4rVYHZgBid54vRKrZVBZQY`
- Current rank: Rank I
- Date of initial induction: 2024/12/11
- Date of last report: 2025/08/25
- Area(s) of Expertise/Interest: XCM, NFT


## Reporting period

- Start date: 2025/09/29
- End date: 2025/12/20

## Argument

During the reporting period I focused my attention around XCM refactoring to make XCM more easily upgradable (without huge amount of copy-pasting) to new version**s**.
This activity should eventually resolve the corresponding issue https://github.com/paritytech/polkadot-sdk/issues/7095.

I initially started by picking up [the existing work done by Bryan Chen](https://github.com/paritytech/polkadot-sdk/pull/7123) and [tried](https://github.com/UniqueNetwork/polkadot-sdk/commit/bacb61bca1fdfa8432746bcf8e9a2b4e937c06f9) to finish it.
But it became clear that this approach demands a lot of changes accross all the Polkadot SDK.

So, I decided to find an alternative (but similar) approach to minimize the changes in the SDK and contain them purely within `polkadot/xcm`.

I came up with a proc-macro approach which should:
* help us generate most of the conversion logic automatically
* provide a clear instruction definition in one place
* maintain Bryan's idea of having instructions as individual structs so we can implement their execution logic separately (as well as test them that way)
* the individual structs should also allow us to implement special conversions granularly, without implementing the trivial ones by hand. For details, see the example below.

I was trying to find a design that have a good enough balance between clarity and automation.
You can see an early implementation draft here: https://github.com/UniqueNetwork/polkadot-sdk/tree/xcm-refactor.

Note that this is WIP and may change in the future.

Here is an example of what I'm currently trying to achieve.

```rust
// A versioned enum declaration.
//
// NOTE: I didn't fully figure out how to consistently expand #[versioned] attribute to versioned structs.
// But I have some ideas, the versioned structs are WIP.
#[versioned]

// The version range of all the instructions.
//
// The macro will generate the corresponding `Instruction` enum for each version
// within the corresponding v{version} module.
//
// They are aggregated in the automatically generated the `VersionedInstruction` enum
// which implements `From`, `IdentifyVersion`, the new `Versioned<const VERSION: usize>` trait, etc.
#[version(3..=5)]

#[derive(/* #[derive] attrs for `Instruction` enums within the corresponding v{version} modules */)]
#[/* other attributes for `Instruction` enums in the v{version} modules */]

#[versioned_enum(/* attributes for the `VersionedInstruction` enum */)]

// attributes for each of the VersionedInstruction enum's variants:
// #[codec(index = 3)]
// V3(_),
// #[codec(index = 4)]
// V4(_),
// #[codec(index = 5)]
// V5(_),
// NOTE: I'm unsure that this is the best way to do this. May change in the future.
// This is implemented in the draft as well, as I currently don't see a better way.
#[versioned_enum_variants(codec(index = version!()))]
pub enum Instruction {
  // `WithdrawAsset` instruction will appear in every version starting from v3.
  #[version(3..)]

  // `#[version(flatten)]` extracts the corresponding type for each version
  // via the new `Versioned<const VERSION: usize>` trait
  //
  // the `Versioned` trait is automatically implemented for every #[versioned] type
  // (e.g., it is implemented for `VersionedInstruction`).
  #[for_struct(/* attrs for the corresponding `WithdrawAsset` struct that will be generated in the v{version} module. */)]
  // NOTE: The `TryFrom` impls for `WithdrawAsset` structs of different versions are generated automatically
  WithdrawAsset(#[version(flatten)] VersionedAssets),

  #[version(3..=4)]
  Transact {
    origin_kind: OriginKind,
    require_weight_at_most: Weight,

    // The generic args are automatically pulled into the corresponding struct declaration / impls
    call: DoubleEncoded<Call>,
  },

  // The format has been changed, this requires a hand-written conversion.
  // The user needs to implement the `TryFrom` for the corresponding Transact structs (see below).
  //
  // NOTE: The conversions between `Instruction` enums of different versions are generated automatically.
  // They use `TryFrom` impls of the corresponding structs to perform the variant-to-variant conversions between versions.
  #[version(5..)]
  Transact {
    origin_kind: OriginKind,
    fallback_max_weight: Option<Weight>,
    call: DoubleEncoded<Call>,
  },
}

// User-defined conversion
impl<Call> TryFrom<v4::Transact<Call>> for v5::Transact<Call> {
  type Error = ();

  fn try_from(v4_transact: v4::Transact<Call>) -> Self {
    let v4::Transact { origin_kind, require_weight_at_most, call } = v4_transact;

    Ok(Self {
        origin_kind,
        call,
        fallback_max_weight: Some(require_weight_at_most),
    })
  }
}
// User-defined conversion
impl<Call> TryFrom<v5::Transact<Call>> for v4::Transact<Call> {
  type Error = ();

  fn try_from(v5_transact: v5::Transact<Call>) -> Self {
    let v5::Transact { origin_kind, mut call, fallback_max_weight } = v5_transact;

    let require_weight_at_most = todo!("... as defined in the current code ... ");

    Ok(Self {
        origin_kind,
        call,
        require_weight_at_most,
    })
  }
}
```


## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   | There were no referenda I was eligible to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |
