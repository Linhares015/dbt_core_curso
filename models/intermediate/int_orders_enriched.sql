with orders as (
  select * from {{ ref('stg_orders') }}
),
order_items as (
  select * from {{ ref('stg_order_items') }}
),
item_totals as (
  select
    order_id,
    sum(quantity) as item_quantity,
    sum(line_revenue) as item_revenue
  from order_items
  group by order_id
)
select
  orders.order_id,
  orders.customer_id,
  orders.order_date,
  orders.order_status,
  orders.subtotal,
  orders.discount,
  orders.tax,
  orders.order_total,
  coalesce(item_totals.item_quantity, 0) as item_quantity,
  coalesce(item_totals.item_revenue, 0) as item_revenue
from orders
left join item_totals using (order_id)
