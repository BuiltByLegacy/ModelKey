from __future__ import annotations

from modelkey.adapters.base import PartSummary, SessionHealth


class MockAdapter:
    """Deterministic adapter for development without Siemens NX."""

    def __init__(self, connected: bool = True) -> None:
        self.connected = connected

    def health(self) -> SessionHealth:
        if not self.connected:
            return SessionHealth(False, None, None, "Mock CAD session unavailable")
        return SessionHealth(
            True,
            "MOCK-NX-0.1",
            PartSummary(
                name="alpha_test.prt",
                full_path="/mock/alpha_test.prt",
                feature_count=3,
                expression_count=2,
                sketch_count=1,
            ),
            "Connected",
        )
