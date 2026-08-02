-- A business rule for the capstone: completed orders cannot have a negative total.
-- This test is intentionally written before the model exists (TDD RED phase).
select *
from {{ ref('fct_orders') }}
where order_status = 'completed'
  and order_total < 0
