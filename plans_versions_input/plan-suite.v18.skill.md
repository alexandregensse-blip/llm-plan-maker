# plan-suite v18 — Framing Before Framing, Compelled Navigation, Honest Independence

Generic planning skill for LLM agents. Vendor-neutral. Single file.
**Meta-status: `unproven`.** By its own standards this skill carries no
evidence that following it produces better plans. Before trusting it on
high-consequence work, replay 3–5 past planning failures through it and
record which gates would have caught them, at what cost. Cut any section
that does not earn its keep in your environment.

---

## 0. Core principle

> Planning is **state navigation**, not document production. You move from a
> **Verified Current State** to an **Observable Target State**. Every
> load-bearing commitment that closes options is validated by the cheapest
> source that can settle it — the environment first, the user second, a
> blind isolated model third, nothing last. Multi-agent compute is spent on
> exactly three things: **innovation** (framings nobody proposed),
> **blind confirmation** (independent verification of a claim), and **option
> diversity** (methods that genuinely differ). Never on ceremony, never on
> ensembles-by-default, never on re-litigating a compelled answer.

### 0.1 Invariants (survive every depth)

1. **State over prose.** Maintain a living state (§2), not a static
   document, until one is requested or required for handoff.
2. **Compulsion first.** If verified facts + hard constraints leave exactly
   one viable path, take it. Zero candidates, zero debate — deliberating a
   compelled answer manufactures doubt, not rigor.
3. **Framing before framing.** The most expensive planning failures are
   framing failures, not choice failures. Challenge the problem statement
   before resolving anything inside it (§5.1).
4. **Blind or nothing.** An agent that saw another agent's conclusion
   before forming its own is not an independent confirmation. Label
   independence honestly, never upgrade the label.
5. **Containment before confidence.** An irreversible or costly action
   ships only with a named revert path, or behind an explicit user gate.
6. **Agents are not evidence.** Only the environment (tool, test,
   inspection, source) or the user verifies a fact. A model's output —
   including another instance's — becomes evidence only when it performed
   an independent, inspectable check.
7. **No invented steps past the fog of war.** A step whose shape depends on
   an earlier step's outcome is not planned in advance; it is named as an
   open question.
8. **Silence is not authorization.** For a preference-dependent,
   irreversible trade-off, no reply from the user is never approval, unless
   that decision class was explicitly delegated in advance.
9. **Token economy is a design constraint.** Every section, every spawn,
   every evidence check must earn its cost. Default to the cheapest thing
   that resolves the commitment.

### 0.2 Failure modes this skill exists to prevent

Hallucinated load-bearing facts · anchoring · agreement mistaken for
evidence (including self-agreement) · mode collapse under identical briefs ·
hidden uncertainty · invented steps past the fog of war · skipped
containment on irreversible steps · guessed preferences · heavy multi-agent
machinery where compulsion or a direct answer sufficed.

---

## 1. Triage — the only mandatory gate

Answer from the request alone, before any drafting.

**Q1 — Reversibility.** *Can the next required action go wrong in a way I
cannot cheaply and certainly undo?*
- **No** → Act directly. State your expectation before acting so a mismatch
  is visible. No plan artifact. Stop reading here.
- **Yes** → this is a **Commitment**. Continue.

**Q2 — Territory.** *How well is this territory known?*
- **Known path** — runbook, documented API, procedure executed before,
  predictable environment → §9.2 **Sequence**.
- **Frontier** — the outcome of step N reshapes what step N+1 even is →
  §9.1 **Frontier Loop**.

**Q3 — Shape.** *Plan-dominant* (path known or evidence-discoverable;
ledger → execution sequence), *learning-dominant* (value = reducing named
unknowns; ledger → **experiment queue**, each entry with a stop condition —
do not fabricate a decision graph that doesn't exist), or *mixed* (mark
which commitments belong to which).

**Q4 — Depth.** How much of the rest of this skill is warranted?

| Depth | Condition | Protocol |
|---|---|---|
| **L0** | Question, explanation, or trivial reversible action | Answer or act directly. Nothing below applies. |
| **L1** | Reversible or single commitment, known territory, low consequence | Living state (§2) + action contract (§9.4). No ledger, no candidates. |
| **L2** | A commitment is load-bearing, OR material unknowns remain, OR the environment is unfamiliar | Full ledger (§3) + evidence (§4) + framing pass + blind confrontation where §5 triggers (§5–§6) + resolution (§7). |
| **L3** | Irreversible, cascading, high-consequence, or a material disagreement survives L2 | L2 + mandatory independent attack with a transition lens (§6.2) + explicit user gate before execution (§8). |

Default when unsure between L1 and L2: **L1**, unless the action is
irreversible.

Write one internal line before proceeding:
`depth=L2, shape=mixed, territory=frontier because: <observable signals>`.

---

## 2. Living State — the only artifact you maintain by default

Four lines, revised **only when execution contradicts them**, never
preemptively. Reused everywhere below — inside the Frontier Loop, at the
head of a written Plan, and in a handoff.

```
Target:         <observable, falsifiable success condition>
Invariants:     <hard limits that must hold at every step — never preferences>
Verified now:   <facts established EXCLUSIVELY by external observation>
Open questions: <unknowns that could reshape the plan, and how each resolves>
```

Rules:

- **Target must be falsifiable.** "Improve security" fails; "Test X shows
  access paths closed under threat model T" passes.
- **Invariants ≠ preferences.** "Do not delete production data" vs. "prefer
  managed services" — record preferences, escalate only when one decides a
  commitment (§8).
- **"Verified" means you looked** — tool output, inspection, a direct user
  statement. Never training data, memory, or another agent's assertion.
- **Evidence has a shelf life.** A load-bearing fact's implicit TTL is "this
  session". Re-check at execution time; a stale fact is a replan trigger
  (§10), not a silent carry-over.

---

## 3. Commitments — the only unit worth confronting

Do **not** confront a whole plan. Confront the individual points where it
closes options. Everything else is glue.

A **commitment** is any point that closes options or consumes non-trivial
resources: an irreversible or costly action (delete data, spend money, send
an email, notify a third party); adopting an architecture or dependency
that forecloses alternatives; taking on an external dependency (a person, a
service, an approval); an experiment that spends budget to resolve a named
unknown.

**Not a commitment:** the mechanical consequence of a commitment already
resolved (a directory implied by an approved migration, the health check
that validates a step already decided). Tag these `derived` — they inherit
their parent's justification; do not re-open them.

```yaml
commitment:
  id: C1
  statement: <what we commit to, one sentence>
  type: action | architecture | dependency | experiment
  load_bearing: true|false          # would a different answer change target/invariant/cost/recoverability?
  why_load_bearing: <what changes if this is wrong>
  reversibility: reversible | partial | irreversible | unknown
  evidence: []      # §4
  attacks: []       # §6
  resolution: null  # §7
  confidence: null  # §7
  robustness: null  # §7.3 — robust | sensitive | contained
```

At L1, skip the schema; carry the commitment as one sentence in your head
or the Living State.

### 3.1 Compulsion check — mandatory, per commitment, before any generation

> **Do the verified facts + hard constraints leave exactly ONE viable
> technical path?**

- **Yes** → resolve `now`, `confidence: high`, cite the evidence that
  compels it. **Spawn nothing.**
- **No, because a fact is missing** → not a choice, a gap. Convert to a
  discovery action (§4) or an experiment. Do not generate candidates to
  paper over missing information.
- **No, because ≥2 options genuinely survive the evidence** → candidates
  may be warranted. Continue to §5.
- **No, because it depends on what the user wants** → do not guess. Go
  straight to the user oracle (§8). Generating candidates to disguise a
  preference question as an analysis question wastes tokens and still ends
  at the same question.

Most commitments are compelled. The default candidate count is **zero**.
Every spawn needs a justification, not a default.

---

## 4. Evidence — verify before you generate, not instead of thinking

Verify a claim only when it is **(a) load-bearing** — it would change a
commitment's resolution — **and (b) externally checkable** — a source,
inspection, test, or recomputable calculation exists for it. Everything
else stays an explicit assumption.

### 4.1 Evidence budget (stop rule)

| Depth | Max evidence items per load-bearing commitment |
|---|---|
| L1 | 0–1 |
| L2 | ≤2 |
| L3 | ≤4, independently re-verified where feasible |

Hit the budget without resolving the claim? Stop. Mark the remainder a
**gap**, and branch, gate, or escalate — do not keep spending tokens
chasing certainty the budget already says isn't worth it.

```yaml
evidence:
  id: E1
  claim: <exact claim, one sentence>
  status: verified | supported | derived | unproven | contested
  source: user_input | observation | primary | secondary | test | calculation
  locator: <file/URL/command/formula/observation>
  ttl: <how long this stays true; default "this session">
  limitations: <what this does NOT prove>
```

### 4.2 Rules

1. A citation is not evidence unless the source actually supports the claim
   as stated.
2. A model's own statement — including a sub-agent's — is not evidence. It
   becomes evidence only when it reports the result of an inspection, test,
   or calculation someone else could rerun.
3. The same source cited by three separate agents is **one** evidence item,
   not three.
4. A calculation must expose its inputs and formula to count as
   recomputable.
5. Cannot inspect it? Mark `unproven`. Do not launder an unprovable claim
   into a fact by restating it confidently enough times.
6. Contradictory evidence is `contested`. Do not average it, and do not
   silently pick the version that's more convenient for the plan.
7. A commitment is only as certain as its weakest load-bearing premise: one
   strong item and one `unproven` item still leave the commitment
   unresolved.

---

## 5. Multi-agent confrontation — innovation, blind confirmation, honest diversity

> **Trigger, not quota.** Spawn agents only when at least one of these
> holds. Otherwise skip this section and record in the ledger that it was
> skipped and why. A spawn without a distinct question, information
> boundary, or method to test is theater — it inflates apparent confidence
> without adding it.

Three legitimate reasons to spend multi-agent compute:

1. **Innovation.** The current framing might be too narrow; nobody has
   proposed a genuinely different approach yet. → **Framing pass / Explorer**
   (§5.1).
2. **Blind confirmation.** A load-bearing claim needs independent
   verification that does not inherit the claim's case. → **Verifier**
   (§5.2).
3. **Contested choice.** ≥2 options survive the compulsion check, the
   commitment is load-bearing, and the choice is at least weakly
   reversible or wrong-pick-expensive. → **Candidates** (§5.3), then
   **attack** (§6).

Everything else — mechanical consequences, "review" passes with no distinct
lens, second opinions on a compelled answer — is ceremony. Refuse it.

### 5.0 Spawn justification — mandatory before any spawn

State it in one block; if you cannot fill it, do not spawn:

```yaml
spawn:
  question: "<the specific question this context answers>"
  why_cheaper_paths_fail: "<why evidence/inspection/user cannot settle it>"
  expected_gain: high | medium | low   # can it change a commitment, or only make it sound better?
  stop_condition: "<when this context stops>"
```

**Stopping rule:** stop spawning when the decision is stable (no plausible
agent output would change the commitment), when remaining uncertainty is
safely held by a gate/monitor/reversible experiment, or when the marginal
agent would only make the story sound better. Before every spawn, ask:
*"Could this context change what we do, or merely make it sound better?"*
Only the first justifies the tokens.

### 5.1 The framing pass — mandatory at L2/L3, cheapest sufficient form

The highest-value move this skill prescribes, and the most often skipped.
Before the framing freezes, challenge the problem statement itself:

- Are there materially different approaches to this objective?
- Is the current problem statement assuming something false?
- What dependency, constraint, or preference is being silently imported?
- What cheap experiment could collapse the biggest uncertainty?
- "It is six months later and this failed badly — what happened?" (one
  line, from the pre-mortem tradition)

**Form, in strict preference order:** (1) spawn an **Explorer** in isolated
mode if the runtime allows; (2) run it as a **staged** pass in the same
context under strict information hygiene (§5.4) and label it `staged`;
(3) at L1 or when even that is uneconomic, run it as an explicit
self-challenge checklist — same questions, written down before any
resolution — and label it `staged-weak`. Never call it isolated. The
obligation is to **confront the framing**, not to burn a spawn.

The output is not a candidate; it is input to whether the compulsion check
even applies to the framing you were about to use.

### 5.2 Roles, and when each earns its spawn

| Role | Purpose | Spawn when |
|---|---|---|
| **Explorer** | Reframes the problem, surfaces unproposed options, hunts hidden dependencies | §5.1 fires |
| **Verifier** | Independently checks one load-bearing claim against the environment | A claim is load-bearing and externally checkable (§4) |
| **Candidate** | Proposes one resolution for a specific commitment, from a stated method/lens | Compulsion check failed, ≥2 viable options (§5.3) |
| **Risk attacker** | Attacks a proposed resolution — does not defend it | Any load-bearing commitment, mandatory for irreversible ones (§6) |
| **Transition attacker** | Attacks the state transition: partial completion, rollback failure, downstream validity | L3, or any cascading commitment |

Prompts in Appendix A. All roles receive the facts and the question —
never the requester's persuasive case for a particular answer.

### 5.3 Candidate generation — diversity of method, not of wording

Trigger only per §5. Then:

| Scenario | Candidates |
|---|---|
| Compelled (§3.1 passed) | 0 |
| Triggered, default | 2 |
| L3, or two options within one trade-off grade | 3 |

If the runtime cannot spawn that many isolated contexts, fall back to
`staged` mode and label it — never claim independence you didn't achieve.

Give every candidate the **same** normalized brief; vary them by method or
optimization lens, not by wording:

```yaml
brief:
  problem: <...>
  target_state: <...>
  hard_constraints: <...>
  invariants: <...>
  verified_evidence: <list, or "none">
  unresolved_unknowns: <list>
  commitment: <C1 statement>
  optimize_for: <reversibility | failure-avoidance | simplicity | evidence-first>  # different per candidate
```

Each candidate must state: option (one sentence); rationale (3–5 bullets);
explicit assumptions; rejected alternatives *and why they remain viable*;
dependencies; its two most likely failure modes; a validation plan; what
would change the recommendation. A candidate that silently fills an
unknown with an assumption instead of naming it is invalid — discard and
regenerate the brief, don't patch the output.

### 5.4 Information hygiene (mandatory in `staged` mode, good practice always)

1. Generate each candidate before reading any persuasive rationale for a
   competing one.
2. Never let a candidate revise itself using another candidate's output
   before the attack pass runs.
3. Never show the attacker a candidate's persuasive rationale — give it the
   action and the facts (§6).
4. Never ask an agent to "agree with" or "improve on" a prior candidate
   before independent generation has finished.
5. Never call staged passes "isolated". The label is a claim about
   information flow, not effort.

### 5.5 Independence — label it honestly, never upgrade the label

| Mode | What it actually is | What it's worth | Use when |
|---|---|---|---|
| **staged** | Same context, sequential passes, strict information hygiene | Weakest — reduces anchoring, nothing more | Single-model / no sub-agent environment |
| **isolated** | Separate invocation or sub-agent, own context, blind to the others | Real information-flow independence, but same-family models share blind spots | Multi-agent runtimes |
| **external** | A different model family, or an actual test/inspection | Strongest practical independence | High-consequence decisions, when available |

Temperature is not independence. Self-critique is not a review. A
same-model "reviewer" in a fresh context is *weakly* independent — useful
for surfacing failure modes, useless as corroboration — and that label
never gets upgraded because the output sounds confident.

---

## 6. Adversarial pass — attack, don't review

Runs independently of generation. Same rule as above: give the attacker
the proposed action and the facts, not the case for it.

### 6.1 Risk lenses — pick by actual failure surface, not by depth level

| Lens | Focus | Use when |
|---|---|---|
| Operational | Sequencing, partial completion, rollback, observability | Any commitment with a state change |
| Environmental | Wrong assumptions about versions, permissions, timing, infra | Unfamiliar environment |
| Adversarial | Hostile, malformed, or worst-case input | Security-sensitive or public-facing work |
| Invariant | Any path that reaches the target by violating a hard constraint | Mandatory for every irreversible commitment |
| Transition | Partial completion → rollback failure → downstream validity | L3, or cascading commitments |

L2: one lens, chosen by what actually worries you about this commitment.
L3: at least two distinct lenses.

```yaml
attack:
  id: X1
  commitment_ref: C1
  scenario: <what goes wrong>
  trigger: <observable signal>
  impact: low | medium | high | critical
  prevention: []
  mitigation: []
  rollback: <specific revert command, or "impossible" + consequence>
  residual: <what remains after mitigation>
  independence: staged | isolated | external
```

**Hard rule:** a plan that reaches the target only by violating a hard
constraint or invariant is `invalid` — not "risky," not "acceptable with
monitoring." A mitigation existing is not evidence that the underlying risk
is small.

### 6.2 Transition lens (L3 / cascading, mandatory)

For each material transition `S0 --A1--> S1 --A2--> S2`, check:
preconditions of A1; post-condition of S1; partial completion; rollback
failure and its conditions; the recovery state; invariant preservation;
whether A2 is still valid after each failure mode; what newly learned
information could invalidate A2. Return concrete defects and minimal
corrections — not a rewrite.

---

## 7. Resolution — commitment by commitment, never plan by plan

Never pick a "winning candidate's whole plan." Resolve each commitment on
its own merits and reassemble.

### 7.1 Precedence, when evidence doesn't cleanly decide it

1. Hard constraints and invariants.
2. Verified observation / primary evidence.
3. A demonstrated test or calculation.
4. Independently supported reasoning.
5. Reversibility, when evidence doesn't distinguish the remaining options.
6. Simplicity, if still tied.

### 7.2 Confidence and what it licenses

| Confidence | Definition | Reversible | Consequence | Action |
|---|---|---|---|---|
| high | Compelled — one option survives facts + constraints | any | any | Ship. |
| medium | Supported, residual uncertainty remains | yes | any | Ship with monitoring. |
| medium | Supported, residual uncertainty remains | no | material | Gate, or user veto (§8). |
| low | Preference, assumption, or evidence gap remains | yes | trivial | Ship, flagged visibly. |
| low | Preference, assumption, or evidence gap remains | no | any | Branch, discover, or escalate — never ship. |

### 7.3 Robustness — what would flip it

After resolving, ask: *"What plausible unresolved fact could flip this
commitment?"*

- `robust` — no known plausible uncertainty would materially alter the path.
- `sensitive` — one or more unresolved facts could change the path (name
  them; they become replan triggers, §10).
- `contained` — uncertainty could change the path, but is safely held by a
  gate, test, or rollback.

Robustness is more useful than confidence alone: a `high`-confidence
compelled commitment can still be `sensitive` if its compelling evidence
decays quickly.

### 7.4 Outcomes

`resolved` — adequately supported · `resolved-with-tradeoff` — chosen, but a
material trade-off remains and is stated · `branch` — legitimately
preference- or observation-dependent · `gated` — a discovery must happen
first · `unresolved` — evidence insufficient, no safe default · `invalid` —
every path violates a hard constraint.

Never force `resolved` to make the output look finished.

### 7.5 Standing rules

- **No majority voting.** Agent count is not evidence. One candidate with a
  decisive, checkable finding beats three that agree without one.
- **Correlated-error check.** Before treating agreement as confirmation,
  ask: did the candidates use genuinely different evidence paths, or do
  they share an assumption, a source, or a model family? If they share one,
  that shared point is still unverified, however many agents repeated it.
- **No silent synthesis.** Any action in the final plan that no candidate
  proposed must be tagged `derived-from: [C1, E2, constraint_X]`. If the
  derivation isn't obvious, it's a new commitment — run §3.1–§7 on it,
  don't wave it through because assembly is almost done.

---

## 8. The user as oracle

The user is the cheapest source of *preference* and *authorization*
available. Use them deliberately, not as a last resort after guessing
fails.

**When to ask:** the choice cannot be settled by evidence or constraint;
it's materially consequential; and it's a preference rather than a fact.
Ask once, batched, with a recommended default:

> "VETO? A: `<trade-off one-liner>` vs B: `<trade-off one-liner>`.
> Defaulting to A. Reply only if you want B."

**Rules:**

- Silence is **not** authorization for an irreversible,
  preference-dependent trade-off — unless the user has previously and
  explicitly delegated that class of decision.
- No reachable user and no delegation → gate the action. Never invent an
  approval.
- At L3, a user gate before executing any irreversible commitment is
  mandatory, not optional — even if the user already approved the plan in
  general terms; the specific irreversible step gets its own checkpoint.
- Cap questions per phase at 2. Never ask about what is cheaper to verify
  by inspection, test, or search.
- `ask_user` is a first-class action type with a cost field: what a wrong
  guess costs vs. the latency of asking.

---

## 9. Turning resolved commitments into steps

### 9.1 Frontier Loop — unknown territory (§1 Q2 = frontier)

Maintain the Living State (§2) plus one field, updated before each material
action:

```
Next Step: <Action -> Expected Tool Output -> Rollback Plan>
```

Loop: execute `Next Step` → tool output matches Expected? Advance `Verified
now`, determine the new `Next Step`. Doesn't match? **Stop.** Do not
compound errors — revert if the Rollback Plan is still safe, re-evaluate
`Verified now`, and only then decide the next step.

Rule: if you notice you're writing "Step 5" but its parameters depend
entirely on Step 2's not-yet-observed output, delete steps 3–5. You are
hallucinating certainty past the fog of war.

### 9.2 Sequence — known territory (§1 Q2 = known path)

Emit this when the path is solved and either the user wants a plan artifact
before execution, or you're handing off to another agent:

```text
# Execution Sequence
Target: <falsifiable end state>
Invariants: <hard constraints>

1. <Action intent>
   Expected: <observable tool output>
   Containment: <revert command, or "GATE: user approval required">
2. <Action intent>
   Expected: <observable tool output>
   Containment: <revert command, or "GATE: user approval required">
```

Rule: a step whose parameters depend on an earlier step's not-yet-observed
output ends the sequence there. What follows is a named open question, not
an invented step — delete Steps 3+ and drop into the Frontier Loop instead.

### 9.3 Full plan artifact — only when it earns its length

Emit this instead of the bare Sequence when interdependent commitments must
be visible together before execution starts (L2/L3, multi-commitment work,
or explicit request).

```text
# Plan — <target>
Depth: L1 | L2 | L3        Shape: plan-dominant | learning-dominant | mixed

Target:         <observable success condition>
Invariants:     <hard limits>
Verified now:   <facts established by observation>
Open questions: <unknowns, and how execution resolves each>

## Steps (ordered by precondition)
1. <step>
   type: discovery | commitment | derived | experiment | ask_user
   expected: <observable>
   containment: <revert / gate>
   on failure: <stop / replan from step N>

## Resolution ledger
<one line per commitment: id, outcome, confidence, robustness, why>

## Gates
<user veto points, branch conditions, escalation triggers>

## Residual risk
<what is contained | accepted | delegated>

## Planning debt
<what is unverified, and how it resolves during execution — see §11>
```

One page per phase, maximum. More than that means you're planning fiction
past the fog — cut back to the next few material steps and drop the rest
into open questions.

### 9.4 The action contract (used everywhere above)

```
Intent:       <what I am about to do>
Expected:     <the exact observable that tells me it worked — falsifiable>
Containment:  <revert path, or "GATE: user approval required">
```

If `Expected` can't be stated precisely ("check it works" is not
falsifiable), the step is underspecified — sharpen it before acting. If
`Containment` can't be named for a commitment, you may not execute it
unilaterally: convert it to a discovery/experiment, or gate it (§8).

---

## 10. Execute, observe, replan

- **Match** → update `Verified now`, advance.
- **Mismatch** → **stop**. Inspect actual state with a discovery action;
  roll back if Containment is still safe; identify the false premise;
  replan the smallest affected subtree — rebuild the Living State only if
  Target or an invariant is in question.

### 10.1 Global replan triggers

An invariant was violated · a load-bearing fact turned out false, stale, or
TTL-expired-and-changed · the environment changed materially · repeated
local failures mean the world model is wrong, not the step · the target or
a hard constraint changed · a `sensitive` commitment's named flip-fact
materialized.

### 10.2 After each phase, one line

```
done | failed | new unknowns | state delta | next gate
```

### 10.3 Handoff to another agent

Give: Target, invariants, verified state, the plan slice, open questions,
replan triggers, and the `sensitive` commitments with their flip-facts.
Nothing load-bearing lives in memory alone — if it mattered enough to act
on, it's written down.

---

## 11. Planning debt — ship at 80% when the rest is safe

A plan must be executable and recoverable, not exhaustively complete. If
the missing 20% is held behind a gate, a monitor, or a cheap reversible
experiment, ship and record it:

```yaml
planning_debt:
  - what: <what is unverified>
    resolves_by: <how it gets resolved during execution>
```

Never silently drop coverage to fit a budget — an omission the reader
can't see is worse than one flagged and shipped.

---

## 12. Budget degradation — when compute or time runs out

Degrade in this order, never below the floor:

1. Fewer candidates (2 → 1 → 0 where compulsion re-checks pass).
2. Fewer lenses / fewer spawned explorers.
3. Less prose in the artifact.

**Never remove, at any budget:** evidence provenance on load-bearing
claims · the adversarial pass on irreversible commitments · the user veto
on irreversible preference-dependent trade-offs · visible uncertainty.

When only one context exists, use `staged` mode everywhere and label it —
the structure survives, the independence claims shrink.

---

## 13. When to abandon this protocol

Answer or act directly, no protocol, when: the request is a question, an
explanation, or a trivial reversible action · no commitment in the request
is load-bearing · the user explicitly wants speed and every step is
reversible · running this costs more than the plan is worth · the
environment offers no observation to validate against — say so, don't plan
against your own imagination.

A skill that never says "I am not the right tool for this" is dangerous.
This one does — and that judgment happens at Triage (§1), every time, not
just at the start of a session.

---

## 14. Final check — before emitting or executing

- [ ] Target is observable; invariants are separated from preferences.
- [ ] Every "verified" fact comes from observation with a locator, not
      memory or agreement.
- [ ] The framing pass ran at L2/L3 before the framing was frozen — in its
      cheapest sufficient form, honestly labeled.
- [ ] The compulsion check ran on every commitment before any candidate
      generation — most should show zero candidates.
- [ ] Every spawn had a §5.0 justification and a stop condition.
- [ ] Every spawned candidate was genuinely blind, lens-diverse, and its
      independence mode labeled honestly (staged/isolated/external).
- [ ] No majority voting; correlated-assumption check ran; no silent
      synthesis.
- [ ] Every step is typed; every commitment is contained or gated; every
      `Expected` is falsifiable.
- [ ] No invented steps past a fog-of-war boundary.
- [ ] Preference-dependent trade-offs were asked or explicitly delegated —
      silence was never treated as approval.
- [ ] Nothing irreversible ships on an unverified or contested fact.
- [ ] Every resolution carries a robustness tag; `sensitive` commitments
      have named flip-facts wired to replan triggers.
- [ ] Remaining uncertainty is visible in the output; planning debt is
      recorded, not hidden.

Fail one → revise, gate, or escalate. Do not polish and ship anyway.

---

## 15. One-sentence principle

> Confront the framing before resolving inside it; let compulsion decide
> where you deliberate; spend multi-agent compute only on innovation, blind
> confirmation, and genuine option diversity — each spawn justified and
> stoppable; contain what you cannot undo; verify with the environment, not
> your model of it; and let what execution observes decide the next step.

---

## Appendix A — Role prompts

### A.1 Explorer (framing pass)
```
You are an independent planning explorer. Do NOT optimize the current
draft. Do NOT assume its framing is correct. Do NOT see other agents'
proposals.

Given: objective, target state, current state, hard constraints,
invariants, known evidence, known unknowns.

Find: materially different approaches; missing assumptions; hidden
dependencies; alternative problem framings; experiments that could
collapse a key uncertainty cheaply.

For each finding, state what it could change, distinguish fact from
hypothesis, and name what evidence would verify it.

Do not write the final plan.
```

### A.2 Candidate (resolving one commitment)
```
You are proposing ONE resolution to a single commitment. You have not
seen any other candidate's answer.

Given: <candidate_brief from §5.3>

Return: option (one sentence); rationale (3-5 bullets); explicit
assumptions; rejected alternatives and why they remain viable; two most
likely failure modes; validation plan; what would change this
recommendation.

Do not silently fill an unknown with an assumption — name it.
```

### A.3 Verifier
```
You are a verification agent. Determine whether this load-bearing claim
is supported.

CLAIM: <exact claim>

Use the strongest available method: direct inspection, authoritative
source, reproducible test, recomputable calculation.

Return: status (verified | supported | derived | unproven | contested);
evidence; exact locator; scope/date/version where relevant; limitations;
contradictions; what remains unknown.

Never turn your own reasoning into evidence.
```

### A.4 Risk attacker
```
You are an independent risk attacker. Do NOT defend the proposed action.
Do NOT treat another agent's agreement as evidence.

Given: the commitment, the proposed action, hard constraints,
invariants, verified facts — not the requester's case for the action.

Find: what could make this fail; which assumption is most likely false;
what happens under partial completion; whether rollback itself can fail
and under what conditions; the first observable signal of failure;
whether this creates irreversible or cascading state; whether any path
violates a hard constraint or invariant.

For each material risk: trigger, consequence, detectability, prevention,
mitigation, rollback/containment, residual risk.
```

### A.5 Transition attacker (L3 / cascading only)
```
You are a state-transition reviewer.

Given: current state S0, action A1, expected state S1, failure
handling, next action A2.

Check: preconditions for A1; post-condition after A1; partial-completion
scenarios; rollback-failure scenarios; recovery state; invariant
preservation; whether A2 is still valid after each failure mode; what
newly learned information could invalidate A2.

Return concrete defects and minimal corrections — not a rewrite.
```

---

Schemas live inline where they are used (commitment §3, evidence §4,
attack §6, spawn §5.0) — one definition per concept, no duplication.
