# Evidence-0001: Retention at Rank I

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | 2024/12/14                                                                                  |
| **Submitted by**| Dónal Murray                                                                                |


## Member details

- Matrix username: `@donal:parity.io`
- Polkadot address: <a target='_blank' href='https://collectives.statescan.io/#/accounts/142zGifFwRrDbFLJD7LvbyoHQAqDaXeHjkxJbUVwmDYBD7Gf'>142zGifFwRrDbFLJD7LvbyoHQAqDaXeHjkxJbUVwmDYBD7Gf</a>
- Current rank: **I**
- Date of initial induction: `2024/06/02`
- Date of last report: `2024/09/11`
- Area(s) of Expertise/Interest: `System Parachains, Agile Coretime`


## Reporting period

- Start date: 2024/09/11
- End date: 2024/12/14

## Evidence
In this reporting period my main focus has been the realisation of RFC-32 - minimal relay. I have been leading a team in Parity to spec out the protocol level changes required to move Staking, Governance and Balances to Asset Hub. I have planned out the phases and overall scope of the project, and we together broke these down into work packages. I have been dealing with parachains, wallet and UI teams and other stakeholders, hosting AMA sessions and explaining scope and stages of the project as well as clarifying technical details. I have been working to create a runtime representing the future state of Asset Hub (the Polkadot Hub) including this functionality, as the other members of the team finalise the implementation of the migration and changes required for specific subsystems to run on the Hub.

The transition of the Polkadot network to Agile Coretime [happened](https://polkadot.subsquare.io/referenda/1143) at the start of this reporting period, but the leases were migrated with incorrect end times due to a bug that we did not catch in testing. I root caused the problem, then proposed a [fix](https://github.com/polkadot-fellows/runtimes/pull/458) along with [instructions](https://hackmd.io/kurv6rTXTF6yvaUJ9uSNoQ) to verify the fix and test the upgrade. The migration to fix this was enacted before the point at which the problems in state would lead to parachains losing their core prematurely.
Since this point I have been working on some general cleanups and improvements to the broker pallet and Coretime Chain, and also scoping out future additions to improve UX and the economics of Agile Coretime primary markets.

I have onboarded and mentored several new developers in the ecosystem, mostly through my work within Parity.
I have been working towards a vision of better end to end testing of system parachain runtimes with one of my mentees. This is in part within the ecosystem tests repo to allow better testing for the system as a whole, and paving the way for better end to end tests for the Asset Hub Migration. 

I continue to be a regular reviewer in both the `polkadot-sdk` and `runtimes` repositories and remain active on Matrix and the Polkadot Forum, and I am an active participant in the Polkadot Fellowship monthly calls and in OpenGov. Referenda: [1](https://polkadot.subsquare.io/referenda/1161), [2](https://polkadot.subsquare.io/referenda/1202), [3](https://polkadot.subsquare.io/referenda/1271), [4](https://kusama.subsquare.io/referenda/466), [5](https://kusama.subsquare.io/referenda/454) and the referenda mentioned above in the transition to Agile Coretime.

As usual, code and review contributions since my last report can be found on my GitHub profile [`seadanda`](https://github.com/seadanda), but date-filtered links are below for the two most relevant repos:
- [`polkadot-sdk`](https://github.com/paritytech/polkadot-sdk/pulls?q=is:pr+author:seadanda+merged:%3E%3D2024-09-11)
- [`runtimes`](https://github.com/polkadot-fellows/runtimes/pulls?q=is:pr+author:seadanda+merged:%3E%3D2024-09-11)
Reviews:
- [`polkadot-sdk`](https://github.com/paritytech/polkadot-sdk/pulls?q=is%3Apr+reviewed-by%3Aseadanda+merged:%3E%3D2024-09-11)
- [`runtimes`](https://github.com/polkadot-fellows/runtimes/pulls?q=is%3Apr+reviewed-by%3Aseadanda+merged:%3E%3D2024-09-11)

These higher level architectural and mentoring activities have led to a decrease in my code contributions during the last couple of months compared with previous reporting periods, but I hope to return to previous levels as I aim towards a better balance. I also aim to solidify my thoughts and gather more input on the next iteration of the Agile Coretime economics and continue working towards the realisation of the minimal relay and the first stage of the Polkadot Hub.

## Voting record

|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote (i.e 0% voting activity). Out of 0 referenda in which members of higher ranks were in complete agreement, I have voted in line with the consensus 0 times (i.e 0 % voting agreement). |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |


## Misc

- [ ] Question(s): 

- [ ] Concern(s): 

- [ ] Comment(s): During the transition to Agile Coretime we encountered several avoidable issues, most embarrassingly when I used the wrong number of decimals and accidentally started Coretime sales at 1 nanoDOT, fixed in a subsequent [follow-up referendum](https://polkadot.subsquare.io/referenda/1172) which passed in (a record?) 4.5 days, but also some issues that could have been caught in testing. Together with @eskimor and @tmitrov we had a retrospective of the launch and I've tried to apply what we learnt to the Asset Hub Migration project with more refined processes and a more rigorous testing plan.
