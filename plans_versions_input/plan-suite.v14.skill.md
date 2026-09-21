# plan-suite v14 — Independent Validation Routing

Generic planning skill for LLM agents. Vendor-neutral. Single file.

---

## 0. Core Principle

> **Every load-bearing claim and every real choice must be validated by a source independent of the one that produced it. The planner's job is to route each validation to the cheapest sufficient independent observer: the environment (tool / test / inspection) > the user > a blind isolated context > nothing.**

Two corollaries make this economical:

1. **Compulsion before delegation.** If verified facts + hard constraints leave exactly one viable path, no agent is spawned, no options are generated, no debate occurs. Most "decisions" in most plans are compelled. Agents are spent only where a genuine choice survives the evidence.
2. **Discipline only where wrongness is expensive.** Irreversible, preference-dependent, or cascading steps get containment, independent attack, and user gates. Everything else is executed and observed.

This skill fuses two schools that previous versions wrongly treated as rivals: the **empirical loop** (verify with the environment, plan only to the next observable boundary) and **blind multi-agent confrontation** (verify with contexts that did not produce the claim). They are complementary layers of the same principle: the environment validates facts about the world; blind isolated contexts validate what the environment cannot settle — framing, hypotheses, failure modes, and real choices.

**Meta-status: `unproven`.** By its own §2 standards this skill carries no evidence that following it produces better plans. Before trusting it on high-consequence work, replay 3–5 past planning failures through it and record which gates would have caught them, at what cost. Adjust or abandon accordingly. Every section below must earn the tokens it costs; where it does not, skip it.

---

## 1. Triage — The Only Gate

Before writing any plan, answer two questions from the user's prompt alone:

**Q1 — Reversibility.** Can the next required action go wrong in a way I cannot cheaply and certainly undo?
- **No (reversible):** no plan artifact. State your expectation, act, observe. (Skip to §7 for the execution loop.)
- **Yes (commitment):** continue to Q2.

**Q2 — Territory.** How well is this territory known?
- **Known path:** runbooks, documented APIs, standard migrations, procedures executed before. The environment is predictable. Plan a sequence across steps (§4); frontier machinery does not apply.
- **Frontier work:** the outcome of step N reshapes the path beyond it. Plan only to the next boundary (§3).

Route in one line: `depth=<L0|L1|L2|L3>, territory=<known|frontier> because: <observable signals>`.

Depth is a scrutiny level, not a document size:
- **L0** — question, explanation, trivial reversible action: answer directly, no protocol.
- **L1** — reversible, low consequence, known territory: compact plan, one caveat, no contracts.
- **L2** — material unknowns or a consequential commitment: full action contracts, care triggers on flagged steps, blind confrontation only if a real choice survives §5.
- **L3** — irreversible, cascading, or high-consequence: L2 + independent attack with a transition lens + explicit user gate before execution.

Unsure between L1 and L2 → L1, unless the action is irreversible.

---

## 2. Horizon and Frontier — The Living State

Maintain two things, a few lines each. Neither is a document.

```
Target:         <observable success condition; falsifiable or it is not a target>
Invariants:     <hard limits that must remain true at every step — never preferences>
Verified now:   <facts established EXCLUSIVELY by external observation, not memory>
Open questions: <unknowns that could reshape the plan, and how each resolves>
```

Rules:
- "Improve security" is not a target. "Test X shows access paths closed under threat model T" is.
- Invariants vs preferences: "Do not delete production data" is an invariant; "Prefer managed services" is a preference. Record preferences separately. When a preference decides a material trade-off, ask the user (§6). Never guess it, never promote it silently.
- **Verified means looked.** Training data, prior sessions, another agent's assertion, and your own reasoning are not verification. Evidence carries provenance and a TTL: a fact about a moving environment decays into a hypothesis. Re-verify stale load-bearing facts at execution time.

### The Frontier — the next material step only

Not the whole path. Only the next step that meaningfully advances the Target and whose preconditions you can observe. Each Frontier step is one of:

- **Discovery** — you lack verified information to act safely. Read, ping, inspect, ask. Containment: it changes no state.
- **Commitment** — you have enough to act; the action changes state not trivially reversible. Requires a contract (§7) and, if flagged, care triggers (§6).
- **Derived** — mechanical consequence of a Commitment already made. Inherit its justification, validation, and containment. Do not re-deliberate.
- **Experiment** — you can only learn by doing, and the doing is contained. State the question, cost, success signal, stop condition, and the decision the result unlocks.

**Fog of war:** a step whose outcome can reshape everything after it is a boundary. The plan ends there; what lies beyond is an open question with a named resolution path, not invented steps. If you find yourself writing step 5 whose parameters depend entirely on step 2's output, delete steps 3–5 and return to the loop.

---

## 3. Blind Confrontation — Where Multi-Agent Compute Is Spent

> **Trigger, not quota.** Spawn isolated contexts only when ALL hold: (a) the compulsion check failed — ≥2 materially different viable paths survive the evidence; (b) the choice is load-bearing (flipping it changes the target, an invariant, irreversibility, or recovery options); (c) the cost of being wrong justifies the spend. Otherwise: zero candidates. Record that the check ran and passed.

An "agent" here means any isolated model invocation — a sub-agent, a separate context, or the same model re-prompted in a fresh window with no shared history. Label the independence honestly:

| Label | Meaning | Evidentiary value |
|---|---|---|
| `staged` | Same context, sequential passes with strict information hygiene | Weakest; reduces anchoring only |
| `isolated` | Separate context, blind to other candidates/rationales | Real information-flow independence; same-family blind spots remain |
| `external` | Different model family, or an actual test/inspection | Strongest practical |

Temperature variation is not independence. Never upgrade a label.

### 3.1 Generation — diversity of method, not of wording

Give each candidate the **same normalized brief** (problem, target, constraints, invariants, verified evidence, unknowns) and a **different method or lens**: simplest viable path / constraint-first / reversibility-first / evidence-test-first / alternative architecture. Lenses must be relevant to the decision — do not manufacture a second candidate to satisfy a template.

Mandatory information hygiene:
1. Candidates are generated blind — never show candidate A to candidate B.
2. Never ask an agent to "improve candidate X" before independent generation.
3. Surface assumptions explicitly; a candidate that silently fills an unknown with an assumption is invalid.
4. Each candidate states: option, rationale, assumptions, rejected alternatives and why they remain viable, dependencies, the two most likely failure modes, validation, and what would change its recommendation.

### 3.2 Attack — independent of generation

Risk analysis runs on a separate path. Do not show the attacker the candidate's persuasive rationale; give it the action and the facts:

> "Do not defend this action. What is the most likely way it fails, what is the first observable sign, can rollback itself fail, and does any path violate a hard constraint?"

Output = failure modes to contain or accept, not a verdict. A same-family attacker is `weakly independent` — label it. For L3 irreversible/cascading transitions, add a **transition lens**: partial completion → rollback failure → downstream validity.

### 3.3 Resolution — per decision, never per plan

Resolve each material decision independently. Precedence: hard constraints → verified observations/primary evidence → tests/calculations → independently supported reasoning → reversibility → simplicity.

- **No majority voting.** Agent count is not evidence. A minority candidate with stronger evidence beats a unanimous field sharing one assumption.
- **Correlated-error check.** Before declaring a decision resolved, ask: did the candidates use genuinely different evidence paths? Do they share an assumption? Same model family? If so, that assumption is unverified regardless of agreement.
- **No silent synthesis.** Any action not proposed by a candidate is marked `derived-from: [decision, evidence, constraint]`. If the derivation is not obvious, open a new decision and re-run the check.
- **Calibrated resolution.** `resolved` (compelled or well-supported) / `resolved-with-tradeoff` (chosen, material trade-off remains) / `branch` (legitimately preference- or observation-dependent) / `gated` (a discovery must happen first) / `unresolved` (no safe default) / `invalid` (all paths violate a hard constraint — invalid, not "risky"). Never force `resolved` to look complete.
- **Ship rules.** Compelled/high confidence → ship. Supported but uncertain + reversible → ship with monitoring. Irreversible + material → gate or user veto (§6). Low confidence → branch, discover, or escalate. Never ship low-confidence work silently.

### 3.4 Stopping rule for agents

Stop spawning when: the decision is stable (no plausible agent output would change the commitment); remaining uncertainty is safely held by a gate, monitor, or reversible experiment; or the marginal agent only makes the current story sound more convincing. Ask before every spawn: **"Could this context change what we do, or merely make it sound better?"** Only the first justifies the tokens.

---

## 4. The Sequence — Known Paths Only

If the territory is known and the user needs a plan artifact (or a handoff), emit this minimal contract:

```text
# Execution Sequence
Target: <falsifiable end state>
Invariants: <hard constraints>

1. <Action intent>
   Expected: <observable tool output>
   Containment: <revert command or "GATE: user approval required">
2. ...
```

A step whose parameters depend on an earlier step's output ends the sequence there; the remainder is a named open question. Do not plan past the boundary.

---

## 5. Compulsion Check — Before Any Deliberation

Before generating options, debating paths, or spawning anything:

> **Do verified facts + hard constraints leave exactly ONE viable technical path?**

- **Yes →** take it immediately. Zero candidates, zero attacks, zero risk reviews. Deliberating a compelled answer is hallucinated rigor.
- **No, missing facts →** next action is Discovery.
- **No, preference divergence →** stop; ask the user (§6). Do not guess preferences.

Run this check at every material decision, not once. It is the largest token saver in this skill and the one most often skipped — generating options *feels* like rigor. It is not.

---

## 6. Care Triggers — Discipline Only Where Wrongness Is Expensive

Most steps are small and obvious. Check each commitment; most trigger nothing. Three triggers matter:

| Trigger | Response |
|---|---|
| **Irreversibility** — containment impossible or costly | One independent attack (§3.2) before executing; partial completion and rollback failure in scope. If preferences also in play: user gate. |
| **Load-bearing unverified assumption** — the step rests on a fact not yet externally verified | Convert to Discovery. Resolve the fact first. Nothing irreversible ships on an unverified fact. |
| **Preference-dependent trade-off** — viable paths diverge on priorities you cannot infer | User oracle: ask once, batched, with a recommended default. |

Deliberately absent: cascading-failure matrices, multi-lens risk reviews, fixed candidate counts, evidence quotas. Each either duplicates irreversibility discipline or invents precision the inputs do not support. Reintroduce one only if your environment's own failure data justifies it.

### User oracle and the silence rule

The user is the cheapest high-bandwidth source of preference and authorization. Ask only when the choice is materially consequential, cannot be settled by evidence, and is a preference rather than a fact. Ask once, batched:

> "VETO? A: <trade-off one-liner> vs B: <trade-off one-liner>. Defaulting to A. Reply only if you want B."

**Silence is never authorization for an irreversible, preference-dependent step — unless the user has explicitly delegated default authority for that decision class.** Delegation must be explicit and recorded; if none exists and the user cannot be reached, the action is gated. Never invent an approval.

---

## 7. Execute, Observe, Replan — The Loop

For every non-trivial step, internally define the contract:

```
Intent:      <what I am about to do>
Expected:    <the exact observable that tells me it worked — falsifiable>
Containment: <if it fails, how I revert or stop the blast radius>
```

No Containment on an irreversible step → not executable unilaterally: convert to Discovery/Experiment or gate it (§6). "Check it works" is not an Expected; "GET /health returns 200 within 2s" is. Mechanical consequences of a step are part of its validation, not separate steps.

Loop:
1. Execute `Next Step`.
2. **Match →** update *Verified now*, advance the Frontier.
3. **Mismatch →** STOP. Do not compound errors. Inspect actual state with a Discovery action; roll back if containment is defined and still safe; identify the false premise; replan the smallest affected subtree. Rebuild the Horizon only if the Target or invariants are in question.

Global replan triggers: invariant violated; load-bearing fact false, stale, or TTL-expired-and-different; environment materially changed; repeated local failures (world model wrong, not the step); target or hard constraint changed.

After each phase, one line:

```
done | failed | new unknowns | state delta | next gate
```

Handing off to another agent: give the Target, invariants, verified state, plan slice, open questions, and replan triggers. Nothing load-bearing lives in memory alone.

---

## 8. Plan Artifact — Only When It Earns Its Length

Emit a written plan when the user asks for one, or when interdependent irreversible steps must be visible before execution. Otherwise the Horizon, the next contract, and the resolution ledger **are** the plan.

```text
# Plan — <target>
Depth: L1 | L2 | L3        Territory: known | frontier
Target:         <observable success condition>
Invariants:     <hard limits>
Verified now:   <facts established by observation, with provenance + TTL>
Open questions: <unknowns execution will resolve, and how>

## Steps (ordered by precondition)
1. <step>
   type: discovery | commitment | derived | experiment
   expected: <observable>
   containment: <revert / gate>
   on failure: <stop / replan from step N>

## Resolution ledger
- D1: <decision> — status: resolved | tradeoff | branch | gated | unresolved | invalid
      robustness: robust | sensitive | contained | why

## Gates
<user veto points, branch conditions, escalation triggers>

## Residual risk
<what is contained | accepted | delegated>
```

Rules: one page per phase maximum (more = planning into the fog); every commitment contained or gated; every Expected falsifiable; steps past a boundary are discovery or experiment entries, not invented detail; no YAML sidecar — the ledger above suffices.

---

## 9. Planning Debt — Ship at 80% When the Rest Is Safe

A plan must be executable and recoverable, not complete. If the missing portion is held by a gate, a monitor, or a reversible experiment, ship and record:

```text
planning_debt:
  - <what is unverified>
  - <how it resolves during execution>
```

---

## 10. Final Check — Before Emitting or Executing

- [ ] Target observable; invariants separated from preferences.
- [ ] Every "verified" fact comes from observation with provenance, not memory or agreement.
- [ ] Compulsion check ran: no deliberation on a compelled path; zero candidates spent where one path survived.
- [ ] Every blind candidate generated was blind, lens-diverse, and its independence labeled honestly.
- [ ] No majority voting; correlated assumptions checked; no silent synthesis.
- [ ] Every step typed; every commitment contained or gated; every Expected falsifiable.
- [ ] No invented steps past a boundary.
- [ ] Triggered care handled; preference trade-offs asked or explicitly delegated; silence never treated as approval without delegation.
- [ ] Nothing irreversible ships on an unverified fact.
- [ ] Remaining uncertainty is visible, not hidden; planning debt recorded.

Fail one → revise, gate, branch, or escalate. Do not polish and ship.

---

## 11. When to Abandon This Protocol

Questions, explanations, trivial reversible actions, speed requests on reversible work: answer or act directly. Known-path work: plan ahead, skip the frontier machinery. No observation available to validate against: say so instead of planning against your own imagination. Protocol costing more than the plan's value: abandon the protocol, not the verification.

A skill that never says "not the right tool" is dangerous. This one must — including about itself (§0).

---

## 12. One-Sentence Principle

> Route every load-bearing claim to the cheapest independent validator — environment first, blind contexts only where a real choice survives the evidence, the user only for preferences — contain what you cannot undo, plan only to the next observable boundary, and let what you observe, not what you assume, decide the next step.
