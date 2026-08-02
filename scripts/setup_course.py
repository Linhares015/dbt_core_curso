#!/usr/bin/env python3
"""Set up and verify the local dbt Core + DuckDB course environment."""

from __future__ import annotations

import argparse
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"\nERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def run(command: list[str]) -> None:
    print(f"\n$ {' '.join(command)}")
    completed = subprocess.run(command, cwd=ROOT)
    if completed.returncode:
        fail(f"Command failed with exit code {completed.returncode}.")


def uv_install_hint() -> str:
    system = platform.system()
    if system == "Windows":
        return "Install uv with: powershell -ExecutionPolicy ByPass -c \"irm https://astral.sh/uv/install.ps1 | iex\""
    return "Install uv with: curl -LsSf https://astral.sh/uv/install.sh | sh"


def dbt_executable() -> Path:
    name = "dbt.exe" if platform.system() == "Windows" else "dbt"
    return ROOT / ".venv" / ("Scripts" if platform.system() == "Windows" else "bin") / name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create the course environment and optionally validate the full dbt project."
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="also run dbt seed and dbt build after dependency installation",
    )
    parser.add_argument(
        "--no-sync",
        action="store_true",
        help="skip uv sync; useful only when the environment already exists",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("Northstar Analytics — course environment setup")
    print(f"Repository: {ROOT}")
    print(f"Python: {sys.version.split()[0]}")

    if sys.version_info < (3, 10) or sys.version_info >= (3, 14):
        fail("Use Python 3.10, 3.11, 3.12, or 3.13 for this course.")
    if not (ROOT / "pyproject.toml").is_file() or not (ROOT / "profiles.yml").is_file():
        fail("Run this script from an intact course repository checkout.")

    uv = shutil.which("uv")
    if not uv:
        fail(f"uv is required but was not found. {uv_install_hint()}")
    assert uv is not None

    if not args.no_sync:
        run([uv, "sync"])

    dbt = dbt_executable()
    if not dbt.is_file():
        fail("dbt was not created in .venv. Re-run without --no-sync.")

    run([str(dbt), "debug", "--profiles-dir", "."])

    if args.verify:
        run([str(dbt), "seed", "--profiles-dir", "."])
        run([str(dbt), "build", "--profiles-dir", "."])

    print("\nSUCCESS: Your dbt Core + DuckDB course environment is ready.")
    if not args.verify:
        print("Run this for the full project check: python scripts/setup_course.py --verify")


if __name__ == "__main__":
    main()
