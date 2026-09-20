from pathlib import Path

from dirbudget.cli import main


def test_cli_returns_failure_and_reports_over_budget(tmp_path: Path, capsys) -> None:
    (tmp_path / "artifact").write_bytes(b"123456")

    exit_code = main([str(tmp_path), "--max-bytes", "5"])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert '"exceeded": true' in captured.out


def test_cli_returns_success_at_budget(tmp_path: Path, capsys) -> None:
    (tmp_path / "artifact").write_bytes(b"12345")

    exit_code = main([str(tmp_path), "--max-bytes", "5"])

    assert exit_code == 0
    assert '"exceeded": false' in capsys.readouterr().out


def test_cli_rejects_missing_directory(tmp_path: Path, capsys) -> None:
    exit_code = main([str(tmp_path / "missing"), "--max-bytes", "5"])

    assert exit_code == 2
    assert "not a directory" in capsys.readouterr().err
