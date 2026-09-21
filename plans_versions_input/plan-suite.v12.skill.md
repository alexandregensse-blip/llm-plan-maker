# plan-suite v12 — Planning that pays rent

Generic planning skill for LLM agents. Vendor-neutral. Single file.

---

## 0. What this is

A plan is a sequence of observable actions from a verified current state to
an observable target. This skill exists because LLM planners fail
predictably: hallucinated load-bearing facts, deliberation where evidence
already compels the answer, invented steps past the fog of war, skipped
containment on irreversible actions, and guessed preferences.

It also works under a constraint most planning skills ignore: **the protocol
itself must pass its own triage.** Every section must earn the tokens it
costs. Where it doesn't, skip it (§11, §12).

Meta-status: `unproven`. Before trusting it on high-consequence work, replay
3–5 past planning failures through it and check which gates would have
caught them, at what cost. Adjust or abandon accordingly.

---

## 1. Triage — one question, then one more

> Can the next action go wrong in a way I cannot cheaply and certainly undo?

- **No** → act. No plan artifact. The skill's only residue: state your
  expectation before acting so a mismatch is visible.
- **Yes** → the action is a **Commitment**. Continue here.
- **No commitment anywhere in sight and the path is known?** A plan document
  is overhead. Act stepwise instead.

Second question, rarely asked, which changes everything:

> **How well do I know this territory?**

- **Known path** — a solved shape: runbook, standard migration,
  well-documented API, procedure executed before. Plan ahead across steps;
  the plan's job is sequencing and validation checkpoints, not discovery.
  Fog-of-war doctrine (§5) does not apply.
- **Frontier work** — outcomes of early steps reshape later ones. Plan only
  to the next boundary. Do not write step 7 before step 2 has executed.

Most planning skills silently assume frontier work everywhere. That forces
re-discovery of known paths and wastes compute. Ask explicitly.

---

## 2. Horizon — four lines

```
Target:         <observable success condition>
Invariants:     <what must remain true at every step>
Verified now:   <facts established by external observation>
Open questions: <unknowns that could reshape the plan, and how each resolves>
```

- Target is falsifiable or it isn't a target. "Improve security" fails;
  "test X shows access paths closed under threat model T" passes.
- Invariants are hard limits. Preferences are recorded separately and never
  promoted to invariants silently.
- "Verified now" means you looked: tool output, inspection, the user's
  statement. Training data, prior sessions, and other agents' assertions are
  not verification (§7).

Revise the Horizon only when execution contradicts it — not preemptively.

---

## 3. Action contract

Every non-trivial step, internally:

```
Intent:       <what I am about to do>
Expected:     <the exact observable that tells me it worked>
Containment:  <revert path — required for commitments>
```

- Expected must be falsifiable. "Check it works" is not an Expected.
  "GET /health returns 200 within 2s" is.
- No Containment → you may not make this commitment unilaterally. Convert it
  to a discovery, run a bounded experiment, or gate it behind the user (§6).
- Pure mechanical consequences of a step inherit its contract. Do not
  re-deliberate them.

---

## 4. Compulsion check — before any deliberation

Before generating options, attacking anything, or asking anyone:

> **Do verified facts + hard constraints already leave exactly one viable path?**

- **Yes** → take it. Zero candidates, zero attacks, zero "risk reviews."
  Deliberating a compelled answer is theater: it spends compute and
  manufactures doubt where none should exist.
- **No, and the gap is a fact about the world** → your next step is
  discovery (§5). Resolve the fact before choosing.
- **No, and two or more paths remain** → a real choice exists. Run the care
  triggers (§6) before committing.

This is the largest compute saver in the skill, and the check most often
skipped — because generating options *feels* like rigor. It isn't.

---

## 5. Fog of war — plan to the boundary (frontier work only)

When a step's outcome can reshape everything after it, the plan ends there.
What lies beyond is an **open question with a named resolution path**, not
invented steps.

```
... Step 3 (experiment: probe API behavior under load)
    → outcome A: proceed via discovery D1
    → outcome B: replan from Horizon
```

- **Discovery** — read-only; reduces an unknown. Its containment is that it
  changes no state.
- **Experiment** — bounded action taken to learn. State the question, the
  cost, the success signal, the stop condition, and the decision the result
  unlocks.

A step that exists only because a document template has a slot for it is not
a step. Cut it.

---

## 6. Care triggers — discipline only where wrongness is expensive

Check each commitment. Most trigger nothing. Three matter:

| Trigger | Response |
|---|---|
| **Irreversibility** — containment impossible or costly | One independent attack (§7) before executing. Partial completion and rollback failure must be in scope. If preferences are also in play: user veto. |
| **Load-bearing unverified assumption** — the step rests on a fact not yet externally verified | Convert to discovery. Resolve the fact first. Never ship irreversible work on an unverified fact. |
| **Preference-dependent trade-off** — viable paths diverge on priorities you cannot infer | User oracle. Ask once, batched, with a recommended default: "VETO? A: ... vs B: ... Defaulting to A." **Silence is not authorization** unless the user has explicitly delegated that decision class. No delegation → gate the action. |

Deliberately absent: cascading-failure matrices, multi-lens risk reviews,
fixed candidate counts, evidence quotas. Each either duplicates
irreversibility discipline or invents precision the inputs don't support.
Reintroduce one only if your environment's own failure data justifies it.

---

## 7. Epistemic hygiene — three rules, no more

1. **Agents are not evidence.** A sub-agent's output, a self-critique, or a
   same-model "reviewer" changes no fact's status. Only external observation
   — tools, sources, tests, the environment, the user — verifies.
2. **Label independence honestly.** A same-family instance in a fresh
   context is *weakly* independent: useful for hunting failure modes,
   useless as corroboration. Never upgrade the label. Temperature is not
   independence.
3. **Load-bearing claims need provenance.** For any fact a commitment rests
   on, know its source and its limitation. If the source is your own
   reasoning, the fact is unverified — regardless of how many of your own
   passes agree with it.

---

## 8. Depth — a scrutiny level, not a document size

- **L1** — every step reversible; environment known; no material unknowns.
  Compact plan: target, ordered steps, one caveat. No contracts.
- **L2** — material unknowns or one consequential commitment. Full §3
  contracts; care triggers on flagged steps; one independent attack on the
  riskiest commitment.
- **L3** — irreversible, cascading, or high-consequence work. L2 plus a
  transition check (partial completion → rollback failure → downstream
  validity) and an explicit user gate before execution.

Unsure between L1 and L2 → L1, unless the action is irreversible.

---

## 9. Plan artifact — only when it earns its length

Emit a written plan when the user asks for one, or when interdependent
irreversible steps must be visible before execution starts. Otherwise the
Horizon and the next contract *are* the plan.

```
# Plan — <target>
Depth: L1 | L2 | L3
Target:         <observable success condition>
Invariants:     <hard limits>
Verified now:   <facts established by observation>
Open questions: <unknowns execution will resolve, and how>

## Steps (ordered by precondition)
1. <step>
   type: discovery | commitment | derived | experiment
   expected: <observable>
   containment: <revert / gate>
   on failure: <stop / replan from step N>

## Gates
<user veto points, branch conditions, escalation triggers>

## Residual risk
<what is contained | accepted | delegated>
```

One page per phase, maximum. More than that means you are writing fiction
past the fog.

---

## 10. Execute, observe, replan

- Result matches Expected → update *Verified now*, advance to the next
  Frontier.
- **Mismatch → stop.** Do not compound failures. Inspect the actual state
  with a discovery action; roll back if containment is defined and still
  safe; identify the false premise; replan the smallest affected subtree.
  Rebuild the whole Horizon only if the Target or invariants are in
  question.

Global replan triggers: an invariant was violated; a load-bearing fact is
false or stale; the environment changed materially; repeated local failures
mean your world model is wrong, not the step; the target or a hard
constraint changed.

After each phase, one line:

```
done | failed | new unknowns | state delta | next gate
```

Handing off to another agent: give the Target, invariants, verified state,
plan slice, open questions, and replan triggers. Nothing load-bearing lives
in memory alone.

---

## 11. Planning debt — ship at 80% when the rest is safe

A plan must be executable and recoverable, not complete. If the missing 20%
is held by a gate, a monitor, or a reversible experiment, ship and record:

```
planning_debt:
  - <what is unverified>
  - <how it resolves during execution>
```

---

## 12. When not to use

Questions, explanations, trivial reversible actions, speed requests on
reversible work: answer or act directly — no protocol. Known-path work: plan
ahead, but skip the frontier machinery. If the environment offers no
observation to validate against, say so instead of planning against your own
imagination.

A skill that never says "not the right tool" is dangerous. This one must —
and must also ask whether *it* is earning its tokens on this task. If the
protocol costs more than the plan's value, abandon the protocol, not the
verification.

---

## 13. Final check — before emitting or executing

- [ ] Target observable; invariants separated from preferences.
- [ ] Every "verified" fact comes from observation, not memory or agreement.
- [ ] Compulsion check ran: no deliberation on a compelled path.
- [ ] Every step is typed; every commitment is contained or gated; every
      Expected is falsifiable.
- [ ] No invented steps past a boundary.
- [ ] Triggered care handled; preference trade-offs asked or delegated.
- [ ] Nothing irreversible ships on an unverified fact.

Fail one → revise, gate, or escalate. Do not polish and ship.

---

## 14. One-sentence principle

> Know your territory before you plan across it; let compulsion, not
> habit, decide where you deliberate; contain what you cannot undo; verify
> with the environment rather than your own model of it; and spend
> discipline only where being wrong is expensive.
