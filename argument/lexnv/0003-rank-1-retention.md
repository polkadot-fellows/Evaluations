# Argument-0002: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2025/07/31)                                                             |
| **Submitted by**| Alexandru Vasile                                                                            |


## Member details

- Matrix username: @lexnv:parity.io
- Polkadot address: 14Mjra9hNggCSLyVv3AmtvpjeyBhUMwiEEBXGFidu3ZWTEQN
- Current rank: I
- Date of initial induction: 2025/02/12
- Date of last report: 2025/02/12
- Area(s) of Expertise/Interest: `Substrate Node`, `Substrate RPC`, `FRAME`


## Reporting period

- Start date: 2025/05/06
- End date: 2025/07/31


## Argument

Over recent months, I have focused on stabilizing the Litep2p network backend and enabling Async Backing in Polkadot Asset Hub. These efforts have enhanced network performance, reduced resource consumption, and paved the way for faster block times, significantly improving the Polkadot ecosystem's efficiency and scalability.

### Litep2p Network Backend: The Default Network Backend

Litep2p is now the default network backend in the Polkadot SDK release 2503-7, marking its transition to a production-ready state across all chains. The implementation, detailed in [PR #8461](https://github.com/paritytech/polkadot-sdk/pull/8461), delivers substantial performance improvements over its predecessor, libp2p.

Litep2p consumes roughly half the CPU resources compared to libp2p, which frees up significant processing power for other subsystems and allows nodes to operate on more cost-effective hardware. Additionally, Litep2p’s optimized Kademlia DHT implementation enables faster peer discovery, finding 1,000 authority records in approximately two minutes, compared to the ten minutes required by libp2p. To engage with the community, I announced the stabilization of Litep2p in a post on the [Polkadot Forum]((https://forum.polkadot.network/t/announcing-the-stabilization-of-the-litep2p-network-backend/13712)), fostering feedback and encouraging adoption.


### Async Backing in Polkadot Asset Hub

The Polkadot Asset Hub now benefits from Async Backing, a critical step toward reducing block times to six seconds, which enhances transaction throughput and network responsiveness.

This implementation optimizes block production, allowing for faster finalization and improved transaction processing efficiency.
To ensure stability during the rollout, I closely monitored the Kusama Asset Hub network and documented my findings in a comment on GitHub [issue #460](https://github.com/polkadot-fellows/runtimes/issues/460#issuecomment-3078678176).

The Async Backing implementation performs reliably under normal conditions. However, under extreme network scenarios, such as when collators cannot connect to the backing group, parachains may produce blocks at one-minute intervals, as noted in Polkadot SDK issue [#9227](https://github.com/paritytech/polkadot-sdk/issues/9227).

To support this work, I developed a block visualizer tool, hosted at [lexnv/block-visualizer](https://lexnv.github.io/block-visualizer/), which allows users to scroll through a timeline to observe parachain forks dynamically. I also created a monitoring script, available at my [async-backing-monitor](https://github.com/lexnv/async-backing-monitor) GitHub repository, to detect identical block timestamps, similar to the polkadot-interceptor tool. My proof-of-concept in [PR #9160](https://github.com/paritytech/polkadot-sdk/pull/9160) and a subsequent fix by Alex Gheorghe in [PR #9178](https://github.com/paritytech/polkadot-sdk/pull/9178) outline potential solutions to address these edge cases.

The transition to Async Backing has been smooth, with no issues reported to date.

### Substrate

Within the Substrate realm, I implemented several improvements to enhance network stability and performance. I ensured that Litep2p does not report localhost addresses as external, which promotes a healthier DHT over time, as detailed in [PR #9281](https://github.com/paritytech/polkadot-sdk/pull/9281). Additionally, I modified GRANDPA to prevent peer disconnects or bans during authority set changes, ensuring network stability, as addressed in [PR #9015](https://github.com/paritytech/polkadot-sdk/pull/9015). I also resolved issues with gap sync cleanup during synchronization in [PR #8445](https://github.com/paritytech/polkadot-sdk/pull/8445).


### Other work:

Besides the mentioned topics, I'm providing reviews for my area of expertise in polkadot-sdk and RFCs.

## Voting record
*Provide your voting record in relation to required thresholds for your rank.*

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 100 % voting activity)  | There were no referendums available for my rank to vote on. |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): 

