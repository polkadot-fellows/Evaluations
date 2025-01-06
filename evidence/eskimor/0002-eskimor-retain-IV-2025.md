# Evidence-0002: Retain at Rank IV

|                  |                  |
| ---------------- | ---------------- |
| **Report Date**  | 2025/01/06       |
| **Submitted by** | Robert Klotzner  |

## Member details

- Polkadot address: `12pRzYaysQz6Tr1e78sRmu9FGB8gu8yTek9x6xwVFFAwXTM8`

- Current rank: 4
- Date of initial induction: 2023/07/16
- Date of last report: 2024/06/07
- Area(s) of Expertise/Interest: `Parachains Consensus`

## Reporting period

- Start date: 2024/06/07
- End date: 2025/01/06

## Evidence

### Implementation Efforts

I was together with Donal responsible for the launch of Agile Coretime an
Polkadot. The launch was successful, although not trouble-free. Due to the
offset of leases only present on Polkadot the migrated leases had been off. A
[fix](https://github.com/seadanda/runtimes/blob/50d429bce26ccf78d826aaea654e221827d6c950/system-parachains/coretime/coretime-polkadot/src/migrations.rs)
was provided in a timely manner, preventing user visible effects of this
mistake before they occurred.

I advised on how to make interlacing in Agile Coretime actually resilient and
working and I am fixing small issues with partioning in Agile Coretime [right
now](https://github.com/paritytech/polkadot-sdk/pull/6224) by simultaneously
also reducing latency for on-demand coretime by 6s: With #6224 in place an
order coming in at block X can already be served at block X+1. 

For elastic scaling I contributed with guidance and solutions, e.g. [here](https://github.com/polkadot-fellows/RFCs/pull/103#discussion_r1699146564).

### Designs & Architecture Work

Design wise I have a couple of ideas in the works, super-low-latency messaging
will be an RFC in the next period, but for this period I sketched down a way to
make [parachain runtime upgrades off-chain](https://github.com/polkadot-fellows/RFCs/blob/95f976311f92ba4138a2f31db2a2aebe86662105/text/0102-offchain-parachain-runtime-upgrades.md).
This is of lower priority for now, because for reducing barrier to entry we are
currently focusing on making smart contracts first-class citizens on Polkadot.
On the other hand for teams requiring an actual chain, lower deposits are not
their most important concern, but rather latency, reliability and scalability.
Nevertheless off-chain runtime play a major role in long-term stability and
scalability of the network. It also provides the basis for moving often used
smart contracts out of the PoV, further improving scalability.

In the last period, a solution to the probabalistic finality soundness issue,
which is summarized
[here](https://github.com/paritytech/polkadot-sdk/issues/633#issuecomment-2422484619),
was found.

I also formalized a general purpose, low-effort sybil resilience mechanism,
which should be useful for any p2p network wanting to improve its sybil
resilience. It is called [Proof of DOT](https://github.com/paritytech/polkadot-sdk/issues/6173) and is useful for
many p2p2 protocols, where only a larger number of sybil nodes can do harm to a
network, e.g. distributed hash tables. In particular it provides the means to
make reputation systems in p2p networks actually work. With sufficiently long
lock periods, sustained attacks become costly very quickly. I can also see how
this could provide the foundation for implementing full node incentivization
mechanisms for supporting efficient light client operations.

In addition to Proof of DOT, a simple mechanism to make the collator protocol
more resilient was also
[devised](https://github.com/paritytech/polkadot-sdk/issues/616#issuecomment-2422607361).
This relies on the more generic UMP messages introduced in
[RFC-103](https://github.com/polkadot-fellows/RFCs/pull/103), which is proving
over and over again to be a very powerful and enabling technique. It is also
the enabling piece of functionality, making very low latency messaging
possible. 

### Outreach

We identified that one of our short-comings is that we don't actually show off. We think our system can handle a lot of load, because it was designed to, but we never actually tried. This has two important implications:

1. We don't actually know how good we really are and where we still have work to do.
2. Most people out there don't bother looking into Polkadot's architecture, they wan to (rightly so) see what it can do in practice.

To tackle both of these, we decided to buy cheap cores on Kusama and put the network to the test. The resulting event is known as the "Spammening" and can be considered successful for a number of reasons:

1. It did have quite an impact marketing wise and the sentiment around Polkadot is slowly shifting (by far not only because of the Spammening, but it is an important ingredient).
2. We actually identified weaknesses in the implementation which either have been fixed already or are being fixed, resulting in an even more resilient Polkadot network: The canary served its purpose once more!

On a smaller scale I connected with the local Polkadot community and talked about Polkadot and the spammening in particular at the [Beefi meetup](https://www.meetup.com/web3-on-chain-dev-meetup-group/) in Prague.

### Learnings

Experience with the launch of Agile Coretime and the Spammening showcased that we need to get better in quality assurance, making Polkadot the resilient network it is technically setup to be. Further iterations of the Spammening are planned and we are investing in better testing strategies and techiques.

### Voting Participation

I usually try my best to be quite active and apparently managed to vote in more than 50% of the proposals I could vote on, in total numbers, I voted on [129 proposals according to subsquare](https://collectives.subsquare.io/user/12pRzYaysQz6Tr1e78sRmu9FGB8gu8yTek9x6xwVFFAwXTM8/votes).
