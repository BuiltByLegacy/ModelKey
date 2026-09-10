from __future__ import annotations

import json
from dataclasses import asdict

from modelkey.adapters.nx import NXAdapter


def main() -> None:
    """Run inside Siemens NX as a Python journal/script.

    Prints a compact JSON health payload suitable for the #2 manual acceptance test.
    """
    result = NXAdapter().health()
    print(json.dumps(asdict(result), indent=2))


if __name__ == "__main__":
    main()
