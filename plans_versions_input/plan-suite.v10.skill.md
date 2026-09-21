# plan-suite v10 — Empirical Planning with Calibrated Containment

Generic planning skill for LLM agents. Vendor-neutral.

---

## 0. The One Claim

You cannot reliably simulate reality inside your own head. Plans that assume
you can — long state graphs, predicted adversary moves, "if X then Y else Z"
trees — are hallucination dressed as rigor.

The best planner is a small, safe, observable action whose result you then
read from the environment.

But this is not the whole story. LLMs also fail in predictable ways *before*
they act: hallucinating a load-bearing fact, anchoring on the first idea,
mistaking agreement for evidence, hiding uncertainty to look complete,
skipping containment on irreversible steps.

v10 is the smallest skill that preserves v9's empirical loop while keeping
just enough hygiene to prevent those five failure modes. It spends discipline
only where the cost of being wrong is real.

**Invariant:** *an action is only as good as the observation it produces.*

---

## 1. Triage — One Question

> Is the next action irreversible, expensive, or materially consequential?

- **No** — Just act. Use your tools. Answer. No plan artifact. No ledger.
- **Yes** — Use the protocol below.

If you are unsure, ask: *if this goes wrong, can I undo it cheaply and with
certainty?* If yes, it is reversible. If no, it is a Commitment and this
protocol applies.

A request for speed reduces breadth of exploration. It never removes
containment from an irreversible step.

---

## 2. Horizon and Frontier

Maintain only two living things. Both fit in a few lines. Neither is a
document.

### Horizon — the non-negotiables

```
Target:        <observable success condition>
Invariants:    <what must remain true through every step>
Verified now:  <facts established by external observation, not memory>
```

**Target must be observable.** "Improve security" is not a target.
"Unauthorized access paths under threat model T are closed, demonstrated by
test X" is.

**Invariants are not preferences.** "Do not delete production data" is an
invariant. "Prefer managed services" is a preference. If you cannot tell
which, treat it as an invariant until the user says otherwise.

**"Verified now" means you actually looked.** Training data, prior session
memory, and another agent's assertion are not verification.

### Frontier — the single next material step

Not the whole path. Not a branch plan. Only the next step that meaningfully
advances the Target and whose preconditions you can observe.

Every Frontier step is one of:

- **Discovery** — you don't yet have enough verified information to act
  safely. Read a file. Ping a service. Search a source. Ask the user. Run a
  bounded probe.
- **Commitment** — you have enough to act, and the action changes state that
  is not trivially reversible.
- **Derived** — a mechanical consequence of a Commitment you already made.
  Do not re-deliberate it; inherit its justification and give it the same
  validation and containment rules.
- **Experiment** — you can only learn the answer by doing, and the doing is
  itself contained. State the question, the cost, the success signal, the
  stop condition, and what decision it unlocks.

---

## 3. The Action Contract

Before executing any Commitment, write these three lines. No more.

```
Intent:        <what I am about to do>
Expected:      <the exact observable that will tell me it worked>
Containment:   <if it fails, how I revert or stop the blast radius>
```

Rules:

- **Expected must be falsifiable.** "It works" is not falsifiable.
  "GET /health returns 200 within 2s" is.
- **If you cannot name Containment, it is not a Commitment you are allowed
  to make unilaterally.** Either convert it to a Discovery or Experiment, or
  invoke §5 (a Care Trigger).
- **A Discovery action needs only Intent and Expected.** Its containment is
  that it does not change state.
- **An Experiment needs Intent, Expected, a stop condition, and what
  decision the result unlocks.**

If the three lines can't be written, the action is underspecified. Sharpen
it or replace it with a Discovery.

---

## 4. Execute, Observe, Decide

Run the action. Then compare the actual result to Expected.

- **Match** → update the Horizon's *Verified now*. Identify the next Frontier.
- **Mismatch** → Stop. Do not take the next step. The Horizon was built on
  something false. Go to §7 (Replan).

Do not narrate success. State the observation and move on. Do not narrate
failure as "interesting" — state the observation, stop, and replan.

---

## 5. Care Triggers — When More Discipline Is Required

Most Frontier steps are small and obvious. A small number are not. Invoke
additional discipline *only* when a trigger fires.

| Trigger | What it forces you to do |
|---|---|
| **Irreversibility** — Containment is impossible or costly | One independent attack (§6.1) before executing. If user preferences are also relevant, one user veto (§6.3). |
| **Preference-dependent trade-off** — two viable paths whose choice hinges on priorities you cannot infer | User Oracle (§6.3). Never guess a preference. |
| **Load-bearing assumption** — your next step rests on a fact you haven't verified and cannot verify by simple inspection | Convert the step into a Discovery. Resolve the assumption *first*. |
| **False consensus** — a fact "confirmed" only by another instance of the same model, or by your own prior reasoning | Echo Chamber check (§6.2). Downgrade the fact to *unverified*. |
| **Cascading Commitment** — this step, if it partially completes, changes the validity of two or more downstream steps | Pre-commitment attack with a transition lens (§6.1) covering partial completion and rollback failure. |

**Do not fire triggers that do not apply.** Discipline spent on reversible,
preference-neutral, single-step actions is theater.

---

## 6. Epistemic Hygiene

Three tools. Use only when a Care Trigger fires. Each is small.

### 6.1 Independent attack

Ask, in a fresh context if one is available, or as a deliberate step away
from your own reasoning if not:

> "Do not defend this action. What is the most likely way it fails, what is
> the first observable sign, and can rollback itself fail?"

Rules:

- An attack is not a review of your reasoning. Give the attacker the action
  and the facts, not your persuasive case for it.
- Another instance of the same model is *weakly* independent. Label it as
  such. Do not upgrade the label.
- Temperature is not independence.
- The attack's output is not evidence. It is a list of failure modes to
  contain or accept, not a verdict on the plan.

### 6.2 Echo Chamber check

Before treating any load-bearing fact as "verified", ask:

- Did this fact originate from the same reasoning that is about to act on
  it? (if yes → unverified)
- Did two sources "agree" because they share an origin, a corpus, or a
  model family? (if yes → one source, not two)
- Is the "evidence" actually model-generated text restating the claim?
  (if yes → unverified)

If the answer to any is yes, downgrade the fact. This is not paranoia; it is
the single most common way LLM plans become confidently wrong.

### 6.3 User Oracle

The user is the cheapest source of *preference* information and *authorization*
in the environment. Use them deliberately.

Ask only when:

- the choice cannot be settled by evidence or constraint;
- the choice is materially consequential;
- the choice is a preference, not a fact.

Ask once, batched, with a recommended default:

> "VETO? <A: trade-off one-liner> vs <B: trade-off one-liner>. Defaulting
> to <A>. Reply only if you want B."

Rules:

- **Silence is not authorization** for an irreversible, preference-dependent
  trade-off, unless the user has previously and explicitly delegated default
  authority for that class of decision.
- If the user cannot be reached and no delegation exists, gate the action.
- Never invent an approval.

---

## 7. Replan

When observation diverges from expectation:

1. **Stop** before the next step. Cascading failures compound.
2. **Inspect** the actual resulting state with a Discovery action.
3. **Contain** — roll back if Containment was defined and is still safe. If
   it is not, do not improvise; treat the new state as the working Horizon.
4. **Identify the false premise.** Which assumption in the Horizon or the
   Action Contract was wrong?
5. **Replan the smallest affected subtree.** Do not rebuild the whole
   Horizon unless the target or invariants themselves are now in question.

Replan triggers at the Horizon level (not just the step level):

- an invariant was violated;
- a load-bearing fact is discovered to be false or stale;
- the environment materially changed;
- repeated local failures suggest the world model is wrong, not the step;
- the target or a hard constraint changed.

After each substantive phase, record a one-line digest:

```
done | failed | new unknowns | state delta | next gate
```

---

## 8. When a Written Plan Is Actually Needed

Sometimes the work is multi-step and the user asks for a plan, not an action.
Emit one only when it is asked for, or when the actions are interdependent
and irreversible enough that the user must see the sequence before it starts.

Keep it to one page:

```
# Plan — <target>

depth: L1 | L2 | L3
target: <observable success condition>
invariants: <hard limits>
verified now: <facts established by observation>

## Steps
A1. <action>
    type: discovery | commitment | derived | experiment
    expected: <observable>
    containment: <revert / stop>
    if fail: <replan response>

A2. ...

## Gates
<user veto points, branch conditions, escalation triggers>

## Open questions
<unknowns that execution will resolve, with how>

## Residual risk
<what is contained, what is accepted, what is delegated>
```

Rules:

- No YAML sidecar. No schema cathedral. If a downstream agent needs more,
  they can read the actions.
- Every step must have an observable Expected. If it can't, it's not a step.
- Every Commitment must have Containment. If it can't, it's gated.
- Depth is a scrutiny level, not a document format. L1 is three lines.
- If you find yourself writing more than a page, you are planning past the
  fog of war. Cut it back to the next three material steps.

Depth guidance:

- **L1** — reversible, low consequence, single domain. Three lines: target,
  next step, caveat.
- **L2** — material uncertainty or a consequential commitment. Full plan
  format above, with at least one independent attack on the risky step.
- **L3** — high consequence, novel environment, cascading commitments.
  L2 plus a transition check on the irreversible step (partial completion,
  rollback failure, downstream validity) and a user veto before execution.

If you are unsure between L1 and L2, use L1 — *unless* the action is
irreversible.

---

## 9. When Not To Use This Skill

Skip the protocol and just answer or act when:

- the request is a question, an explanation, or a trivial reversible action;
- the user explicitly wants a fast answer and the action is reversible;
- no step is a Commitment;
- the environment offers no observation to validate against (in which case
  the honest move is to say so, not to plan).

A skill that never says "this is not the right tool" is dangerous. This one
does.

---

## 10. Quality Check Before Executing an Irreversible Step

Ask each. If any fails, revise, gate, or escalate — do not polish and ship.

- [ ] Target is observable.
- [ ] Invariants are separated from preferences.
- [ ] "Verified now" facts were established by external observation, not
      memory or agreement.
- [ ] The next action is tagged discovery / commitment / derived / experiment.
- [ ] A Commitment has Containment, or it is gated.
- [ ] Expected is falsifiable in a specific observation.
- [ ] Any load-bearing assumption has been reduced, or the step is marked
      Discovery instead.
- [ ] No Care Trigger was silently skipped.
- [ ] If a preference-dependent trade-off exists, the user was asked, or a
      delegation exists, or the step is gated.
- [ ] Nothing irreversible is being shipped on an unverified fact.

---

## 11. One-Sentence Principle

> Act from the smallest observable step that moves the Horizon, verify with
> the environment rather than your own model of it, spend discipline only on
> what is irreversible, preference-dependent, or cascading, and let what you
> actually observe — not what you assumed — decide the next step.
