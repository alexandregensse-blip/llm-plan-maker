# plan-suite v4 — Plan Making with Model Allocation & Consolidation

Generic planning skill for multi-model LLM environments.
Core idea: spend compute where it changes the outcome.
Cheap models draft, medium models diversify, strong models judge and consolidate.
Every load-bearing claim carries a proof. Every planning step has a cost and a stop rule.

================================================================================
## 0. ROLES & MODEL CLASSES

Three model classes, defined by capability tier, not vendor:

| Class | Symbol | Definition | Typical use here |
|---|---|---|---|
| Router | [R] | Cheapest viable model | Classify request, score depth, extract, summarize |
| Drafter | [D] | Medium model | Generate candidate plans, enumerate options, draft actions |
| Judge | [J] | Strongest available model | Critique, consolidate, arbitrate contradictions, final validation |

Rules:
- Never use [J] for a task where [D] output is provably sufficient (see §3 stop rules).
- Never let the same model instance be "independent reviewer" of its own output.
   Diversity requirement: independent agents must differ on ≥1 of {model class, system prompt, temperature, context slice}.
- If your environment only has one model: simulate classes by prompting (e.g. "answer as a skeptical reviewer"),
   and disable multi-agent patterns. The skill degrades gracefully; it does not require a fleet.

================================================================================
## 1. DEPTH DECISION (replaces PCS formula)

The v3 PCS formula had invented coefficients. v4 uses an explicit decision table — qualitative, auditable, no fake arithmetic.

Route the request in ONE pass by [R]:

| Signal present | Depth | Process |
|---|---|---|
| Single objective, reversible actions, one domain, no unknowns | L0 | Answer directly, no artifact |
| ≤2 objectives, low risk | L1 | 1×[D] draft → self-check → output |
| Multiple objectives OR any irreversible action OR ≥2 independent domains | L2 | Ensemble (§2) → consolidate [J] → output |
| ≥3 objectives AND high consequence (money/safety/legal) AND irreversible steps | L3 | Ensemble → consolidate → adversarial review (§4) → contingencies → output |

Decision is documented as one line: `depth=L2 because: <signals>`. Not a number. The line is reviewed in §4.
Ambiguity → take the HIGHER depth; the cost delta between depths is bounded by §5.

================================================================================
## 2. ENSEMBLE GENERATION (the pattern you asked for)

At L2+, run N=3 drafters [D] in parallel, each isolated (sees only the brief, not the others):

```yaml
brief:        # identical for all drafters
  need:        # problem, why it matters, cost of inaction
  states:      # current (with evidence tags) vs target (observable outcomes)
  guards:      # invariants + hard/soft/preference constraints
  objective:   # ONE objective per drafter when objectives are separable
  style_seed:  # different per drafter: e.g. "optimize for speed" / "optimize for reversibility" / "optimize for simplicity"
  output:      candidate plan per action contract (§3)
```

Why style seeds: identical briefs on the same model family converge (mode collapse).
Style seeds force genuinely different trade-off surfaces; the consolidator then picks per-decision, not per-plan.

Drafter output contract:
- Candidate plan: objectives → options → actions (prereq-ordered).
- For each option: ONE explicit trade-off statement.
- For each fact: tag [Known | Inferred | Assumed | Unknown] (unchanged from v3, kept — it works).
- Blocking unknowns → discovery actions, not questions to the user, unless truly blocking → ask ONCE with default paths.

Cost note: N=3 is the default, not the law. N=2 if objectives are few and one domain; N=5 only when ≥2 options are within one trade-off grade of each other AND the decision is irreversible.

================================================================================
## 3. CONSOLIDATION BY STRONG MODEL (Judge)

The [J] receives: the brief, the N candidate plans, and NOTHING else (no drafter reasoning chains, no prior consolidations — anti-anchoring, keeps "fresh eyes" honest).

Consolidation protocol, in order:

1. EXTRACT — pull every distinct claim/option/action from all candidates. Dedupe by content, not by phrasing.
2. EVIDENCE AUDIT — for each extracted item, collect the proof attached by drafters:
   - citation (source quoted),
   - calculation (recomputable),
   - inspection result (test, command output),
   - or "none".
   Items with no proof are marked UNPROVEN, not rejected. They enter the plan flagged, or as discovery actions.
3. ATTACK — for each candidate plan: hidden assumptions, ordering violations, constraint conflicts,
   missing validation, actions that can't name their objective.
4. PER-DECISION MERGE — never pick "plan A over plan B" wholesale.
   For each decision point: choose the best-supported option across all candidates.
   Tie rule (unchanged from v3, kept): prefer the more reversible option, flag the trade-off.
   Contradictions that are evidence-backed on both sides → escalate to user with both paths.
5. REBUILD — assemble the merged plan; re-check global coherence (a plan assembled from winners can still be incoherent as a whole).
6. PROOF ATTACHMENT — every surviving load-bearing claim in the final plan has either
   attached proof or is explicitly tagged UNPROVEN with a discovery action.
   A plan where >30% of required objectives rest on UNPROVEN claims → downgrade confidence and state it in the output header.

Judge output = final plan + consolidation memo:
- what was kept, from which drafter, and why (one line each);
- what was discarded, and the evidence that killed it;
- residual UNPROVEN items and their discovery actions.

This memo is the "preuves" trail. It is mandatory, not decorative: it is what lets a human or a later agent audit WHY the plan is what it is, without re-running the ensemble.

================================================================================
## 4. ADVERSARIAL REVIEW (L3 only, or on demand)

Reviewer roles on [J] (or a different strong model — diversity rule of §0 applies):

A. Risk lens — simulate: action fails / partial completion / env ≠ assumed / dependency gone / rollback fails.
B. Logic lens — coverage matrix (objective → implementation → action → acceptance), contradiction hunt, invariant check.

Format: verdict per reviewer = pass / pass-with-changes / fail, with blocking findings.
A plan that reaches the target by violating a hard constraint is INVALID, not "risky" (kept from v3 — correct rule).

State-transition simulation (cheap, only for costly/irreversible/novel transitions):
  S0 →[A1]→ S1 (check: <criterion>) →[A2]→ S2 …
  Failure injection: A1 fails → state? recovery? next action still valid?

================================================================================
## 5. BUDGET & STOP RULES (new in v4)

The skill tracks a rough cost ledger. Unit = one model invocation at each class (R≪D≪J).

Defaults (adjust to environment):
- L0: ≤1 [R]
- L1: ≤1 [R] + ≤1 [D]
- L2: ≤1 [R] + ≤3 [D] + ≤1 [J] (+1 [J] if contradictions remain after first consolidation)
- L3: L2 + 2 [J] reviews + contingency pass

Stop planning when ANY holds:
- every required objective has an implementation + validation path;
- incremental consolidation pass changed <10% of prior plan (convergence);
- budget cap reached → ship best plan with UNPROVEN flags explicit. Never silently drop coverage to fit budget; the header must say what was skipped.

================================================================================
## 6. ACTION CONTRACT (unchanged core, one addition)

id / objectives / prerequisites / execution / expected_output / validation / risk / rollback / effort
ADDED: proof — what evidence backs that this action works (citation | calculation | prior inspection | none)

Rules kept from v3:
- validation defined ON the action, not deferred to the end;
- rollback defined BEFORE execution; "impossible" → risk flag + escalation;
- an action that can't answer "which objective? how verified? what if it fails?" is redesigned or cut.

================================================================================
## 7. EXECUTION HANDOFF & DYNAMIC REPLANNING (new in v4 — replaces v3's static view)

Plans handed to executors are **living within a run**:

- Chunking: executor receives (a) plan slice of ≤ its context budget, (b) invariants + hard constraints in full,
  (c) pointers to remaining plan, not its content.
- On action failure at execution: executor rolls back if possible, then re-plans ONLY the affected subtree
  (local repair preferred over global re-plan). Global re-plan triggers: ≥2 consecutive failures, or any invariant violated.
- After local repair, only the repaired branch is re-validated (re-checking the whole plan burns budget for nothing).
- Compaction: after each phase, executor appends a 5-line state digest (done / failed / discovered-unknowns / state-delta)
  to a run log; fresh context starts from the digest, not from full history.
- Executors report status per action (pending/done/failed/skipped + evidence) in the plan artifact — kept from v3 schema.

================================================================================
## 8. OUTPUT TEMPLATE

Depth-proportional. L0-L1: answer + (plan if L1) in ≤1 page.
L2+: full structure, and the header ALWAYS contains:
  depth, model ledger (R/D/J counts actually used), UNPROVEN ratio, residual risks one line each.

  1. Problem & states (evidence-tagged)
  2. Objectives + acceptance criteria
  3. Constraints & invariants
  4. Options considered (trade-offs, not fake "best")
  5. Plan (actions per §6, prereq-ordered)
  6. Consolidation memo (kept/discarded + why)
  7. Decision points & branches (max 2 levels; trigger/evidence/path/fallback each)
  8. Validation map: objective → proof
  9. Risks: initial / introduced / residual / unknown (qualitative only — no invented numbers, kept from v3)
 10. Future work (separate from core plan)

================================================================================
## 9. DEGRADATION & ANTI-PATTERNS

Degrades gracefully: single model → classes become prompts; ensemble of 1; judge = same instance re-prompted as critic (weaker, flag it).

Explicit anti-patterns (the skill must refuse to do these):
- Running the ensemble then averaging / voting plans instead of per-decision merge.
- Using [J] to draft (anchoring + cost; [J] judges, [D] drafts).
- Marking Assumed as Known silently (kept from v3).
- Producing validation fields that restate the action ("validation: check it works").
- Planning past the budget cap to reach cosmetically complete coverage.

================================================================================
## 10. WHAT CHANGED FROM v3 — summary

| v3 | v4 | Why |
|---|---|---|
| PCS arithmetic formula | Qualitative signal table | Removes false precision, same routing power |
| Agents as free primitives | Model classes R/D/J + cost ledger | Matches real multi-model economics |
| Planner + critics | Drafter ensemble → Judge consolidation | Per-decision merge with proof trail, kills mode collapse via style seeds |
| Reviewer "fresh eyes" | Diversity rule (model/prompt/temp/context) | Same-family reviewers share blind spots |
| Validation field | Proof attachment (citation/calc/inspection) | "Validation" was often tautological |
| Static plan + append-only versioning | Local repair + branch revalidation + run log | Plans execute in changing environments |
| 20%-of-execution stop rule | Budget caps + convergence rule | 20% of execution effort is unmeasurable for LLM runs |
| 3-file suite | Single file, conditional sections | Kills drift between duplicated schemas |
