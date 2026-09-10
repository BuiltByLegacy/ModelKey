# ModelKey

**AI-assisted engineering review and automation for Siemens NX.**

ModelKey adds a controlled intelligence layer on top of Siemens NX using NX Open. The first product focus is model review: inspect a live NX part, run deterministic engineering best-practice rules, explain findings, and allow an engineer to approve safe fixes.

## Product principle

**The AI is not the compliance checker.**

Deterministic rules create findings from NX model data. The AI explains those findings, helps prioritize them, and proposes actions. Model-changing actions are constrained, auditable, explicitly approved, and revalidated after execution.

## Product progression

1. **ModelKey Review** — model health, sketches, expressions, feature dependencies, standards checks
2. **ModelKey Fix** — engineer-approved NX Open remediations
3. **ModelKey MBD** — PMI, datum, GD&T, manufacturing-definition readiness and standards assistance
4. **ModelKey Build** — controlled generative CAD through typed ModelKey actions

## Initial architecture

```text
Siemens NX
   |
   v
NX Open Adapter
   |
   v
Normalized Model Graph
   |----------------------|
   v                      v
Deterministic Rule Engine  AI Reasoning Layer
   |                      |
   v                      v
Findings + Evidence ---> Explanation / Proposed Actions
                               |
                               v
                         Engineer Approval
                               |
                               v
                          NX Open Safe Fix
                               |
                               v
                            Revalidate
```

## MVP

The first sellable capability is **AI Model Review for Siemens NX**.

The MVP should be able to:

- Attach to an active NX session
- Inspect the active part through NX Open
- Build a normalized model graph
- Detect underconstrained sketches
- Find hard-coded / unnamed controlling dimensions that should be expressions
- Detect duplicated controlling values and selected feature-tree/dependency issues
- Run customer-configurable standards rules
- Produce a model health score and actionable finding list
- Let the user ask questions about findings
- Execute a small set of safe fixes only after approval
- Re-run rules after model changes
- Perform an initial MBD-readiness review

## Example experience

> Review this model against our modeling and MBD standards.

ModelKey may report:

```text
MODEL HEALTH: 74/100

HIGH
- Sketch 7: underconstrained, 2 unresolved degrees of freedom
- Hole pattern uses six independent hole features instead of a pattern
- Datum B referenced by PMI but datum definition is incomplete

MEDIUM
- 14 unnamed dimensional expressions
- WALL_THICKNESS is represented by three independent values
- Extrude 22 depends on fragile downstream geometry

MBD
- 3 manufacturing features lack expected product definition
- 2 PMI objects are not associated with valid model geometry
```

Then the engineer can ask:

> Why is Sketch 7 unstable?

or:

> Convert the repeated wall-thickness dimensions into one named expression.

ModelKey proposes the action, the engineer approves it, NX Open performs the change, and ModelKey revalidates the model.

## Enterprise direction

ModelKey is intended to support restricted engineering environments. Review rules should remain usable without cloud AI. AI connectivity, outbound model context, redaction, tool permissions, approval policy, and audit logging must be configurable.

ModelKey should never require arbitrary OS control to modify NX. NX changes should occur through constrained NX Open operations.

## Current backlog

- #1 — Epic: ModelKey MVP — AI Model Review for Siemens NX
- #2 — NX Open connector
- #3 — Normalized model graph
- #4 — Deterministic rule engine
- #5 — Review experience
- #6 — Claude bridge
- #7 — Safe Fix engine
- #8 — MBD readiness checker
- #9 — Enterprise standards packs
- #10 — Enterprise security and audit model
- #11 — Generative CAD action protocol
- #12 — NX test corpus
- #13 — Commercialization plan
- #14 — Developer setup
- #16 — Initial rule catalog
- #17 — Scoring and release readiness

See `docs/ARCHITECTURE.md` and `docs/ROADMAP.md` for the implementation direction.