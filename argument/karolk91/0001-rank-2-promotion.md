# Argument-0001: Promotion to Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2026/06/03                                                                                  |
| **Submitted by**| Karol Kokoszka                                                                              |

## Member details

- Matrix username: @karol:parity.io
- Polkadot address: 1556APd4jcMDRod9SUxfTwGLasqFy3y3QFMGokkBwTdk2tev
- Current rank: Rank 0 (Candidate)
- Date of initial induction: 2025/05/21
- Date of last report: N/A
- Area(s) of Expertise/Interest: Bulletin Chain, XCM, Runtime, end-to-end & integration testing

## Reporting period

- Start date: 2023/06/20
- End date: 2026/06/03

## Argument
I am applying for accelerated promotion to **Rank 2, II Dan: Proficient Member**.

My first contribution to the Polkadot ecosystem was in 2023, when I received a Web3 Foundation grant to work on [`smart-bench`](https://github.com/paritytech/smart-bench), a utility for measuring smart contract performance (focused on ink! and Solidity).

In May 2024, I attended the in-person Polkadot Blockchain Academy cohort in Singapore and graduated with distinction:
https://assethub-polkadot.subscan.io/nft_item/171-12

Since late 2024, my work has been focused fully on Polkadot.

My public contributions can be found here:

- **Polkadot SDK:** https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Akarolk91+
- **Polkadot Ecosystem Tests:** https://github.com/open-web3-stack/polkadot-ecosystem-tests/pulls?q=is%3Apr+author%3Akarolk91+
- **Fellowship Runtimes:** https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Akarolk91+
- **Chopsticks:** https://github.com/AcalaNetwork/chopsticks/pulls?q=is%3Apr+author%3Akarolk91+
- **Bulletin Chain:** https://github.com/paritytech/polkadot-bulletin-chain/pulls?q=is%3Apr+author%3Akarolk91+

For the Rank 2 requirement of taking primary responsibility for the implementation or improvement of a major protocol component, my strongest evidence is my work on **Bulletin Chain**. I have taken a leading role in its design, implementation, testing, and delivery.

### Main contributions

1. **Bulletin Chain**

   I have taken primary responsibility for major parts of Bulletin Chain's design, implementation, testing, and delivery.

   One specific example is the **Auto Renewal** feature. I designed the feature, and the implementation details were developed according to the design:
   - https://github.com/paritytech/polkadot-bulletin-chain/pull/313

   The feature also required related support in Polkadot SDK, including:
   - https://github.com/paritytech/polkadot-sdk/pull/11474
   - https://github.com/paritytech/polkadot-sdk/pull/11962

   I also contributed directly to the validation and operational readiness of Bulletin Chain, including the auto-renewal end-to-end suite and stress/load testing infrastructure:
   - https://github.com/paritytech/polkadot-bulletin-chain/pull/519
   - https://github.com/paritytech/polkadot-bulletin-chain/pull/369
   - https://github.com/paritytech/polkadot-bulletin-chain/pull/380
   - https://github.com/paritytech/polkadot-bulletin-chain/pull/475

   Beyond implementation, I fully owned the operational side of launching Bulletin Chain on Polkadot. I prepared and drove the registration referendum (https://polkadot.subsquare.io/referenda/1886), coordinated directly with collator and RPC operators, and ran the initial testing to bring the network into a working state. On the Bulletin Paseo deployment I act as the de-facto on-call maintainer: I have a solid track record of investigating and resolving issues there, including diagnosing and fixing chain stalls, which reflects the deep, component-level understanding and increased availability expected of a network maintainer.

2. **XCM**

   I have contributed to protocol changes, end-to-end testing, and issue resolution. I also regularly support others in public XCM channels when questions or problems arise.

   **Protocol changes:**
   - `pallet-xcm` API change to use `VersionedAssetId` instead of a `u32` index to specify the fee asset, a breaking API change affecting `teleport_assets`, `reserve_transfer_assets`, `transfer_assets`, and the `limited_*` variants: https://github.com/paritytech/polkadot-sdk/pull/10243

   **End-to-end testing:**
   - XCMv5 asset exchange test scenarios (remote `Transact`, `add_authorized_alias`, remote swaps via Asset Hub): https://github.com/paritytech/polkadot-sdk/pull/9195

   **Issue resolution:**
   - Fixed `subsume_assets` incorrectly merging two `AssetsInHolding` instances, a bug that could result in loss of funds: https://github.com/paritytech/polkadot-sdk/pull/9179

   **Polkadot Ecosystem Tests**: I authored a body of end-to-end XCM and runtime-upgrade test coverage in [`polkadot-ecosystem-tests`](https://github.com/open-web3-stack/polkadot-ecosystem-tests).

   Runtime upgrade authorization (XCM origin propagation across chains):
   - Initial E2E system tests for `set_code` and `authorize_upgrade`: https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/411
   - Runtime upgrade scenarios via referenda (root & whitelisted-caller tracks): https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/461

   XCM teleport coverage between system chains:
   - Teleports between Polkadot Asset Hub and other system chains: https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/215
   - Teleports between Kusama Asset Hub and other chains: https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/216

3. **Asset Hub Migration**

   End-to-end testing, XCM-related work, and governance migration support.

   I contributed mainly to the governance and upgrade-authorization parts of the Asset Hub Migration, especially OpenGov migration to Asset Hub and origin propagation between Asset Hub, the Relay Chain, and system parachains.

   A key part of this work was introducing `LocationAsSuperuser` in Polkadot SDK, a generic XCM origin converter that allows a configured `Location` to act as Root on the local chain. This was needed for Asset Hub to execute Root-level calls such as `authorize_upgrade` on Relay Chain and system chains:
   - https://github.com/paritytech/polkadot-sdk/pull/8210

   I worked on the Polkadot and Kusama OpenGov/AHM branches. This included upstream work such as:
   - https://github.com/polkadot-fellows/runtimes/pull/626
   - https://github.com/polkadot-fellows/runtimes/pull/877

   I also authored integration-test work covering system-chain runtime upgrade authorization and AHM governance-origin propagation:
   - https://github.com/polkadot-fellows/runtimes/pull/783
   - https://github.com/polkadot-fellows/runtimes/pull/900

4. **Polkadot Referenda Tester**

   I authored and maintain [`polkadot-referenda-tester`](https://github.com/karolk91/polkadot-referenda-tester), which is used by Fellowship members to verify referendum outcomes. I am also extending its capabilities by working on Polkadot-Kusama bridge support in Chopsticks, which is needed for more complete referendum testing across bridged environments:
   - https://github.com/AcalaNetwork/chopsticks/pull/1029

### Governance & writing

Outside of implementation work, I have submitted referenda including:

1. Fellowship-related referenda:
   1. **Bulletin Chain registration:** https://polkadot.subsquare.io/referenda/1886
   2. **Kusama runtime upgrade:** https://kusama.subsquare.io/referenda/608
2. I have also published a semi-technical article related to referendum testing: https://hackmd.io/@karolk/S1qWzAs2-x

I believe this work meets the expectations for **Rank 2**: I have taken primary responsibility for a major protocol component (Bulletin Chain), becoming deeply familiar with it as a builder and with the design considerations typical in protocol development.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | N/A | As a Rank 0 Candidate, I was not eligible to vote on any referenda during the reporting period. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
