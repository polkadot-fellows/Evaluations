# Argument-0001: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/12/15)                                                             |
| **Submitted by**| Skalman🐢                                                                        |


## Member details

- Matrix username: @skalman:matrix.org
- Polkadot address: 13zbXMsJgQbMkrjai3JUaQmVERZHKLNt42xaGjqJq7mBasDk
- Current rank: I
- Date of initial induction: 2023/10/30
- Date of last report: NA
- Area(s) of Expertise/Interest: Cryptographic research and implementation

## Reporting period

- Start date: 2025/09/21
- End date: 2025/12/20


## Argument
I am working on introducing BLS signature into Polkadot which enable many applications including more efficient bridging and various protocols base on aDKG including unbiasable random beacon and encrypt to the future.
1. Following the discovery of the weakness of previous design, I have redesigned and (re)implemented the proof of possession in Substrate cryptography module to be able to handle diverse type of proofs so it can defends against multiple attacks: https://github.com/paritytech/polkadot-sdk/pull/9471

2. With the new system in place of proof of possession, I worked with @bkchr to update the code for the runtime generation and verification of Proof of Possession. I resolved the errors arising from runtimes implemented after the original code was authored 2 years ago, such as AssetHub and other test runtimes:

https://github.com/paritytech/polkadot-sdk/pull/9471
https://github.com/paritytech/polkadot-sdk/pull/9949
https://github.com/paritytech/polkadot-sdk/pull/10002
https://github.com/paritytech/polkadot-sdk/pull/10033

3. I also worked on improving the efficiency of the w3f-bls library, the BLS library used in Polkadot BLS signature implementation and to benchmark various curves and algorithm used in generating this signature including using a third sister curve for the Chaum-Pederson signatures and implementing Strauss-Shamir optimization for double scalar multiplications, I also wrote the benchmarking code to assess the effects of these efforts:

https://github.com/w3f/bls/compare/master...skalman--cp-on-sister-curve

4. I mentored a PBA alumni to submit a grant for a prototype Web3Sum based bridge and reviewed grants related to JAM cryptography and ZK crypto on Polkadot:

https://github.com/PolkadotOpenSourceGrants/apply/pull/46#issuecomment-3529911905
https://github.com/w3f/Grants-Program/pull/2603/files
https://github.com/PolkadotOpenSourceGrants/delivery/pull/8


5. I gave a talk on the merits of decentralization: 
https://cfp.openfest.org/openfest-2025/talk/PNBMQV/

6. I regularly attended the OpenDev calls. I guess this is verifiable on Youtube: https://www.youtube.com/playlist?list=PLtyd7v_I7PGlDJCCCLGLjJ0yv33JAEE_-

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | My understanding is that at Rank I, I am not eligible to vote on referenda. |  |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

