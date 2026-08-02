# dbt_core_curso — Starter Repository

This is the **student workspace** for the Udemy course **dbt Core for Data Analysts**. It contains the environment automation, synthetic data, guided exercises, and empty folders where you will build the project lesson by lesson.

> Do not expect the final models to be present on day one. You will create them during the course.

## Start here

1. Read [SETUP.md](SETUP.md).
2. Clone this repository.
3. Run the setup assistant:

   **macOS/Linux**
   ```bash
   python3 scripts/setup_course.py --verify
   ```

   **Windows PowerShell**
   ```powershell
   py scripts/setup_course.py --verify
   ```

4. Follow [LEARNING_PATH.md](LEARNING_PATH.md) alongside the course lessons.
5. Use [DATA_GUIDE.md](DATA_GUIDE.md) to understand the synthetic datasets.

## What is included

- `seeds/`: synthetic e-commerce data used throughout the lessons.
- `models/sources.yml`: source declarations for the raw data.
- `models/staging/`, `models/intermediate/`, `models/marts/`: folders where you write models during the course.
- `macros/`: folder for reusable Jinja macros.
- `tests/`: folder for custom data tests.
- `exercises/`: guided task specifications and checkpoints.
- `scripts/`: environment setup and reset automation.

## Reset your local work

To reset generated data, the local DuckDB database, target artifacts, and logs while preserving your source files:

```bash
python3 scripts/reset_course.py
```

On Windows, use `py scripts/reset_course.py`.

## Important

- All data is synthetic and safe for local practice.
- `profiles.yml` is preconfigured for a local DuckDB file: no credentials or cloud account are required.
- Do not commit `.venv/`, `northstar.duckdb`, `target/`, or `logs/`; they are ignored already.
- The complete instructor solution is intentionally not part of this student branch.
