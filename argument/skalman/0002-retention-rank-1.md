# Argument-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/03/20)                                                             |
| **Submitted by**| Skalman🐢                                                                        |


## Member details

- Matrix username: @skalman:matrix.org
- Polkadot address: 13zbXMsJgQbMkrjai3JUaQmVERZHKLNt42xaGjqJq7mBasDk
- Current rank: I
- Date of initial induction: 2023/10/30
- Date of last report: 2025/12/15
- Area(s) of Expertise/Interest: Cryptographic research and implementation

## Reporting period

- Start date: 2025/12/21
- End date: 2025/03/20

## Argument
I continued my work working on introducing BLS signature into Polkadot which enables many applications including more efficient bridging and various protocols base on aDKG including unbiasable random beacon and encrypt to the future. I also worked on the cryptography related to "Ring Proof" and "Ring VRF" which makes the cryptographic base for the proof of personhood and anonymous voting in Polkadot.

I. Work related to BLS in Polkadot:
I.1. Collaborated and pushed for 

  https://github.com/paritytech/polkadot-sdk/pull/1739
 
to be merged. This introduces measures to prevent Rogue key attacks against BLS keys and allows Polkadot to safely use BLS keyo. With that in, I drafted a PR for validators to be able to include BLS keys in their session keys on the Westend network pending approval:

https://github.com/paritytech/polkadot-sdk/pull/11149

I.2. Discussed, reviewed and modified RFC 156 for BLS host functions so BLS actually could go ahead into production:
https://github.com/polkadot-fellows/RFCs/pull/156

During RFC 156 discussion, we decided on some changes to host calls so we can use them for other BLS related application, I changed the code to that aim:

https://github.com/paritytech/polkadot-sdk/pull/11369

I.3. Implemented and benchmark Straus+GLV scalar multiplication for the w3f-bls library used in Polkadot to improve its performance, also implemented triple nugget BLS to compare its performance with double nugget currently used in Polkadot (and verified that double nugget is more efficient). Additionally refactored and cleaned up the w3f-bls library preparing it for a pending release and audit:

https://github.com/paritytech/bls/pull/81

II. Ring Proof:

II.1. Helped with batched verification of multiple ring proofs:

https://github.com/paritytech/ring-proof/pull/72

II.2. Review result of RingProof implementation in Python Grant

https://github.com/PolkadotOpenSourceGrants/delivery/pull/8

II.3. Reviewed the new changes to Ring VRF spec related to finding from security audit (https://github.com/davxy/bandersnatch-vrf-spec/pull/21) and inspected and gave advised to resolve linear growth in verification time with the size of the ring in the verifiable crate.


III. Misc
Review Generic BEEFY pull request and ZK blog post on Kusama:

https://github.com/paritytech/polkadot-sdk/pull/10763#pullrequestreview-3723962806

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | at Rank I, I was not eligible to vote on any referendum in this period. |  |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

