# AI-SDLC Loop — Speaker Notes (15-minute presentation)

**Audience:** Executive Vice President (non-technical)
**Format:** 15 min presentation + 15 min Q&A
**Goal:** Secure buy-in for a tool-agnostic AI-SDLC loop running on GitHub Copilot.

Time budget per slide is below each header. Total is 14:45 with a 15-second buffer.

---

## Slide 1 — Title (45 sec)

Open with the headline: **"AI does the work. Humans approve every critical gate."**

Set the frame in one breath: this is not a tool pitch. It is a process pitch. The process is portable across any AI vendor; we run it on GitHub Copilot today because the team and the code already live in GitHub.

**Transition:** "Before I show you the loop, let me show you why we need one."

---

## Slide 2 — Where the time goes (90 sec)

Walk the four stat cards left to right:

- **70% Lost to Ceremony** — the developer's day is mostly tickets, breakdowns, status updates, PR review. Less than a third is actual product work.
- **3-5 days Requirement to PR** — even a simple story takes most of a sprint to go from clarification to merged code.
- **15-25% Rework Rate** — a quarter of every sprint is re-doing work because the requirements were misread.
- **10 Developers** — and inconsistency across the team, no shared quality bar.

Land the closing line: **"The problem is execution quality, not product ideas. AI should free judgment — not replace it."**

**Transition:** "There are two ways to apply AI to this problem. One is the spec-driven approach popular right now. The other is what I'm proposing we build."

---

## Slide 3 — Spec-driven vs Our Loop (90 sec)

Frame the choice honestly. The spec-driven approach is a real pattern emerging in the market. We respect it — but it does the wrong thing for us.

**Spec-driven side (red):**

- Write a detailed spec, generate code from it, ship.
- Three problems: it assumes the spec is perfect (it never is); there is no built-in testing — you trust, you don't prove; and you are tied to one vendor's editor and cloud.
- It only covers roughly 30% of the SDLC.

**Our side (teal):**

- Iterative — the loop never stops until the work is provably done.
- Tested first — code is written to make tests pass, not the other way around.
- Tool-agnostic — Copilot today, anything tomorrow.
- Four hard human gates — nothing ships without us.

**Transition:** "Let me show you what the loop actually looks like."

---

## Slide 4 — The Loop diagram (2 min — the centerpiece)

This is the single most important slide. Walk it slowly, clockwise, starting at 12 o'clock.

1. **Drill Reqs** — AI asks the questions a senior engineer would ask. What about edge cases? What about the empty state? Surfaces gaps before any code is written.
2. **Write PRD** — AI drafts the product requirement doc from the answers. Human reads it. **Gate 1: PRD approval.**
3. **Plan & Decompose** — AI breaks the PRD into a sequenced plan and tasks. Human reviews. **Gate 2: Plan approval. Gate 3: Issue breakdown approval.**
4. **Tests First** — for every task, AI writes the failing test before writing any code. This is test-driven development.
5. **AI Builds** — AI writes just enough code to make the tests pass.
6. **QA & Edge** — AI runs the tests, runs the linter, hunts edge cases, generates additional test scenarios.
7. **Loop to Green** — if anything fails, AI iterates. The loop does not stop until everything is green.
8. **Human Approve** — AI proposes the merge. **Gate 4: PR merge.** A human approves. The change ships.

**Land:** "Notice what's missing — there is no step where AI ships code by itself. Every loop ends with a human."

**Transition:** "Let me zoom in on those four gates."

---

## Slide 5 — Four Human Gates (60 sec)

These are the safety mechanism. Walk them quickly:

1. **PRD Approval** — before any code is written.
2. **Plan Approval** — before architecture is committed.
3. **Issue Breakdown Approval** — before AI starts iterating.
4. **PR Merge** — before code reaches production.

**Land:** "Four gates. Nothing ships without us. AI accelerates — humans decide."

**Transition:** "Inside the loop, every task runs in one of two modes."

---

## Slide 6 — HITL vs AFK (90 sec)

Two operating modes. Every task is tagged as one or the other.

**HITL — Human In The Loop:**

- High-stakes decisions: architecture, security, schema changes.
- First-time patterns: anything we have not done before.
- Judgment calls: trade-offs, ambiguity, customer impact.

**AFK — Away From Keyboard:**

- Well-defined work: standard CRUD endpoints, integrations.
- Clear repro bug fixes: known cause and known scope.
- Test generation: established patterns, existing contracts.

The footer line is the takeaway: **"AFK keeps the AI working while you're in meetings. HITL stops and asks when it matters."**

This is what enables a 10-developer team to act like 20.

**Transition:** "And here is why the loop outlasts any single vendor."

---

## Slide 7 — Tool-Agnostic by Design (60 sec)

The loop is the asset, not the vendor. **Copilot today** because:

- The code lives in GitHub.
- Enterprise SSO and audit are already configured.
- Cost is predictable.
- The team is already familiar with the editor.

But the same loop runs on Claude Code, Cursor, Gemini Code Assist, or whatever wins next year. **We own the process. The AI vendor is a swappable component — not a strategic dependency.**

**Transition:** "Here is what that gets us in business terms."

---

## Slide 8 — Business Impact (90 sec)

Walk the four stats. Be specific, never vague:

- **2x Feature Throughput** — dev capacity on features rises from 30-40% today to 60-70% with the loop.
- **5-10x Faster Cycle Time** — requirement to PR drops from days to hours.
- **Near 0 PRD Rework** — because AI drilled the requirements before any code was written.
- **Shift-Left 2** — defects caught during development by TDD, not after deployment by customers.

**Closing line:** "10 developers, same headcount — twice the features, fewer bugs. And early adopters of this loop are already running autonomous sprints that close hundreds of issues."

**Transition:** "If you're still wondering whether the loop beats the spec-driven alternative, here's the head-to-head."

---

## Slide 9 — Scorecard (75 sec)

Walk the table top-to-bottom. The pattern is the message — every row is a green check on our side and a red cross on the spec-driven side.

Call out the two rows that do the heavy lifting:

- **Quality mechanism: TDD red-green-refactor** vs none. This is the single biggest quality difference. We write a failing test (red), make it pass (green), then refactor with confidence. The spec-driven approach just generates code in one shot.
- **Proving it works end-to-end: Tracer-bullet slices** vs spec, then hope. We build a thin vertical slice that exercises every layer end-to-end before scaling out — like a tracer round in artillery, you watch where it lands and adjust.
- **Vendor independence** — a single-vendor lock-in is a multi-year commitment we don't need to make.

**Land:** "Eight capabilities. Our loop wins all eight."

**Transition:** "Of course, this isn't risk-free. Here's what could go wrong and how we prevent it."

---

## Slide 10 — Risks & Mitigations (75 sec)

Walk the four risks honestly.

1. **AI writes wrong tests** — tests are reviewed at Gate 4. Tracer-bullet slices prove end-to-end behavior before we scale out. Approved test patterns go in the shared library.
2. **Over-reliance on AI** — four human gates enforce judgment. HITL is mandatory for architecture, security, and schema.
3. **Vendor or tool shifts** — process is portable. If Copilot stalls, we swap in another AI. The loop, templates, and skills stay.
4. **Inconsistency across devs** — shared skills library and standard gates enforce one process across every repo.

**Land:** "We've thought about what could go wrong. The loop is designed so that no single failure ships code."

**Transition:** "Which brings me to the closing picture."

---

## Slide 11 — Closing (45 sec)

The final framing line: **"Spec-driven tools give you a faster waterfall. We give you a test-driven, iterative, developer-controlled AI engine — that catches bugs before they exist."**

Pause. Pipeline graphic on screen.

**Sign-off:** "Any AI. Any stack. Any team size. I'm ready to start the pilot whenever you are."

Open the floor for Q&A.

---

## Q&A — Anticipated Questions and Strong Answers

**Q: How do you know this works?**

The mechanics are not theoretical — TDD has 25 years of evidence behind it (Kent Beck, Extreme Programming). What's new is that AI can now write the tests and the code at developer speed. Industry early adopters running this style of loop are already closing hundreds of tickets per autonomous sprint. The pilot is how we prove it on our codebase before scaling.

**Q: Why not just use the spec-driven tool that's already getting attention?**

That approach covers requirements-to-code in a single pass. It does not cover testing, iteration, refactoring, or the 70% of the lifecycle that is "make it work right." It also locks us to one vendor's ecosystem — and every AI vendor relationship will look very different in 12 months. We don't want to bet the SDLC on one vendor's product roadmap.

**Q: What if Copilot loses ground to a competitor?**

The whole point of this approach. The loop is the asset; the AI is a swappable component. If Anthropic or Google or anyone else ships a better engine, we plug it in. Templates, skills, and gates stay.

**Q: How do you prevent AI from doing something destructive?**

Four human gates. Two operating modes (HITL/AFK). Pre-commit hooks block bad code from being committed. Tests block bad behavior from being merged. No human approval, no merge.

**Q: What's the cost?**

Copilot Enterprise seats for 10 developers — that is the new line item. No new infrastructure, no new platforms, no consulting fees. The pilot is staffed by the existing team.

**Q: What if developers resist?**

They won't — they are already using AI assistance ad-hoc. The loop gives them structure and removes the parts they hate (ticket grooming, status updates, ceremony). Pilot is opt-in among the 2-3 most enthusiastic developers; the rest see the results before they're asked to switch.

**Q: How do you measure success?**

Three numbers, baselined in week 1: cycle time (requirement → merged PR), defect rate (escaped bugs per 100 PRs), sprint capacity on feature work (vs. ceremony). Report at the end of a 2-week pilot. Concrete go/no-go.

**Q: How does this affect headcount?**

It doesn't. The plan is more output from the same 10 — not fewer developers. AI is the leverage; the developers are the judgment.

---

## Brand & QA Notes

- 11 slides, 16:9, generated from `build_deck.js` using PptxGenJS.
- Brand tokens applied per `deck-standard.skill.md` (Calibri; blue #003F68, midnight #00284A, teal #007886).
- Sandwich structure: dark title → 2 white → dark loop diagram → dark gates → 3 white → dark closing.
- Centerpiece is Slide 4: 8-step elliptical cycle with center label "CONTINUOUS LOOP — AI works • Humans approve."
- Rehearse Slide 4 (the loop diagram) and the closing line on Slide 11 — those are the two memorable beats.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       