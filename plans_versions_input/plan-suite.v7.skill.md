# plan-suite v7 — Calibrated Commitment Planning

Generic planning skill for LLM agents. Vendor-neutral.

---

## 0. WHAT THIS IS — AND WHAT IT CLAIMS

This skill is a defense against predictable LLM failure modes when planning:
hallucinated load-bearing facts, anchoring, agreement mistaken for evidence,
hidden uncertainty, skipped risk analysis on irreversible steps, and plans
with no provenance.

**Meta-status: `unproven`.** By its own §3 standards, this skill carries no
evidence that following it produces better plans. Budget numbers, candidate
triggers, and confidence rules are starting hypotheses, not findings. Before
trusting it on high-consequence work, run the self-test:

1. Take 3–5 past planning failures (yours or documented).
2. Re-run each through this skill's gates, honestly.
3. Count how many failures a gate would have caught, and what the protocol
   would have cost.
4. If the ratio is poor for your environment, adjust the skill or abandon it.

A skill that never says "I am not the right tool" is dangerous. This one does
(§13).

**What changed from v6, in one line:** v6 taught you where to spend
multi-agent compute; v7 teaches you to spend *none at all* when evidence or
constraints already compel the answer, and to treat uncertainty as a
calibrated quantity rather than a binary status.

---

## 1. TRIAGE — READ THIS FIRST

Answer six questions before doing anything else.

1. Is there a **commitment** here — a point where the plan closes options or
   consumes resources irreversibly?
2. Is the request plan-dominant (execute a known path), learning-dominant
   (the path is discovered by doing), or mixed?
3. Is the environment well-understood (known tools, known constraints)?
4. Is the user asking for a plan, or for an answer / an action / an
   explanation?
5. What is the consequence of being wrong (trivial / material / high)?
6. Is there enough compute for more than one isolated invocation?

Route:

| Signals | Level | What to do |
|---|---|---|
| No commitment, reversible, trivial | L0 | Answer or act directly. Skip this skill. |
| One domain, low consequence, small uncertainty | L1 | Plan directly. Self-check. One caveat. |
| Any load-bearing commitment under real uncertainty, or unfamiliar environment | L2 | Run §2–§9. |
| High consequence, novel environment, interacting commitments, hard-to-reverse, or unresolved L2 contradictions | L3 | L2 + second adversarial lens (§5) + state-transition check (§8.4) + user veto on all irreversible trade-offs (§7.2). |

Request **shape** changes the artifact, not the depth:

- **Plan-dominant** → the commitment ledger assembles into an execution
  sequence.
- **Learning-dominant** → the ledger is an experiment queue: each entry
  spends something to reduce a named unknown, with a stop criterion. Do not
  fabricate a decision graph; there isn't one yet.

Write your route in one line:
`depth=L2, shape=mixed because: <observable signals>`.

**If in doubt between L1 and L2, prefer L1 unless the action is irreversible
or the environment is unfamiliar.**

---

## 2. THE COMMITMENT LEDGER (replaces the decision spine)

**Goal:** record only the points where the plan closes options or consumes
resources. Everything else is a derived action and inherits its legitimacy
from a ledger entry.

A **commitment** is any of:

- an irreversible or costly action (sent message, deleted data, money spent,
  public state);
- adoption of an architecture, dependency, or constraint that closes
  alternatives;
- an external dependency (on a person, a service, or an approval);
- an experiment that spends budget to reduce a named unknown
  (learning-dominant work).

A "decision" that is the mechanical consequence of a settled commitment is
**not** a ledger entry. Mark it as a derived action (§8).

```yaml
commitment:
  id: C1
  statement: <what we are committing to, one sentence>
  type: action | constraint | dependency | experiment
  load_bearing: true|false
  why_load_bearing: <what changes if this is wrong>
  reversibility: reversible | partial | irreversible | unknown
  evidence: []       # filled in §3
  attacks: []        # filled in §5
  resolution: null   # filled in §6
  confidence: null   # filled in §6
  actions: []        # filled in §8
```

### 2.1 Decomposition self-check

- **Coverage:** which of security, permissions, data, timing, cost, people,
  external dependencies, rollback, observability could bite here?
- **Granularity:** is any entry several commitments bundled? Any so small it
  doesn't matter?
- **Dependencies:** does C3 secretly depend on C1? Draw the edges.
- **Laziness:** did I create entries for things evidence or constraints
  already compel? Delete them (§3.1).
- **Blind spots:** what would a skeptical domain expert ask that I haven't
  considered? Name at least two.

### 2.2 Pre-mortem (L2+)

Before resolving anything, write one paragraph: "It is six months later and
this failed badly. What happened?" Keep it as input to §5.

---

## 3. EVIDENCE — FIRST, CANDIDATES LAST

### 3.1 The compulsion check (run before any candidate generation)

For each load-bearing commitment, ask: **do the verified evidence and the
hard constraints already leave exactly one viable option?**

- Yes → mark `resolved`, `confidence: high`, cite the evidence, spend **zero
  candidates**.
- No, and the gap is a fact about the world → verification or a discovery
  action (§3.2).
- No, and ≥2 options remain viable → candidates may be warranted (§4).

Most commitments in most plans are compelled. The default is **zero
candidates**; §4 is the exception, not the rule. This is the single biggest
budget saver in this skill.

### 3.2 Evidence budget

Verify claims that are load-bearing **and** externally checkable (source,
inspection, test, calculation).

- L1: 0–1 items. Only if a single fact is uncertain and decisive.
- L2: at most **2 per load-bearing commitment**.
- L3: at most **4**, with independent verification when feasible.

Hit the budget → stop collecting. Mark remaining unknowns as gaps and
branch, gate, or escalate.

### 3.3 Evidence record

```yaml
evidence:
  id: E1
  claim: <exact claim, one sentence>
  status: known | supported | derived | unproven | contested
  source: user_input | primary | secondary | inspection | test | calculation | derivation
  locator: <file, command, URL, formula, observation>
  checked_at: <timestamp>
  ttl: <how long this stays true; default: this session>
  limitations: <what this does NOT prove>
```

### 3.4 Evidence rules

- A citation is not evidence unless the source actually supports the claim.
- An agent's statement is not evidence.
- Two agents citing the same source are one piece of evidence.
- A calculation must expose inputs and formula to be recomputable.
- If you cannot inspect it, mark it `unproven`. Do not launder it into a
  fact.
- Contradictory evidence is `contested`. Do not average. Do not pick the
  convenient one.
- A conclusion is only as strong as its weakest load-bearing premise.
- **Evidence decays.** A fact verified last month about a moving environment
  is a hypothesis. Honor `ttl`; re-verify at execution time if stale.

---

## 4. CANDIDATE GENERATION — ONLY WHEN TRIGGERED

Generate candidates only if **all** hold:

1. the compulsion check failed (≥2 viable options remain after evidence);
2. the commitment is load-bearing;
3. the choice is weakly reversible or the consequence is material.

Otherwise skip this section entirely and record in the ledger that it was
skipped.

### 4.1 Independence modes — label what you actually achieved

| Mode | What it means | Honest claim |
|---|---|---|
| **staged** | One context, sequential passes with explicit information hygiene (§4.2) | Weakest; reduces anchoring, not shared bias |
| **isolated** | Separate invocation / sub-agent, own context, blind to others | Real information-flow independence — but same-family models share training data and blind spots |
| **external** | Different model family, or an actual test/inspection | Strongest practical |

Never upgrade a label. Same-family isolated agents converging is weak
evidence.

### 4.2 Information hygiene (mandatory in `staged` mode)

- Generate the candidate **before** reading any persuasive rationale for
  another option.
- Never re-read your own candidate during the adversarial pass; the attacker
  receives the action, not your reasoning.
- Temperature changes are not independence.
- Self-critique is not a review.

### 4.3 Number of candidates

- Compelled commitments: **0** (§3.1).
- Triggered: **2**. Use 3 only if the decision is close *and* weakly
  reversible (L3).
- If you cannot spawn that many, use `staged` mode and label it.

### 4.4 Candidate contract

Each candidate states: option (one sentence); rationale (3–5 bullets);
assumptions; rejected alternatives and why they remain viable; dependencies;
the two most likely failure modes; validation; what would change the
recommendation. A candidate that silently fills an unknown with an
assumption is invalid. Template: Appendix A.1.

---

## 5. ADVERSARIAL PASS — ONE PASS, LENSES BY CONSEQUENCE

Risk analysis and cross-examination are a single pass, run independently of
candidate generation. Do not show the attacker the candidate's persuasive
rationale unless a specific attack needs it.

**Choose lenses by what can break this commitment, not by depth level:**

- **Operational** — sequencing, partial completion, rollback, observability.
- **Environmental** — wrong assumptions about versions, permissions, people,
  timing.
- **Adversarial** — hostile or malformed inputs, worst case.
- **Invariant** — any path that violates a hard constraint (mandatory lens
  for every irreversible commitment).

L3: at least two distinct lenses. L2: one — chosen by the failure mode that
worries you most from the pre-mortem.

```yaml
attack:
  id: X1
  commitment_ref: C1
  scenario: <what goes wrong>
  trigger: <observable signal>
  impact: low | medium | high | critical
  prevention: [...]
  mitigation: [...]
  rollback: <specific, or "impossible" + consequence>
  residual: <what remains after mitigation>
```

A mitigation is not evidence that a risk is small. A path that reaches the
target only by violating a hard constraint is **invalid**, not risky.

---

## 6. RESOLUTION — CALIBRATED, COMMITMENT BY COMMITMENT

### 6.1 Resolution order

1. Hard constraints and invariants.
2. Verified observations and primary evidence.
3. Demonstrated test or calculation.
4. Independently supported reasoning.
5. Reversibility when evidence doesn't distinguish options.
6. Simplicity when still tied.

### 6.2 Confidence levels — operational definitions

- **high** — compelled: exactly one option survives the evidence and the
  constraints.
- **medium** — supported, but residual uncertainty exists and is safely
  held by a gate, a monitor, or a reversible experiment.
- **low** — a preference, an assumption, or an evidence gap remains; only
  safe under reversibility.

### 6.3 Ship rules

| Confidence | Reversible? | Consequence | Rule |
|---|---|---|---|
| high | any | any | ship |
| medium | yes | any | ship with monitoring |
| medium | no | material | gate or user veto before execution (§7) |
| low | yes | trivial | ship, flagged visibly |
| low | otherwise | — | branch, discovery action, or escalate. **Never ship silently.** |

### 6.4 Outcomes

`resolved` / `resolved-with-tradeoff` / `branch` / `gated` / `unresolved` /
`invalid`. Never force `resolved` to make the output look complete.

### 6.5 Standing rules

- **No majority voting.** Agent count is not evidence. A minority candidate
  with stronger evidence beats a majority with weaker. Unanimity among
  candidates sharing one assumption is still unproven.
- **Correlated error check:** did the candidates use genuinely different
  evidence paths? Same model family? Same assumption? Downgrade accordingly.
- **No silent synthesis.** Any action not proposed by a candidate is marked
  `derived-from: [C#, E#, constraint]`. If the derivation is not obvious,
  open a new commitment and run §3–§6 on it.

---

## 7. THE USER AS ORACLE

The user is the cheapest high-bandwidth oracle in the environment. Use them
deliberately.

### 7.1 ask_user — a first-class action type

```yaml
action:
  type: ask_user
  question: <one question, self-contained>
  recommended_default: <your best answer if they don't respond>
  cost: <what a wrong guess costs vs the latency of asking>
```

Rules:

- Batch questions; never ask serially.
- Cap: 2 per phase — and **never** ask about what is cheaper to verify by
  inspection, test, or search.
- Always ship a recommended default so the plan remains executable without
  a reply.

### 7.2 Trade-off veto (L2+, mandatory at L3 before irreversible steps)

Before any irreversible commitment executes, emit every
`resolved-with-tradeoff` as a one-line veto list:

```
VETO? C3: launch on raw VMs (cheaper, 2h rollback) vs managed service
(2x cost, 5min rollback). Proceeding with managed service.
```

Silence = approval. This is the highest-ROI safety mechanism in the skill:
one cheap question per material trade-off, asked before the door closes.

---

## 8. PLAN ASSEMBLY

Only after load-bearing commitments are resolved, gated, branched, or
explicitly shipped under the §6.3 rules.

### 8.1 Action contract

```yaml
action:
  id: A1
  from: C1
  evidence_used: [E1]
  attacks_used: [X1]
  type: discovery | change | validation | rollback | ask_user | branch | handoff
  objective: <which objective this serves>
  prerequisites: [<state conditions, not action ids>]
  execution: <precise action>
  expected_output: <observable result>
  validation: <specific acceptance test>
  failure_signals: [...]
  rollback: <specific, or "impossible" + consequence>
  provenance: candidate | derived | user-directed | compelled
  effort: low | medium | high
```

Rules:

- Validation is defined on the action: "GET /health returns 200 within 2s",
  not "check it works".
- Rollback is considered before execution. Impossible rollback + high
  impact → explicit gate.
- An action that cannot answer "which objective, how validated, what if it
  fails" is redesigned or cut.

### 8.2 Sequence

Order by prerequisite. For each action: what changes, what must be true
first, how success is observed, how failure is detected, how to recover,
what new information could invalidate downstream steps.

### 8.3 Reality gate

Before emitting: "A skeptical domain expert reads this — what do they
challenge first?" Address the top 1–2 challenges, or escalate.

### 8.4 State-transition check (L3, and for any expensive or irreversible
transition)

```text
S0 --A1--> S1 --A2--> S2 --A3--> S3
     |             |
  failure       failure
     v             v
  recovery      recovery
```

For each material transition: verify prerequisites; verify post-condition;
inject a plausible failure; verify the recovery state; verify the next
action is still valid; check that an earlier mitigation did not create a
later invariant violation. If execution is expected to reveal information,
make the information-gathering step explicit rather than pretending the
information is known.

### 8.5 Planning debt

A plan needs to be executable and recoverable, not complete. Ship at 80% if
the missing 20% is safely held by a gate or a reversible experiment. Record
it:

```yaml
planning_debt:
  - <what is unverified>
  - <how it resolves during execution>
```

---

## 9. MEMORY — DON'T RE-DERIVE WHAT YOU ALREADY PROVED

Commitment resolutions and evidence records are durable artifacts, not
session scratch.

- Store the ledger (§2), evidence records (§3.3), and attack records (§5)
  in the plan artifact.
- Honor `ttl`: at execution time, re-verify any evidence whose ttl expired.
  A re-check that returns a *different* answer is a replan trigger, not an
  annoyance.
- A commitment already resolved at `high` confidence with fresh evidence is
  not re-debated. Compute goes to what is new.

---

## 10. EXECUTION AND REPLAN

Hand off:

1. the relevant plan slice;
2. all hard constraints and invariants in full;
3. current validated state;
4. only the evidence needed for this slice;
5. pointers to the rest.

On failure: stop before compounding; validate the actual resulting state;
rollback when specified and safe; identify which assumption or transition
failed; re-plan the smallest affected subtree.

Global replan triggers: invariant violation; load-bearing evidence
invalidated, or expired-and-different; repeated failures showing the local
model is wrong; a change in target / constraints / environment touching
multiple commitments.

After each phase, append a digest:
`done / failed / new unknowns / state delta / next gate`.

---

## 11. STOP, SHIP, ESCALATE

**Stop when:** every load-bearing commitment is resolved, gated, branched,
or shipped under the §6.3 rules, and every action has an executable
validation.

**Stop earlier if:** a new candidate cannot change a compelled decision;
confrontation only restates existing findings; remaining uncertainty cannot
be reduced economically and is safely held by a gate or reversible
experiment; the compute budget is exhausted.

**Escalate instead of guessing when:** evidence is genuinely contested and
changes the path; a critical assumption cannot be tested; a hard constraint
conflicts with the requested outcome; rollback is unavailable for a
high-impact action; a trade-off depends on user priorities you cannot infer
— use §7, do not guess.

**Budget degradation order:** fewer candidates → fewer lenses → less prose.
**Never** remove evidence provenance, the adversarial pass, or the
trade-off veto from a high-consequence irreversible commitment to save
budget.

---

## 12. OUTPUT FORMAT

Depth-proportional. No fake audit trail for L0/L1.

### L0

Direct answer or action. No plan structure.

### L1

```
Objective: ...
Actions: ...
Validation: ...
Caveat: ...
```

### L2 / L3

Executable plan first, then a **machine-readable sidecar** — not a prose
appendix. Prose appendices are never re-read; a YAML ledger is cheap to emit
and cheap to audit.

```
## Plan
depth: L2 | shape: plan-dominant | learning-dominant | mixed
commitments: <count> | load_bearing: <count>
confidence: high=<n> medium=<n> low=<n>
unresolved: [] | gaps: [] | residual_risks: []

### Steps
A1. <action>
    from: C1 | evidence: E1 | attack: X1 | provenance: compelled
    validation: <observable>
    rollback: <specific>
    if fail: <response>

### Veto points (before irreversible steps)
<trade-off one-liners, §7.2>

### Gates
<branch / gate / escalation points, with triggers>

### Unknowns to resolve during execution
<list>

---
## Ledger (machine-readable sidecar)
commitments: [...]   # §2 schema, filled
evidence: [...]      # §3.3 schema, filled
attacks: [...]       # §5 schema, filled
planning_debt: [...]
```

---

## 13. WHEN TO ABANDON THIS SKILL

Answer directly when:

- the request is a question, an explanation, or a trivial action;
- the user explicitly wants a fast answer;
- no commitment is load-bearing;
- running the protocol would cost more than the plan's value;
- your achievable independence is only `staged` and the consequence is low
  — in that case, use L1 honestly.

---

## 14. QUALITY GATES — FINAL CHECK

- [ ] Every irreversible or costly action is a ledger entry marked
      load-bearing.
- [ ] Every load-bearing factual premise has provenance or is visibly
      `unproven`.
- [ ] The compulsion check ran before any candidate was generated — most
      decisions should have zero candidates.
- [ ] No commitment was resolved by majority vote; correlated assumptions
      were checked.
- [ ] Every irreversible commitment passed the adversarial pass and, at L3,
      the user veto.
- [ ] Every action has an observable validation criterion and explicit
      rollback or consequence.
- [ ] No action appears without a provenance tag
      (candidate | derived | user-directed | compelled).
- [ ] Confidence levels follow the §6.3 ship rules; nothing `low` shipped
      silently.
- [ ] Trade-offs are visible to the user before irreversible execution.
- [ ] Evidence TTLs are set; stale evidence is scheduled for re-verification,
      not trusted.
- [ ] The sidecar lets a future agent retrace the plan without trusting the
      author's memory.

Fail a gate → revise, gate, branch, or escalate. Do not polish and ship.

---

## 15. ONE-SENTENCE PRINCIPLE

> Verify before you generate; generate only when evidence leaves a real
> choice; attack what survives from an independent path; calibrate the
> residue instead of hiding it; and let the user veto a trade-off before it
> becomes irreversible.

---

## Appendix A — Templates

### A.1 Candidate prompt (use only when §4 triggers)

```
You are planning one commitment. Do not write a full plan.

Brief:
  Problem: <...>
  Target state: <...>
  Hard constraints: <...>
  Invariants: <...>
  Verified evidence: <list, or "none">
  Unknowns: <list>

Commitment: <C1 statement>

Produce:
  1. Chosen option (one sentence)
  2. Rationale (3–5 bullets)
  3. Assumptions you are making
  4. Alternatives you rejected and why they remain viable
  5. Dependencies
  6. The two most likely ways this fails
  7. How you would validate this worked
  8. What would change your recommendation

Do not fill unknowns with assumptions. If a fact is missing, say so.
```

Second candidate: add `Optimize for: <reversibility / failure-avoidance /
simplicity / testability>` — a different lens, not different wording.

### A.2 Adversarial prompt

```
You are attacking a proposed action. You are not a planner. Do not endorse
the plan.

Context:
  Commitment: <C1>
  Proposed action: <...>
  Hard constraints: <...>
  Environment facts: <...>

Answer:
  1. What could make this fail?
  2. Which assumption is most likely false?
  3. What happens under partial completion?
  4. Can rollback fail? Under what conditions?
  5. What is the first observable signal of failure?
  6. Does this create irreversible or cascading state?
  7. Does any path violate a hard constraint or invariant?
  8. What would a hostile or worst-case environment do to this?

For each risk: trigger, impact, detectability, prevention, mitigation,
residual.
```

---

## Appendix B — What changed from v6, and why

| v6 | v7 | Why |
|---|---|---|
| Decision spine, decomposed up front | Commitment ledger, built lazily | Most "decisions" are compelled by evidence, or are experiment queues, not decision points. The artifact should match the work. |
| 2 candidates per load-bearing decision | 0 by default; compulsion check first | Same-family candidates are correlated; evidence and constraints settle most choices before confrontation could add anything. |
| self / simulated / isolated / external | staged / isolated / external + explicit information hygiene | Closes the false dichotomy between "one context" and "sub-agents". Specifies what must not circulate, not how to isolate. |
| Binary evidence status, resolved/unresolved | Calibrated confidence + explicit ship rules | "Adequately supported" was undefined. Confidence x reversibility x consequence now decides ship / gate / veto. |
| User as escalation target | User as oracle + trade-off veto | Cheapest high-bandwidth information source. One question per irreversible trade-off is the highest-ROI safety mechanism available. |
| Separate risk-analysis and cross-examination phases | Single adversarial pass, lenses chosen by consequence | The two phases attacked the same object. Lens choice now follows what can break, not the depth label. |
| Prose audit appendix | Machine-readable YAML sidecar | Prose appendices are never re-read; a ledger is cheap to emit and cheap to audit. |
| Skill asserts its own prescriptions | §0: tagged `unproven`, with a self-test procedure | The skill violated its own evidence standards. Honesty is cheaper than false authority. |
| Session-scoped reasoning | Evidence TTL + re-verification policy | Environment facts decay. Silent evidence drift is a hidden replan trigger. |
| 13 dense sections | Core protocol (§1–§8) compressed; templates and rationale in appendices | Long protocols get performed, not followed. Compliance theater is the dominant failure mode of skills like this one. |
