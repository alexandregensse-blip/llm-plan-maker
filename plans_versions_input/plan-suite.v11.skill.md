# plan-suite v11 — Frontier Planning

Generic planning skill for LLM agents. Vendor-neutral. Single file.

---

## 0. Principle

A plan is a sequence of observable action contracts leading from the current
state to an observable target.

You cannot see past the fog of war: any step whose outcome can reshape the
path beyond it is a boundary. Plan up to the boundary, mark what lies beyond
as discovery, and let execution — not imagination — fill it in.

Two failure modes to avoid: planning past the boundary (hallucinated steps),
and acting without a contract (uncontained commitments).

---

## 1. Triage

First question: **what does the user want — an answer, an action, or a plan?**

- **Question, explanation, or trivial reversible action** → provide it
  directly. No plan artifact. Skip this skill.
- **An action where every step is reversible and cheap** → act directly,
  applying §3 contract discipline lightly to anything non-trivial.
- **A plan, or work containing an irreversible, expensive, or materially
  consequential step** → run the protocol below.

Second question, asked of any step that changes state: **if this goes wrong,
can I undo it cheaply and with certainty?** If no, the step is a
**Commitment** (§3) and §5 discipline applies to it.

---

## 2. Horizon

Establish before planning. Four lines. Revise whenever execution contradicts
them — not before.

```
Target:         <observable success condition>
Invariants:     <what must remain true through every step>
Verified now:   <facts established by external observation>
Open questions: <unknowns that could reshape the plan, and how each resolves>
```

Rules:

- **Target must be falsifiable.** "Improve security" is not a target.
  "Unauthorized access paths under threat model T are closed, demonstrated
  by test X" is.
- **Invariants are hard limits, not preferences.** "Do not delete production
  data" is an invariant. "Prefer managed services" is a preference. Record
  preferences separately; when one decides a material trade-off, ask the
  user (§5) — never guess it.
- **"Verified now" means you actually looked** — tool output, inspection,
  user statement. Training data, prior-session memory, and another agent's
  assertion are not verification (see §5, echo check).

---

## 3. The action contract

Every step in the plan carries these fields:

```
Step:         <what is done>
Type:         discovery | commitment | derived | experiment
Expected:     <the exact observable that tells it worked>
Containment:  <revert path — required for commitments>
On failure:   <stop / replan from which point>
```

- **Discovery** — read-only step that reduces an unknown. Intent + Expected
  suffice; its containment is that it changes no state.
- **Commitment** — changes state that is not trivially reversible.
  If Containment cannot be written, the step is not executable
  unilaterally: convert it to a discovery or experiment, or gate it (§5).
- **Derived** — the mechanical consequence of another step. Inherit its
  justification and validation; do not re-deliberate it.
- **Experiment** — a bounded action taken to learn. Adds a stop condition
  and the decision the result unlocks.
- **If Expected cannot be stated, the step is underspecified.** Sharpen it
  or drop it. "Check it works" is not an Expected. "GET /health returns 200
  within 2s" is.

---

## 4. Building the plan

This is the core act of planning. Do not skip it.

1. **Work backward from the Target.** What must be true immediately before
   it? And before that? Chain preconditions back to the Verified now state.
2. **Tag each step** with a type (§3). Merge pure mechanical consequences
   into their parent step as derived — they are not separate decisions.
3. **Order by precondition**, not by narrative, habit, or convenience.
4. **Stop at the fog boundary.** When the shape of the remaining path
   depends on a step's outcome, the next step is a discovery or experiment.
   Do not invent steps beyond that point.
5. **Prune.** If removing a step does not change the outcome, remove it.
   Keep only steps that materially advance the Target.

Then set the depth (§6) and run care triggers (§5) on flagged steps.

---

## 5. Care triggers

Most steps are small and obvious. Spend discipline only where the cost of
being wrong is real. Check each step; on trigger, apply the tool.

| Trigger | Tool |
|---|---|
| **Irreversibility** — containment impossible or costly | Independent attack (a) + user veto (c) |
| **Preference-dependent trade-off** — viable paths differ on priorities you cannot infer | User oracle (c). Never guess a preference. |
| **Load-bearing assumption** — the step rests on a fact not yet verified | Convert it to discovery. Resolve the fact first. |
| **Same-origin "confirmation"** — a fact verified only by your own reasoning or a same-family agent | Echo check (b): downgrade to unverified |
| **Cascading** — partial completion invalidates two or more downstream steps | Independent attack (a) with a transition lens: partial completion, rollback failure, downstream validity |

Do not fire triggers that do not apply. Discipline spent on reversible,
preference-neutral, single steps is theater.

**(a) Independent attack.** In a fresh context if available, otherwise as a
deliberate step away from your own reasoning. Give the attacker the action
and the facts — not your persuasive case:

> "Do not defend this action. What is the most likely way it fails, what is
> the first observable sign, and can rollback itself fail?"

The output is a list of failure modes to contain or accept, not a verdict.
Another instance of the same model is *weakly* independent — label it as
such and do not upgrade the label. Temperature is not independence.

**(b) Echo check.** Before treating a load-bearing fact as verified, ask:
did it originate in the reasoning that is about to act on it? Do the "two
sources" share an origin, a corpus, or a model family? Is the evidence
model-generated text restating the claim? Any yes → the fact is unverified.
This is the single most common way LLM plans become confidently wrong.

**(c) User oracle.** The user is the cheapest source of preference and
authorization. Ask only when the choice is materially consequential, cannot
be settled by evidence, and is a preference rather than a fact. Ask once,
batched, with a recommended default:

> "VETO? A: <trade-off one-liner> vs B: <trade-off one-liner>.
> Defaulting to A. Reply only if you want B."

Silence is **not** authorization for an irreversible, preference-dependent
step unless the user has explicitly delegated that decision class. If the
user cannot be reached and no delegation exists, gate the action. Never
invent an approval.

---

## 6. Depth

Depth is a scrutiny level, not a document size.

- **L1** — every step reversible, environment known, no material unknowns.
  Compact plan: target, ordered steps, one caveat.
- **L2** — material unknowns, or at least one consequential commitment.
  Full contracts per §3; care triggers on flagged steps; one independent
  attack on the riskiest commitment.
- **L3** — irreversible, cascading, or high-consequence work. L2 plus a
  transition-lens attack and an explicit user gate before execution.

If unsure between L1 and L2, use L1 — unless a step is irreversible.

---

## 7. Plan format

Emit the artifact when the user asks for a plan, or when interdependent
irreversible steps must be visible before execution begins.

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
<what is contained, what is accepted, what is delegated>
```

Rules:

- Every step has a falsifiable Expected; every commitment has Containment
  or a gate.
- Steps past the fog boundary are discovery or experiment entries, not
  invented detail.
- If the plan grows past one page per phase, you are planning into the
  fog — cut back to the boundary.

---

## 8. Execute, observe, replan

When the plan executes — by you or by a downstream agent:

- **Result matches Expected** → update *Verified now*, advance to the next
  step.
- **Mismatch** → stop. Do not compound failures. Inspect the actual state
  with a discovery action; roll back if containment was defined and is still
  safe; identify the false premise; replan the smallest affected subtree.
  Rebuild the whole Horizon only if the Target or invariants are in
  question.

Global replan triggers: an invariant was violated; a load-bearing fact
turned out false or stale; the environment changed materially; repeated
local failures indicate the world model is wrong, not the step; the target
or a hard constraint changed.

After each phase, record one line:

```
done | failed | new unknowns | state delta | next gate
```

Handing off to another agent: give the Target, invariants, verified state,
the plan slice, open questions, and replan triggers. Nothing load-bearing
lives in memory alone.

---

## 9. Final check

Run before emitting or executing the plan.

- [ ] Target is observable; invariants separated from preferences.
- [ ] Every "verified" fact comes from observation, not memory or agreement.
- [ ] Every step is typed; every commitment is contained or gated; every
      Expected is falsifiable.
- [ ] No invented steps past the fog boundary.
- [ ] Care triggers fired where applicable; preference trade-offs asked or
      explicitly delegated.
- [ ] Nothing irreversible ships on an unverified fact.

Fail an item → revise, gate, or escalate. Do not polish and ship.

---

## 10. When not to use

Questions, explanations, trivial reversible actions, and speed requests
where every step is reversible: answer or act directly — no protocol. If
the environment offers no observation to validate against, say so instead
of planning.

A skill that never says "not the right tool" is dangerous. This one does.
