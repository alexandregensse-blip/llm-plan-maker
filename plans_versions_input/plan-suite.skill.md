# plan-suite — Generic Plan Making v3 (fichier fusionné)

# Ce fichier regroupe 4 skills : le skill principal (plan-core) et 3 sous-skills chargés à la demande.

# Chargez UNIQUEMENT la section correspondant à votre rôle courant ; les sections sont indépendantes.


================================================================================
# DÉBUT FICHIER : plan-core.skill.md
# RÔLE : Skill principal — boucle de décision de planification. Toujours chargé. Contient le Plan Complexity Score (PCS), la boucle need→states→guards→objectives→options→actions, le contrat d'action, et les règles de chargement des sous-skills (§6).
================================================================================

# plan-core — Generic Plan Making (v3)

You transform a request into a **validated, traceable, executable plan**: a sequenced set of actions
that moves a system from an explicit current state to an explicit target state, under constraints,
with validation and recovery paths.

Do not confuse: request ≠ need ≠ objective ≠ option ≠ implementation ≠ action ≠ outcome.

---

## 0. Decide planning depth FIRST (this drives everything)

Compute a **Plan Complexity Score (PCS)** before doing anything else:

```
PCS = O + 2·B + 3·I + D + S

O = number of required objectives (>1 adds 1 each beyond the first)
B = number of BLOCKING unknowns (cap at 3)
I = irreversibility of the worst action (0 = fully reversible … 3 = irreversible / high blast radius)
D = number of distinct technical/business domains touched
S = 1 if failure consequence is high (money, safety, legal, public/SEO), else 0
```

| PCS | Level | Process |
|---|---|---|
| 0–1 | **L0 Direct answer** | No plan. Answer or single action. |
| 2–3 | **L1 Simple plan** | Understand → Objectives → Actions → Verify (one pass) |
| 4–7 | **L2 Structured plan** | Full loop below, single candidate plan |
| 8–14 | **L3 Complex plan** | Full loop + options comparison + failure analysis + **spawn reviewer** |
| ≥ 15 | **L4 Critical plan** | L3 + explicit contingencies + **2+ independent reviewers** + independent plan generation |

Never fake a high-risk task as simple because it "looks technically easy".

## 1. The loop (all levels ≥ L1)

```
1. NEED       — what problem, why it matters, what if nothing changes
2. STATES     — current state (evidence) vs target state (observable outcomes, not actions)
3. GUARDS     — invariants (what must stay true) + constraints (hard / soft / preference)
4. OBJECTIVES — required / desired / optional; each with acceptance criteria
5. OPTIONS    — only meaningfully different strategies (≥2 at L3+); trade-offs recorded
6. PLAN       — select implementations → actions, ordered by prerequisites & safety, not by number
7. VALIDATE   — coverage matrix, state-transition simulation, failure paths (see plan-review)
8. OUTPUT     — per template §5; assumptions and unknowns stated explicitly
```

Backward moves are legal at any point when new evidence invalidates an assumption.
Replanning is a feature, not a failure.

## 2. Epistemics (apply to every load-bearing statement)

Tag each fact as: **Known** (evidence) / **Inferred** / **Assumed** / **Unknown** / **Conditional**.
Never promote Assumed → Known silently.
Unknowns become **discovery actions** (with success/failure condition and consequences),
not blocking questions — unless they are blocking (then ask the user *once*, with proposed
default paths per answer).

## 3. Action contract (every non-trivial action must define)

```yaml
id: A-007
objectives: [O2]            # traceability forward
purpose: one sentence
prerequisites: [A-003]
execution: concrete command/step
expected_output: observable result
validation: how we KNOW it worked   # attached to the action, not deferred to the end
risk: what it can break
rollback: mechanism or "impossible — flag as I-risk"
effort: S / M / L
```

Rules: validation immediately after each risky action · rollback defined BEFORE execution ·
an action that can't answer "which objective? how verified? what if it fails?" gets redesigned or cut.

## 4. Branching discipline

Conditional plans are allowed, capped: **max 2 branch levels**, and only where the condition
is genuinely decision-relevant. Each branch = {trigger, evidence required, path, fallback}.
Prefer `Assumption A → Path A / Assumption B → Path B` over blocking the user with questions.

## 5. Output template (default; user may override)

```markdown
## 1. Problem understanding — current state, real need, target state, assumptions, critical unknowns
## 2. Objectives — | ID | Objective | Priority | Acceptance criteria | Depends on |
## 3. Constraints & invariants — hard / soft / preference separated
## 4. Options considered — characteristics & trade-offs, no fake "best"
## 5. Plan architecture — why this implementation set is coherent
## 6. Execution plan — phases of actions per the action contract (§3)
## 7. Decision points — conditions & branches
## 8. Critical path & parallelizable work
## 9. Validation — how each required objective is proven (coverage matrix)
## 10. Risks — initial / introduced / residual / unknown, qualitative only (no invented numbers)
## 11. Optional & future work — kept strictly separate from core plan
```

## 6. When to invoke the sub-skills

| Trigger | Load |
|---|---|
| PCS ≥ 4, or ≥ 2 independent research domains, or blocking unknowns resolvable by inspection | `plan-research` |
| PCS ≥ 8, or any irreversible action (I ≥ 2), or options were close calls | `plan-review` |
| Plan will be handed to executor agents | `plan-artifact` (schema) |
| PCS ≤ 3 and single domain | none — do it inline, don't manufacture process |

## 7. Stop conditions (planning has a budget too)

Stop when ALL hold: need & target explicit · required objectives defined with acceptance criteria ·
feasible implementation set · dependencies respected · meaningful failure paths considered ·
every required objective has a validation path · residual uncertainty stated.
If planning exceeds ~20% of estimated execution effort, ship the best plan with explicit
unknowns rather than refining further.

## 8. Central rule

> What must become true? What prevents it? What changes it? What governs those changes?
> How will we know it worked — and what do we do when it doesn't?

================================================================================
# FIN FICHIER : plan-core.skill.md

================================================================================
# DÉBUT FICHIER : plan-research.skill.md
# RÔLE : Sous-skill de délégation — quand et pourquoi spawner des agents. Chargé quand plan-core §6 le déclenche (PCS ≥ 4 ou déclencheurs R1–R5). Contient la matrice de décision de spawn, les règles de non-spawn, le design de briefs d'agents et la fusion des sorties.
================================================================================

# plan-research — When and Why to Spawn Agents

Load only when plan-core §6 triggers this skill. Spawning is a cost, not a feature.

## 1. Decision matrix (concrete triggers, not vibes)

| # | Trigger condition | Spawn | Pattern | Why |
|---|---|---|---|---|
| R1 | ≥ 2 genuinely independent domains to investigate (e.g., "stack Servebolt" vs "durcissement WP" vs "contraintes SEO") | 1 agent per domain, parallel | A — Parallel exploration | Wall-clock speed; no cross-contamination |
| R2 | ≥ 2 viable strategies at L3+ and the choice is consequential | 2–3 planners, isolated | B — Independent plans | Kills anchoring; surfaces non-obvious options |
| R3 | Well-bounded subproblem needing expertise you don't have (legal, forensique DB, perf) | 1 specialist | Specialist | Quality of analysis, not speed |
| R4 | Factual uncertainty HIGH (many load-bearing unknowns) | research agents BEFORE planning | E — Research → Plan | Prevents building on sand |
| R5 | Plan irreversible / high blast radius (I ≥ 2) | 1+ adversarial reviewers | C — Planner + critics | Independent failure detection |

## 2. When NOT to spawn (check first)

- Task trivial (PCS ≤ 3) or single-domain.
- Subproblem tightly coupled to the whole — can't be scoped independently.
- Orchestration overhead ≥ expected value (agent cost ≥ ~30% of doing it inline well).
- Sub-agent has access to nothing you don't (no new tools/sources).

Cap: **max 4–5 parallel agents**. Beyond that, coordination noise dominates.

## 3. Task design (a spawned agent is only as good as its brief)

Every brief specifies, minimally:
```yaml
scope: exactly what is IN and OUT
output: expected artifact (findings / options / risks / evidence / recommendation)
evidence: what counts as proof (source, test, inspection) — never "your opinion"
format: structured, schema-compatible with plan-artifact
independence: (for reviewers) do NOT see other agents' conclusions
```
Bad: "Think about the problem." Good: "List every external constraint that could block
implementation X. For each: evidence, impact, mitigation. Unknowns flagged, not guessed."

## 4. Merging outputs (agents are sources, not authorities)

1. Extract what each agent established vs assumed.
2. Diff against other agents: real contradiction or scope difference?
3. Resolve by evidence quality. Tie (equal evidence, equal assumptions)?
   **Tie-breaker: prefer the more reversible / lower-risk option, and flag the trade-off in the plan.**
   Never average contradictory conclusions.
4. Unresolvable AND decision-relevant → escalate to user with both paths.

## 5. Patterns

A Parallel exploration · B Independent plans (isolated!) · C Planner + critics (risk / logic / feasibility)
· D Hierarchical workstreams · E Research → Plan → Verify.
Choose by the matrix in §1, not by taste.

================================================================================
# FIN FICHIER : plan-research.skill.md

================================================================================
# DÉBUT FICHIER : plan-review.skill.md
# RÔLE : Sous-skill de validation adverse — attaquer le plan candidat plutôt que le reformuler. Chargé quand plan-core §6 le déclenche (PCS ≥ 8 ou action irréversible I ≥ 2). Contient la checklist adverse, le format de simulation par transitions d'état et le format de verdict.
================================================================================

# plan-review — Adversarial Validation

Load when plan-core §6 triggers this skill. The reviewer sees the candidate plan,
NOT the reasoning that produced it (fresh eyes, no anchoring).

## 1. Review passes (proportional to PCS)

| PCS | Passes |
|---|---|
| 4–7 | Self-check checklist (§2) |
| 8–14 | Self-check + 1 independent reviewer |
| ≥ 15 | Self-check + 2 independent reviewers (different lenses: risk vs logic/feasibility) + nominal & failure simulation |

## 2. Adversarial checklist (reviewer must attack, not restate)

- **Coverage:** every required objective → implementation → action → acceptance criterion. Gaps? Partial coverage justified?
- **Hidden assumptions:** for each major step: "what must be true that we never established?" → promote to prerequisite/discovery/risk.
- **Contradictions:** incompatible implementations, constraint violations, objectives in conflict.
- **Ordering:** prerequisites actually precede dependents? Validation points early enough? Rollback defined BEFORE the risky action?
- **Failure paths:** simulate at least {action fails · partial completion · environment ≠ assumed · dependency unavailable · regression · rollback itself fails}.
- **Side effects:** each significant action — new dependencies, operational burden, invariant impact, SEO/compat regressions.
- **Invariants & hard constraints:** final plan preserves them? A plan that hits the target by breaking a hard constraint is INVALID, not "risky".
- **Feasibility:** people/access/tools/time/windows realistic? Maintenance burden sustainable after delivery?
- **Outcome check:** does the plan solve the actual need (loop step 1), or merely perform requested activities?

## 3. Simulation format (state transitions, keep it cheap)

```
S0 → [Action A] → S1 (verify: <criterion>) → [Action B] → S2 ...
Failure injection: A fails → state? recovery? blast radius? next action still valid?
```
Only simulate transitions that are costly, irreversible, or novel. Don't simulate the trivial.

## 4. Verdict

```yaml
verdict: pass / pass-with-changes / fail
blocking_findings: [...]   # must fix before execution
suggestions: [...]         # optional improvements
confidence: per-claim notes (inspected > documented > assumed > untested)
```
No single arbitrary confidence score — attach confidence to claims.

================================================================================
# FIN FICHIER : plan-review.skill.md

================================================================================
# DÉBUT FICHIER : plan-artifact.schema.md
# RÔLE : Schéma machine-readable du plan — garantit la traçabilité entre planner → reviewers → exécuteurs. Chargé quand le plan est transmis à des agents exécuteurs. Contient le schéma YAML, les règles de handoff et de versionning.
================================================================================

# plan-artifact — Machine-Readable Plan Schema (v1)

Purpose: hand plans between planner → reviewers → executor agents without losing traceability.
Serialize as JSON or YAML. Every cross-reference uses IDs, never prose.

```yaml
plan:
  id: PLN-2026-0001
  version: 3
  pcs: 11                      # plan complexity score at creation
  level: L3
  created_by: agent-planner-1
  states:
    current: { summary: "...", evidence: [inspected | documented | stated-by-user] }
    target:  { summary: "...", observable: true }
  invariants: ["no URL change", "SEO crawlability preserved", ...]
  constraints:
    hard: [...]
    soft: [...]
    preferences: [...]
  objectives:
    - id: O1
      description: "..."
      priority: required | desired | optional
      acceptance_criteria: ["measurable, checkable"]
      depends_on: []
      conflicts: []
  options:
    - id: OP1
      description: "..."
      addresses: [O1, O2]
      benefits: [...]; costs: [...]; risks: [...]
      reversible: true | partial | false
      status: selected | rejected           # rejected: one-line reason mandatory
  actions:
    - id: A1
      option: OP1
      objectives: [O1]
      purpose: "..."
      prerequisites: []
      depends_on: []
      execution: "concrete step / command"
      expected_output: "..."
      validation: "how verified"
      risk: "..."
      rollback: "..." | "IMPOSSIBLE"         # IMPOSSIBLE forces risk flag + escalation
      effort: S | M | L
      owner: agent-or-human
      status: pending | done | failed | skipped
      result: null | { verified: bool, evidence: "...", at: timestamp }
  branches:
    - id: BR1
      condition: "..."
      evidence_required: "..."
      if_true: [A5]; if_false: [A6]; fallback: "..."
  risks:
    - id: RK1
      kind: initial | introduced | residual | unknown
      description: "..."
      mitigation: "..."
  unknowns:
    - id: U1
      blocking: true | false
      discovery_action: A7 | null            # null + blocking=true → user question required
  reviewers:
    - agent: reviewer-1
      verdict: pass | pass-with-changes | fail
      at: timestamp
      blocking_findings: [...]
```

Handoff rules
- Executors MUST update `actions[].status` and `result` in place; no side-channels.
- Any action with rollback "IMPOSSIBLE" whose execution fails ⇒ STOP execution, escalate.
- Plan version bumps on any structural change (new action, resequencing); reviewers re-run on version change.
- History is append-only: edits create a new version, never mutate the past.

================================================================================
# FIN FICHIER : plan-artifact.schema.md
