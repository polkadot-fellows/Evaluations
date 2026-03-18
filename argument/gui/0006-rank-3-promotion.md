# Argument-0006: Promotion to Rank III

|                 |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Report Date** | Date of submission (2026/02/03)                                                             |
| **Submitted by**| Guillaume Thiolliere                                                                        |


## Member details

- Matrix username: @guillaume:parity.io
- Polkadot address: 13psJuWEjBuZGaFqXvFnLMC6ME8RVVfQAhtFhydYjW45oKgZ
- Current rank: I
- Date of initial induction: 2025/01/09
- Date of last report: 2025/11/02
- Area(s) of Expertise/Interest:
  - polkadot business-logic (aka the 'runtime')
  - the internals of the frame pallet framework
  - runtime and host APIs


## Executive Summary
I am applying for promotion to **Rank III**. My contributions to the Polkadot SDK demonstrate the technical mastery and security-conscious mindset required of a Fellow. Since my induction, I played a **primary role in the implementation** of the new Transaction Extensions, a major protocol component. Additionally, I have been a core implementer for the Proof-of-Personhood initiative (Referendum 1783) and have consistently demonstrated a security-first approach by precisely reviewing and even identifying one vulnerability before external auditors. My work is grounded in a deep understanding of FRAME's internals, knowledge built during my foundational contributions (2019–2022) and maintained through rigorous current-day code review.

## Argument

### 1. Primary Implementation of Major Protocol Components
*Manifesto Requirement: "Played a supporting role in the code-design and a primary role in the implementation of a major protocol component."*

My primary contribution during this period has been the **Transaction Extensions** overhaul. While the initial ideation and code originated from Gavin Wood and the implementation was then taken over by George Pisaltu, I took a **primary role in the concrete implementation, refactoring, and finalization** of this major component.

*   **Implementation:** I identified and fixed critical logic gaps in the original design, specifically regarding bare extrinsics and versioning in signed payloads. I refactored the codebase to ensure these changes were production-ready.
*   **Feature Expansion:** I engineered support for more than 12 extensions ([PR #7028](https://github.com/paritytech/polkadot-sdk/pull/7028)) and am currently implementing support for multiple extension pipelines per runtime ([PR #7035](https://github.com/paritytech/polkadot-sdk/pull/7035)).
*   **Resource Management:** I implemented the new weight reclaim logic ([PR #6140](https://github.com/paritytech/polkadot-sdk/pull/6140)) within this pipeline and fixed calculation errors in the initial specifications, ensuring accurate block resource accounting.

Additionally, I have implemented substantial components for the **People Chain** (Proof-of-Personhood):
*   **Origin Restriction:** I designed and implemented the Origin Restriction pallet ([Code](https://github.com/paritytech/polkadot-sdk/tree/f134881a56e7733a6b5171c81b05ce4df40dd695/substrate/frame/origin-restriction)) to regulate anonymous interactions.
*   **Modern APIs:** I introduced `pallet::authorize` ([PR #6324](https://github.com/paritytech/polkadot-sdk/pull/6324)) to replace the deprecated "validate unsigned" flow, significantly improving the developer experience by abstracting validation complexity.

### 2. Security-Conscious & Game-Theoretic Thinking
*Manifesto Requirement: "Thinking in a security-conscious, game-theoretic way... systems must function adequately even with a modest minority of malicious users."*

A Fellow must act as a guardian of the network. My contributions demonstrate this mindset:

*   **Proactive Security:** Through rigorous auditing of the SDK, I identified and notified Parity Technologies of a **moderate security issue three months prior** to its independent discovery by external auditors (SRLabs).
*   **Defensive Engineering:** The **Origin Restriction pallet** I designed is explicitly game-theoretic, created to grant some free usage to specific actors while keeping it fair with other actors by taking into account the congestion mechanism used in transaction fees.
*   **Code Hardening:** I regularly identify safety issues in the codebase, such as finding panics in the `verifiable` crate regarding invalid member keys ([PR #21](https://github.com/paritytech/verifiable/pull/21)) and fixing potential transaction pool spam vectors in the experimental tasks feature ([PR #10162](https://github.com/paritytech/polkadot-sdk/pull/10162)).

### 3. Knowledge Sharing & Advocacy
*Manifesto Requirement: "Demonstrable presence of knowledge sharing within the ecosystem."*

I actively bridge the gap between internal implementation and ecosystem adoption:

*   **Ecosystem Education:** I produced a technical deep-dive presentation on **Transaction Extensions** ([YouTube Video](https://www.youtube.com/watch?v=H1Y4pm8KIUI)) to help parachain developers prepare for this major breaking change.
*   **Documentation & Mentorship:** I provide high-volume code reviews, frequently catching some issues, such as the accidental removal of Sudo keys ([Comment](https://github.com/paritytech/polkadot-sdk/pull/7476#pullrequestreview-2622690960)), or using the same type for different concept like the relay chain and the parachain block number, or missing subtleties in the difference between the currency and the fungible API. I use these opportunities to mentor contributors on FRAME best practices.

### 4. Foundational Proficiency
*Manifesto Requirement: "Understand the difference between what something does and how it works... build substantial protocol components alone."*

My expertise is grounded in long-standing contributions to the core of FRAME (2019-2022). I rewrote the `decl_*` macros into the modern `pallet` macros and designed the **Instantiable Pallet** system (now critical for Asset Hub). This historical context proves my ability to design and maintain the foundational infrastructure that the entire network relies upon.

## Voting record
|  Ranks | Activity thresholds | Agreement thresholds | Member's voting activities | Comments |
|---|---|---|---|---|
|I  |90%   |N/A   | I have voted on 0 out of 0 referenda in which I was eligible to vote. |  |
|II |80%   |N/A   |   |  |
|III|70%   |100%  |   |  |
|IV |60%   |90%   |   |  |
|V  |50%   |80%   |   |  |
|VI |40%   |70%   |   |  |

## Misc
- [ ] Question(s):
- [ ] Concern(s):
- [ ] Comment(s):
