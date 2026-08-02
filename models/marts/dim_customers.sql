select
  customer_id,
  signup_date,
  country
from {{ ref('stg_customers') }}
