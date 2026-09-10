# ModelKey Roadmap

## Product sequence

ModelKey starts by proving the **Claude ↔ NX connection**, then builds higher-level products on top of that foundation:

1. **Connect** — Claude reads, reasons about, acts on, and verifies a live NX model through NX Open
2. **Review** — consume NX model state and native validation results; correlate and explain findings
3. **Fix** — execute safe engineer-approved remediations
4. **MBD** — assist PMI/GD&T/MBD workflows using NX capabilities plus ModelKey reasoning
5. **Build** — create and modify geometry through constrained AI actions

The immediate priority is not to recreate native NX checkers. The alpha must first prove that Claude can safely interact with the active NX model through a constrained ModelKey tool layer.

## Phase 0 — Foundation

Primary issues: #14, #2, #6

Goals:
- Establish Python project structure
- Document NX Open development workflow
- Build the local ModelKey bridge
- Connect Claude to explicit ModelKey tools
- Add logging/configuration/test harness

Exit criteria:
- ModelKey can attach to an active NX session
- Claude can invoke a read-only ModelKey tool
- Tool calls are logged and constrained

## Phase 1 — Claude ↔ NX alpha

Reference: `docs/ALPHA_TEST.md`

Goals:
- `get_active_part()` returns the live NX part
- `get_features()`, `get_expressions()`, and `get_sketches()` return structured model state
- Claude can answer: `What is in the model I currently have open?`
- Claude can propose `set_expression(name, value, unit)`
- Engineer approval is required before write execution
- NX Open changes one named expression in a disposable test part
- NX regenerates successfully
- ModelKey rereads the expression and verifies the result back to Claude

Exit criteria:
- End-to-end **read → reason → act → verify** loop succeeds
- No screenshots, mouse/keyboard automation, arbitrary shell, or arbitrary Python execution are required
- User does not need to manually copy generated code into NX for every command

This is the first major product proof point.

## Phase 2 — Rich model interrogation

Primary issue: #3

Goals:
- Normalize features, sketches, expressions, dependencies, datums, bodies, PMI, and errors
- Preserve traceability back to NX objects
- Make model context compact enough for AI use
- Add dependency/root-cause graph support

Exit criteria:
- Claude can answer useful engineering questions about how a model is constructed and what depends on what

## Phase 3 — Native NX validation orchestration + Review

Primary issues: #4, #5, #12, #16, #17

Goals:
- Reuse native NX validation where available instead of duplicating it
- Ingest/normalize relevant outputs from Check-Mate, sketch state, PMI/MBD tools, and other available validation APIs
- Add only ModelKey-specific deterministic rules where NX has a real gap
- Correlate multiple findings to likely root causes
- Produce model health/release-readiness views
- Create known-good and intentionally flawed validation parts

Exit criteria:
- ModelKey explains and prioritizes real NX/model findings with evidence
- Multiple downstream findings can be correlated to a shared model dependency/root cause

## Phase 4 — ModelKey Fix

Primary issue: #7

Goals:
- Preview/approve/write/revalidate loop
- Expression cleanup
- Selected naming-standard fixes
- Safe shared-expression conversions
- Other typed NX Open remediations

Exit criteria:
- At least three remediation classes work end-to-end
- Every fix is approved, logged, and verified

## Phase 5 — Enterprise standards and security

Primary issues: #9, #10

Goals:
- Versioned customer standards packs
- Company knowledge/context support
- Data minimization/redaction
- Local/offline deterministic operation where possible
- Tool allowlists and audit records
- Restricted-network deployment definition

Exit criteria:
- A pilot customer can govern what data leaves the workstation and what actions Claude is allowed to invoke

## Phase 6 — ModelKey MBD

Primary issue: #8

Goals:
- Build an MBD copilot around existing NX PMI/MBD capabilities rather than recreate them
- Inspect PMI inventory/association, datums, feature definition, and native validation results
- Explain incomplete or conflicting product definition
- Propose approved MBD remediation

Future expansion:
- GD&T assistance
- Automated PMI authoring under explicit approval
- Manufacturing/inspection readiness orchestration

Exit criteria:
- Claude can discuss the actual NX product definition and guide an engineer through an evidence-based MBD release workflow

## Phase 7 — ModelKey Build

Primary issue: #11

Goals:
- Typed ModelKey CAD Action Protocol
- Plan/preview/approval flow
- Core modeling operations through NX Open
- Post-action update and verification

Initial action set:
- new/open/save part
- create/set expression
- create sketch
- rectangle/circle
- extrude/cut
- hole
- fillet/chamfer
- update model
- export STEP

Exit criteria:
- Natural-language request can be translated into a constrained action plan
- Approved plan modifies NX through NX Open
- Result is verified before Claude reports success

## Commercial path

Primary issue: #13

Initial packaging hypothesis:
- **ModelKey Connect** — Claude ↔ NX bridge and model interrogation
- **ModelKey Review** — native validation orchestration and engineering reasoning
- **ModelKey Fix** — automation/remediation tier
- **ModelKey MBD** — premium MBD/PMI module
- **ModelKey Build** — advanced AI CAD authoring module

## Immediate implementation order

The priority sequence is now:

**#14 → #2 → #6 → Alpha closed-loop test → #3 → Review/validation work**

Do not invest heavily in review-rule duplication until the Claude ↔ NX alpha passes.