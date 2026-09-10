# ModelKey Alpha Test — Claude ↔ NX Open Closed Loop

## Purpose

The first ModelKey alpha does **not** attempt to compete with NX Check-Mate, Sketch Checker, PMI Advisor, DFM Advisor, or other native validation tools.

The alpha exists to prove the core product thesis:

> A user can talk to Claude about the Siemens NX model currently open on their workstation, Claude can retrieve structured model state through ModelKey/NX Open, Claude can request a constrained model change, NX performs the change, and ModelKey verifies the result back to Claude.

## Alpha architecture

```text
User
  |
  v
Claude
  |
  | structured ModelKey tool calls
  v
ModelKey Bridge
  |
  v
ModelKey NX Adapter
  |
  v
NX Open
  |
  v
Siemens NX
  |
  | verified model state / operation result
  +-------------------------------> Claude
```

## Alpha test scenario

### Preconditions
- Siemens NX installed and licensed for the required NX Open workflow
- A disposable test `.prt` is open
- Test part contains at least one named dimensional expression, for example `LENGTH = 100 mm`
- ModelKey bridge is running
- Claude has access only to the explicit ModelKey tool set

### Step 1 — Connection
Claude calls `get_active_part()`.

Expected result:
- NX version
- active part name/path or safe identifier
- connection status

### Step 2 — Read model state
Claude calls read-only tools such as:
- `get_features()`
- `get_expressions()`
- `get_sketches()`

User prompt example:

> What is in the model I currently have open?

Expected result:
Claude describes the active NX model using actual structured NX data rather than screenshots or guessed state.

### Step 3 — Request one controlled change
User prompt example:

> Change LENGTH from 100 mm to 125 mm.

Claude proposes a typed ModelKey action:

```text
set_expression(name="LENGTH", value=125, unit="mm")
```

Expected behavior:
- ModelKey validates the target expression and value
- ModelKey shows/provides the intended change for approval
- No arbitrary Python, shell, mouse, keyboard, or OS command is accepted

### Step 4 — Execute through NX Open
After approval, ModelKey modifies the expression through NX Open and updates/regenerates the part.

Expected result:
- old value captured
- new value applied
- NX update completes without error

### Step 5 — Verify
ModelKey reads the expression and model state again.

Expected result returned to Claude:

```text
success: true
expression: LENGTH
old_value: 100 mm
new_value: 125 mm
update_status: successful
verified: true
```

Claude confirms completion to the user only after verification.

## Alpha pass criteria

The alpha passes only if all of the following are true:

- Claude can identify the active NX part through ModelKey
- Claude can retrieve structured model information from NX
- Claude can answer a natural-language question using that real model state
- Claude can request a constrained change to one named expression
- NX performs the change through NX Open
- ModelKey verifies the updated value after regeneration
- The full read → reason → act → verify loop is logged
- No UI automation or arbitrary OS execution is required

## Alpha fail conditions

The alpha is not considered successful if:
- model state is inferred from screenshots instead of NX Open data
- the user must manually copy generated code into NX for every operation
- Claude can execute arbitrary code on the workstation
- ModelKey cannot verify whether the requested change actually succeeded
- changing a named expression requires rebuilding the part rather than updating the existing parametric model

## What this proves

Successful completion proves the fundamental ModelKey product architecture: Claude can be connected to Siemens NX as a controlled engineering agent.

It does **not** prove production readiness, enterprise security, MBD automation, best-practice review, or broad generative CAD. Those become applications built on top of the proven connection.

## After alpha

Expand in this order:

1. richer read-only model interrogation
2. additional safe expression operations
3. feature/dependency interrogation
4. selected modeling actions
5. native NX validation-result ingestion
6. model review/root-cause reasoning
7. MBD copilot
8. broader generative CAD
