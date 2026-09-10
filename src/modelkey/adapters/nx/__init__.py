"""Siemens NX adapter package.

Importing this module outside NX is safe. NXOpen is imported lazily by NXAdapter.
"""

from modelkey.adapters.nx.adapter import NXAdapter, NXUnavailableError

__all__ = ["NXAdapter", "NXUnavailableError"]
