from pathlib import Path

import pytest

from dirbudget.core import BudgetExceeded, measure_directory


def test_measure_directory_sums_regular_files_recursively(tmp_path: Path) -> None:
    (tmp_path / "top.txt").write_bytes(b"abc")
    nested = tmp_path / "nested"
    nested.mkdir()
    (nested / "bottom.bin").write_bytes(b"12345")

    report = measure_directory(tmp_path, 10)

    assert report.total_bytes == 8
    assert report.budget_bytes == 10
    assert report.files == 2
    assert report.exceeded is False


def test_measure_directory_reports_budget_exceeded(tmp_path: Path) -> None:
    (tmp_path / "payload.bin").write_bytes(b"0123456789")

    report = measure_directory(tmp_path, 5)

    assert report.exceeded is True
    assert report.total_bytes == 10
    assert report.budget_bytes == 5


def test_measure_directory_rejects_negative_budget(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="budget"):
        measure_directory(tmp_path, -1)


def test_measure_directory_rejects_non_directory(tmp_path: Path) -> None:
    target = tmp_path / "file"
    target.write_text("content")

    with pytest.raises(NotADirectoryError):
        measure_directory(target, 10)
