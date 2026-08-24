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
- Area(s) of Expertise/Interest: XCM, Bulletin Chain, Governance, Runtime, Node, end-to-end & integration testing

## Reporting period

- Start date: 2023/06/20
- End date: 2026/06/03

## Argument

I am applying for a fast promotion to **Rank 2, II Dan: Proficient Member**. I believe it is justified by the scope of work I already own and present in this argument.

Historically, my engagement with the ecosystem began in 2023 with a Web3 Foundation grant to build [`smart-bench`](https://github.com/paritytech/smart-bench), a benchmarking utility focused on ink! and Solidity contract performance comparisons. In May 2024 I attended the in-person Polkadot Blockchain Academy in Singapore where I [graduated with distinction](https://assethub-polkadot.subscan.io/nft_item/171-12), and since joining Parity in late 2024 my work has been focused fully on Polkadot.


### Bulletin Chain

My strongest evidence for Rank 2 is Bulletin Chain, a new system chain that realises a temporary storage solution for the Polkadot ecosystem, where I have taken a leading role across design, implementation, testing, and delivery for some of its major components. This directly addresses the Rank 2 expectation of taking primary responsibility for the implementation or improvement of a major protocol component.

The clearest example of design ownership is the **Auto Renewal** feature. Bulletin Chain stores data only for a fixed period, after which it expires and must be re-submitted manually, which is impractical for users who need data to persist. I designed the feature so that storage can be renewed automatically, and the [implementation](https://github.com/paritytech/polkadot-bulletin-chain/pull/313) was developed according to that design. The design spans runtime and node-side changes in the transaction-storage layer: the `MultiRenew` capability ensured that renewals preserve their submission order across the client and proof layers ([#11474](https://github.com/paritytech/polkadot-sdk/pull/11474), [#11962](https://github.com/paritytech/polkadot-sdk/pull/11962)).

Beyond features, I drove the validation and operational readiness of the chain, building the auto-renewal end-to-end suite and the stress/load testing infrastructure used to confirm the network behaves correctly under load ([#519](https://github.com/paritytech/polkadot-bulletin-chain/pull/519), [#369](https://github.com/paritytech/polkadot-bulletin-chain/pull/369), [#380](https://github.com/paritytech/polkadot-bulletin-chain/pull/380), [#475](https://github.com/paritytech/polkadot-bulletin-chain/pull/475)).

I also fully owned the operational side of launching Bulletin Chain on Polkadot. I prepared and drove the [registration referendum](https://polkadot.subsquare.io/referenda/1886) related to [tracking issue](https://github.com/polkadot-fellows/runtimes/issues/1153), coordinated directly with collator and RPC operators, and ran the initial testing needed to bring the network into a working state. While not related strictly to Polkadot, on the Bulletin Paseo deployment I act as one of the maintainers of the chain: I have a solid track record of investigating and resolving production issues there, including diagnosing and fixing chain stalls. I mention this because such sustained ownership reflects the component-level understanding and availability expected of a network maintainer.

### Asset Hub Migration: governance migration

I contributed to a critical and high-impact part of the Asset Hub Migration (AHM): the migration of governance from the Relay Chain to Asset Hub. This required Asset Hub to perform Root-level actions, such as `authorize_upgrade`, on the Relay Chain and system chains, and it required governance origin to propagate correctly between Asset Hub, the Relay Chain, and the system parachains.

I introduced [`LocationAsSuperuser`](https://github.com/paritytech/polkadot-sdk/pull/8210) in the Polkadot SDK, a generic XCM origin converter that lets a configured `Location` act as Root on the local chain; it became a building block for cross-chain governance origin propagation among all system chains.

I carried out much of the integration work to bring this together, syncing the OpenGov/AHM work with the latest feature branches ([bkontur/runtimes #20](https://github.com/bkontur/runtimes/pull/20), [#22](https://github.com/bkontur/runtimes/pull/22), [runtimes #877](https://github.com/polkadot-fellows/runtimes/pull/877)). To make sure these governance flows are verified before they reach the live networks, I built test coverage at multiple levels: Rust integration tests covering system-chain runtime-upgrade authorization and governance-origin propagation ([runtimes #783](https://github.com/polkadot-fellows/runtimes/pull/783), [#900](https://github.com/polkadot-fellows/runtimes/pull/900), [polkadot-sdk #9595](https://github.com/paritytech/polkadot-sdk/pull/9595)) and Polkadot Ecosystem Tests for the same flows, including initial `set_code`/`authorize_upgrade` system tests ([#411](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/411)), upgrade authorization by the Polkadot Relay Chain ([#218](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/218)), the "Asset Hub authorizes Polkadot upgrade via Collectives" scenario ([#577](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/577)), runtime-upgrade-via-referenda scenarios on the root and whitelisted-caller tracks ([#461](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/461)), and related system-test cleanup ([#472](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/472)). As part of this effort I also supervised contributions such as [polkadot-sdk #7321](https://github.com/paritytech/polkadot-sdk/pull/7321), providing guidance and reviews throughout and pushing the change over the finish line.

### Asset Hub Migration: Default DOT/KSM reserve changes

A subtle but high-impact consequence of AHM is that the Relay Chain stops being the default reserve for DOT/KSM, with Asset Hub taking over that role. As funds move to Asset Hub, including the Sovereign Account balances that parachains rely on for reserve transfers, any reserve transfer that still assumes the Relay Chain as the reserve risks trapping user assets once those balances are gone. 

For a seamless transition, I explored, designed, and proposed a solution for [remote reserve transfer with reserve discovery](https://github.com/karolk91/polkadot-remote-reserve-transfer-with-discovery), which was later incorporated into the Paraspell XCM SDK. This work laid out guidance for wallet and dApp teams on maintaining stable reserve transfers during and after AHM, as also mentioned in the forum post: https://forum.polkadot.network/t/dapps-action-required-for-ahm-for-keeping-cross-chain-transfers-stable/15169

I also took over the topic and drove the remaining work to completion, contributing the fixes, improvements, and backports to other stable branches that were still required ([polkadot-sdk #9544](https://github.com/paritytech/polkadot-sdk/pull/9544)). Beyond the code, I looked after deploying these features to the live Polkadot and Kusama networks, introducing the changes needed to roll them out ([runtimes #880](https://github.com/polkadot-fellows/runtimes/pull/880)).


### XCM

XCM is my other main area of protocol work, spanning support, issue resolution, protocol changes, and end-to-end testing. I frequently jump in to support people within Parity and across the wider ecosystem; most of this work is visible in the public XCM Element channel. As one example, I helped work through [issue #9093](https://github.com/paritytech/polkadot-sdk/issues/9093), which I then turned into a set of new XCMv5 asset-exchange test scenarios exercising remote `Transact`, `add_authorized_alias`, and remote swaps via Asset Hub ([#9195](https://github.com/paritytech/polkadot-sdk/pull/9195)).

A good example of recognising a subtle issue in code is the bug I found in `subsume_assets`, an essentially original part of the codebase. I assessed the impact with the utmost care and confirmed it could not be used for malicious action before providing a [fix](https://github.com/paritytech/polkadot-sdk/pull/9179).

End-to-end coverage is a large part of my XCM work, and I have contributed both to the emulated-test framework itself and to the scenarios that run on it. On the framework side, I fixed `assert_expected_events` so that it correctly fails when an expected event is missing rather than silently passing ([#8400](https://github.com/paritytech/polkadot-sdk/pull/8400)), synced and upstreamed XCM-related test utilities between the runtimes repo and the Polkadot SDK ([#8369](https://github.com/paritytech/polkadot-sdk/pull/8369)), and am adding a `dry_execute_with` helper that lets emulated tests mimic runtime-API-style execution which discards storage changes ([#8756](https://github.com/paritytech/polkadot-sdk/pull/8756)). On the scenario side, beyond the asset-exchange scenarios above, I added cross-chain teleport coverage between system chains, including total-issuance checks ([#215](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/215), [#216](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/216), [#205](https://github.com/open-web3-stack/polkadot-ecosystem-tests/pull/205)), and introduced `transfer_assets` benchmarking together with teleport test scenarios for the Coretime and People system chains ([#8752](https://github.com/paritytech/polkadot-sdk/pull/8752), [#8700](https://github.com/paritytech/polkadot-sdk/pull/8700)).

### Governance: Polkadot Referenda Tester

While working on governance migration topics and closely with Fellowship members, I noticed a gap in the ecosystem tooling with regard to testing referendum outcomes. I authored and maintain the [`polkadot-referenda-tester`](https://github.com/karolk91/polkadot-referenda-tester) project, which anyone can use to verify the effect of a referendum. It is an active project, and I am currently extending it with Polkadot-Kusama bridge support (related changes in Chopsticks, [#1029](https://github.com/AcalaNetwork/chopsticks/pull/1029)) that enables bridged Polkadot Collectives whitelisting scenarios. The tool has already been positively recognised among Fellowship members and has been put to use for every runtime-upgrade governance proposal since then.

Beyond implementation, I have gained experience expected of a Fellowship member by submitting Polkadot and Kusama referenda, including the Bulletin Chain registration referendum described above and a [Kusama runtime upgrade](https://kusama.subsquare.io/referenda/608). I have also published a [semi-technical article](https://hackmd.io/@karolk/S1qWzAs2-x) on referendum testing, sharing this knowledge with the wider community.

### Conclusion

I believe this work meets the expectations for **Rank 2** promotion: I have taken primary responsibility for a major protocol component (Bulletin Chain), becoming deeply familiar with it as a builder and with the design considerations typical in protocol development. I have made design-level contributions to the Polkadot SDK, authored the reserve-discovery design, built substantial end-to-end and integration test coverage, and provide ongoing public technical support in XCM channels. Through owning Bulletin Chain's operational launch on Polkadot, and acting as maintainer of the Bulletin Paseo deployment, I have demonstrated the availability and component-level understanding expected of a network maintainer, alongside continued, focused contribution to Polkadot.

### References

All my code contributions can be found through my Github profile, providing some of the important links below for easier accesibility

- **Polkadot SDK:** https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+author%3Akarolk91+
- **Polkadot Ecosystem Tests:** https://github.com/open-web3-stack/polkadot-ecosystem-tests/pulls?q=is%3Apr+author%3Akarolk91+
- **Fellowship Runtimes:** https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+author%3Akarolk91+
- **Chopsticks:** https://github.com/AcalaNetwork/chopsticks/pulls?q=is%3Apr+author%3Akarolk91+
- **Bulletin Chain:** https://github.com/paritytech/polkadot-bulletin-chain/pulls?q=is%3Apr+author%3Akarolk91+

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
