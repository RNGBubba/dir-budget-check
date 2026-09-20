"""Directory size measurement and budget enforcement."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


class BudgetExceeded(ValueError):
    """Raised when measured bytes exceed the configured budget."""


@dataclass(frozen=True)
class BudgetReport:
    """Measured regular-file bytes under a directory."""

    directory: Path
    total_bytes: int
    budget_bytes: int
    files: int

    @property
    def exceeded(self) -> bool:
        return self.total_bytes > self.budget_bytes


def measure_directory(directory: Path, budget_bytes: int) -> BudgetReport:
    """Return recursive regular-file bytes and whether the budget is exceeded."""
    directory = Path(directory)
    if budget_bytes < 0:
        raise ValueError("budget must be >= 0")
    if not directory.is_dir():
        raise NotADirectoryError(f"{directory} is not a directory")

    total = 0
    files = 0
    for path in directory.rglob("*"):
        if path.is_file() and not path.is_symlink():
            total += path.stat().st_size
            files += 1
    return BudgetReport(directory, total, budget_bytes, files)
