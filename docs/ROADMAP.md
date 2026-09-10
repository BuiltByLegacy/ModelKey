# ModelKey Roadmap

## Product sequence

ModelKey should progress in four major product layers:

1. **Review** — understand and score existing NX models
2. **Fix** — execute safe engineer-approved remediations
3. **MBD** — evaluate and assist model-based definition readiness
4. **Build** — create and modify geometry through constrained AI actions

The sequence is intentional. Review provides the model understanding, evidence, standards engine, safety model, and trust needed before more autonomous write capabilities are introduced.

## Phase 0 — Foundation

Primary issues: #14, #15

Goals:
- Establish Python project structure
- Document NX Open development workflow
- Add mock NX adapter
- Create logging/configuration/test harness
- Lock product architecture and safety principles

Exit criteria:
- Core package runs without NX
- Mock fixtures can exercise model graph and rule-engine tests
- NX-specific runtime setup is documented

## Phase 1 — ModelKey Review alpha

Primary issues: #2, #3, #4, #12, #16, #17

Goals:
- Connect to active NX session
- Extract a normalized model graph
- Establish first deterministic rule catalog
- Detect underconstrained sketches
- Detect expression/modeling anti-patterns
- Detect selected feature dependency / model-quality problems
- Create known-good and intentionally flawed validation parts
- Produce deterministic model health and release-readiness results

Exit criteria:
- Open an NX part and run review successfully
- Expected findings match test-corpus ground truth
- Same input produces same results
- Findings trace back to NX objects

## Phase 2 — Review UX + AI explanation

Primary issues: #5, #6

Goals:
- ModelKey review panel/workflow
- Findings grouped by severity/category
- Navigate/highlight affected NX objects
- Ask questions about findings
- Claude explains deterministic evidence and proposes remediation
- Record AI interactions and tool proposals for traceability

Exit criteria:
- Engineer can complete a useful model review without leaving the workflow
- AI explanation is grounded in actual model/rule evidence
- AI cannot silently modify NX

## Phase 3 — ModelKey Fix

Primary issue: #7

Goals:
- Preview/approve/write/revalidate loop
- Expression cleanup
- Selected naming-standard fixes
- Safe shared-expression conversions
- Simple unambiguous sketch corrections

Exit criteria:
- At least three remediation classes work end-to-end
- Every fix is approved, logged, and revalidated
- Failed writes produce a clear recovery state

## Phase 4 — Enterprise standards

Primary issues: #9, #10

Goals:
- Versioned customer standards packs
- Customer rule enablement/severity/threshold configuration
- Data minimization and redaction
- Local/offline deterministic review mode
- Tool allowlists and audit records
- Restricted-network deployment definition

Exit criteria:
- A pilot customer can load a controlled company standards pack
- Review remains useful without cloud AI
- Model-changing actions and outbound AI context are governed and auditable

## Phase 5 — ModelKey MBD

Primary issue: #8

Goals:
- PMI inventory and association review
- Datum and datum-reference checks
- Missing-definition detection
- Duplicate/conflicting PMI detection
- Customer MBD standards hooks
- AI explanations and proposed MBD remediation

Future expansion:
- Feature recognition for product-definition expectations
- GD&T assistance
- Automated PMI authoring under explicit approval
- Downstream manufacturing/inspection readiness

Exit criteria:
- ModelKey can produce a deterministic MBD-readiness report with evidence linked to NX objects

## Phase 6 — ModelKey Build

Primary issue: #11

Goals:
- Typed ModelKey CAD Action Protocol
- Plan/preview/approval flow
- Core modeling operations through NX Open
- Post-action update and review

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
- Result is revalidated by ModelKey Review

## Commercial path

Primary issue: #13

Initial packaging hypothesis:
- **ModelKey Review** — core product
- **ModelKey Fix** — automation tier
- **ModelKey MBD** — premium MBD/PMI module
- **ModelKey Build** — advanced AI CAD authoring module

A first customer pilot should focus on measurable outcomes such as review-time reduction, standards adherence, defect/finding detection, model cleanup time, and reduction in release/rework loops.

## Immediate implementation order

Recommended first engineering sequence:

**#14 → #2 → #3 → #16/#4 → #12 → #17 → #5 → #6 → #7**

MBD (#8) can begin once #3 and #4 provide enough model/PMI structure to support reliable checks.