# Developer Setup

## Core development without NX

ModelKey core must remain testable without Siemens NX installed.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e '.[dev]'
pytest -q
```

The `MockAdapter` and injected-session NX adapter tests let contributors develop the bridge contracts and model logic without launching NX.

## Runtime configuration

Optional environment variables:

- `MODELKEY_LOG_LEVEL` — defaults to `INFO`
- `MODELKEY_ENV` — defaults to `development`

Do not commit API keys, NX credentials, customer data, or `.env` files.

## Siemens NX / NX Open alpha setup

The first live connector is deliberately in-process: `NXAdapter` runs from an NX Python/NX Open runtime and calls `NXOpen.Session.GetSession()`.

This avoids relying on unsupported external-process attachment behavior during the alpha.

### Live smoke test

1. Use a disposable test part in NX.
2. Ensure the ModelKey `src` directory is available on the Python import path used by the NX journal environment.
3. Run `src/modelkey/adapters/nx/probe.py` as an NX Python journal/script.
4. Confirm it prints JSON containing:
   - `connected: true`
   - NX version when available
   - active work-part name/path
   - feature count
   - expression count
   - sketch count
5. Close the work part and rerun; the connector should remain connected and report that no work part is open.

Example shape:

```json
{
  "connected": true,
  "nx_version": "...",
  "active_part": {
    "name": "alpha_test.prt",
    "full_path": "...",
    "feature_count": 3,
    "expression_count": 2,
    "sketch_count": 1
  },
  "message": "Connected"
}
```

## Architecture boundary

NX-specific code belongs under `modelkey.adapters.nx`. Core ModelKey logic should consume normalized dataclasses/protocols rather than raw NX Open objects. This is required so tests can run outside NX and so future bridge implementations can change without rewriting the rest of ModelKey.

## Next step after #2

Issue #6 should expose this read-only session/part state to Claude through the constrained ModelKey tool interface. Write operations such as `set_expression` remain outside #2 and are validated in the #22 alpha closed-loop test.
