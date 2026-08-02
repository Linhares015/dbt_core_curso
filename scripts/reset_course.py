#!/usr/bin/env python3
"""Remove artefatos dbt locais gerados sem tocar no código do aluno."""

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
    parser = argparse.ArgumentParser(description="Reinicia os artefatos locais gerados pelo curso.")
    parser.add_argument("--reseed", action="store_true", help="executa a verificação do setup depois da limpeza")
    args = parser.parse_args()

    for relative_path in GENERATED_PATHS:
        remove(ROOT / relative_path)
        print(f"Removido (se existia): {relative_path}")

    if args.reseed:
        command = [sys.executable, "scripts/setup_course.py", "--verify"]
        print(f"\n$ {' '.join(command)}")
        raise SystemExit(subprocess.run(command, cwd=ROOT).returncode)

    print("\nSUCESSO: Artefatos locais gerados foram removidos. Seus modelos, macros, testes e anotações não foram alterados.")


if __name__ == "__main__":
    main()
