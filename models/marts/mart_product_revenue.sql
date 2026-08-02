with order_items as (
  select * from {{ ref('stg_order_items') }}
),
products as (
  select * from {{ ref('stg_products') }}
),
orders as (
  select * from {{ ref('fct_orders') }}
)
select
  products.product_id,
  products.product_name,
  products.category,
  sum(case when orders.order_status = 'completed' then order_items.quantity else 0 end) as completed_quantity,
  sum(case when orders.order_status = 'completed' then order_items.line_revenue else 0 end) as completed_revenue,
  sum(case when orders.order_status = 'completed' then order_items.quantity * products.unit_cost else 0 end) as completed_cost,
  sum(case when orders.order_status = 'completed' then order_items.line_revenue - (order_items.quantity * products.unit_cost) else 0 end) as completed_gross_profit
from order_items
inner join products using (product_id)
inner join orders using (order_id)
group by 1, 2, 3
