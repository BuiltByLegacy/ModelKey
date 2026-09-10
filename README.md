# ModelKey

**Connect Claude to Siemens NX through a controlled NX Open bridge.**

ModelKey gives Claude structured, auditable access to the Siemens NX model currently open on an engineer's workstation. Claude can inspect real model state, reason about it, propose constrained actions, execute approved changes through NX Open, and verify the result.

## Core product thesis

ModelKey is **not** intended to replace native NX capabilities such as Check-Mate, Sketch Checker, PMI Advisor, DFM Advisor, or NX Inspector.

The core product is the connection layer:

```text
Claude ↔ ModelKey Bridge ↔ ModelKey NX Adapter ↔ NX Open ↔ Siemens NX
```

Once that connection is reliable, ModelKey can support higher-level applications such as:

- Ask Claude questions about the active NX model
- Read features, sketches, expressions, dependencies, PMI, and validation results
- Explain modeling problems and likely root causes
- Modify approved parameters and features
- Orchestrate native NX review/validation tools
- Assist with MBD and PMI workflows
- Perform controlled generative CAD actions

## Product principle

**Claude reasons; ModelKey constrains and verifies.**

Claude should never need arbitrary OS control, UI automation, or unrestricted code execution to modify NX. Model-changing actions must use typed ModelKey operations executed through NX Open. Writes are approved, logged, and verified after NX updates.

## First alpha

The first ModelKey alpha is deliberately small:

1. Open a disposable NX part with a named expression such as `LENGTH = 100 mm`.
2. Claude calls ModelKey and identifies the active part.
3. Claude retrieves structured features/expressions/sketch state.
4. The user asks: `What is in the model I currently have open?`
5. The user asks: `Change LENGTH to 125 mm.`
6. Claude proposes a typed `set_expression(...)` action.
7. After approval, ModelKey executes the change through NX Open.
8. NX regenerates.
9. ModelKey reads the expression again and verifies `LENGTH = 125 mm`.
10. Claude confirms completion only after verification.

Passing this test proves the fundamental product architecture: **Claude can read, act on, and verify a live Siemens NX model through ModelKey.**

See `docs/ALPHA_TEST.md` for the complete alpha procedure and pass/fail criteria.

## Product progression

1. **ModelKey Connect** — Claude ↔ NX read/reason/act/verify bridge
2. **ModelKey Review** — consume NX model state and native validation results; correlate and explain findings
3. **ModelKey Fix** — engineer-approved NX Open remediations
4. **ModelKey MBD** — PMI/GD&T/MBD copilot built on NX capabilities and ModelKey reasoning
5. **ModelKey Build** — controlled generative CAD through typed ModelKey actions

## Architecture direction

```text
Siemens NX
   |
   v
NX Open Adapter
   |
   v
Normalized Model State / Model Graph
   |
   +---------------------> ModelKey Read Tools
   |
   +---------------------> Native NX Validation Adapters
   |
   v
ModelKey Bridge
   |
   v
Claude
   |
   v
Proposed Typed Action
   |
   v
Engineer Approval
   |
   v
NX Open Write Operation
   |
   v
NX Update / Regenerate
   |
   v
Verification back to Claude
```

## Native NX capability strategy

ModelKey should reuse existing NX capabilities where they already solve the deterministic problem. We should ingest and reason over native results rather than recreate them unnecessarily.

Likely native integrations include:

- Check-Mate
- Sketch Checker / sketch state
- PMI Advisor
- MBD logical rules
- DFM Advisor
- NX Inspector / model-based characteristics

ModelKey's differentiation is the conversational engineering layer, cross-feature/root-cause reasoning, orchestration, safe actions, company-knowledge context, and closed-loop verification.

## Enterprise direction

ModelKey is intended to support restricted engineering environments. Review and local interrogation should remain useful without cloud AI where possible. AI connectivity, outbound model context, redaction, tool permissions, approval policy, and audit logging must be configurable.

## Current backlog

- #1 — Epic: ModelKey MVP — AI Model Review for Siemens NX
- #2 — NX Open connector
- #3 — Normalized model graph
- #4 — Deterministic rule engine / native validation strategy
- #5 — Review experience
- #6 — Claude bridge
- #7 — Safe Fix engine
- #8 — MBD readiness / copilot foundation
- #9 — Enterprise standards packs
- #10 — Enterprise security and audit model
- #11 — Generative CAD action protocol
- #12 — NX test corpus
- #13 — Commercialization plan
- #14 — Developer setup
- #16 — Initial rule catalog
- #17 — Scoring and release readiness

See `docs/ARCHITECTURE.md`, `docs/ROADMAP.md`, and `docs/ALPHA_TEST.md`.