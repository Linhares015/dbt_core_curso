# Capstone Exercise Checklist

## Deliverable

Build a documented, tested dbt project that turns the synthetic Northstar Analytics data into trustworthy customer and product analytics.

## Required models

- [ ] `stg_customers`
- [ ] `stg_orders`
- [ ] `stg_order_items`
- [ ] `stg_products`
- [ ] `int_orders_enriched`
- [ ] `dim_customers`
- [ ] `fct_orders`
- [ ] Customer lifetime value mart
- [ ] Product revenue mart

## Required quality work

- [ ] Document the sources.
- [ ] Add descriptions for each mart and essential columns.
- [ ] Add uniqueness and not-null tests for entity keys.
- [ ] Add relationship tests for the customer/order/product relationships.
- [ ] Add accepted-values testing for order status.
- [ ] Add one custom test for a business rule.

## Final verification

```bash
.venv/bin/dbt seed --profiles-dir .
.venv/bin/dbt build --profiles-dir .
.venv/bin/dbt docs generate --profiles-dir .
```

Your project is complete when all intended models and tests pass, generated documentation shows lineage, and a new learner can follow your README from a clean checkout.
