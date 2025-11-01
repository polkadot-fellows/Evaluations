# Evidence-0002: Retention at Rank 1

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission 2025/02/03                                                               |
| **Submitted by**| George Pisaltu                                                                              |


## Member details

- Matrix username: `@george.pisaltu:parity.io`
- Polkadot address: `128pmEUBSGjGeXZXNaAmomAJgVn77L74YT7Zdjd3fP63HWNP`
- Current rank: `1`
- Date of initial induction: `2024/08/16`
- Date of last report: `2024/11/14`
- Area(s) of Expertise/Interest: `System Parachains, FRAME`


## Reporting period

- Start date: 2024/11/14
- End date: 2025/02/03


## Evidence

During the previous reporting period, I was focused on delivering `TransactionExtension` to
`polkadot-sdk`. I continued to build on that effort this reporting period, starting with a [forum
post](https://forum.polkadot.network/t/introducing-transactionextension/10827) which aimed to raise
awareness of this new feature and the new possibilities it enables. Afterwards, I started
integrating the changes into the Proof of Personhood pallets to enable truly free transactions for
proven people. After it is released on the Polkadot People chain, this will be the first use case of
the free transaction model in the Polkadot ecosystem, which should serve as a blueprint for others
to use `TransactionExtension`s for their own use cases.

Following up on the Proof of Personhood work, I continued my work developing the pallets which will
support DIM1, as announced last year at the Web3 Summit, which will soon be ready for audit and then
will become public and hopefully make their way into a Polkadot People chain runtime upgrade. I
contributed to upgrading and stabilizing the Bulletin chain runtime in order to provide a stable
test environment for the teams developing the Citizenship app.

My other main focus this reporting period has been the collator selection pallet. Notably, I
[addressed a loophole](https://github.com/paritytech/polkadot-sdk/pull/7317) in the permissionless
collator auction mechanism which allowed collators to outbid someone and replace them in the
candidate list, and then they would immediately deregister and reregister back with a lower bond at
the session boundary. Furthermore, to address the growing problem of invulnerable collator slots
being more and more in demand, I proposed a [two round election mechanism for
invulnerables](https://github.com/polkadot-fellows/RFCs/pull/138), implemented in the collator
selection pallet, which would allow permissionless collators to periodically challenge existing
invulnerables in a referendum. This proposal aims to break down some of the innate barriers to
entering the invulnerable collator set, especially when the set is saturated.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0 % voting activity). | There were no referenda during the current period in which I was allowed to vote. I target to raise it to 90% at least for the next reporting period |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

