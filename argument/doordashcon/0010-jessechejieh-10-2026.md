# Argument-0010: Retention at Rank II

|                 |                                          |
| --------------- | ---------------------------------------- |
| **Report Date** | 2026/10/10                              |
| **Submitted by**| Jesse Chejieh                            |


## Member details

- Matrix username: @jessechejieh:matrix.org
- Polkadot address: 12zsKEDVcHpKEWb99iFt3xrTCQQXZMu477nJQsTBBrof5k2h
- Current rank: II
- Date of initial induction: 2022/09/29
- Date of last report: 2026/07/07
- Link to last report: https://github.com/polkadot-fellows/Evaluations/pull/321
- Area(s) of Expertise/Interest: FRAME, Runtime

## Reporting period

- Start date: 2026/07/07
- End date: 2026/10/10

## Argument

This period the OpenDev hosting pilot ran its remaining calls and, after measuring what the audience actually consumes, changed what a call leaves behind. On the security side, I corrected what the `NonTransfer` proxy admits on each system chain and joined the Fellowship's security working group. The treasury threads from the last report, ordered payouts and asset categories, continued through review. After the salary referendum's cancellation, I joined the initial working group on the Fellowship's mandate, accountability and compensation.

### OpenDev Hosting Pilot: Changing what the public record is

A call only produces value for people who were not on it if the record reaches them. The pilot tested that directly. The [21 July proceedings post](https://forum.polkadot.network/t/polkadot-technical-fellowship-opendev-call-proceedings-21-july-2026/18261) published a link to the full recording; against 128 topic views, the recording drew 2 clicks. The forum publishes per-link click counts on the post, so the figure is checkable by anyone reading this.

The conclusion is that a 27-minute meeting video is the most expensive artifact the pilot produces and the least used one. In the present, where attention is everything and people hardly sit through lengthy videos, the short format makes sense: a recap of a few minutes alongside the written proceedings, which remain the formal record. So from the final call of the pilot the post-call record is two things: the written proceedings, and a short talking-head recap cut with clips from the call itself. The calls are still recorded. The recording stops being the published deliverable and becomes source material for the recap. The September recording, posted unedited in that role, was opened five times in its first three days, more than the July edit drew in eight weeks.

The recap can also carry something the written proceedings cannot. Where a feature discussed on the call has an implementation to point at, the recap can show a short preview of it actually running. A paragraph describing what an RFC would do asks the reader to picture it; thirty seconds of it working does not. This is why the format is one to three minutes rather than a fixed sixty seconds: the base recap is short, and it stretches only when there is something worth showing. Being able to put a working snippet of the feature in front of people is the part a meeting recording never delivered, because nobody reached the timestamp where it was discussed.

This matters beyond format. The Fellowship's technical decisions are only public in any meaningful sense if someone outside the room absorbs them, and the measured answer was that almost nobody was. A written summary and a recap of a few minutes are both artifacts people finish.

One operational change came out of running the pilot: the agenda now goes up one week ahead of the call rather than two. Building an agenda means scanning the forum, the RFC and SDK repositories and the Fellowship channels for the topics most pressing right now, and that picture goes stale: two weeks out, half of it has moved on by the call. Posting one week out, after seeding the most pressing topics myself, leaves members room to add theirs without the thread overcrowding. The response has been more engaged: the September agenda, run on this schedule, drew five speakers including one from outside the Fellowship, the fullest of the pilot.

One closing note: this is the last retention Argument that will report on OpenDev. The pilot ended with the September call, and hosting now stands as a separate commitment under its own [operations funding proposal](https://collectives.subsquare.io/posts/39), which covers the delivered months and the rest of 2026. The proposal states the split plainly: the salary is judged at retention against the technical work of the period, while OpenDev is a scheduled service with fixed deliverables of its own: a call every month, an agenda ahead of it, proceedings and a recap after. The calls continue on that basis, and future Arguments will not cite them.

### Security (ongoing)

The `NonTransfer` proxy exists so an account can act on the system chains through a proxy without exposing it to value-moving calls. An audit of the per-chain filters this period found both directions wrong in places: some chains admitted value-moving calls, others blocked legitimate non-transfer ones like username management. The corrections span Asset Hub, Collectives and People on Polkadot and Kusama, plus their Westend counterparts ([runtimes#1296](https://github.com/polkadot-fellows/runtimes/pull/1296), [runtimes#1307](https://github.com/polkadot-fellows/runtimes/pull/1307), [runtimes#1243](https://github.com/polkadot-fellows/runtimes/pull/1243), [#13304](https://github.com/paritytech/polkadot-sdk/pull/13304), [#13306](https://github.com/paritytech/polkadot-sdk/pull/13306), [#13309](https://github.com/paritytech/polkadot-sdk/pull/13309)). The effect: a proxy can no longer move funds it was never meant to touch, including drawing Fellowship salary through `payout_other`, and the legitimate uses the proxy exists for work again.

Two smaller pieces in the same vein. [#13208](https://github.com/paritytech/polkadot-sdk/pull/13208) fixes a post-expiry underflow in `pallet-asset-rewards` so expired pools can no longer corrupt the reward accounting. And reviewing [#13290](https://github.com/paritytech/polkadot-sdk/pull/13290), a fix for a reported overflow that could bypass a child bounty's payout delay, surfaced that the parent pallet's `award_bounty` carries the same flaw; I asked for the same fix there and a test at the block-number limit, so one reported finding does not leave its twin unfixed.

I also joined the Fellowship's security working group this period and am currently working through the [security-findings](https://github.com/polkadot-fellows/security-findings) backlog.

### Governance: Ordered Payouts and Asset Categories

Both treasury threads from the last report continued through review. [Ordered Payouts](https://github.com/paritytech/polkadot-sdk/pull/11603) gives the treasury a fair queue: OpenGov-approved spends of each asset are paid in the order they were approved, so a later spend cannot jump ahead of earlier ones. [Asset Categories](https://github.com/paritytech/polkadot-sdk/pull/12687), under active review, lets the treasury hold and pay out more than one asset kind. The two touch the same dispatchables and the `Spends` migration, so the ordering work is being kept aligned with the categories work as it lands.

### Fellowship Restructuring: Mandate, Accountability and Compensation Working Group

The context is the cancellation of [Referendum 1940](https://polkadot.subsquare.io/referenda/1940), the salary funding request cancelled by [Referendum 1941](https://polkadot.subsquare.io/referenda/1941) at 99.2% aye, and the conditions the Web3 Foundation set out on the September OpenDev call for supporting a successor: no salary on top of full-time funding elsewhere, and a clearly specified mandate for what the Fellowship does. Gavin Wood's direction since then is that the expertise-for-salary model is not supportable as-is: compensation must be proportional to accountability, with the retention Argument sufficient for a low passive retainer, and the active salary requiring named supervision over a subsystem.

The mandate, accountability and compensation working group formed in response ([WG-0002](https://github.com/polkadot-fellows/Evaluations/pull/354)), its scope covering active-salary accountability, subsystem assignments and reporting, assignees and delegates, and a separate salary treasury. I am one of its initial members.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   |   |  |
|II |80%   |100%  |I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e undefined% voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e undefined% voting agreement).  | No referenda requiring Rank II votes during this period |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc

- [ ] Question(s):

- [ ] Concern(s):

- [ ] Comment(s):
