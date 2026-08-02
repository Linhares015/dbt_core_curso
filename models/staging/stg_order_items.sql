select
  order_item_id,
  order_id,
  product_id,
  cast(quantity as integer) as quantity,
  cast(unit_price as decimal(18, 2)) as unit_price,
  cast(quantity * unit_price as decimal(18, 2)) as line_revenue
from {{ source('raw', 'raw_order_items') }}
