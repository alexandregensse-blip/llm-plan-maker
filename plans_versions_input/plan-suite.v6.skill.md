# plan-suite v6 — Decision-First Planning Under Uncertainty

Generic planning skill for LLM agents. Vendor-neutral.

---

## 0. WHAT THIS IS

This skill is a **defense against predictable LLM failure modes when planning**:

- hallucinating facts the plan depends on;
- anchoring on the first plausible answer;
- confusing agreement with evidence;
- hiding uncertainty to look complete;
- skipping risk analysis on irreversible steps;
- producing plans that look rigorous but have no provenance.

It is **not** a theory of planning. Real experts often plan iteratively,
conversationally, and opportunistically. This skill imposes structure because
LLMs, left unstructured, reliably fail in the ways above.

**Cost is real.** Most requests should not use this skill. Use the triage in §1.

---

## 1. TRIAGE — READ THIS FIRST

Answer five questions before doing anything else.

1. Is there a decision here whose answer could change the plan materially?
2. Is the action reversible if it goes wrong?
3. Is the environment well-understood (known tools, known constraints)?
4. Is the user asking for a plan, or for an answer / an action / an explanation?
5. Is there enough compute to run more than one agent?

Route:

| Signals | Level | What to do |
|---|---|---|
| No material decision, reversible, trivial | **L0** | Just answer or act. Skip this skill. |
| One domain, low consequence, small uncertainty | **L1** | Plan directly. Self-check. Note one caveat. |
| Multiple material decisions, OR real uncertainty, OR irreversible action, OR unfamiliar environment | **L2** | Run the full protocol below. |
| High consequence, novel environment, interacting decisions, hard-to-reverse, or unresolved L2 contradictions | **L3** | L2 + adversarial risk lenses + state-transition check + reality gate. |

Write your route in one line: `depth=L2 because: <observable signals>`.

**If in doubt between L1 and L2, prefer L1 unless the action is irreversible
or the environment is unfamiliar.** Over-running the protocol produces bloated
plans that look rigorous and communicate nothing.

---

## 2. DECOMPOSITION — THE HIGHEST-RISK STEP

Everything downstream depends on this. Do it carefully.

**Goal:** produce a decision spine, not a plan.

```yaml
decision_spine:
  - id: D1
    question: <the decision, in one sentence>
    load_bearing: true|false
    why_load_bearing: <what changes if the answer flips>
    reversibility: reversible|partial|irreversible|unknown
    evidence: []      # filled in §3
    risks: []         # filled in §5
    resolution: null  # filled in §6
    actions: []       # filled in §7
```

A decision is **load-bearing** if flipping it changes at least one of:

- the target outcome;
- a hard constraint or invariant;
- safety, security, legal, or financial exposure;
- architecture or topology;
- irreversibility;
- downstream dependencies;
- recovery options.

If a "decision" is just the mechanical consequence of another decision, **do
not make it a decision unit**. Mark it as a derived action.

### 2.1 Decomposition self-check (do not skip)

Before proceeding, ask:

- **Coverage:** have I missed a decision category? Consider: security,
  permissions, data, timing, cost, people, external dependencies, rollback,
  observability. Which of these could bite me here?
- **Granularity:** are any "decisions" actually several decisions bundled?
  Are any so small they don't matter?
- **Dependencies:** does D3 secretly depend on D1? Draw the edges.
- **Reversibility:** did I mark anything reversible that isn't?
- **Unknown unknowns:** what would a skeptical domain expert ask that I
  haven't considered? List at least two candidate blind spots.

If the self-check surfaces a new decision, add it. If it surfaces a category
you cannot reason about, mark it as an explicit evidence gap for §3.

### 2.2 Pre-mortem (L2+)

Before generating candidates, write one paragraph: "It is six months later and
this plan failed badly. What happened?"

This is your best defense against unknown unknowns. Keep it as an input to §5.

---

## 3. EVIDENCE — WITH BUDGET

Not every claim needs verification. Verify claims that are:

- load-bearing (they change a decision), AND
- externally checkable (a source, an inspection, a test, a calculation).

### 3.1 Evidence budget

- **L1:** 0–1 evidence items. Only if a single fact is genuinely uncertain and decisive.
- **L2:** at most **3 evidence items per load-bearing decision**. More than that is usually a sign the decision isn't actually load-bearing.
- **L3:** at most **5 per load-bearing decision**, with independent verification when feasible.

If you hit the budget, you do not collect more. You mark remaining unknowns
as gaps and either branch, gate, or escalate.

### 3.2 Evidence record

```yaml
evidence:
  id: E1
  claim: <exact claim, in one sentence>
  status: known | supported | derived | unproven | contested
  source: user_input | primary | secondary | inspection | test | calculation | derivation
  locator: <file, command, URL, formula, observation>
  limitations: <what this does NOT prove>
```

### 3.3 Evidence rules

- A citation is not evidence unless the source actually supports the claim.
- An agent's statement is not evidence.
- Two agents citing the same source are one piece of evidence.
- A calculation must expose inputs and formula to be recomputable.
- If you cannot inspect it, mark it `unproven`. Do not launder it into a fact.
- Contradictory evidence is `contested`. Do not average. Do not pick the convenient one.

### 3.4 Evidence dependency rule

A conclusion is only as strong as its weakest load-bearing premise. If D1
depends on E1 (strong) and E2 (unproven), D1 is not fully supported.

---

## 4. CANDIDATE GENERATION

Only for load-bearing decisions. Skip if the decision is compelled by evidence
or constraints.

### 4.1 Independence modes

| Mode | What it means | Honest claim |
|---|---|---|
| **self** | Same context, self-check | Not independent. Do not call it a review. |
| **simulated** | Isolated context, same model, different prompt, blind to other candidates | Weak independence. Reduces anchoring, not bias. |
| **isolated** | Separate invocation / sub-agent, own context, same brief, blind to others | Real information-flow independence. |
| **external** | Different model, different source, or actual test/inspection | Strongest available. |

State which mode you used. Do not upgrade `simulated` to `isolated` in your
claims. **Same-vendor models are correlated**: they share training data and
biases. Isolated same-family agents converging is weak evidence.

### 4.2 Number of candidates

- L1: 1 candidate, self-check.
- L2: 2 candidates per load-bearing decision. Use 3 if the decision is close.
- L3: 3 candidates per load-bearing decision.

If you cannot spawn that many, say so and downgrade the independence claim.

### 4.3 Candidate prompt template

```
You are planning one decision. Do not write a full plan.

Brief:
  Problem: <...>
  Target state: <...>
  Hard constraints: <...>
  Invariants: <...>
  Verified evidence: <list, or "none">
  Unknowns: <list>

Decision: <D1 question>

Produce:
  1. Your chosen option (one sentence).
  2. Rationale (3-5 bullets).
  3. Assumptions you are making.
  4. Alternatives you rejected and why they remain viable.
  5. Dependencies.
  6. The two most likely ways this fails.
  7. How you would validate this worked.
  8. What would change your recommendation.

Do not fill unknowns with assumptions. If a fact is missing, say so.
```

For a second candidate, add: "Optimize for: <reversibility / failure-avoidance /
simplicity / testability>." Use a different lens, not just different wording.

### 4.4 Candidate contract

Each candidate must state: option, rationale, assumptions, rejected
alternatives, dependencies, failure modes, validation, revision trigger.

A candidate that silently fills an unknown with an assumption is invalid.

---

## 5. RISK ANALYSIS — INDEPENDENT PATH

Run risk separately from candidate generation. Do not show the risk analyst
the candidate's persuasive rationale unless you need a specific attack.

### 5.1 Risk prompt template

```
You are analyzing the risks of a proposed action. You are not a planner.
Do not endorse the plan.

Context:
  Decision: <D1>
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

### 5.2 Risk lens (pick for L3)

- **Operational:** sequencing, partial completion, rollback, observability.
- **Adversarial:** hostile or malformed inputs, worst case.
- **Environmental:** wrong assumptions about versions, permissions, people, timing.
- **Invariant:** any path to the target that violates a hard constraint.

### 5.3 Risk record

```yaml
risk:
  id: R1
  decision_ref: D1
  scenario: <what goes wrong>
  trigger: <observable signal>
  impact: low | medium | high | critical
  prevention: [...]
  mitigation: [...]
  rollback: <specific, or "impossible" + consequence>
  residual: <what remains after mitigation>
```

A mitigation is not evidence that a risk is small. An action that reaches the
target only by violating a hard constraint is **invalid**, not risky.

---

## 6. RESOLUTION — DECISION BY DECISION

Do not pick a winning plan. Resolve each decision independently.

### 6.1 Resolution order

1. Hard constraints and invariants.
2. Verified observations and primary evidence.
3. Demonstrated test or calculation.
4. Independently supported reasoning.
5. Reversibility when evidence doesn't distinguish options.
6. Simplicity when still tied.

### 6.2 Outcomes

- `resolved` — one option is adequately supported.
- `resolved-with-tradeoff` — chosen, but a material trade-off remains.
- `branch` — the answer legitimately depends on a user preference or a future observation.
- `gated` — an action must happen first (a discovery step).
- `unresolved` — insufficient evidence, no safe default exists.
- `invalid` — all paths violate a hard constraint.

**Never force `resolved` to make the output look complete.**

### 6.3 No majority voting

Agent count is not evidence. A minority candidate with stronger evidence
survives a majority with weaker evidence. Unanimity among candidates that
share an assumption is still unproven.

### 6.4 Correlated error check

Before declaring a decision resolved, ask:

- Did the candidates use genuinely different evidence paths?
- Do they share an assumption? If so, that assumption is unverified even if all candidates agree.
- Are the candidates from the same model family? If so, downgrade the confidence.
- Would a different *kind* of expert agree? If not, why not?

### 6.5 No silent synthesis

If you introduce an action not proposed by any candidate, mark it:

`derived-from: [D#, E#, constraint]`

If the derivation is not obvious, create a new decision unit and run §4–§6 on it.

---

## 7. PLAN ASSEMBLY

Only after load-bearing decisions are resolved.

### 7.1 Action contract

```yaml
action:
  id: A1
  from_decision: D1
  evidence_used: [E1]
  risk_used: [R1]
  type: discovery | change | validation | rollback | branch | handoff
  objective: <which objective this serves>
  prerequisites: [<state conditions, not action ids>]
  execution: <precise action>
  expected_output: <observable result>
  validation: <specific acceptance test>
  failure_signals: [...]
  rollback: <specific, or "impossible" + consequence>
  effort: low | medium | high
```

Rules:

- Validation is defined on the action, not at the end. "Check it works" is not
  validation. "GET /health returns 200 within 2s" is.
- Rollback is considered *before* execution.
- If rollback is impossible, the action needs an explicit gate or escalation.
- An action that cannot answer "which objective, how validated, what if it
  fails" is redesigned or cut.

### 7.2 Sequence

Order by prerequisite, not by aesthetic. For each action, ask:

- what changes;
- what must be true before;
- how success is observed;
- how failure is detected;
- how to recover;
- what new information could invalidate downstream steps.

### 7.3 Reality gate (L2+)

Before emitting, ask once: "If a skeptical domain expert read this plan, what
would they challenge first?" Address the top 1–2 challenges in the plan, or
escalate.

---

## 8. EXECUTION AND REPLAN

Hand off:

1. the relevant plan slice;
2. all hard constraints and invariants;
3. current validated state;
4. evidence needed for this slice;
5. pointers to the rest.

On failure:

- stop before compounding;
- validate the actual resulting state;
- rollback if specified and safe;
- identify which assumption or transition failed;
- re-plan the smallest affected subtree.

Global replan triggers: invariant violation, load-bearing evidence
invalidated, repeated failures showing the local model is wrong, or a change
in target / constraints / environment that affects multiple decisions.

After each phase, record a digest:
`done / failed / new unknowns / state delta / next gate`.

---

## 9. STOP, SHIP, AND ESCALATE

### 9.1 When to stop planning

Stop when every load-bearing decision is resolved, gated, or explicitly
unresolved, and every action has an executable validation.

Stop earlier if:

- a new candidate is unlikely to change a decision (evidence or constraints compel it);
- confrontation only restates existing findings;
- remaining uncertainty cannot be reduced economically before execution;
- compute budget is exhausted.

### 9.2 Planning debt

A plan does not need to be perfect. It needs to be **executable and
recoverable**. If the plan is at 80 % and the missing 20 % is safely handled
by a gate or a reversible experiment, ship it. Record the debt explicitly:

```yaml
planning_debt:
  - <what is unverified>
  - <how it will be resolved during execution>
```

### 9.3 Escalate instead of guessing

Escalate when:

- evidence is genuinely contested and changes the path;
- a critical assumption cannot be tested;
- a hard constraint conflicts with the requested outcome;
- rollback is unavailable for a high-impact action;
- a decision depends on user priorities you cannot infer.

When budget-constrained, degrade in this order:

1. fewer candidates;
2. fewer non-load-bearing reviews;
3. less prose in the output.

**Do not remove evidence provenance or risk analysis from a high-consequence
decision to save budget.**

---

## 10. OUTPUT FORMAT

Depth proportional to work. Do not generate a fake audit trail for L0/L1.

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

Emit **the executable plan first**, then a compact audit appendix.

```
## Plan
depth: L2
decisions: <count>
load_bearing: <count>
unresolved: []
gaps: []
residual_risks: []

### Steps
A1. <action>
    from: D1 | evidence: E1 | risk: R1
    validation: <observable>
    rollback: <specific>
    if fail: <response>

### Gates
<branch / gate / escalation points, with triggers>

### Unknowns to resolve during execution
<list>

---

## Audit appendix

### Decisions
D1: <question>
  load-bearing: yes | why: <...>
  options considered: [...]
  evidence: [E1, E2]  (status: ...)
  risks: [R1, R2]  (residual: ...)
  resolution: resolved | gated | unresolved | invalid
  why: <one paragraph>
  revisit if: <trigger>

### Evidence
E1: <claim> — <status> — <source> — <limitation>
...

### Independence note
mode used: <self | simulated | isolated | external>
correlated errors: <assumptions shared across candidates>

### Planning debt
<list>
```

The audit appendix exists so a future agent or a human can retrace the
reasoning without trusting the consolidator's memory. It is not a place for
ceremony.

---

## 11. QUALITY GATES — FINAL CHECK

- [ ] Every load-bearing decision is identified and marked.
- [ ] No load-bearing decision was resolved by majority vote.
- [ ] Every load-bearing factual premise has provenance or is visibly `unproven`.
- [ ] Load-bearing risky actions have independent risk analysis.
- [ ] Hard-constraint violations are treated as invalid, not risky.
- [ ] Every action has an observable validation criterion.
- [ ] Rollback or non-rollback consequence is explicit for irreversible actions.
- [ ] No action appears without a decision origin or a marked derivation.
- [ ] Remaining uncertainty is visible, not hidden.
- [ ] The audit trail is sufficient to retrace the plan without trusting the author.
- [ ] The plan is executable *now*, not "after we figure out X".

If a gate fails: revise, gate, branch, or escalate. Do not polish and ship.

---

## 12. WHEN TO ABANDON THIS SKILL

Abandon the protocol and answer directly when:

- the request is a question, an explanation, or a trivial action;
- the user explicitly wants a fast answer;
- no decision is load-bearing;
- running the protocol would cost more than the plan's value;
- the environment does not allow sub-agents and the independence you can
  actually achieve is `self` (in which case, use L1 honestly).

A skill that never says "I am not the right tool" is dangerous. This one does.

---

## 13. ONE-SENTENCE PRINCIPLE

> Spend multi-agent compute only on decisions that can make the plan wrong;
> verify the facts those decisions depend on; attack them from an independent
> risk path; build the plan from what survives; ship when it is executable
> and recoverable, not when it looks complete.