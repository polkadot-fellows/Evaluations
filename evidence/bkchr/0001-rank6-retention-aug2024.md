# Evidence-0001: Retention at Rank 6

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2024/09/04)                                                             |
| **Submitted by**| Bastian Köcher                                                                              |


## Member details

- Matrix username: @bkchr:parity.io
- Polkadot address: 13fvj4bNfrTo8oW6U8525soRp6vhjAFLum6XBdtqq9yP22E7
- Current rank: 6
- Date of initial induction: Seeding
- Date of last report: -
- Area(s) of Expertise/Interest: Runtime, Node, Parachains


## Reporting period

- Start date: 2024/03/19
- End date: 2024/09/04


## Evidence

My main contribution during this time was around the **Merkleized Metadata** feature, better known as "generic support for offline signers", as described in [RFC78](https://polkadot-fellows.github.io/RFCs/approved/0078-merkleized-metadata.html). I helped write the RFC, was responsible for its implementation in the Polkadot SDK, and also I contributed to rolling this essential feature out in the ecosystem. With this new feature, offline signers like Ledger are now able to support any FRAME-based parachain. 
Before this essential feature was implemented, the developers of the Ledger application had to hardcode the calls of each parachain/relay chain runtime; and each Ledger application update required a separate audit. This process was quite slow and didn't really fit in with the model of forkless runtime upgrade provided by Polkadot SDK.

The upgrade that enabled the generic offline signers support wasn't as smooth as I had wished. I knew beforehand that it would break the transaction format, requiring wallets and platform builders to be prepared for this breaking change. 
I helped to initiate a new process for ecosystem-wide notifications to get this critical information out and make sure that it reaches all ecosystem teams. But some builders still fell through the cracks and experienced difficulties with adapting to the new feature. 
To ensure that this never happens again, I proposed [RFC 99](https://polkadot-fellows.github.io/RFCs/approved/0099-transaction-extension-version.html) to introduce a new version in the transaction format. Thanks to this version, the runtime is now able to decode transactions made in the old format, and thus continue to support non-upgraded wallets.

My other important area of contribution was in supporting core developers, ecosystem builders, and blockchain engineers. 
For the launch of Coretime on Kusama, my work has mainly been about providing insights on the internals of Coretime to improve developers and users understanding, reviewing pull requests, and fixing small issues as they came up. The runtime upgrade on Kusama that should migrate the parachains from leases to Coretime did not work as expected. Some of the XCM messages for setting up the state on the Coretime chain failed. So, I debugged these XCM issues to ensure that ecosystem builders have a smooth transition to Coretime without any major issues.

I'm often involved in discussions with builders/users in various public channels like Element, [Polkadot Forum](https://forum.polkadot.network/u/bkchr/summary), or [Stackexchange](https://substrate.stackexchange.com/users/73/bkchr) to help solve their issues.

Besides the work highlighted above, I'm also very active in maintaining the [Fellowship runtimes repo](https://github.com/polkadot-fellows/runtimes/issues/created_by/bkchr) by providing reviews, helping with releases, and proposing changes of my own. 
I'm also very active when it comes to on-chain voting in the Fellowship, such as opening retention and promotion proposals for many members. I have taken part in an in-person interview to promote one
member to Architect (rank 4) and I have submitted Whitelisting referendums to fast track network upgrades and RFC related referendums. 
Since March, I have spent a lot of time reflecting on how to improve the Fellowship collective and coordination between members. I set up the [Fellowship Secretary](https://github.com/polkadot-fellows/help-center/issues/8) as a new role to help with internal Fellowship processes and also to work as a bridge with ecosystem teams.

For the past 6 years, I have dedicated myself to Polkadot to help the network become successful from the technical side of things and grow even more. I hope that my work and contributions listed above will convince you to vote in favor of my retention as a Grand Architect of the Polkadot Technical Fellowship.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.* 

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|III|70%   |100%  |   |  |
|I  |90%   |N/A   |   |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   | There currently doesn't exist any aggregation of the data, but I'm leading in the number of votes and should clearly fulfill the requirements. |

