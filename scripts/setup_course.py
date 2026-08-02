#!/usr/bin/env python3
"""Configura e valida o ambiente local do curso dbt Core + DuckDB."""

from __future__ import annotations

import argparse
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"\nERRO: {message}", file=sys.stderr)
    raise SystemExit(1)


def run(command: list[str]) -> None:
    print(f"\n$ {' '.join(command)}")
    completed = subprocess.run(command, cwd=ROOT)
    if completed.returncode:
        fail(f"O comando terminou com código {completed.returncode}.")


def uv_install_hint() -> str:
    if platform.system() == "Windows":
        return "Instale uv com: powershell -ExecutionPolicy ByPass -c \"irm https://astral.sh/uv/install.ps1 | iex\""
    return "Instale uv com: curl -LsSf https://astral.sh/uv/install.sh | sh"


def dbt_executable() -> Path:
    name = "dbt.exe" if platform.system() == "Windows" else "dbt"
    folder = "Scripts" if platform.system() == "Windows" else "bin"
    return ROOT / ".venv" / folder / name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cria o ambiente e opcionalmente valida a configuração inicial do projeto.")
    parser.add_argument("--verify", action="store_true", help="também carrega os dados de exemplo e valida a estrutura dbt")
    parser.add_argument("--no-sync", action="store_true", help="pula uv sync; use apenas se o ambiente já existir")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("Northstar Analytics — configuração do ambiente do curso")
    print(f"Repositório: {ROOT}")
    print(f"Python: {sys.version.split()[0]}")

    if sys.version_info < (3, 10) or sys.version_info >= (3, 14):
        fail("Use Python 3.10, 3.11, 3.12 ou 3.13 neste curso.")
    if not (ROOT / "pyproject.toml").is_file() or not (ROOT / "profiles.yml").is_file():
        fail("Execute este script a partir de um checkout intacto do repositório do curso.")

    uv = shutil.which("uv")
    if not uv:
        fail(f"uv é obrigatório, mas não foi encontrado. {uv_install_hint()}")
    assert uv is not None

    if not args.no_sync:
        run([uv, "sync"])

    dbt = dbt_executable()
    if not dbt.is_file():
        fail("dbt não foi criado em .venv. Execute novamente sem --no-sync.")

    run([str(dbt), "debug", "--profiles-dir", "."])
    if args.verify:
        run([str(dbt), "seed", "--profiles-dir", "."])
        run([str(dbt), "parse", "--profiles-dir", "."])

    print("\nSUCESSO: Seu ambiente do curso dbt Core + DuckDB está pronto.")
    if not args.verify:
        print("Para validar todo o ambiente, execute: python scripts/setup_course.py --verify")


if __name__ == "__main__":
    main()
