# Argument-0010: Retention at Rank II

|                 |                                          |
| --------------- | ---------------------------------------- |
| **Report Date** | 2026/10/10                              |
| **Submitted by**| Jesse Chejieh                            |
| **Sponsored by**|                                          |


## Member details

- Matrix username: @jessechejieh:matrix.org
- Polkadot address: 12zsKEDVcHpKEWb99iFt3xrTCQQXZMu477nJQsTBBrof5k2h
- Current rank: II
- Date of initial induction: 2022/09/29
- Date of last report: 2026/07/07
- Link to last report: https://github.com/polkadot-fellows/Evaluations/pull/321
- [Subsystems](subsystems.md) developed/maintained: Runtimes (FRAME, APIs, integrations); System chains

## Reporting period

- Start date: 2026/07/07
- End date: 2026/10/10

## Argument

This period I ran the remaining calls of the OpenDev hosting pilot and changed what gets published after each call. I audited and corrected what the `NonTransfer` proxy admits on each system chain, and joined the Fellowship's security working group. The treasury threads from the last report, ordered payouts and asset categories, continued through review.

### OpenDev Hosting Pilot

I hosted the pilot's three remaining monthly calls (July, August, September), each with an agenda thread ahead. I also changed what a call publishes: in place of the full recording, the published record is now the written proceedings plus a one-to-three-minute recap cut from the call. The [21 July proceedings post](https://forum.polkadot.network/t/polkadot-technical-fellowship-opendev-call-proceedings-21-july-2026/18261) linked the full recording: 128 topic views, 2 recording clicks (per-link click counts are shown on the post). The September recording, posted unedited as source material, was opened five times in its first three days, more than the July edit drew in eight weeks. The Fellowship's technical decisions now reach people outside the call in a form they finish.

### Security Working Group

I audited the `NonTransfer` proxy filters on the system chains this period. The proxy exists so an account can act on those chains without exposing itself to value-moving calls, and I found both directions wrong in places: some chains admitted value-moving calls, others blocked legitimate non-transfer ones like username management. I wrote the corrections for Asset Hub, Collectives and People on Polkadot and Kusama, plus their Westend counterparts ([runtimes#1296](https://github.com/polkadot-fellows/runtimes/pull/1296), [runtimes#1307](https://github.com/polkadot-fellows/runtimes/pull/1307), [runtimes#1243](https://github.com/polkadot-fellows/runtimes/pull/1243), [#13304](https://github.com/paritytech/polkadot-sdk/pull/13304), [#13306](https://github.com/paritytech/polkadot-sdk/pull/13306), [#13309](https://github.com/paritytech/polkadot-sdk/pull/13309)). The effect: a proxy can no longer move funds it was never meant to touch, including drawing Fellowship salary through `payout_other`, and the legitimate uses the proxy exists for work again.

Two smaller pieces in the same vein. I fixed a post-expiry underflow in `pallet-asset-rewards` so expired pools can no longer corrupt the reward accounting ([#13208](https://github.com/paritytech/polkadot-sdk/pull/13208)). And reviewing [#13290](https://github.com/paritytech/polkadot-sdk/pull/13290), a fix for a reported overflow that could bypass a child bounty's payout delay, I found that the parent pallet's `award_bounty` carries the same flaw; I asked for the same fix there and a test at the block-number limit, so one reported finding does not leave its twin unfixed.

### Governance: Ordered Payouts and Asset Categories

Both treasury threads from the last report continued through review. [Ordered Payouts](https://github.com/paritytech/polkadot-sdk/pull/11603) gives the treasury a fair queue: OpenGov-approved spends of each asset are paid in the order they were approved, so a later spend cannot jump ahead of earlier ones. [Asset Categories](https://github.com/paritytech/polkadot-sdk/pull/12687), under active review, lets the treasury hold and pay out more than one asset kind. The two touch the same dispatchables and the `Spends` migration, so I am keeping the ordered payouts branch in step with the categories work as it lands through review.

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
