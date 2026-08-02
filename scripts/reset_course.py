#!/usr/bin/env python3
"""Remove generated local dbt artifacts without touching a learner's source work."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED_PATHS = ("northstar.duckdb", "target", "logs")


def remove(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description="Reset generated local course artifacts.")
    parser.add_argument(
        "--reseed",
        action="store_true",
        help="run the setup assistant's verification after the cleanup",
    )
    args = parser.parse_args()

    for relative_path in GENERATED_PATHS:
        path = ROOT / relative_path
        remove(path)
        print(f"Removed (if present): {relative_path}")

    if args.reseed:
        command = [sys.executable, "scripts/setup_course.py", "--verify"]
        print(f"\n$ {' '.join(command)}")
        raise SystemExit(subprocess.run(command, cwd=ROOT).returncode)

    print("\nSUCCESS: Generated local artifacts were removed. Your models, macros, tests, and notes remain unchanged.")


if __name__ == "__main__":
    main()
