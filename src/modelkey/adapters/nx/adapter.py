from __future__ import annotations

import os
from typing import Any

from modelkey.adapters.base import PartSummary, SessionHealth


class NXUnavailableError(RuntimeError):
    """Raised when ModelKey is executed outside an NX Open Python runtime."""


class NXAdapter:
    """Read-only connector to the active Siemens NX session.

    For alpha development this adapter is intended to execute inside NX's
    Python/NX Open runtime. NXOpen is imported lazily so ModelKey core and its
    tests remain runnable on ordinary developer machines.
    """

    def __init__(self, session: Any | None = None) -> None:
        self._session = session

    def _get_session(self) -> Any:
        if self._session is not None:
            return self._session
        try:
            import NXOpen  # type: ignore
        except ImportError as exc:
            raise NXUnavailableError(
                "NXOpen is unavailable. Run the live connector from Siemens NX "
                "or inject a test session."
            ) from exc
        self._session = NXOpen.Session.GetSession()
        return self._session

    @staticmethod
    def _safe_len(collection: Any) -> int:
        try:
            return len(collection)
        except TypeError:
            return sum(1 for _ in collection)

    @staticmethod
    def _nx_version(session: Any) -> str | None:
        for key in ("UGII_FULL_VERSION", "UGII_VERSION"):
            try:
                value = session.GetEnvironmentVariableValue(key)
                if value:
                    return str(value)
            except Exception:
                value = os.environ.get(key)
                if value:
                    return value
        return None

    @staticmethod
    def _part_summary(part: Any) -> PartSummary:
        full_path = getattr(part, "FullPath", None) or None
        name = getattr(part, "Leaf", None) or getattr(part, "Name", None) or "<unnamed>"
        return PartSummary(
            name=str(name),
            full_path=str(full_path) if full_path else None,
            feature_count=NXAdapter._safe_len(part.Features),
            expression_count=NXAdapter._safe_len(part.Expressions),
            sketch_count=NXAdapter._safe_len(part.Sketches),
        )

    def health(self) -> SessionHealth:
        try:
            session = self._get_session()
        except NXUnavailableError as exc:
            return SessionHealth(False, None, None, str(exc))
        except Exception as exc:
            return SessionHealth(False, None, None, f"NX session error: {exc}")

        try:
            part = session.Parts.Work
            version = self._nx_version(session)
            if part is None:
                return SessionHealth(True, version, None, "Connected to NX; no work part is open")
            return SessionHealth(True, version, self._part_summary(part), "Connected")
        except Exception as exc:
            return SessionHealth(False, self._nx_version(session), None, f"NX interrogation error: {exc}")
