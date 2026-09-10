from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class PartSummary:
    name: str
    full_path: str | None
    feature_count: int
    expression_count: int
    sketch_count: int


@dataclass(frozen=True)
class SessionHealth:
    connected: bool
    nx_version: str | None
    active_part: PartSummary | None
    message: str


class CadAdapter(Protocol):
    """Minimal read-only adapter contract used by ModelKey core."""

    def health(self) -> SessionHealth: ...
