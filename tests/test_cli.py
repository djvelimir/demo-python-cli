"""Tests for the demo-python-cli password generator (run pytest from repo root)."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
MAIN = SRC / "main.py"


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(MAIN), *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


def test_generate_password_prints_16_chars():
    result = run_cli("generate", "password")
    assert result.returncode == 0
    assert "Traceback" not in result.stderr
    password = result.stdout.strip()
    assert len(password) == 16


def test_no_args_shows_usage_without_traceback():
    result = run_cli()
    assert "Traceback" not in result.stderr
    assert "Usage:" in result.stdout


def test_validator_accepts_generate_password():
    sys.path.insert(0, str(SRC))
    try:
        from validator.argument_validator import ArgumentValidator
    finally:
        sys.path.remove(str(SRC))
    assert ArgumentValidator().validate(["main.py", "generate", "password"]) is True
    assert ArgumentValidator().validate(["main.py"]) is False
