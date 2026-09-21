# plan-suite v8 — Evidence-Guided Adaptive Planning

Generic planning skill for LLM agents. Vendor-neutral.  
Designed to work whether the runtime supports sub-agents, isolated invocations, tools, or only one model context.

---

# plan-suite v8 — Evidence-Guided Adaptive Planning

## 4. Purpose

This skill produces plans that are:

- proportionate to consequence and uncertainty;
- grounded in explicit evidence and constraints;
- adversarially challenged when it matters;
- traceable from facts to commitments to actions;
- explicit about unresolved uncertainty;
- recoverable when execution diverges from the model;
- usable by a single LLM or a multi-agent runtime.

It is not a requirement to use many agents.

The objective is not agent consensus.

The objective is:

> **Before a material commitment closes options, reduce the uncertainties that can change that commitment, confront the remaining viable paths from independent perspectives, and make the resulting plan adapt to what execution reveals.**

---

# 5. Core invariants

These are the rules that survive every budget level.

### I1 — Separate world, belief, preference, and decision

Never silently mix:

- **fact/observation** — what is directly known or observed;
- **source-supported claim** — what a source establishes;
- **derived claim** — what follows from known premises;
- **hypothesis** — plausible but not established;
- **assumption** — temporarily adopted for planning;
- **preference** — what the user/owner wants;
- **constraint/invariant** — what must not be violated;
- **decision/commitment** — what the plan is going to do.

### I2 — Materiality governs effort

Spend additional research, agents, tests, and critique only when the result could change a material commitment.

### I3 — Agents are not evidence

An agent may discover, compare, verify, challenge, model, or synthesize.

Its output becomes evidence only when tied to an actual source, observation, test, or recomputable derivation.

### I4 — Independence must be characterized honestly

Do not call a self-critique independent.

Do not call same-input/same-source agreement independent confirmation.

Record what information, source, and method were independent.

### I5 — No majority voting

Three agents agreeing is not stronger than one agent finding a decisive contradiction.

Resolve disagreements by tracing claims, evidence, assumptions, and tests.

### I6 — Compulsion is conditional, not absolute

If current verified facts and hard constraints leave one viable path, mark the path `constrained`.

Still ask whether the option space or world model is incomplete when the consequence is material.

### I7 — Every material action is observable

Every material action needs:

- a precondition;
- an objective;
- an observable expected result;
- a validation;
- a failure signal;
- a rollback or explicit consequence.

### I8 — Irreversibility requires containment

Before an irreversible or high-impact transition:

- unresolved critical assumptions are not hidden;
- risk has an independent attack;
- the user/owner makes preference-sensitive trade-offs explicitly, or has previously delegated that authority;
- rollback or consequence is explicit;
- a gate exists when the transition must not happen under uncertainty.

### I9 — Silence is not authorization

No response from the user is not approval for an irreversible trade-off unless explicit delegation says otherwise.

### I10 — Plans are closed-loop

Execution is allowed to produce new information.

A plan must state what observations can invalidate downstream steps and when to replan.

---

# 6. Triage: decide how much planning is justified

Before planning, establish:

1. Is the user asking for a plan, or for an answer/action/explanation?
2. What is the consequence of a wrong plan?
3. What is unknown about the environment?
4. Which actions close options or consume meaningful resources?
5. How reversible are the relevant actions?
6. Does the choice depend on user/owner preferences?
7. What tools, sources, tests, and agent isolation are actually available?

Use four depths.

| Depth | Typical condition | Protocol |
|---|---|---|
| L0 | No material commitment; trivial/reversible | Answer or act directly |
| L1 | Low consequence; mostly known environment; small uncertainty | Direct plan + validation + one explicit caveat |
| L2 | Material uncertainty, unfamiliar environment, or meaningful commitment | Full evidence/risk/provenance loop |
| L3 | High consequence, novel environment, cascading commitments, or unresolved material disagreement | L2 + independent option exploration + independent risk attack + transition analysis + explicit gates |

The depth is a **budget and scrutiny level**, not a claim about plan quality.

If the user requests speed, reduce breadth before removing essential safety and provenance checks.

Write internally:

`depth=L2 because: <observable signals>.`

---

# 7. The planning map

Do not begin by writing a final sequence of actions.

First create a compact planning map.

```yaml
planning_map:
  objective:
    requested: "<what the user asked for>"
    target_state: "<observable desired state>"
  current_state:
    known: []
    unknown: []
  constraints:
    hard: []
    invariants: []
  preferences:
    explicit: []
    delegated_defaults: []
    unknown: []
  material_unknowns:
    - id: U1
      question: "<unknown>"
      what_it_can_change: "<commitment/action>"
      consequence: low | material | high | critical
      reduction_method: source | inspection | test | user | agent | execution
  commitments: []
  risks: []
  dependencies: []
```

### 7.1 Frame the objective

Convert vague intent into an observable target state whenever possible.

Avoid:

> "Improve security."

Prefer:

> "Deploy the specified controls and be able to demonstrate that unauthorized access paths are closed under the stated threat model."

Do not silently add goals.

---

## 7.2 Capture constraints and invariants

Distinguish:

- `constraint`: a boundary on the plan;
- `invariant`: a condition that must remain true through every material state transition.

Examples:

- budget must remain below a specified ceiling;
- no production data may be deleted;
- customer-visible downtime must remain below a limit;
- legal approval must exist before release;
- secrets must never be written to a public repository.

A path that reaches the target by violating an invariant is `invalid`, not merely `risky`.

---

## 7.3 Record user preferences separately

Examples:

- optimize cost over convenience;
- minimize operational burden;
- prefer open source;
- preserve existing vendor relationships.

Do not transform an unstated preference into a hard constraint.

When a preference is unknown and materially changes a trade-off, create a `user_gate`.

---

# 8. Identify what can actually make the plan wrong

Instead of creating dozens of decisions, identify **material planning elements**.

A material element is something whose reversal could materially alter:

- the target outcome;
- a hard constraint/invariant;
- safety/security/legal/financial exposure;
- architecture or dependency structure;
- irreversibility;
- recovery options;
- a major user/owner preference trade-off.

Material elements usually fall into four types:

```text
M1 = load-bearing factual claim
M2 = load-bearing decision/commitment
M3 = material risk or dependency
M4 = material state transition
```

Do not create a separate planning unit for mechanical consequences.

For example:

`"Use managed database" -> "Create database instance"`

is one commitment followed by a derived action, not two independent decisions.

---

# 9. Unknowns before options

For every material unknown ask:

> "Could resolving this change a material commitment?"

If no, defer it.

If yes, classify how it can be reduced:

- `source` — authoritative external information;
- `inspection` — inspect the actual environment;
- `calculation` — recomputable derivation;
- `test` — empirical experiment;
- `user` — owner preference/context/authorization;
- `agent` — alternative hypothesis, search strategy, critique;
- `execution` — deliberately discover during a bounded step.

This creates a **value-of-information queue** without pretending to calculate precise economics.

---

# 10. The confrontation architecture

The key v8 change is that not every plan element follows the same epistemic route.

## 10.1 Type A — Constrained element

Use when current verified evidence and hard constraints leave no materially distinct viable path.

Process:

`verify -> compulsion check -> independent hazard check -> accept or reopen`

No candidate debate is required unless the hazard check finds a framing problem.

---

## 10.2 Type B — Contested choice

Use when multiple viable materially different paths remain.

Process:

`independent option discovery -> evidence verification -> independent risk attack -> resolution`

At L2, seek at least two genuinely different proposals when the environment supports it.

At L3, add more exploration only when it can change the decision.

Do not generate "alternative #2" solely to satisfy a quota.

---

## 10.3 Type C — Derived action

If an action is the mechanical consequence of an accepted commitment, do not waste agent budget debating it.

Trace it:

`commitment -> derived action`

It still needs validation and failure containment.

---

## 10.4 Type D — Experiment

When the key uncertainty can only be reduced by doing something, do not pretend a decision is settled.

Represent it as:

```yaml
experiment:
  question: "<what we need to learn>"
  action: "<bounded experiment>"
  cost: "<resources consumed>"
  success_signal: "<what observation answers the question>"
  stop_condition: "<when to stop>"
  consequence_containment: "<why this experiment is safe enough>"
  decision_unlocked: "<what changes after learning>"
```

This is especially important for discovery-heavy work.

---

# 11. When to spawn agents

Do not spawn agents because "more agents are better."

Spawn an agent only if its output has a plausible route to changing or validating a material plan element.

Use this trigger:

```text
SPAWN when:
  material consequence
  AND unresolved uncertainty or contested option
  AND the new agent has a distinct information/method/source role
  AND the expected value of the result justifies the cost.
```

The fourth condition can be judged qualitatively.

Ask:

> "What would this agent discover that the current context is unlikely to discover?"

If there is no good answer, do not spawn it.

---

## 11.1 Agent roles

### Explorer

Purpose: discover alternatives, hidden dependencies, unknowns, or a different framing.

Input:
- problem;
- target;
- constraints;
- current state;
- known evidence;
- explicit instruction to challenge the current framing.

Blindness:
- does not see other agents' candidate rationales.

Output:
- alternatives;
- missing constraints;
- assumptions;
- reasons the apparent option space may be incomplete.

---

### Verifier

Purpose: determine whether a specific load-bearing claim is actually supported.

Input:
- one or more claims;
- relevant sources/tools/environment access.

Output:
- claim status;
- evidence;
- exact locator;
- limitations;
- contradictions.

The verifier should prefer direct inspection, primary sources, tests, and recomputable calculations over model memory.

---

### Specialist

Purpose: analyze one domain boundary that the main planner may not cover reliably.

Examples:
- security;
- legal/compliance;
- database operations;
- finance;
- networking;
- performance;
- accessibility.

Do not use specialist outputs as evidence unless their claims are themselves tied to evidence.

---

### Risk attacker

Purpose: find failure modes without becoming invested in the plan.

Input:
- material commitment/action;
- verified facts;
- constraints/invariants;
- relevant current state.

Do not show persuasive rationale unless necessary for a targeted attack.

Output:
- failure scenario;
- trigger;
- consequence;
- detectability;
- prevention;
- mitigation;
- rollback/containment;
- residual risk.

---

### Transition attacker

Purpose: test whether the plan remains valid across state changes.

For each material transition:

`precondition -> action -> expected state -> failure state -> recovery state -> next-step validity`

Ask:

- can the action partially complete;
- can rollback fail;
- can mitigation create a later invariant violation;
- can newly observed information invalidate the next step?

---

### Integrator

Purpose: synthesize independent outputs into a plan.

The integrator should operate **after** independent exploration, verification, and attacks.

The integrator must not manufacture certainty.

It should resolve by:

1. hard constraints/invariants;
2. verified facts and direct observations;
3. tests/calculations;
4. source quality and relevance;
5. independent reasoning;
6. reversibility/containment;
7. explicit user preferences.

---

# 12. Independence protocol

Record independence with three fields.

```yaml
independence:
  information: none | partial | isolated
  method: same | meaningfully_different
  sources: shared | partially_independent | independent
```

Interpretation:

- `information=isolated` means the agent did not see prior proposals/reasoning.
- `method=meaningfully_different` means it attacked the problem using a different reasoning/search/test approach.
- `sources=independent` means the factual basis is not simply duplicated.

### Required hygiene for isolated proposals

1. Give each proposal the same core brief.
2. Do not reveal earlier rationales.
3. Do not ask later agents to "improve candidate A" before independent generation.
4. Keep evidence and candidate reasoning distinct.
5. Record when agents share a model family, source corpus, or assumption.

Temperature variation is not meaningful independence.

---

# 13. Evidence protocol

## 13.1 Evidence is about claims, not documents

Create an evidence record for every load-bearing external claim.

```yaml
evidence:
  id: E1
  claim: "<exact claim>"
  status: verified | supported | derived | assumption | disputed | unknown
  source_type: user_statement | observation | primary_source | secondary_source | test | calculation | model_reasoning
  locator: "<file / URL / command / formula / observation>"
  checked_at: "<timestamp when relevant>"
  freshness: stable | low_volatility | volatile | unknown
  limitations: "<what this evidence does not establish>"
```

---

## 13.2 Evidence precedence

Use source fit, not a simplistic universal hierarchy.

As a default:

`direct observation / reproducible test / invariant`
>
`authoritative primary source`
>
`relevant secondary source`
>
`independent expert reasoning`
>
`model reasoning`

But the right source depends on the claim.

Example:

- current server state -> inspect/test it;
- product documentation behavior -> primary documentation;
- business preference -> user/owner;
- mathematical conclusion -> recomputable calculation;
- possible failure mode -> independent attack is useful even without a source.

---

## 13.3 Contradictions

When evidence conflicts:

1. preserve both claims;
2. determine whether they concern different dates, versions, states, scopes, or definitions;
3. identify which source actually bears on the current question;
4. verify where possible;
5. mark the claim `disputed` when unresolved;
6. branch or gate the plan if the contradiction changes a material commitment.

Never average contradictory facts merely to produce a smooth answer.

---

## 13.4 Evidence freshness

Do not use a universal TTL.

Classify evidence by volatility:

- `stable` — unlikely to change on the planning horizon;
- `low_volatility` — changes occasionally;
- `volatile` — changes frequently;
- `unknown` — freshness behavior is unclear.

A source's age matters only relative to the claim.

At execution time, re-check evidence whose freshness is material to the transition.

---

## 13.5 Evidence stopping rule

Stop verification when one of these becomes true:

### A — Decision stable

Additional evidence is unlikely to change the current commitment.

### B — Safe containment

The remaining uncertainty is held by a gate, monitor, or reversible experiment.

### C — Diminishing value

Another check is possible but its expected information value is lower than its cost and no safety/integrity requirement demands it.

Do not stop merely because an arbitrary evidence count has been reached.

---

# 14. Pre-decision hazard scan

Before selecting among materially different options, perform an attack that does not depend on candidate persuasion.

Prompt:

```text
You are an independent hazard analyst.

Do not choose a solution.
Do not defend any candidate.
Analyze the problem as if the current plan is wrong.

Given:
  objective
  current state
  constraints/invariants
  known facts
  unknowns

Find:
  1. the most dangerous missing fact;
  2. assumptions most likely to be false;
  3. hidden dependencies;
  4. irreversible/cascading transitions;
  5. failure modes common to all obvious options;
  6. conditions under which the problem has been framed incorrectly;
  7. evidence or experiment that would most reduce the uncertainty.

For each issue provide:
  trigger, consequence, detectability, containment, and residual uncertainty.
```

The result can reopen the planning map.

---

# 15. Candidate confrontation

Only after the option space is sufficiently understood.

Use independent option proposals for material choices.

### Candidate contract

Each proposal must contain:

```yaml
proposal:
  option: "<one sentence>"
  intended_outcome: "<what becomes true>"
  assumptions: []
  supporting_evidence: []
  dependencies: []
  tradeoffs: []
  main_failure_modes: []
  validation: []
  revision_trigger: []
```

A proposal is invalid when it silently turns an unknown into a fact.

---

## 15.1 Compare by dimensions, not fake certainty

Do not create an overall numeric score unless the user explicitly provides a defensible scoring model.

Compare on:

- constraint fit;
- evidence support;
- unknowns;
- reversibility;
- operational complexity;
- failure containment;
- dependency risk;
- user/owner preferences;
- observability;
- expected cost/effort where measurable.

A trade-off that cannot be resolved from evidence should remain visible.

---

# 16. Post-selection adversarial pass

Every selected material commitment gets an independent attack.

Prompt:

```text
You are the final adversarial reviewer.

You are not the planner and you are not defending the selected path.

Context:
  commitment
  selected action
  hard constraints/invariants
  relevant verified facts
  current state

Attack:
  1. what assumption is most likely false;
  2. what can fail before completion;
  3. what can fail after partial completion;
  4. whether rollback can fail;
  5. whether mitigation can create a later problem;
  6. first observable failure signal;
  7. whether any path violates a constraint/invariant;
  8. whether a missing alternative should reopen the choice;
  9. what test/gate would most reduce the residual risk.

Do not use the existence of another agent's agreement as evidence.
```

At L3, use at least two distinct risk lenses when the failure surface warrants it.

Typical lenses:

- operational;
- environmental;
- adversarial;
- invariant/constraint;
- dependency/supply-chain;
- human/process;
- data/state consistency.

Choose lenses from the actual failure surface, not from a fixed quota.

---

# 17. Resolve each material commitment

Use these resolution statuses:

```text
constrained
supported
preference-dependent
experiment-gated
branch
unresolved
invalid
```

### constrained

Current verified facts + hard constraints leave one viable path in the considered option space.

### supported

A choice remains among alternatives, but one path is sufficiently supported for the consequence involved and survives independent attack.

### preference-dependent

The evidence does not decide the choice; the user/owner's priorities materially determine it.

### experiment-gated

A bounded experiment must happen before the choice can be safely resolved.

### branch

Different future states or preferences produce legitimately different paths.

### unresolved

Evidence is insufficient and no safe default or contained experiment exists.

### invalid

Every currently available path violates a hard constraint or invariant.

---

# 18. Robustness check

After resolution, ask:

> "What plausible unresolved fact could flip this commitment?"

Classify:

```text
robust       = no known plausible uncertainty would materially alter the path
sensitive    = one or more unresolved facts could change the path
contained    = uncertainty could change the path, but is safely held by a gate/test/rollback
```

This is more useful than a generic confidence label.

---

# 19. User/owner gates

Create a gate whenever a material choice depends on a value judgment that evidence cannot settle.

```yaml
user_gate:
  decision: "<commitment>"
  tradeoff: "<what is being exchanged>"
  options:
    - "<option A>"
    - "<option B>"
  why_the_user_decides: "<preference that matters>"
  default_authorized: true | false
  required_before: "<state/action>"
```

Rules:

- ask only when the answer can change a material commitment;
- batch questions where possible;
- never pretend the user has approved a trade-off they have not approved;
- if no answer arrives and no default authority exists, leave the transition gated;
- if the user has explicitly delegated default decisions within a stated policy, use that delegation and record it.

---

# 20. Assemble the plan as a state-transition graph

A final plan is not just a list.

Represent:

```text
S0 --A1--> S1 --A2--> S2 --A3--> S3
             |             |
           fail          fail
             v             v
           recovery      recovery
```

For each material transition:

1. preconditions;
2. action;
3. observable post-condition;
4. failure signal;
5. recovery/containment;
6. information newly learned;
7. whether downstream steps remain valid.

A plan should be able to say:

> "If observation X occurs, stop and replan from state S2."

That is a first-class part of the plan, not an afterthought.

---

# 21. Action contract

```yaml
action:
  id: A1
  origin:
    type: compelled | selected | derived | experiment | user_directed | conditional
    refs: [C1, E1, R1]
  objective: "<what this action changes>"
  preconditions:
    - "<state condition>"
  execution: "<precise action>"
  expected_result: "<observable result>"
  validation: "<specific acceptance test>"
  failure_signals:
    - "<observable failure>"
  containment:
    rollback: "<specific rollback or impossible>"
    consequence: "<what happens if rollback is impossible>"
  replan_trigger:
    - "<condition that invalidates downstream steps>"
  effort: low | medium | high
```

### Action rules

- "Check it works" is not sufficient validation.
- An action that cannot state its observable result is underspecified.
- An irreversible action without containment must be gated or escalated.
- A derived action does not need a new agent debate when its derivation is mechanical and traceable.
- A material derived action still needs independent risk analysis before execution.

---

# 22. Execution-time adaptation

Planning ends only when the plan is safe to hand off, not when every future detail is known.

Handoff contains:

1. relevant plan slice;
2. complete hard constraints/invariants;
3. current validated state;
4. evidence required for that slice;
5. open unknowns that matter;
6. replan triggers;
7. pointers to the broader plan.

On failure:

```text
stop before compounding
-> inspect actual state
-> contain/rollback if safe
-> identify failed assumption or transition
-> update planning map
-> replan smallest affected subtree
```

Global replan triggers:

- invariant violation;
- load-bearing evidence invalidated;
- environment changed materially;
- repeated local failures;
- target/constraints changed;
- new information changes multiple commitments;
- a previously hidden dependency appears.

After each phase, record:

`done / failed / state delta / new evidence / new unknowns / next gate`.

---

# 23. Stop conditions

Stop planning when:

- every material commitment is in a safe resolution state;
- every material action is validated and contained;
- unresolved uncertainty is visible;
- no remaining unknown is both material and currently worth resolving before execution;
- additional agent/research passes are unlikely to change the path.

Stop earlier when new work only produces repetition.

Do not stop because:

- a quota was reached;
- enough agents agreed;
- the document "looks complete";
- the output has become long.

The stopping criterion is **decision stability plus safe containment**, not document completeness.

---

# 24. Budget degradation

When tools/compute/time are constrained, degrade in this order:

1. optional exploration;
2. extra candidate generation;
3. additional specialist lenses;
4. prose/detail in the final report.

Do not remove:

- provenance for load-bearing claims;
- essential constraint checks;
- adversarial review for irreversible/high-impact actions;
- explicit uncertainty;
- validation and containment.

When only one context exists, use staged information hygiene and label it `isolated=false`.

---

# 25. Output format

## L0

```text
Answer/action: ...
```

No fake planning apparatus.

## L1

```text
Objective: ...
Steps:
1. ...
2. ...

Validation: ...
Main caveat: ...
```

## L2 / L3

Emit the executable plan first.

```markdown
# Plan

depth: L2 | L3
target_state: ...
current_state: ...
resolution_summary: constrained=<n> supported=<n> preference-dependent=<n> gated=<n> unresolved=<n>

## Steps

A1. ...
    origin: selected | compelled | derived | experiment
    validation: ...
    containment: ...
    replan if: ...

## Gates

- ...

## Unknowns

- U1: ...
  reduction: ...
  material_if_changed: ...

## Residual risks

- ...

---

# Planning Trace

## Material commitments

- C1: ...
  status: ...
  robustness: robust | sensitive | contained
  refs: [E1, X1, ...]

## Evidence

- E1: ...
  status: ...
  source: ...
  locator: ...
  limitation: ...

## Attacks

- X1: ...
  scenario: ...
  impact: ...
  trigger: ...
  containment: ...
  residual: ...

## Agent independence

- Explorer: information=isolated, method=meaningfully_different, sources=shared
- Verifier: information=isolated, method=meaningfully_different, sources=independent

## Planning debt

- ...
```

The trace is a causal record, not a transcript of hidden reasoning.

---

# 26. Quality gates

Before emitting an L2/L3 plan, check:

- [ ] Objective and target state are explicit enough to validate.
- [ ] Hard constraints and invariants are separated from preferences.
- [ ] Current state is distinguished from assumptions about the current state.
- [ ] Every material unknown states what it could change.
- [ ] Load-bearing claims have provenance or are visibly uncertain.
- [ ] Agents are not being treated as evidence merely because they agree.
- [ ] Independence claims are honest about shared context, method, and sources.
- [ ] Candidate generation happened only where the option space was genuinely contested or incomplete.
- [ ] Constrained decisions were checked for framing/option-space risk when consequence warrants it.
- [ ] Every irreversible or high-impact action has independent risk analysis.
- [ ] Material state transitions have preconditions, post-conditions, failure signals, and containment.
- [ ] Preference-sensitive trade-offs are explicit.
- [ ] Silence was not interpreted as approval without explicit delegated authority.
- [ ] Every material action has validation.
- [ ] Replan triggers are explicit.
- [ ] Remaining uncertainty is visible.
- [ ] No arbitrary candidate/evidence quota is being used as a substitute for judgment.
- [ ] The plan can be handed to another agent without relying on hidden context.

A failed gate means:

`revise | verify | branch | gate | experiment | escalate`

Do not polish around a failed gate.

---

# 27. When not to use the skill

Do not run the full protocol for:

- factual questions;
- explanations;
- trivial reversible actions;
- obvious procedural requests with no material uncertainty;
- work where protocol overhead clearly exceeds its value.

However, do not let a request for speed suppress essential verification or containment for a high-consequence irreversible action.

The skill should be able to say:

> "There is no meaningful planning problem here."

That is a successful outcome.

---

# 28. Compact orchestration algorithm

This is the vendor-neutral execution loop.

```text
1. TRIAGE
   Determine consequence, uncertainty, reversibility, novelty, preference sensitivity, and available tools/agents.

2. FRAME
   Define objective, target state, current state, hard constraints, invariants, preferences.

3. MAP MATERIALITY
   Identify load-bearing claims, commitments, risks, dependencies, and state transitions.

4. IDENTIFY UNKNOWNS
   Keep only unknowns that could change a material commitment.

5. REDUCE HIGH-VALUE UNCERTAINTY
   Prefer direct inspection, authoritative sources, calculations, and tests.
   Use user questions when the user is the appropriate information/authorization source.
   Spawn agents when their role is distinct and their result could change the plan.

6. CONFRONT
   If the path is constrained: verify + hazard-check.
   If choices remain: independent option proposals + evidence comparison.
   Do not manufacture candidates.

7. ATTACK
   Independently analyze risk.
   For material selected commitments, run a post-selection adversarial pass.

8. RESOLVE
   Use constraints, verified evidence, tests, reasoning, reversibility/containment, and explicit preferences.
   Preserve unresolved or preference-dependent states.

9. ASSEMBLE
   Build an executable state-transition graph from resolved commitments.
   Every material action gets validation and containment.

10. TRANSITION-CHECK
    Test material state changes, partial completion, rollback failure, and downstream validity.

11. STOP
    Stop when the plan is decision-stable and remaining uncertainty is safely contained.

12. HAND OFF / EXECUTE
    Carry the relevant evidence, constraints, current state, and replan triggers.

13. REPLAN
    When reality invalidates a load-bearing premise or transition, replan the smallest affected subtree.
```

---

# 29. Agent spawning matrix

Use this as a practical shortcut.

| Situation | Agent | Why |
|---|---|---|
| Option space may be incomplete | Explorer | discover alternatives/framing errors |
| One fact can flip a material choice | Verifier | resolve a specific claim |
| Domain boundary is unfamiliar/high-risk | Specialist | expose domain-specific failure modes |
| Material candidate selected | Risk attacker | independent attack |
| Irreversible/cascading transition | Transition attacker | validate state/recovery logic |
| Several independent outputs exist | Integrator | reconcile without anchoring |

### A planner may spawn multiple agents

An agent should spawn additional agents only when it can state:

```text
purpose:
question:
why_current_context_is_insufficient:
expected_information_gain:
independence_mode:
stop_condition:
```

Example:

```yaml
spawn:
  purpose: "Test whether a critical environmental assumption is true."
  question: "Is feature X enabled on the actual target system?"
  why_current_context_is_insufficient: "The planning context has documentation but no system inspection."
  expected_information_gain: high
  independence:
    information: isolated
    method: meaningfully_different
    sources: independent
  stop_condition: "Return verified state or explicit inability to inspect."
```

Do not recursively spawn agents merely because another agent exists.

---

# 30. Recommended orchestration patterns

## Low consequence

```text
planner
  -> self-check
  -> plan
```

## Material uncertainty, one context

```text
planner
  -> staged explorer
  -> evidence verification
  -> staged critic
  -> plan
```

Label the result honestly. It is not genuinely independent.

## Material uncertainty with isolated agents

```text
              -> explorer A
planner ------> verifier
              -> explorer B

all independent outputs
         |
         v
     integrator
         |
         v
  risk attacker
         |
         v
      final plan
```

## High consequence

```text
planner
  |
  +--> independent hazard scan
  +--> independent option explorer A
  +--> independent option explorer B
  +--> domain specialist where justified
  |
  v
evidence / tests
  |
  v
integrator
  |
  +--> adversarial attacker
  +--> transition attacker
  |
  v
resolution + user/owner gates
  |
  v
state-transition plan
  |
  v
execution + observation + replan
```

The exact topology is optional. The epistemic separation is not.

---

# 31. Why v8 changes the underlying model

The central design shift is:

### v6

`decision -> candidate -> risk -> resolution -> action`

### v7

`commitment -> compulsion check -> candidate if needed -> adversarial pass -> calibrated resolution -> action`

### v8

`state + goal + constraints`
`-> materiality map`
`-> high-value unknown reduction`
`-> independent confrontation where choice exists`
`-> risk attack`
`-> resolution with explicit uncertainty`
`-> validated state transition`
`-> observation`
`-> replan`

This matters because the hardest planning failures are often not "the wrong candidate won."

They are:

- the wrong problem was framed;
- a critical world fact was assumed rather than observed;
- all agents shared the same blind spot;
- the apparent options were incomplete;
- a transition behaved differently from the assumed state;
- an irreversible action happened before the uncertainty was safely contained;
- a user's value judgment was silently guessed.

v8 puts those failure modes before candidate selection rather than trying to repair them after selection.

---

# 32. What v8 deliberately removes

The following are intentionally not retained as universal protocol rules:

- fixed candidate counts;
- fixed evidence counts;
- a universal evidence TTL;
- `high = compelled`;
- "silence = approval";
- a universal question quota;
- "ship at 80%";
- "most commitments are compelled";
- candidate generation quotas at each depth;
- model-family diversity as a proxy for factual independence;
- a requirement to produce an audit trail for low-stakes tasks.

These may still be useful local heuristics in a specific environment, but they should not be mistaken for general planning laws.

---

# 33. Self-test and calibration

This skill is itself a hypothesis.

Before deploying it as a default protocol for high-consequence work:

1. collect several real planning failures;
2. replay them through v8;
3. record which failures would actually have been caught;
4. measure added compute/time/questions;
5. inspect false positives and unnecessary work;
6. remove gates that do not change outcomes;
7. strengthen gates that repeatedly catch consequential failures.

Measure at least:

```text
failure_capture_rate
unnecessary_compute_rate
unresolved_unknowns_at_execution
replan_frequency
false_alarm_rate
user_interruptions
time_to_safe_commitment
```

The goal is not maximum process.

The goal is **better decisions per unit of attention, compute, and risk**.

---

# 34. One-sentence principle

> **Plan from state, not from prose: verify the facts that can change a material commitment, confront real alternatives from genuinely distinct perspectives, attack irreversible transitions independently, expose what remains uncertain, and let execution feed evidence back into the plan.**

---

# Appendix A — Minimal schemas

## A.1 Material commitment

```yaml
commitment:
  id: C1
  statement: "<commitment>"
  reason_material: "<what changes if this is wrong>"
  type: action | architecture | dependency | experiment | user_tradeoff
  constraints: []
  evidence: []
  risks: []
  status: constrained | supported | preference-dependent | experiment-gated | branch | unresolved | invalid
  robustness: robust | sensitive | contained
  actions: []
  revisit_if: []
```

## A.2 Risk

```yaml
risk:
  id: X1
  commitment_ref: C1
  scenario: "<failure scenario>"
  trigger: "<observable trigger>"
  consequence: low | material | high | critical
  detectability: low | medium | high
  prevention: []
  mitigation: []
  rollback_or_containment: "<specific>"
  residual: "<remaining exposure>"
```

## A.3 Evidence

```yaml
evidence:
  id: E1
  claim: "<claim>"
  status: verified | supported | derived | assumption | disputed | unknown
  source_type: user_statement | observation | primary_source | secondary_source | test | calculation | model_reasoning
  locator: "<locator>"
  checked_at: "<timestamp>"
  freshness: stable | low_volatility | volatile | unknown
  limitations: "<limitations>"
```

## A.4 Action

```yaml
action:
  id: A1
  origin:
    type: compelled | selected | derived | experiment | user_directed | conditional
    refs: []
  objective: "<objective>"
  preconditions: []
  execution: "<execution>"
  expected_result: "<observable result>"
  validation: "<acceptance test>"
  failure_signals: []
  rollback: "<specific or impossible>"
  consequence_if_not_rollbackable: "<consequence>"
  replan_trigger: []
  effort: low | medium | high
```

---

# Appendix B — Ready-to-use prompts

## B.1 Explorer

```text
You are an independent planning explorer.

Do not optimize the current draft.
Do not assume its framing is correct.
Do not see other agents' proposals.

Given:
  objective:
  target state:
  current state:
  hard constraints:
  invariants:
  known evidence:
  known unknowns:

Find:
  - materially different approaches;
  - missing assumptions;
  - hidden dependencies;
  - alternative problem framings;
  - experiments that could collapse uncertainty.

For each important finding:
  state what it could change;
  distinguish fact from hypothesis;
  identify what evidence would verify it.

Do not write the final plan.
```

## B.2 Verifier

```text
You are a verification agent.

Your task is to determine whether the following load-bearing claim is supported:

CLAIM:
<claim>

Use the strongest available method:
  direct inspection,
  authoritative source,
  reproducible test,
  recomputable calculation,
  or clearly attributed expert reasoning.

Return:
  status;
  evidence;
  exact locator;
  scope/date/version where relevant;
  limitations;
  contradictions;
  what remains unknown.

Never turn your own reasoning into evidence.
```

## B.3 Risk attacker

```text
You are an independent risk attacker.

Do not defend the proposed plan.
Do not use another agent's agreement as evidence.

Context:
  commitment:
  action:
  current state:
  hard constraints:
  invariants:
  verified facts:

Find:
  - hidden assumptions;
  - partial-completion failures;
  - rollback failures;
  - cascading state changes;
  - constraint violations;
  - dependency failures;
  - hostile or malformed conditions;
  - earliest observable failure signal.

For every material risk:
  trigger;
  consequence;
  detectability;
  prevention;
  mitigation;
  rollback/containment;
  residual risk.

State what finding would cause the plan to be reopened.
```

## B.4 Transition attacker

```text
You are a state-transition reviewer.

Given:
  current state S0
  action A1
  expected state S1
  failure handling
  next action A2

Check:
  - preconditions;
  - post-condition;
  - partial completion;
  - rollback failure;
  - recovery state;
  - invariant preservation;
  - whether A2 is still valid after each failure mode;
  - what newly learned information could invalidate A2.

Do not rewrite the plan unless necessary.
Return concrete defects and the minimal correction.
```

## B.5 Integrator

```text
You are integrating independent planning outputs.

Inputs:
  planning map
  verified evidence
  independent proposals
  independent hazard findings
  risk attacks
  user preferences
  hard constraints

Rules:
  - do not majority-vote;
  - do not turn model statements into evidence;
  - preserve contested claims;
  - preserve unresolved uncertainty;
  - prefer constraints, verified observations, tests, and primary evidence;
  - make preference-dependent trade-offs explicit;
  - mark derived actions as derived;
  - never invent approval.

For each material commitment:
  return status;
  rationale based on traceable inputs;
  robustness;
  what would reopen it.

Then assemble only the actions justified by those commitments.
```

---

# Appendix C — Final evaluator prompt

Use this as a last pass on the assembled plan.

```text
You are evaluating a proposed plan for epistemic and operational integrity.

Do not improve wording.
Do not reward length.
Do not infer missing facts.

Check:

1. Is the objective observable?
2. Are current state, constraints, invariants, and preferences separated?
3. Does every material unknown state what it can change?
4. Does every load-bearing claim have provenance?
5. Are agents being mistaken for evidence?
6. Are independence claims honest?
7. Was candidate generation justified rather than quota-driven?
8. Was the selected material path independently attacked?
9. Are irreversible transitions contained and gated where necessary?
10. Are user-dependent trade-offs explicit and authorized?
11. Does every material action have validation and failure handling?
12. Are replan triggers explicit?
13. Could another agent execute the plan without hidden context?
14. What single omitted issue is most likely to invalidate the plan?

Return:
  PASS;
  FAIL with concrete defects;
  or GATED with the exact missing condition.
```

---

# Appendix D — Practical rule of thumb

When uncertain about whether to add another agent, ask:

> **"Could this agent change what we do, or will it merely make the current story sound more convincing?"**

Only the first is a good reason to spend compute.
