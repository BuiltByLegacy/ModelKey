# ModelKey Architecture

## Objective

ModelKey connects Siemens NX to a deterministic engineering review engine and an optional AI reasoning layer. NX Open is the authoritative integration surface for reading and changing NX models.

## Core components

### 1. NX Open adapter
Runs with access to the active NX session and is responsible for:
- Session/work-part discovery
- Read-only model interrogation
- Object identity mapping
- Approved NX write operations
- Update/regeneration status
- NX error reporting

### 2. Normalized model graph
Transforms NX-specific objects into a stable ModelKey schema containing:
- Parts
- Bodies
- Features and feature order
- Sketches and constraint state
- Expressions and dimensions
- Parent/child dependencies
- Datums and coordinate systems
- PMI/MBD objects and associations
- Model errors/status

The rest of ModelKey should depend on this schema rather than raw NX Open objects whenever practical.

### 3. Deterministic rule engine
Evaluates the model graph using explicit versioned rules. Rules produce findings with:
- Rule ID/version
- Severity
- Category
- NX/model object references
- Evidence
- Rationale
- Remediation class
- Auto-fix eligibility
- Release-blocking status where configured

Examples include underconstrained sketches, unnamed controlling expressions, duplicated controls, fragile dependencies, failed features, datum requirements, and MBD completeness checks.

### 4. Standards packs
Customer-specific, versioned configuration defines modeling and MBD expectations without modifying core engine code. Rule execution and review reports record the exact standards-pack version used.

### 5. AI reasoning layer
Optional. Receives only approved normalized model context and deterministic findings. Responsibilities:
- Explain findings
- Answer questions about model structure and rules
- Prioritize remediation
- Propose constrained ModelKey actions

The AI must not invent pass/fail compliance results independently of the rule engine.

### 6. Safe Fix engine
Executes typed, allowlisted write operations only after engineer approval. Each fix follows:
1. Plan
2. Preview
3. Approval
4. Capture pre-change state
5. NX Open execution
6. NX update/regeneration
7. Re-extract affected state
8. Re-run applicable rules
9. Report result and audit record

### 7. Review UX
Initial UX should support:
- Run Review
- Model health/release readiness
- Findings by severity and category
- Navigate/highlight affected NX objects
- Explain finding
- Preview/approve fix
- Compare before/after review state
- Export report

## Data flow

```text
NX Session
  -> NX Open Adapter
  -> Normalized Model Graph
  -> Deterministic Rule Engine
  -> Findings + Evidence
      -> Review UI
      -> Optional AI Reasoning
           -> Proposed typed action
           -> Engineer approval
           -> Safe Fix Engine
           -> NX Open Adapter
           -> NX
           -> Revalidation
```

## Security principles

- Core review must function without cloud AI.
- No arbitrary shell/OS control is required for NX modeling.
- AI actions are constrained to an allowlist of typed ModelKey operations.
- Outbound model context must be configurable and minimizable.
- Support redaction/sanitization for enterprise environments.
- Secrets must stay outside source control.
- Every write action must be attributable and auditable.
- Restricted-network/offline deployments should retain deterministic review capability.

## Initial implementation direction

Python is the preferred prototype language for the ModelKey core and initial NX Open exploration because it enables rapid iteration. Keep boundaries clean enough that NX-specific runtime constraints can later move to C# or another supported NX Open language without redesigning the rule engine.

Suggested package boundaries:

```text
modelkey/
  adapters/
    nx/
    mock/
  model/
  rules/
  standards/
  review/
  ai/
  actions/
  audit/
  reporting/
```

## Long-term CAD abstraction

ModelKey should avoid making the product synonymous with one AI provider or raw NX Open. The normalized model graph and typed action protocol are the abstraction boundaries that can eventually allow additional CAD systems or AI providers while keeping NX as the first and deepest integration.