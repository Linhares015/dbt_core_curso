with customers as (
  select * from {{ ref('dim_customers') }}
),
orders as (
  select * from {{ ref('fct_orders') }}
)
select
  customers.customer_id,
  customers.signup_date,
  customers.country,
  count(orders.order_id) as order_count,
  coalesce(sum(case when orders.order_status = 'completed' then orders.order_total else 0 end), 0) as completed_revenue,
  {{ safe_divide("sum(case when orders.order_status = 'completed' then orders.order_total else 0 end)", "nullif(count(case when orders.order_status = 'completed' then orders.order_id end), 0)") }} as average_completed_order_value
from customers
left join orders using (customer_id)
group by 1, 2, 3
