select
  product_id,
  product_name,
  category,
  cast(unit_cost as decimal(18, 2)) as unit_cost
from {{ source('raw', 'raw_products') }}
