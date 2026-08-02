select
  order_id,
  customer_id,
  order_date,
  order_status,
  subtotal,
  discount,
  tax,
  order_total,
  item_quantity,
  item_revenue
from {{ ref('int_orders_enriched') }}
