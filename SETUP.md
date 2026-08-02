# Environment Setup Guide

This course uses **dbt Core + DuckDB locally**. You do not need a cloud warehouse account, database password, API key, or paid service.

## What the setup assistant does

The repository includes `scripts/setup_course.py`. It:

1. checks your Python version;
2. installs the project’s locked dependencies through `uv sync`;
3. confirms that dbt can read `profiles.yml` and connect to local DuckDB;
4. with `--verify`, loads the sample data and validates the dbt project configuration without requiring the final course models.

## Requirements

- Git
- Python **3.10, 3.11, 3.12, or 3.13**
- `uv` package manager

No credentials are required: `profiles.yml` already points to a local `northstar.duckdb` file.

## Install `uv`

Use the official instructions at https://docs.astral.sh/uv/getting-started/installation/.

Common commands:

### Windows PowerShell

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen PowerShell after installation.

### macOS or Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen the terminal after installation if `uv --version` is not found.

## One command after cloning

### macOS/Linux

```bash
python3 scripts/setup_course.py --verify
```

### Windows PowerShell

```powershell
py scripts/setup_course.py --verify
```

Expected final message:

```text
SUCCESS: Your dbt Core + DuckDB course environment is ready.
```

The verification loads the synthetic datasets and confirms the dbt project parses correctly. At the start of the course, final models and tests are intentionally not present yet.

## Faster daily setup

After the first successful install, run without `--verify` when you only want to confirm the environment:

```bash
python3 scripts/setup_course.py
```

## Troubleshooting

### `uv is required but was not found`

Install `uv`, reopen your terminal, and confirm it with:

```bash
uv --version
```

### Python version error

Install Python 3.10–3.13, reopen the terminal, and check:

```bash
python3 --version
```

On Windows use `py --version`.

### dbt connection/debug fails

Start from a clean local database and run the complete setup again:

```bash
rm -f northstar.duckdb
python3 scripts/setup_course.py --verify
```

On Windows PowerShell:

```powershell
Remove-Item northstar.duckdb -ErrorAction SilentlyContinue
py scripts/setup_course.py --verify
```

### Something still fails

Copy the full terminal output into the course support channel, together with your operating system and `python --version` / `uv --version` output.
