# plan-suite v15 — State-Driven Commitment Protocol

Generic planning skill for LLM agents. Vendor-neutral. Single file.
**Meta-status: `unproven`.** Before trusting on high-consequence work, replay 3–5 past failures through it and record which gates would have caught them, at what cost.

---

## 0. Core Principle

> **Planning is state navigation, not document writing. Every load-bearing commitment must be independently validated before closing options. Spend compute only where it can change the outcome.**

### 0.1 Invariants
1. **State over prose** – Maintain a living Horizon (§2), not a static document.
2. **Compulsion first** – If verified facts + hard constraints leave exactly one viable path, take it immediately. Zero candidates, zero debate.
3. **Containment before confidence** – Irreversible actions require explicit containment or gates (§3.3).
4. **Independent validation** – Route every load-bearing claim to the cheapest sufficient independent validator: **environment (tool/test/inspection) > user > blind isolated context > nothing** (§4).
5. **Token economy** – Default to zero agents. Spawn only when a real choice survives the evidence (§5).

### 0.2 Failure Modes This Skill Targets
- Hallucinated load-bearing facts
- Anchoring on first plausible answer
- Confusing agreement with evidence
- Hiding uncertainty to look complete
- Skipping containment on irreversible steps
- Planning past the fog of war

---

---

## 1. Triage — The Only Gate

Answer **two questions** from the user’s prompt **alone**. Do not look ahead.

**Q1 — Reversibility**
*Can the next required action go wrong in a way I cannot cheaply and certainly undo?*
- **No (reversible)** → No plan artifact. State expectation, act, observe. Skip to §10.
- **Yes (commitment)** → Continue to Q2.

**Q2 — Territory**
*How well is this territory known?*
- **Known path** – Runbooks, documented APIs, standard migrations. Environment is predictable. Use **Sequence** (§9).
- **Frontier work** – Outcome of Step N reshapes the path beyond it. Use **Frontier Loop** (§8).

**Route in one line:**
`depth=<L0 L1|L2|L3>, territory=<known|frontier> because: <observable signals>`

### 1.1 Depth Levels
 | Depth | Condition | Protocol |
 |---|---|---|
 | **L0** | Question, explanation, trivial reversible action | Answer directly. No protocol. |
 | **L1** | Reversible, known territory, low consequence | Compact plan + one caveat. No candidates. |
 | **L2** | Material unknowns **OR** consequential commitment | Full contracts + care triggers + blind confrontation **only if real choice survives** (§5). |
 | **L3** | Irreversible, cascading, high-consequence | L2 + independent attack with **transition lens** + explicit **user gate** before execution. |

**Default rule:** Unsure between L1 and L2 → **L1**, unless the action is irreversible.

---

---

## 2. Horizon — The Living State

Maintain **four lines**. Revise **only when execution contradicts them** — not preemptively.

```
Target:         <observable success condition; falsifiable or it is not a target>
Invariants:     <hard limits that must remain true at every step — never preferences>
Verified now:   <facts established EXCLUSIVELY by external observation, not memory>
Open questions: <unknowns that could reshape the plan, and how each resolves>
```

### 2.1 Rules
- **Target must be falsifiable.**
  ❌ *"Improve security"* | ✅ *"Test X shows access paths closed under threat model T"*
- **Invariants vs. preferences:**
  ✅ Invariant: *"Do not delete production data"*
  ✅ Preference: *"Prefer managed services"* (record separately; ask user when material §7.2)
- **"Verified" means looked:**
  ✅ Tool output, inspection, user statement
  ❌ Training data, prior sessions, another agent’s assertion
- **Evidence has TTL:**
  Re-verify stale load-bearing facts at execution time. A changed fact is a **replan trigger**.

---

---

## 3. Commitment Ledger — Only What Closes Options

A **commitment** is any point where the plan **closes options** or **consumes non-trivial resources**:
- Irreversible/costly action (delete data, spend money, send email)
- Architecture/dependency adoption that closes alternatives
- External dependency (person, service, approval)
- Experiment that spends budget to reduce a named unknown

**Do not** create ledger entries for mechanical consequences. Mark them as **derived actions** (§9.3).

```yaml
commitment:
  id: C1
  statement: <what we commit to, one sentence>
  type: action | architecture | dependency | experiment
  load_bearing: true
  why_load_bearing: <what changes if this is wrong>  # e.g., "violates invariant X"
  reversibility: reversible | partial | irreversible | unknown
  evidence: []    # Filled in §4
  attacks: []     # Filled in §6
  resolution: null
  confidence: null
```

### 3.1 Compulsion Check — **Mandatory Before Any Generation**
For **each** commitment, ask:
> **Do the verified facts + hard constraints leave exactly ONE viable technical path?**

- **Yes** → Mark `resolved`, `confidence: high`, cite evidence. **Spawn zero candidates.**
- **No, missing facts** → Convert to **discovery action** (§4.1).
- **No, ≥2 options remain** → Candidates **may** be warranted (§5).

**Most commitments are compelled.** Default is **zero candidates**.

---

---

## 4. Evidence Protocol — Verify Before You Generate

Verify **only** claims that are:
1. **Load-bearing** (they change a commitment), **AND**
2. **Externally checkable** (source, inspection, test, calculation).

### 4.1 Evidence Budget
 | Depth | Max Evidence Items per Load-Bearing Commitment |
 |---|---|
 | L1 | 0–1 |
 | L2 | ≤2 |
 | L3 | ≤4 (with independent verification when feasible) |

**Hit the budget?** Stop. Mark remaining as **gaps**, then **branch/gate/escalate**.

### 4.2 Evidence Record
```yaml
evidence:
  id: E1
  claim: <exact claim, one sentence>
  status: verified | supported | derived | unproven | contested
  source: user_input | observation | primary | secondary | test | calculation
  locator: <file/URL/command/formula/observation>
  checked_at: <timestamp>
  ttl: <how long this stays true; default: this session>
  limitations: <what this does NOT prove>
```

### 4.3 Evidence Rules
1. A **citation is not evidence** unless the source **actually supports the claim**.
2. An **agent’s statement is not evidence**.
3. The **same source cited multiple times = one evidence item**.
4. A **calculation must expose inputs/formula** to be recomputable.
5. **Cannot inspect?** Mark `unproven`. **Do not launder into a fact.**
6. **Contradictory evidence = `contested`**. Do not average. Do not pick the convenient one.
7. **A conclusion is only as strong as its weakest load-bearing premise.**
   If `C1` depends on `E1` (strong) and `E2` (unproven), `C1` is **not fully supported**.

---

---

## 5. Candidate Generation — **Only When Triggered**

Generate candidates **only if ALL conditions hold**:
1. ✅ Compulsion check **failed** (≥2 viable options remain after evidence).
2. ✅ Commitment is **load-bearing**.
3. ✅ Choice is **weakly reversible** OR consequence is **material**.

Otherwise: **Skip this section entirely.** Record in the ledger that it was skipped.

### 5.1 Independence Modes — **Label Honestly**
 | Mode | Meaning | Honest Claim | When to Use |
 |---|---|---|---|
 | **staged** | Same context, sequential passes with strict information hygiene (§5.2) | Weakest; reduces anchoring only | Single-model environments |
 | **isolated** | Separate invocation/sub-agent, own context, **blind to others** | Real information-flow independence (same-family models share blind spots) | Multi-agent runtimes |
 | **external** | Different model family, or actual test/inspection | Strongest practical | High-consequence decisions |

**Never upgrade a label.** Same-vendor models are **correlated**.

### 5.2 Information Hygiene (Mandatory for `staged` Mode)
1. Generate each candidate **before** reading any persuasive rationale for another option.
2. **Never** re-read your own candidate during the adversarial pass.
3. Temperature changes are **not** independence.
4. Self-critique is **not** a review.

### 5.3 Candidate Contract
Each candidate **must** state:
- **Option** (one sentence)
- **Rationale** (3–5 bullets)
- **Assumptions** (explicit)
- **Rejected alternatives** and why they **remain viable**
- **Dependencies**
- **Two most likely failure modes**
- **Validation plan**
- **What would change the recommendation**

⚠️ **Invalid candidate:** Silently fills an unknown with an assumption.

### 5.4 Number of Candidates
 | Scenario | Candidates |
 |---|---|
 | Compelled | **0** |
 | Triggered (default) | **2** |
 | L3 or close decision | **3** |

**If you cannot spawn that many:** Use `staged` mode and **label it**.

### 5.5 Candidate Brief (Normalized)
Give each candidate the **same** brief:
```yaml
brief:
  problem: <...>
  target_state: <...>
  hard_constraints: <...>
  invariants: <...>
  verified_evidence: <list or "none">
  unresolved_unknowns: <list>
  commitment: <C1 statement>
  optimize_for: <reversibility | failure-avoidance | simplicity | testability>  # Different per candidate
```

**Diversity:** Use **method/lens diversity**, not just wording.
Example lenses:
- Simplest viable path
- Constraint-first
- Reversibility-first
- Evidence-test-first

---

---

## 6. Adversarial Pass — Independent Attack

Run **independently** of candidate generation.
**Do not** show the attacker the candidate’s persuasive rationale unless a specific attack requires it.

### 6.1 Attack Prompt
```
You are an independent risk attacker. Do NOT defend the plan.

Context:
  Commitment: <C1>
  Proposed action: <...>
  Hard constraints: <...>
  Invariants: <...>
  Verified facts: <...>

Find:
  1. The most dangerous missing fact.
  2. Assumptions most likely to be false.
  3. Hidden dependencies.
  4. Irreversible or cascading transitions.
  5. Failure modes common to ALL viable options.
  6. Conditions under which the problem is framed incorrectly.
  7. Evidence or experiment that would MOST reduce uncertainty.

For each risk:
  - trigger
  - consequence
  - detectability
  - containment
  - residual uncertainty
```

### 6.2 Risk Lenses — Choose by Failure Surface
Pick **lenses relevant to the actual failure modes**, not by depth level.
 | Lens | Focus | When to Use |
 |---|---|---|
 | **Operational** | Sequencing, partial completion, rollback, observability | Always for commitments with state changes |
 | **Environmental** | Wrong assumptions about versions, permissions, timing | When environment is unfamiliar |
 | **Adversarial** | Hostile/malformed inputs, worst-case conditions | Security-sensitive or public-facing work |
 | **Invariant** | Any path violating hard constraints | **Mandatory** for every irreversible commitment |
 | **Transition** | Partial completion → rollback failure → downstream validity | L3 or cascading commitments |

**L2:** 1 lens (chosen by what worries you most).
**L3:** ≥2 **distinct** lenses.

### 6.3 Attack Record
```yaml
attack:
  id: X1
  commitment_ref: C1
  scenario: <what goes wrong>
  trigger: <observable signal>
  impact: low | medium | high | critical
  prevention: [...]
  mitigation: [...]
  rollback: <specific revert command, or "impossible" + consequence>
  residual: <what remains after mitigation>
  independence: staged | isolated | external
```

**Rule:** A plan that reaches the target **only by violating a hard constraint** is **`invalid`**, not "risky".

---

---

## 7. Resolution — Calibrated, Commitment by Commitment

Resolve **each commitment independently**. Never pick a "winning plan" wholesale.

### 7.1 Resolution Order (Precedence)
1. Hard constraints and invariants
2. Verified observations and primary evidence
3. Demonstrated test or calculation
4. Independently supported reasoning
5. Reversibility when evidence doesn’t distinguish options
6. Simplicity when still tied

### 7.2 Confidence Levels
 | Level | Definition | Ship Rules |
 |---|---|---|
 | **high** | Compelled: exactly one option survives evidence + constraints | Ship |
 | **medium** | Supported, but residual uncertainty exists | Ship with monitoring **if reversible**; gate **if irreversible** |
 | **low** | Preference/assumption/evidence gap remains | Branch/discover/escalate. **Never ship silently** |

### 7.3 Ship Rules Matrix
 | Confidence | Reversible? | Consequence | Action |
 |---|---|---|---|
 | high | any | any | **ship** |
 | medium | yes | any | ship with monitoring |
 | medium | no | material | **gate or user veto** |
 | low | yes | trivial | ship, **flagged visibly** |
 | low | no | any | **branch/discover/escalate** |

### 7.4 Resolution Outcomes
- `resolved` – One option is adequately supported.
- `resolved-with-tradeoff` – Chosen, but a material trade-off remains.
- `branch` – Legitimately preference- or observation-dependent.
- `gated` – A discovery action must happen first.
- `unresolved` – Insufficient evidence, no safe default.
- `invalid` – All paths violate a hard constraint.

**Never force `resolved` to make the output look complete.**

### 7.5 Standing Rules
1. **No majority voting** – Agent count ≠ evidence. A minority candidate with **stronger evidence** beats a majority with weaker.
2. **Correlated error check** – Did candidates:
   - Use **genuinely different evidence paths**?
   - Share an **assumption**?
   - Belong to the **same model family**?
   If **yes** → that assumption is **unverified** even if all agree.
3. **No silent synthesis** – Any action **not** proposed by a candidate must be marked:
   ```yaml
   derived-from: [C1, E2, constraint_X]
   ```
   If the derivation is **not obvious**, create a **new commitment** and run §3–§7 on it.

---

---

## 8. Frontier Loop — For Unknown Environments

When working in the **fog of war**, maintain a **living state** (not a static document). Update internally before each material action.

```
Target:       <observable success condition>
Invariants:   <hard limits, e.g., "Do not delete DB">
State:        <facts verified EXCLUSIVELY by tool observation, not memory>
Next Step:    <Action -> Expected Tool Output -> Rollback Plan>
```

### 8.1 Execution Loop
1. Execute `Next Step`.
2. Did the tool output match `Expected Tool Output`?
   - **Yes** → Advance `State`. Determine the new `Next Step`.
   - **No** → **STOP**. Do **not** compound errors.
     - Revert if possible (using `Rollback Plan`).
     - Re-evaluate `State`.
     - **Do not** proceed to the next step.

**Rule:** If you find yourself writing "Step 5" but its parameters depend entirely on Step 2’s output, **delete Steps 3–5** and return to the loop.

---

---

## 9. Sequence — For Known Paths Only

If the path is **solved** (runbooks, documented APIs) and the user requires a plan artifact (or handoff), emit this **minimal contract**:

```text
# Execution Sequence
Target: <falsifiable end state>
Invariants: <hard constraints>

1. <Action intent>
   Expected: <observable tool output>
   Containment: <revert command or "GATE: User approval required">
2. <Action intent>
   Expected: <observable tool output>
   Containment: <revert command or "GATE: User approval required">
```

**Rule:** A step whose parameters depend on an earlier step’s output **ends the sequence there**. The remainder is a **named open question** (not invented steps).

---

---
---
---

## 10. Execute, Observe, Replan — The Core Loop

For **every non-trivial step**, define this **internal contract**:

```
Intent:      <what I am about to do>
Expected:    <the exact observable that tells me it worked — falsifiable>
Containment: <if it fails, how I revert or stop the blast radius>
```

### 10.1 Loop
1. **Execute** `Next Step`.
2. **Match** → Update *Verified now* (§2), advance to the next Frontier.
3. **Mismatch** → **STOP**. Do not compound errors.
   - Inspect actual state with a **discovery action**.
   - Roll back if `Containment` is defined and still safe.
   - Identify the **false premise**.
   - Replan the **smallest affected subtree**.

### 10.2 Global Replan Triggers
- An **invariant** was violated.
- A **load-bearing fact** is false, stale, or TTL-expired-and-different.
- The **environment** changed materially.
- **Repeated local failures** → world model is wrong, not the step.
- The **target** or a **hard constraint** changed.

### 10.3 After Each Phase
Record **one line**:
```
done | failed | new unknowns | state delta | next gate
```

### 10.4 Handoff to Another Agent
Provide:
- **Target**
- **Invariants**
- **Verified state**
- **Plan slice**
- **Open questions**
- **Replan triggers**

**Rule:** Nothing load-bearing lives in memory alone.

---
---
---

## 11. User Oracle — Cheapest High-Bandwidth Source

The user is the **cheapest source of preference and authorization**. Use them **deliberately**.

### 11.1 Trade-off Veto (L2+, **Mandatory at L3 Before Irreversible Steps**)
Before **any** irreversible commitment executes, emit every `resolved-with-tradeoff` as a **one-line veto**:

```
VETO? C3: <option A> (<trade-off one-liner>) vs <option B> (<trade-off one-liner>). Defaulting to A. Reply only if you want B.
```

**Silence is never authorization** for an irreversible, preference-dependent step **unless** the user has **explicitly delegated** default authority for that decision class.
**No delegation?** → Gate the action.

### 11.2 ask_user — First-Class Action Type
```yaml
action:
  type: ask_user
  question: <one self-contained question>
  recommended_default: <your best answer>
  cost: <what a wrong guess costs vs. the latency of asking>
```

**Rules:**
- **Batch questions**; never ask serially.
- **Cap:** 2 per phase.
- **Always** provide a recommended default (so the plan remains executable without a reply).
- **Never** ask about what is cheaper to verify by inspection, test, or search.

---
---
---

## 12. Action Contract — For Every Material Step

```yaml
action:
  id: A1
  from: C1               # Commitment ID
  evidence: [E1, E2]     # Evidence IDs
  attacks: [X1]          # Attack IDs
  type: discovery | change | validation | rollback | ask_user | branch | handoff
  objective: <which objective this serves>
  prerequisites: [<state conditions, not action IDs>]
  execution: <precise action>
  expected_output: <observable result — falsifiable>
  validation: <specific acceptance test>
  failure_signals: [<observable failure indicators>]
  rollback: <specific revert command, or "impossible" + consequence>
  provenance: compelled | candidate | derived | user_directed
  effort: low | medium | high
```

### 12.1 Rules
1. **Validation is defined on the action**, not deferred.
   ❌ *"Check it works"* | ✅ *"GET /health returns 200 within 2s"*
2. **Rollback is considered before execution.**
   - If rollback is **impossible** and impact is **high** → **explicit gate**.
3. **An action that cannot answer** *"which objective? how validated? what if it fails?"* **→ Redesign or cut.**

---
---
---

## 13. Plan Artifact — Only When It Earns Its Length

Emit a **written plan** when:
- The user **asks** for one, **OR**
- Interdependent irreversible steps must be visible **before execution**.

Otherwise, the **Horizon** (§2), the **next contract** (§10), and the **resolution ledger** (§7) **are the plan**.

### 13.1 Minimal Plan Format
```markdown
# Plan — <target>
Depth: L1 | L2 | L3        Territory: known | frontier
Target:         <observable success condition>
Invariants:     <hard limits>
Verified now:   <facts established by observation, with provenance + TTL>
Open questions: <unknowns execution will resolve, and how>

## Steps (ordered by precondition)
1. <step>
   type: discovery | change | validation | rollback | ask_user | branch
   from: C1
   evidence: [E1, E2]
   attacks: [X1]
   expected: <observable>
   containment: <revert / gate>
   on failure: <stop / replan from step N>

## Resolution Ledger
- C1: <commitment> — status: resolved | tradeoff | branch | gated | unresolved | invalid
      robustness: robust | sensitive | contained | why: <...>

## Gates
<user veto points, branch conditions, escalation triggers>

## Residual Risk
<what is contained | accepted | delegated>
```

### 13.2 Rules
- **One page per phase maximum** (more = planning into the fog).
- **Every commitment** is contained or gated.
- **Every `Expected`** is falsifiable.
- **Steps past a boundary** are discovery or experiment entries, **not invented detail**.
- **No YAML sidecar** — the ledger above suffices.

---
---
---

## 14. Planning Debt — Ship at 80% When the Rest Is Safe

A plan must be **executable and recoverable**, not complete. If the missing portion is held by a **gate**, a **monitor**, or a **reversible experiment**, ship and record:

```yaml
planning_debt:
  - <what is unverified>
  - <how it resolves during execution>
```

---
---
---

## 15. Agent Spawning — When and How

Spawn agents **only** when:
1. **Material consequence** (can change a commitment).
2. **Unresolved uncertainty** or **contested option** exists.
3. The new agent has a **distinct information/method/source role**.
4. The **expected value** of the result justifies the cost.

### 15.1 Spawning Matrix
 | Situation | Agent Role | Why |
 |---|---|---|
 | Option space may be incomplete | **Explorer** | Discover alternatives/framing errors |
 | Load-bearing claim needs verification | **Verifier** | Resolve a specific fact |
 | Domain boundary is unfamiliar/high-risk | **Specialist** | Expose domain-specific failure modes |
 | Material candidate selected | **Risk Attacker** | Independent attack (§6) |
 | Irreversible/cascading transition | **Transition Attacker** | Validate state/recovery logic (§6.2) |
 | Multiple independent outputs exist | **Integrator** | Reconcile without anchoring |

### 15.2 Spawn Justification Template
Before spawning, state:
```yaml
spawn:
  purpose: "<what the agent will achieve>"
  question: "<specific question the agent answers>"
  why_current_context_is_insufficient: "<...>"
  expected_information_gain: high | medium | low
  independence:
    information: isolated | partial | none
    method: meaningfully_different | same
    sources: independent | shared | none
  stop_condition: "<when the agent stops>"
```

**Example:**
```yaml
spawn:
  purpose: "Verify if the target API supports bulk deletion"
  question: "Does /api/v2/items support DELETE with ?all=true?"
  why_current_context_is_insufficient: "Documentation is ambiguous; need live inspection"
  expected_information_gain: high
  independence:
    information: isolated
    method: meaningfully_different
    sources: independent
  stop_condition: "Return verified API behavior or explicit inability to inspect"
```

---
---
---

## 16. Final Check — Before Emitting or Executing

Run this **checklist**. **Fail any item → revise, gate, branch, or escalate.**

- [ ] Target is **observable**; invariants **separated from preferences**.
- [ ] Every "verified" fact comes from **observation with provenance**, not memory or agreement.
- [ ] **Compulsion check ran** before any candidate generation — most commitments should have **zero candidates**.
- [ ] Every blind candidate was **blind**, **lens-diverse**, and its **independence labeled honestly**.
- [ ] **No majority voting**; correlated assumptions checked; **no silent synthesis**.
- [ ] Every step is **typed**; every commitment is **contained or gated**; every `Expected` is **falsifiable**.
- [ ] **No invented steps** past a boundary.
- [ ] Triggered care handled; preference trade-offs **asked or explicitly delegated**; **silence never treated as approval without delegation**.
- [ ] **Nothing irreversible** ships on an **unverified fact**.
- [ ] Remaining uncertainty is **visible**, not hidden; planning debt **recorded**.

---
---
---

## 17. When to Abandon This Protocol

**Answer directly** (no protocol) when:
- The request is a **question**, **explanation**, or **trivial reversible action**.
- The user **explicitly wants a fast answer** and the action is reversible.
- **No commitment** is load-bearing.
- Running the protocol would **cost more than the plan’s value**.
- The environment **offers no observation** to validate against (say so, don’t plan against imagination).

**A skill that never says "I am not the right tool" is dangerous. This one does.**

---
---
---

## 18. One-Sentence Principle

> **Navigate from verified state to observable target, spending compute only where it can change a material commitment, validating every load-bearing claim independently, containing what you cannot undo, and letting execution feed evidence back into the plan.**

---
---
---

## Appendix A — Prompts

### A.1 Explorer
```
You are an independent planning explorer.
Do NOT optimize the current draft.
Do NOT assume its framing is correct.
Do NOT see other agents' proposals.

Given:
  Objective: <...>
  Target state: <...>
  Current state: <...>
  Hard constraints: <...>
  Invariants: <...>
  Known evidence: <...>
  Known unknowns: <...>

Find:
  - Materially different approaches.
  - Missing assumptions.
  - Hidden dependencies.
  - Alternative problem framings.
  - Experiments that could collapse uncertainty.

For each important finding:
  - State what it could change.
  - Distinguish fact from hypothesis.
  - Identify what evidence would verify it.
```

### A.2 Verifier
```
You are a verification agent.
Your task: Determine whether the following load-bearing claim is supported.

CLAIM: <exact claim>

Use the strongest available method:
  - Direct inspection
  - Authoritative source
  - Reproducible test
  - Recomputable calculation
  - Clearly attributed expert reasoning

Return:
  - status (verified | supported | derived | unproven | contested)
  - evidence
  - exact locator
  - scope/date/version (where relevant)
  - limitations
  - contradictions
  - what remains unknown

NEVER turn your own reasoning into evidence.
```

### A.3 Risk Attacker
```
You are an independent risk attacker.
Do NOT defend the proposed plan.
Do NOT use another agent's agreement as evidence.

Context:
  Commitment: <C1>
  Proposed action: <...>
  Hard constraints: <...>
  Invariants: <...>
  Verified facts: <...>

Find:
  1. What could make this fail?
  2. Which assumption is most likely false?
  3. What happens under partial completion?
  4. Can rollback fail? Under what conditions?
  5. What is the first observable signal of failure?
  6. Does this create irreversible or cascading state?
  7. Does any path violate a hard constraint or invariant?
  8. What would a hostile or worst-case environment do to this?

For each material risk:
  - trigger
  - consequence
  - detectability
  - prevention
  - mitigation
  - rollback/containment
  - residual risk
```

### A.4 Transition Attacker
```
You are a state-transition reviewer.

Given:
  Current state S0: <...>
  Action A1: <...>
  Expected state S1: <...>
  Failure handling: <...>
  Next action A2: <...>

Check:
  - Preconditions for A1.
  - Post-condition after A1.
  - Partial completion scenarios.
  - Rollback failure scenarios.
  - Recovery state.
  - Invariant preservation.
  - Whether A2 is still valid after each failure mode.
  - What newly learned information could invalidate A2.

Return:
  - Concrete defects.
  - Minimal corrections.
```

---
---
---

## Appendix B — Minimal Schemas

### B.1 Commitment
```yaml
commitment:
  id: C1
  statement: "<one sentence>"
  type: action | architecture | dependency | experiment
  load_bearing: true
  why_load_bearing: "<what changes if wrong>"
  reversibility: reversible | partial | irreversible | unknown
  evidence: [E1, E2]
  attacks: [X1]
  resolution: resolved | resolved-with-tradeoff | branch | gated | unresolved | invalid
  confidence: high | medium | low
```

### B.2 Evidence
```yaml
evidence:
  id: E1
  claim: "<one sentence>"
  status: verified | supported | derived | unproven | contested
  source: user_input | observation | primary | secondary | test | calculation
  locator: "<file/URL/command/formula>"
  checked_at: "<timestamp>"
  ttl: "<duration>"
  limitations: "<what this does NOT prove>"
```

### B.3 Attack
```yaml
attack:
  id: X1
  commitment_ref: C1
  scenario: "<what goes wrong>"
  trigger: "<observable signal>"
  impact: low | medium | high | critical
  prevention: [...]
  mitigation: [...]
  rollback: "<specific or impossible + consequence>"
  residual: "<what remains>"
  independence: staged | isolated | external
```

### B.4 Action
```yaml
action:
  id: A1
  from: C1
  evidence: [E1]
  attacks: [X1]
  type: discovery | change | validation | rollback | ask_user | branch | handoff
  objective: "<...>"
  prerequisites: [...]
  execution: "<precise action>"
  expected_output: "<observable>"
  validation: "<specific test>"
  failure_signals: [...]
  rollback: "<specific or impossible + consequence>"
  provenance: compelled | candidate | derived | user_directed
  effort: low | medium | high
```
