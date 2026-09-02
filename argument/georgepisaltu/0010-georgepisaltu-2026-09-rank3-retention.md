# Argument-0010: Retention at Rank 3

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission 2026/09/02                                                               |
| **Submitted by**| George Pisaltu                                                                              |


## Member details

- Matrix username: `@george.pisaltu:parity.io`
- Polkadot address: `128pmEUBSGjGeXZXNaAmomAJgVn77L74YT7Zdjd3fP63HWNP`
- Current rank: `3`
- Date of initial induction: `2024/08/16`
- Date of last report: `2026/02/24`
- Link to last report: https://github.com/polkadot-fellows/Evaluations/pull/259
- Area(s) of Expertise/Interest: `Proof of Personhood, System Parachains, FRAME`


## Reporting period

- Start date: 2026/02/24
- End date: 2026/09/02


## Argument

Since my last argument letter, I continued to lead the Proof of Personhood effort. As stated in my
promotion argument, the project became public under the name
[`individuality-community`](https://github.com/paritytech/individuality-community). We have already
partially integrated it into the runtimes in [PR
1233](https://github.com/polkadot-fellows/runtimes/pull/1233). I was involved in the design and
delivery of all of the components which were first showcased at the Web3 Summit and are now making
their way onto Polkadot.

The manifesto expects a Fellow to

> be able and willing to support that which they built given that it is running 24/7 on a public
network.

Most of the items listed below run on the Paseo testnets we operate for the teams building on top of
them, and are now either in the Polkadot runtimes, pending a runtime upgrade, or planned for the
next upgrade (mostly DIM2-related logic). I have been the main point of contact for the developers
integrating it and I intend to remain the owner of these components once they are live on Polkadot.

### Member set as a service

The ring management logic effort from my last argument, as seen in
[`pallet-members`](https://github.com/paritytech/individuality-community/tree/main/pallets/members),
is now used in a variety of new pallets other than `pallet-people` such as `pallet-coinage`,
`pallet-alias-accounts`, `pallet-pgas`, `pallet-members-subscriber`/`pallet-members-notifier`,
`pallet-airdrop` and `pallet-people-airdrops`. The abstraction of rings and proofs allowed us to
transition all our features to preserve users' privacy.

I kept improving the pallet based on what we saw on testnets in terms of usage patterns and
friction. The most visible change is self-inclusion: people who were recognized but stuck waiting
for a full onboarding cohort had a poor experience, so a self-onboarding path was added which lets
someone who waited long enough in the queue include themselves in a ring, with a configurable delay.
I also fixed a phantom stale ring entry left behind on full ring suspensions and added authorized
transactions for collection deletion. The public repository already has some more fixes, such as the
[suspension bypass in the game](https://github.com/paritytech/individuality-community/pull/33) and
the [leaked sufficient reference on
suspension](https://github.com/paritytech/individuality-community/pull/44).

### PGAS and free execution for people on Asset Hub

People already got some free execution in terms of certain pallet calls through transaction
extensions, but in order to give people free smart contract execution, the transaction extension
wasn't enough, so I proposed PGAS, a sufficient and burnable fee asset which recognized people and
lite people mint once per claim slot per day using Bandersnatch proofs to preserve each claim's
privacy. I implemented the minting and distribution in
[`pallet-pgas`](https://github.com/paritytech/individuality-community/tree/main/pallets/pgas) and
supported the smart contracts team with [PGAS storage
deposits](https://github.com/paritytech/polkadot-sdk/pull/11847) in `pallet-revive`. PGAS can now be
used as a fee asset for all people-originated calls on the companion Asset Hub runtime and has since
grown into a fee payment currency beyond smart contracts with plans to add expiry to each minted
claim so that we avoid hoarding of this asset. Batch claims are [in
review](https://github.com/paritytech/individuality-community/pull/75).

Building on PGAS, I proposed paid alias accounts on Asset Hub in
[`pallet-alias-accounts`](https://github.com/paritytech/individuality-community/tree/main/pallets/alias-accounts),
where people and lite people bind a regular account to an alias in a custom context and pay for it
in PGAS, so that applications which live in a smart contract get a stable alias account to interact
with while the person stays anonymous, available for verification through personhood precompiles.

### Anonymous allowances and rewards

Building on the
[`pallet-resources`](https://github.com/paritytech/individuality-community/tree/main/pallets/resources)
work from last year, I implemented anonymous statement store allowances for people and lite people,
where a member proves membership in a context made of a period and a slot and receives a temporary
allowance for a statement account without linking it to their identity. I supported the same
transition for the Bulletin chain allowances.

I designed and implemented
[`pallet-airdrop`](https://github.com/paritytech/individuality-community/tree/main/pallets/airdrop)
to give DIM2 participants rewards for their involvement in the game. The new design uses VRF-based
tickets and winners are chosen by entropy that nobody can influence and prizes are claimed
anonymously. The next iteration of prizes is
[`pallet-people-airdrops`](https://github.com/paritytech/individuality-community/tree/main/pallets/people-airdrops),
which are out of band draws (unrelated to the game), intended for more frequent and smaller prizes.
This mechanism is based on salt-derived tickets captured at scheduling time and the participant's
alias in the pallet's context.

### Supporting other efforts

I proposed the design of what would become
[`pallet-dotns-gateway`](https://github.com/paritytech/individuality-community/tree/main/pallets/dotns-gateway)
on Asset Hub, which allowed for free claiming of dotNS entries for both people and lite-people with
only the XCM delay between PC and AH. I contributed to the architecture of the
[Honour](https://github.com/paritytech/individuality-community/tree/main/pallets/honour) system
where I was a key reviewer. I pushed for the [proof batch
verification](https://github.com/paritytech/verifiable/pull/26) primitive in `verifiable`.

### `polkadot-sdk`

Following up on Extrinsic Horizon, I opened a PR introducing the [`AccountLike` trait and
`#[pallet::as_account]`](https://github.com/paritytech/polkadot-sdk/pull/11390), which lets pallets
with custom origins expose an account and opt into nonce tracking and fee payment per origin
variant, instead of each pallet writing its own transaction extension for replay protection. This is
needed to make the free transaction model in FRAME easier to use beyond `Signed`. I refactored
[`VerifySignature`](https://github.com/paritytech/polkadot-sdk/pull/11897) to fix an issue generic
signers had with its previous encoding, and I proposed a [sufficiency
query](https://github.com/paritytech/polkadot-sdk/pull/13059) in the `fungibles` traits.

My [PRs
authored](https://github.com/search?q=author%3Ageorgepisaltu+is%3Apr+repo%3Aparitytech%2Fpolkadot-sdk+repo%3Aparitytech%2Findividuality-community+repo%3Aparitytech%2Fverifiable+repo%3Aparitytech%2Fpolkadot-bulletin-chain+created%3A%3E%3D2026-02-24&type=pullrequests)
and [PRs
reviewed](https://github.com/search?q=reviewed-by%3Ageorgepisaltu+-author%3Ageorgepisaltu+is%3Apr+repo%3Aparitytech%2Fpolkadot-sdk+repo%3Apolkadot-fellows%2Fruntimes+repo%3Aparitytech%2Findividuality-community+repo%3Aparitytech%2Fverifiable+updated%3A%3E%3D2026-02-24&type=pullrequests)
in this period can be found on GitHub. The lists are incomplete, as most of the work happened in the
private repository and the history was not preserved when the project was made public.

I hope this argument justifies my retention at rank 3 in the Fellowship.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  | I have voted on 34 out of 58 referenda in which I was eligible to vote (i.e. 59% voting activity). Out of 33 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 33 times (i.e. 100% voting agreement). | 8 of the 58 referenda were M1 interview approvals for the JAM implementers prize, which I am not expected to vote on as I didn't participate in the interviews. Excluding those, I have voted on 34 out of 50 referenda (i.e. 68% voting activity). I acknowledge this is still below threshold. |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
