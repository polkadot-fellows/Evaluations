# Argument-0008: Retention at Rank 2

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission 2026/01/23                                                               |
| **Submitted by**| George Pisaltu                                                                              |


## Member details

- Matrix username: `@george.pisaltu:parity.io`
- Polkadot address: `128pmEUBSGjGeXZXNaAmomAJgVn77L74YT7Zdjd3fP63HWNP`
- Current rank: `2`
- Date of initial induction: `2024/08/16`
- Date of last report: `2025/10/16`
- Area(s) of Expertise/Interest: `Proof of Personhood, System Parachains, FRAME`


## Reporting period

- Start date: 2025/10/16
- End date: 2026/01/23


## Argument

This reporting period I have continued leading the Proof of Personhood effort as we work towards the
release planned for May this year. I created the roadmap for this release and have been actively
contributing to the design of all items on it.

The big ticket items, all currently under development, in our roadmap for our upcoming release
includes a privacy preserving payment system, personal alias authentication for people and
lite-people on AssetHub, and abstracting the ring management logic in the people pallet to a generic
members pallet. I am actively implementing this last item, the member set as a service, which will
provide reusable ring-based anonymous membership functionality. The pallet manages multiple ring
collections for different owners, each with its own configuration in terms of onboarding size,
membership suspension and manual ring deletion while maintaining the automated maintenance performed
by the people pallet in hooks like `on_idle` and `on_poll`.

I created the [resources
pallet](https://github.com/paritytech/individuality-public/tree/master/pallets/resources), which is
responsible for managing the free allowance of resources awarded to people and lite-people. This
includes allocations for statement store usage and bulletin storage. The pallet provides the
infrastructure for recognized individuals to benefit from their personhood status through tangible
resource allowances. The [people-lite
pallet](https://github.com/paritytech/individuality-public/tree/master/pallets/people-lite) and the
resources pallet were deployed to Paseo on a custom "Paseo People Lite" chain. This deployment
enabled the live demo of the Polkadot app chat and free transfers at sub0 in November 2025.

The theme of the Proof of Personhood project not being public continues until we launch. However, we
are about to open source more material with a restricted feature set release on Paseo again, this
time to give people building products a chance to interact with the new primitives.

I hope this argument demonstrates my continued contributions to the Polkadot ecosystem and justifies
my retention at rank 2 in the Fellowship.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II  |80%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referendums available for my rank to vote on. |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

