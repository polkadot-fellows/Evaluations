# Argument-0001: Fast Promotion to Rank II

|                 |                 |
| --------------- | --------------- |
| **Report Date** | 2026/11/11      |
| **Submitted by**| Davide Gessa (dakk) |



## Member details

- Matrix username: @dakkk:matrix.org
- Polkadot address: 12iqwZGB2sguEhjFi2ZRuWWixU8mHJnSiP1pwDefqGsBy4rV
- Current rank: N/A
- Date of initial induction: N/A
- Date of last report: N/A
- Link to last report: N/A
- [Subsystems](subsystems.md) developed/maintained: JAM (Clients) (JamPy)

## Reporting period

- Start date: 2024/07/15 (Jampy first commit)
- End date: 2026/11/11


## Argument

I am requesting the fast promotion to Rank II for continuing the development of Jampy and in general to the ecosystem of JAM.

During the interview I proved my proficiency on the understanding of the graypaper, but not enough in order to be fast promoted to Rank III,
so I was suggested to apply for the Rank II fast promotion.


### Jampy: a clean room implementation of the graypaper (Manifesto §6.3.1)

In the last 2 years and 5 months, I dedicated my full-time activity to the study of the graypaper and to the development of JamPy,
a clean room implementation of the JAM protocol, written in Python.

This process led to 17k lines of code, a fully conformant implementation of the graypaper.

The fellowship already accepted the M1 Milestone of Jampy in full, through the referendum: https://collectives.subsquare.io/fellowship/referenda/641

After the acceptance of the M1 milestone, I continued the development, updating the codebase to every new version of the graypaper, and pushing it forward for the second milestone.

The current software is able to connect to other JAM implementations, and participate in the block production using the JAMNP-S protocol.

For clean room reasons, the code base is kept private at the moment, but it can be shared on request, and I will add reviewers who ask for it. The `jampy-node` and `jampy-target` are available as binaries and as docker images in the repository https://github.com/dakk/jampy-releases.

The git history of the development of Jampy is remarked on-chain (~once a week): https://polkadot.subscan.io/extrinsic?module=system&call=remark&page=1&time_dimension=date&address=12iqwZGB2sguEhjFi2ZRuWWixU8mHJnSiP1pwDefqGsBy4rV while the commit history along with remarks can be found here: https://dakk.github.io/jampy-remarks/

### Other JAM projects I pursued (Manifesto §6.3)

Besides Jampy, during this period I pursued:

- Test vectors for refinement code execution: https://github.com/dakk/jam-refine-vectors
- GP formula in-code tracking system: https://github.com/dakk/jambiato

### Keeping Jampy up to date and cross-checking with other implementations (Manifesto §6.3)

Jampy was always up to date with the latest version of the graypaper. I promptly helped davxy cross-check jampy against the polkajam implementation, finding and fixing discrepancies between the implementations, by running through jampy the trace artifacts and test vectors produced by polkajam in the [jam-test-vectors repository](https://github.com/jam-conformance/jam-test-vectors).

I was also promptly checking inconsistent results that arose in all the batches of the fuzzing process: jampy is registered as a fuzzing target in [jam-fuzzing#30](https://github.com/jam-conformance/jam-fuzzing/pull/30), and I partecipated in all the [batch fuzzing campaign PRs](https://github.com/jam-conformance/jam-fuzzing/).

### References

- Commit history along with on-chain remarks: https://dakk.github.io/jampy-remarks/
- On-chain remarks: https://polkadot.subscan.io/extrinsic?module=system&call=remark&page=1&time_dimension=date&address=12iqwZGB2sguEhjFi2ZRuWWixU8mHJnSiP1pwDefqGsBy4rV
- Fellowship referendum #641 (M1 Milestone acceptance): https://collectives.subsquare.io/fellowship/referenda/641
- Test vectors for refinement code execution: https://github.com/dakk/jam-refine-vectors
- GP formula in-code tracking system: https://github.com/dakk/jambiato
- Jampy binary releases (jampy-node, jampy-target, docker images): https://github.com/dakk/jampy-releases

## Voting record

N/A: I have not been eligible to vote on any referendum.
