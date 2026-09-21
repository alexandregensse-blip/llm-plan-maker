# plan-suite v13 — State-Driven Containment Loop

Generic planning skill for LLM agents. Vendor-neutral. Single file.

---

## 0. Core Principle

Planning is not a document; it is a state machine. You are navigating from a `Verified Current State` to an `Observable Target State`. 
Do not hallucinate long branches of execution past the fog of war. Do not write lengthy risk ledgers. Spend tokens exclusively on verifying the environment, containing irreversible actions, and moving forward.

---

## 1. Triage (The Only Gate)

Before writing any plan, answer two questions based strictly on the user's prompt:

**Q1: Can the next required action go wrong in a way I cannot cheaply and certainly undo?**
- **No (Reversible):** Do not write a plan artifact. Just act, use your tools, or answer the user directly.
- **Yes (Commitment):** The action is irreversible or highly consequential. Proceed to Q2.

**Q2: How well is this territory known?**
- **Known Path:** Runbooks, documented APIs, standard migrations. The environment is predictable. Write a sequential plan (§4).
- **Frontier Work:** The outcome of Step 1 dictates the existence of Step 2. Do not write a sequence. Write an execution loop (§3).

---

## 2. The Compulsion Check (Execution over Deliberation)

Before generating options or debating paths, apply the Compulsion Check:
> **Do the currently verified facts + hard constraints leave exactly ONE viable technical path?**

- **Yes:** Take it immediately. Zero candidates, zero debate. Deliberating a compelled answer is hallucinated rigor.
- **No, because facts are missing:** Your next action is Discovery (read a file, ping an API, search docs).
- **No, because of user preference:** Stop. Ask the user for a priority (e.g., speed vs. cost). Do not guess preferences.

---

## 3. The Frontier Loop (For Unknown Environments)

When working in the fog of war, you maintain a living state, not a static document. Update this internally before each material action:

```text
Target:       <observable success condition>
Invariants:   <hard limits, e.g., "Do not delete DB">
State:        <facts verified EXCLUSIVELY by tool observation, not memory>
Next Step:    <Action -> Expected Tool Output -> Rollback Plan>
```

**Execution Loop:**
1. Execute `Next Step`.
2. Did the tool output match `Expected Tool Output`?
   - **Yes:** Advance state. Determine the new `Next Step`.
   - **No:** STOP. Do not compound errors. Revert if possible. Re-evaluate `State`.

---

## 4. The Sequence (For Known Paths Only)

If the path is solved and the user requires a plan artifact before execution (or if handing off to another agent), emit this minimal contract. 

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
*Rule: If you find yourself writing "Step 5" but realize its parameters depend entirely on the output of "Step 2", you are hallucinating. Delete Steps 3-5 and revert to the Frontier Loop (§3).*

---

## 5. Absolute Epistemic Hygiene

1. **Tools over Memory:** "Verified" means you ran a command or read a source. Your internal training data or assumptions are NEVER treated as verified state.
2. **Containment over Confidence:** If a step is irreversible (e.g., dropping a table, spending money, sending an email) and cannot be contained, it MUST hit a hard gate (User Oracle). Silence from the user is never approval. 
3. **No Phantom Steps:** Mechanical consequences of a step (e.g., "Check if the server restarted successfully") are part of the original action's validation, not separate planning steps.

---

## 6. When to Abandon this Protocol

If the user asks a factual question, requests a script, or wants an explanation: drop this protocol entirely. Serve the user directly. A planning loop applied to a simple Q&A is a failure of the system.
