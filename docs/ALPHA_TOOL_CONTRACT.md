# ModelKey Alpha Tool Contract

The alpha exposes only a minimal, typed tool surface to Claude.

## Read tools

### get_active_part
Returns connection status, NX version, active part identifier/name, and basic metadata.

### get_features
Returns a compact ordered feature summary for the active part.

### get_expressions
Returns named expressions, values, units, and identifiers needed for later write targeting.

### get_sketches
Returns a compact sketch summary including name/ID and constraint status where available.

## Write tool

### set_expression
Typed input:

```text
name: string
value: number
unit: approved engineering unit
```

Behavior:
- validate expression exists
- capture old value
- validate unit/value
- require explicit approval
- execute through NX Open
- update/regenerate NX
- reread expression
- return verified result

## Prohibited in alpha

Claude is not given tools for:
- arbitrary Python execution
- shell/PowerShell/cmd execution
- filesystem traversal unrelated to approved model operations
- mouse/keyboard automation
- arbitrary NX Open method invocation
- arbitrary code evaluation

## Result contract

Every write result should return enough structured evidence for Claude to distinguish requested, attempted, successful, and verified states.

Example:

```text
success: true
verified: true
action: set_expression
target: LENGTH
old_value: 100
new_value: 125
unit: mm
nx_update_status: successful
errors: []
```
