# Learning Path

Use this repository in sequence with the lessons. Each stage has a clear checkpoint before moving forward.

## 1. Environment and raw data

- Run `python3 scripts/setup_course.py --verify`.
- Open the seed CSV files in `seeds/`.
- Run `dbt seed --profiles-dir .`.
- Inspect the raw seed tables in DuckDB.

**Checkpoint:** `dbt debug` succeeds and the four seed files load successfully.

## 2. Sources and staging

- Review `models/sources.yml`.
- Build `stg_customers`, `stg_orders`, `stg_order_items`, and `stg_products` in `models/staging/`.
- Standardize column names, types, dates, and order status.

**Checkpoint:** each staging model builds and has one clear responsibility.

## 3. Dependencies and intermediate logic

- Use `ref()` rather than hard-coded table names.
- Create `int_orders_enriched` in `models/intermediate/`.
- Aggregate item quantity and line revenue at order level.

**Checkpoint:** the model graph shows the source-to-order dependency flow.

## 4. Analytics marts

- Create `dim_customers` and `fct_orders`.
- Create customer-lifetime-value and product-revenue marts.
- Choose model materializations deliberately.

**Checkpoint:** the marts answer customer and product/revenue questions using clean dependencies.

## 5. Reuse and data quality

- Add a small reusable macro under `macros/`.
- Add generic tests in a model `schema.yml` file.
- Add one custom business-rule test under `tests/`.

**Checkpoint:** `dbt build --profiles-dir .` passes with your models and tests.

## 6. Documentation and final delivery

- Add descriptions for exposed models and key columns.
- Run `dbt docs generate --profiles-dir .`.
- Review the lineage graph and complete the capstone checklist in `exercises/README.md`.

**Checkpoint:** a clean clone can install, seed, build, test, and generate docs using your instructions.
