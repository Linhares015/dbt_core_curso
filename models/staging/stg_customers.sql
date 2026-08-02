select
  customer_id,
  cast(signup_date as date) as signup_date,
  country
from {{ source('raw', 'raw_customers') }}
