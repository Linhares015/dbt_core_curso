select
  order_id,
  customer_id,
  cast(order_date as date) as order_date,
  lower(status) as order_status,
  cast(subtotal as decimal(18, 2)) as subtotal,
  cast(discount as decimal(18, 2)) as discount,
  cast(tax as decimal(18, 2)) as tax,
  cast(total as decimal(18, 2)) as order_total
from {{ source('raw', 'raw_orders') }}
