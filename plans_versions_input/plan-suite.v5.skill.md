# plan-suite v5 — Evidence-Grounded Multi-Agent Planning

Generic planning skill for Claude / Gemini / GPT / other LLM environments.

## Core thesis

A plan should not be treated as a single model's answer. It is a **resolved set of decisions** produced by independent candidate generation, evidence verification, adversarial challenge, and independent risk analysis.

The plan is the final projection of those resolved decisions into an executable sequence.

The default goal for material plans is therefore:

> **No load-bearing decision enters the final plan without independent confrontation, evidence provenance, and an explicit risk check.**

The protocol scales down for trivial or low-risk work. The skill must optimize for **decision quality per unit of compute**, not maximum agent count.

The skill is vendor-neutral. An "agent" means an isolated model invocation, sub-agent, tool-assisted worker, or independently prompted model context.

---

# 0. NON-NEGOTIABLE PRINCIPLES

## 0.1 Plan around decisions, not around prose

A plan is composed of **decision units**. Each decision unit represents something that could materially change the path, cost, risk, outcome, or reversibility of the work.

Examples:

- choose architecture A vs B;
- decide whether a migration is safe before modifying production;
- choose between two remediation sequences;
- decide whether an unknown must be investigated before execution;
- determine a prerequisite that changes downstream actions.

Do not waste multi-agent compute on formatting, obvious sequencing glue, or deterministic actions.

## 0.2 Distinguish evidence from agreement

Multiple agents agreeing is **not** evidence.

Three agents repeating the same unsupported claim are still one unsupported claim.

Likewise, three agents citing the same source do not provide three independent pieces of evidence.

Evidence has provenance: source, observation, calculation, experiment, inspection, or derivation that another agent can inspect or reproduce.

## 0.3 Independence is a property of information flow

Calling three prompts "independent" is insufficient.

A reviewer is independent only to the extent that it did not inherit the conclusion it is supposed to test.

Minimum independence levels:

| Level | Meaning | Counts as independent confrontation? |
|---|---|---|
| I0 | Same agent self-checking its own answer | No |
| I1 | Same model, isolated context, different prompt, sees same candidate | Weak review only |
| I2 | Isolated agent generates its own candidate from the same brief before seeing other candidates | Yes |
| I3 | Isolated agent independently verifies evidence / performs a test / derives a result without relying on another agent's conclusion | Yes, for evidence |
| I4 | Independent agent performs a distinct method or evidence path and is blind to the other path's conclusion | Strongest practical independence |

L2+ plans require I2 candidate independence. Load-bearing factual claims should reach I3 evidence verification whenever verification is feasible. High-consequence decisions should use I4 where practical.

## 0.4 Risk analysis must be independent from plan generation

The risk analyst is not another planner wearing a risk label.

It must inspect the proposed decision/action and ask independently:

- What could make this fail?
- What assumption could be false?
- What happens under partial completion?
- What happens if the environment differs from the brief?
- What dependency disappears or changes?
- Can rollback fail?
- What is the first observable signal of failure?
- Does the action create an irreversible or cascading state change?
- Does it violate an invariant or hard constraint?

It does **not** decide that the proposed plan is good merely because mitigations exist.

## 0.5 The final planner may synthesize, but may not invent provenance

A consolidator may create a coherent plan from verified material.

It may not silently turn:

- an assumption into a fact;
- an agent assertion into evidence;
- a convenient implementation detail into a requirement;
- a risk mitigation into a guaranteed outcome;
- a disputed fact into a settled fact.

Every load-bearing final element must point back to its decision, evidence, challenge, and risk records.

## 0.6 Uncertainty is an output, not a defect to hide

When evidence is insufficient, the plan must preserve the uncertainty.

The correct response can be:

- a discovery action;
- a gated step;
- an explicit branch;
- a reversible experiment;
- or one targeted question to the user.

Do not manufacture certainty to make the plan look complete.

---

# 1. THE PLANNING UNIT: DECISION GRAPH

Before generating a plan, transform the request into a compact decision graph.

```yaml
brief:
  problem: <what must change and why>
  current_state: <observable current state>
  target_state: <observable target state>
  objectives: <outcomes to achieve>
  constraints:
    hard: []
    soft: []
    preferences: []
  invariants: []
  known_facts: []
  unknowns: []
  user_authority: <what the user can decide / cannot decide>

decisions:
  - id: D1
    question: <decision to resolve>
    load_bearing: true|false
    depends_on: []
    blocks: []
    reversibility: <reversible|partially-reversible|irreversible|unknown>
```

## 1.1 Load-bearing decision test

Mark a decision `load_bearing=true` when a different answer could materially alter at least one of:

- target outcome;
- hard constraints or invariants;
- safety/security/legal/compliance exposure;
- architecture or topology;
- cost or time materially;
- irreversibility;
- downstream dependencies;
- recovery options.

A plan may contain many non-load-bearing actions. They inherit their legitimacy from a resolved load-bearing decision and do not each need a full debate.

## 1.2 Derived actions

After decisions are resolved, convert each decision into actions.

An action is considered **derived** when its existence and ordering follow mechanically from:

1. the resolved decision;
2. explicit prerequisites;
3. established constraints;
4. accepted implementation conventions;
5. a known validation method.

Derived actions still need validation and risk fields, but they do not require an independent candidate debate unless they introduce a new material decision.

This distinction is what keeps the protocol rigorous without forcing five agents to debate whether to "create a directory" or "run the already-approved migration step."

---

# 2. DEPTH / COMPUTE ROUTING

Route first; do not run the full protocol blindly.

| Level | When | Minimum protocol |
|---|---|---|
| L0 | Deterministic, trivial, reversible, low-risk, no meaningful decision | Direct response; no plan ensemble |
| L1 | Small plan, one domain, low consequence, little uncertainty | 1 candidate + self-check + action validation |
| L2 | Multiple meaningful decisions OR uncertainty OR multiple domains OR an irreversible action | Independent candidate confrontation + evidence audit + independent risk analysis + consolidation |
| L3 | High consequence, novel/complex environment, interacting decisions, major irreversible steps, or unresolved L2 contradictions | L2 + stronger evidence verification + multiple risk lenses + adversarial review + state-transition simulation |

Examples of L3 triggers include material security exposure, production changes with high blast radius, safety-sensitive work, significant financial/legal consequences, or plans whose failure is difficult to reverse.

Do not infer consequence solely from domain labels. A small change in a sensitive domain can remain L1; a technically ordinary change with irreversible impact can be L3.

Document the route in one line:

`depth=L2 because: <observable signals>`

When ambiguous between levels, take the higher level unless the user explicitly sets a lower compute budget. If a lower budget is imposed, preserve skipped safeguards as explicit limitations.

---

# 3. SPAWNING / DELEGATION RULES

Spawn agents when isolation produces information that the parent agent could not reliably generate alone.

## 3.1 Spawn candidates when

- there is a real decision with multiple plausible paths;
- different assumptions or methods could change the answer;
- the cost of a wrong choice is material;
- the parent would otherwise anchor on its first solution.

For L2, default to **2 independent candidates** per decision cluster. Use 3 when decisions are consequential, novel, or close in trade-offs.

## 3.2 Spawn evidence agents when

- a load-bearing factual claim is externally verifiable;
- the current environment must be inspected;
- a numerical result drives a decision;
- the plan relies on compatibility, configuration, version, policy, or infrastructure facts.

Give evidence agents a narrow verification task, not the candidate plan's conclusion.

## 3.3 Spawn risk agents when

- an action is irreversible or has non-trivial blast radius;
- failure could materially damage the target state;
- rollback is uncertain;
- hidden dependencies or environmental variation are plausible;
- security, safety, compliance, or financial exposure is material.

At L2, one independent risk analyst is the minimum for load-bearing decisions. At L3, use two distinct risk lenses when practical.

## 3.4 Spawn critics when

A decision survives candidate generation but contains:

- contradictory evidence;
- unresolved assumption chains;
- a surprising or fragile dependency;
- a mitigation that depends on another unvalidated step;
- a conflict between objectives;
- a plan that appears correct only under one interpretation of the environment.

## 3.5 Do not spawn for ceremony

Do not create agents merely to increase the apparent rigor of the plan.

A spawn is justified when it has a distinct question, information boundary, method, or failure mode to investigate.

---

# 4. PHASE A — FRAME AND DECOMPOSE

The router or lead agent produces:

1. problem/current state/target state;
2. objectives and acceptance criteria;
3. hard constraints and invariants;
4. known facts vs assumptions vs unknowns;
5. decision graph;
6. depth selection;
7. evidence that must be verified before decisions can be resolved.

Do not begin by drafting the full plan.

The first planning question is:

> **What decisions actually determine whether this plan succeeds?**

If a supposed "decision" is simply a deterministic consequence of an already-settled choice, mark it as derived instead.

---

# 5. PHASE B — INDEPENDENT EVIDENCE BUILDING

For L2+, separate evidence collection from candidate selection when feasible.

## 5.1 Evidence card

Each load-bearing factual claim gets an evidence record:

```yaml
evidence:
  id: E1
  claim: <exact claim>
  status: known|supported|corroborated|derived|unproven|contested
  provenance:
    type: user_input|primary_source|secondary_source|inspection|test|calculation|logical_derivation
    locator: <source, file, command, test, calculation, etc.>
  independent_verifiers: []
  limitations: []
  affects: [D1, D2]
```

## 5.2 Evidence rules

- A source citation is not proof unless the source actually supports the claim.
- An agent's statement is not external proof.
- Two agents citing the same source are not independent corroboration.
- A secondary source can support a claim, but distinguish it from primary evidence.
- A calculation must expose enough inputs/formula to be recomputable.
- An inspection/test must record what was observed and under what conditions.
- If evidence cannot be inspected, tag it `unproven`.
- Evidence that directly contradicts another piece of evidence becomes `contested`; do not average the claims.

## 5.3 Evidence dependency rule

A conclusion cannot be more certain than its weakest load-bearing premise.

If D1 depends on E1 and E2, and E2 is unproven, D1 cannot be treated as fully supported merely because E1 is strong.

---

# 6. PHASE C — BLIND CANDIDATE GENERATION

Candidate agents receive the same normalized brief and decision scope, but not each other's candidates, critiques, or conclusions.

```yaml
candidate_brief:
  scope: <decision or decision cluster>
  objectives: []
  constraints: []
  invariants: []
  verified_evidence_refs: []
  unresolved_unknowns: []
  required_output:
    - proposed_decision
    - rationale
    - assumptions
    - alternatives
    - dependencies
    - expected_failure_modes
    - validation_plan
```

Candidate agents should differ by **method or optimization lens**, not merely adjective:

- independent baseline / simplest viable path;
- constraint-first / failure-avoidance path;
- alternative architecture or implementation path;
- reversibility-first path;
- evidence-first / test-first path.

Use only lenses that are relevant to the decision.

## 6.1 Candidate contract

Every candidate must identify:

- the decision it resolves;
- the option selected;
- rejected alternatives and why they remain viable or not;
- assumptions made;
- evidence used;
- dependencies;
- validation;
- failure modes;
- rollback or recovery;
- what would change its recommendation.

A candidate cannot silently fill an unknown with an assumption.

---

# 7. PHASE D — INDEPENDENT RISK ANALYSIS

Run the risk stream separately from candidate generation.

The risk agent should receive:

- the decision question;
- constraints/invariants;
- relevant environment facts;
- candidate options or the currently proposed action;
- but **not the candidate's persuasive rationale** unless needed for a specific attack.

Preferred risk lenses:

### Operational lens
Failure, partial completion, sequencing, dependencies, observability, rollback.

### Adversarial lens
How a hostile, malformed, unexpected, or worst-case condition defeats the plan.

### Environmental lens
What changes if assumptions about versions, infrastructure, people, permissions, data, timing, or external dependencies are wrong.

### Invariant lens
Whether any path can reach the target while violating a hard constraint or invariant.

For L3, use at least two distinct lenses when practical.

Risk records:

```yaml
risk:
  id: R1
  decision_ref: D1
  scenario: <failure or adverse condition>
  trigger: <observable signal>
  impact: low|medium|high|critical
  detectability: early|late|unknown
  prevention: []
  mitigation: []
  rollback: []
  residual: <qualitative statement>
  assumptions_attacked: []
```

A mitigation is not evidence that the underlying risk is small.

A plan that reaches the target only by violating a hard constraint is **invalid**, not merely risky.

---

# 8. PHASE E — ADVERSARIAL CROSS-EXAMINATION

For L2+, after the blind candidate and risk passes, expose the candidate set to independent critics.

Critics test the **decision**, not the prose.

For each decision, ask:

1. Is the decision actually necessary?
2. Does each material premise have evidence?
3. Are the candidates genuinely distinct?
4. Did any candidate rely on an unstated assumption?
5. Does any risk analysis identify a failure that invalidates the option?
6. Does the option satisfy every hard constraint and invariant?
7. Is the validation strong enough to distinguish success from false confidence?
8. Is there a lower-regret reversible experiment that should precede commitment?

Critics must classify findings as:

- `blocking` — invalidates the decision or requires new evidence;
- `material` — changes implementation, sequencing, or mitigation;
- `minor` — improves clarity without changing the decision.

Do not average critic verdicts. Resolve each finding by evidence and explicit reasoning.

---

# 9. PHASE F — DECISION RESOLUTION

The consolidator receives:

- normalized brief;
- decision graph;
- evidence ledger;
- independent candidate outputs;
- independent risk outputs;
- cross-examination findings.

It must resolve decisions **one by one**, not select a winning plan wholesale.

## 9.1 Resolution order

Use this precedence:

1. hard constraints and invariants;
2. verified observations and authoritative evidence;
3. demonstrated test/calculation results;
4. independently supported reasoning;
5. reversibility and recoverability when the evidence does not distinguish options;
6. simplicity / implementation cost when still tied.

This is a decision rule, not a numerical score.

## 9.2 Resolution outcomes

A decision can resolve as:

- `resolved` — one option is adequately supported;
- `resolved-with-tradeoff` — option chosen but a material trade-off remains;
- `branch-required` — evidence or user preference legitimately separates multiple paths;
- `gated` — another observation/action must occur first;
- `unresolved` — evidence is insufficient and no safe default exists;
- `invalid` — all considered paths violate hard constraints or required safeguards.

Never force `resolved` merely because the output needs to look complete.

## 9.3 No majority voting

The number of agents supporting an option is not itself evidence.

A minority candidate with stronger evidence can survive a majority of weaker candidates.

Likewise, unanimous agreement can remain unproven if all candidates depend on the same unsupported assumption.

## 9.4 No silent synthesis

When the consolidator introduces an action that was not explicitly proposed by a candidate, it must mark it:

`derived-from: [D#, E#, constraint/prerequisite refs]`

If that derivation is not obvious or deterministic, create a new decision unit and run the confrontation protocol again.

---

# 10. PHASE G — REBUILD THE EXECUTABLE PLAN

Only after load-bearing decisions are resolved should the plan be assembled.

Each action uses the action contract in §11 and references its origin.

The sequence must be prerequisite-ordered and state-aware.

For every action, answer:

- what changes;
- why this action is needed;
- what must already be true;
- what proves the action succeeded;
- what can fail;
- how failure is detected;
- how to recover;
- what new information could invalidate downstream steps.

The plan must be coherent as a whole. Per-decision resolution does not guarantee global coherence.

---

# 11. ACTION CONTRACT

```yaml
action:
  id: A1
  decision_refs: [D1]
  evidence_refs: [E1, E2]
  risk_refs: [R1]
  type: discovery|change|validation|rollback|branch|handoff
  objective_refs: []
  prerequisites: []
  execution: <precise action>
  expected_output: <observable result>
  validation: <objective-specific acceptance test>
  failure_signals: []
  risk_summary: <material risks only>
  rollback: <specific recovery or explicitly impossible + consequence>
  effort: low|medium|high
  provenance: candidate|derived|user-directed|deterministic
```

Rules:

- Validation is defined on the action, not postponed to the end.
- "Validation: check it works" is invalid; validation must specify an observable criterion.
- Rollback is considered before execution.
- If rollback is impossible, the action needs an explicit risk/escalation gate.
- An action that cannot answer "which objective? how verified? what if it fails?" is redesigned or cut.
- Every load-bearing action must reference the decision/evidence/risk trail that justified it.

---

# 12. COHERENCE AND STATE-TRANSITION VALIDATION

For L3, and for any plan with expensive or irreversible transitions, simulate the state changes.

```text
S0 --A1--> S1 --A2--> S2 --A3--> S3
      |            |
   failure      failure
      v            v
   recovery     recovery
```

For each material transition:

- verify prerequisites;
- verify post-condition;
- inject plausible failure;
- verify recovery state;
- verify that the next action is still valid;
- check that an earlier mitigation did not create a later invariant violation.

If execution is expected to reveal information, make the information-gathering step explicit rather than pretending the information is already known.

---

# 13. STOP / ESCALATION RULES

Stop planning when all required load-bearing decisions are resolved or deliberately gated and every action has an executable validation path.

Additional stop rules:

- an additional candidate is unlikely to change a decision because the decision is already compelled by evidence/constraints;
- repeated confrontation only restates existing findings;
- the remaining uncertainty cannot be reduced economically before execution and is safely handled by a gate or reversible experiment;
- the compute budget is exhausted.

Escalate instead of guessing when:

- evidence is genuinely contested and materially changes the path;
- a critical assumption cannot be tested;
- a hard constraint conflicts with the requested outcome;
- rollback is unavailable for a high-impact action;
- a decision materially depends on user priorities the agents cannot infer.

When budget is constrained, degrade in this order:

1. fewer candidate agents;
2. fewer non-load-bearing reviews;
3. less prose in the consolidation memo.

Do **not** remove evidence provenance or independent risk analysis from a high-consequence load-bearing decision merely to make the output cheaper.

---

# 14. BUDGET MODEL

Track invocations qualitatively rather than pretending model-token cost is universal.

Typical allocations:

### L0
`R: 0–1, D: 0, J: 0`

### L1
`R: ≤1, D: ≤1, J: 0–1`

### L2
Per decision cluster:

`R: ≤1, D: 2–3, evidence: 1, risk: 1, J: 1`

Add another critic or evidence verifier only when a finding can change the decision.

### L3
Per decision cluster:

`R: ≤1, D: 3+, evidence: 1–2, risk: 2, J: 1, coherence review: 1`

These are defaults, not quotas.

The correct stopping question is:

> **What unresolved decision could another agent still change?**

If the answer is "none," stop.

---

# 15. CONVERGENCE WITHOUT FALSE CONSENSUS

Convergence is useful only when the underlying evidence paths are not identical.

Before declaring convergence, verify:

- candidates were blind to each other;
- assumptions were surfaced;
- evidence provenance is known;
- shared sources are recognized as shared;
- independent risk analysis found no blocking issue;
- remaining disagreement is a genuine trade-off rather than an evidence gap.

Do not define convergence as "most agents agree."

A plan can be converged but weakly supported; a plan can be strongly supported but still contain a genuine unresolved trade-off.

Report those states separately.

---

# 16. OUTPUT FORMAT

Output depth must be proportional to the work.

## L0–L1

Provide the answer or compact plan with:

- objective;
- actions;
- validation;
- material caveat(s).

Do not generate a fake multi-agent audit trail when no material decision warranted one.

## L2+

Header:

```yaml
plan:
  depth: L2|L3
  decision_units: <count>
  load_bearing_decisions: <count>
  candidates_used: <count>
  evidence_verifiers_used: <count>
  independent_risk_analysts_used: <count>
  unresolved_decisions: []
  evidence_gaps: []
  residual_risks: []
```

Then:

1. Problem and state model
2. Objectives and acceptance criteria
3. Constraints and invariants
4. Decision graph
5. Evidence ledger
6. Candidate options and trade-offs
7. Independent risk analysis
8. Cross-examination findings
9. Decision resolution ledger
10. Executable plan
11. Validation map
12. Decision branches / gates
13. Residual risks and unknowns
14. Consolidation / provenance memo
15. Execution handoff and replanning rules

## 16.1 Decision resolution ledger

For every load-bearing decision:

```yaml
decision_resolution:
  id: D1
  question: <decision>
  candidates: [C1, C2]
  evidence: [E1, E2]
  risks: [R1, R2]
  challenges: [X1, X2]
  outcome: resolved|resolved-with-tradeoff|branch-required|gated|unresolved|invalid
  chosen_path: <option or null>
  why: <concise evidence-based rationale>
  rejected_or_deferred: []
  trigger_to_revisit: <condition>
```

This ledger is the core audit trail of the plan.

---

# 17. EXECUTION HANDOFF AND DYNAMIC REPLANNING

Plans are living artifacts during execution.

The executor receives:

1. the relevant plan slice;
2. all hard constraints/invariants;
3. current state and prior validated state digest;
4. only the evidence needed for that slice;
5. pointers to the remaining graph.

On failure:

- stop before compounding the failure;
- validate the actual resulting state;
- rollback when specified and safe;
- identify which assumption or transition failed;
- re-plan the smallest affected decision subtree.

Global re-planning is triggered by:

- invariant violation;
- discovery that invalidates a load-bearing evidence item;
- repeated failures showing the local model is wrong;
- a change in the target, constraints, or environment that affects multiple decision units.

After local repair, re-validate the repaired branch and any downstream actions whose prerequisites changed.

Record a compact state digest after each phase:

`done / failed / discovered unknowns / state delta / next gate`

---

# 18. ANTI-ANCHORING / ANTI-CORRELATED-ERROR RULES

The skill must actively prevent the ensemble from becoming a collection of copies.

Never:

- show candidate A to candidate B before blind generation;
- ask agents to "agree with" or "improve" another candidate before independent generation;
- treat temperature changes as sufficient independence;
- call self-critique an independent review;
- use agent count as evidence strength;
- cite an agent's reasoning as external proof;
- let the strongest model define the candidate set before the candidates are generated;
- collapse disagreements before identifying whether they arise from facts, assumptions, constraints, or preferences.

Prefer:

- different methods;
- isolated contexts;
- separate evidence paths;
- distinct risk lenses;
- blind candidate generation followed by structured cross-examination;
- narrow verification tasks;
- explicit provenance.

---

# 19. SINGLE-MODEL DEGRADATION

When only one model is available, the skill still preserves the structure but must accurately weaken its claims.

Use isolated context windows or separate invocations for:

1. candidate generation;
2. evidence checking;
3. risk analysis;
4. consolidation.

Label these as simulated independence:

`independence=simulated`

Do not claim that simulated role separation has the same evidentiary value as independent models, independent sources, or independent tests.

If only one invocation is affordable, fall back to L1 behavior and explicitly preserve important unknowns.

---

# 20. QUALITY GATES

Before emitting a material plan, run this final checklist.

### Decision gate
- [ ] Every load-bearing choice is identified.
- [ ] Each load-bearing choice was independently challenged at the required depth.
- [ ] No decision was resolved only by majority vote.

### Evidence gate
- [ ] Every load-bearing factual premise has provenance.
- [ ] Independent corroboration is distinguished from repeated citation of the same source.
- [ ] Unsupported claims remain visibly unsupported.

### Risk gate
- [ ] Load-bearing risky actions have independent risk analysis.
- [ ] Failure triggers and recovery are explicit.
- [ ] Hard constraint / invariant violations are treated as invalid.

### Execution gate
- [ ] Every action has an observable validation criterion.
- [ ] Prerequisites are correct.
- [ ] Rollback/recovery was considered before execution.
- [ ] Downstream dependencies are protected by gates where necessary.

### Integrity gate
- [ ] The final plan contains no invented facts.
- [ ] No action appears without a decision origin or deterministic derivation.
- [ ] Remaining uncertainty is visible.
- [ ] The plan can be audited without trusting the consolidator's memory of the debate.

If a gate fails, revise, gate, branch, or escalate. Do not cosmetically polish the plan and emit it anyway.

---

# 21. COMPACT REFERENCE ALGORITHM

```text
INPUT: request

1. FRAME
   normalize problem, target, objectives, constraints, invariants

2. DECOMPOSE
   build decision graph
   classify decisions as load-bearing or derived

3. ROUTE
   choose L0/L1/L2/L3

4. EVIDENCE
   identify load-bearing claims
   independently verify important evidence
   preserve provenance and uncertainty

5. GENERATE
   spawn independent candidates for load-bearing decisions
   keep candidate contexts blind

6. RISK
   spawn independent risk analysis
   attack failure, assumptions, rollback, invariants, environment

7. CROSS-EXAMINE
   challenge candidates and evidence
   isolate blocking/material findings

8. RESOLVE
   resolve each decision independently
   use constraints/evidence before reversibility/simplicity
   branch or gate when evidence is insufficient

9. REBUILD
   derive executable actions from resolved decisions
   tag provenance

10. VALIDATE
    check objective → decision → action → acceptance
    simulate state transitions when warranted

11. OUTPUT
    emit plan + evidence/risk/decision trail + residual uncertainty

12. EXECUTE / REPLAN
    operate from validated state
    repair locally unless a global trigger is hit
```

---

# 22. WHAT CHANGED FROM v4 — FUNDAMENTAL REFRAME

| v4 | v5 | Why |
|---|---|---|
| Ensemble of drafters | Decision-centric confrontation | A plan can agree while hiding one critical unresolved decision |
| Style seeds for diversity | Method / information-path diversity | Prompt variation alone does not create meaningful independence |
| Drafters attach proof | Independent evidence stream | Agents can cite the same bad or irrelevant proof |
| Judge performs evidence audit | Evidence is verified before/alongside resolution | Prevents the consolidator from inheriting unsupported premises |
| Adversarial review mainly L3 | Independent risk analysis is part of L2+ for load-bearing risk | Risk should not be an afterthought reserved for the largest plans |
| Per-plan merge | Per-decision resolution ledger | Avoids choosing an entire plan because it "felt better" |
| Validation + proof | Evidence provenance + acceptance test | Evidence that a premise is true is not the same as proof that execution succeeded |
| Judge may rebuild plan | No-silent-synthesis rule | Prevents untraceable actions from appearing during consolidation |
| Consensus / convergence | Evidence-backed resolution or explicit unresolved state | Agreement is not proof |
| Fixed N agents | Spawn per decision cluster | Compute follows uncertainty and consequence |
| Plan is primary artifact | Decision graph + evidence/risk/provenance is primary; plan is derived | Makes the reasoning auditable and repairable during execution |
| Graceful single-model degradation | Explicit simulated-independence label | Prevents overstating the strength of self-critique |

---

# 23. DESIGN PRINCIPLE IN ONE SENTENCE

> **Spend multi-agent compute on the decisions that can make the plan wrong; independently verify the facts those decisions depend on; attack the decisions from a separate risk path; then build the plan only from what survives that confrontation.**
