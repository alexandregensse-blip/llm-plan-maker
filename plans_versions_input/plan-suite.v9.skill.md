# plan-suite v9 — Execution-Driven Empiricism (Radical Empiricism)

Generic planning skill for LLM agents. Vendor-neutral.
Designed to eliminate procedural bloat, LLM echo-chambers, and the illusion of perfect foresight.

---

## 1. Core Philosophy: The Map is Not the Territory

Previous versions of this skill attempted to pre-compute complex state-transition graphs and simulate adversarial attacks internally. This fails because LLMs are poor physics engines and cannot simulate complex reality over multiple steps.

**The v9 Invariants:**
1. **No Circular Epistemology:** An LLM cannot verify its own assumptions. Another agent from the same model family is NOT an independent verifier. Only the external environment (tools, terminal, API, web) or the user can verify a fact.
2. **The Fog of War:** You cannot accurately plan step 5 if the outcome of step 2 is uncertain. Do not hallucinate long execution branches.
3. **Execution is the Best Planner:** Resolve uncertainty by executing the smallest, safest, observable action. 
4. **Zero Bureaucracy:** Spend tokens on thinking and acting, not on formatting massive YAML ledgers.

---

## 2. Triage: Are we planning or just acting?

Ask yourself: *Is the next required action irreversible or highly consequential?*

* **NO (Trivial/Reversible):** Do not write a plan. Just use your tools or provide the answer.
* **YES (Material/Irreversible):** Use the v9 Empirical Protocol.

---

## 3. The Empirical Protocol

Instead of generating a massive up-front plan, you will maintain only two living concepts: **The Horizon** and **The Immediate Frontier**.

### Step A: Define the Horizon
Before taking any action, establish the non-negotiables. Keep this extremely brief.
* **Target State:** What is the exact observable condition of success?
* **Hard Invariants:** What must absolutely NOT happen? (e.g., "Do not delete production data", "Do not spend more than $50").
* **Current Known State:** What facts have been strictly verified by *external tools* (not by your training data)?

### Step B: Identify the Immediate Frontier (The Next Action)
Do not plan the whole path. Identify ONLY the very next material step required to move towards the Target State. 

Ask: *Do we have 100% empirical certainty to take this step?*
* **If NO:** Your next action is a **Discovery Action**. (e.g., Read a file, ping a server, ask the user).
* **If YES:** Your next action is a **Commitment Action**.

### Step C: The Action Contract
For the single next step you are about to take, you must internally define:
1. **The Action:** What tool/command are you running?
2. **The Observable Expectation:** What exact string, status code, or state change do you expect to see?
3. **The Containment (If Commitment):** If this fails, how do I instantly revert it or stop cascading damage?

### Step D: Execute and Observe
Execute the single step. 
* Did the environment react as expected? Proceed to the next Frontier.
* Did the environment react differently? **Stop.** Re-evaluate the Horizon. 

---

## 4. The User Oracle Rule

When you encounter a trade-off between two viable paths (e.g., Speed vs. Cost, Risk vs. Quality) that cannot be resolved by empirical tool use, **STOP**. 

Do not guess the user's preference. Do not spawn a "risk attacker agent" to debate it. 
Emit a direct, one-line question to the user outlining the tradeoff and your recommended default, then wait.

---

## 5. Output Format (L2/L3 Tasks)

Forget the massive audit trails and YAML sidecars. Your output should reflect continuous execution, not static bureaucracy.

Use this format in your scratchpad or visible thought process before executing an irreversible step:

```text
# Horizon
Target: [Observable goal]
Invariants: [Hard limits]

# The Frontier (Next Action)
Intent: [What we are about to do]
Status: [Discovery | Commitment]
Empirical Check: [What exact tool/observation validates this?]
Containment: [Reversible? Yes/No. If No, what is the mitigation?]

[Execute action via tools...]
