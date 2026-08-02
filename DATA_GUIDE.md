# Data Guide

All datasets in this repository are **synthetic educational data** for the fictional e-commerce company Northstar Analytics. They contain no real customer or business information.

## `raw_customers`

| Column | Meaning |
|---|---|
| `customer_id` | Stable customer identifier |
| `signup_date` | Date the customer created an account |
| `country` | Customer country code |

## `raw_orders`

| Column | Meaning |
|---|---|
| `order_id` | Stable order identifier |
| `customer_id` | Customer who placed the order |
| `order_date` | Date of the order |
| `status` | `completed`, `pending`, or `cancelled` |
| `subtotal` | Value before discount and tax |
| `discount` | Discount applied to the order |
| `tax` | Tax applied to the order |
| `total` | Final order total |

## `raw_order_items`

| Column | Meaning |
|---|---|
| `order_item_id` | Stable line-item identifier |
| `order_id` | Parent order identifier |
| `product_id` | Product identifier |
| `quantity` | Number of units bought |
| `unit_price` | Selling price per unit |

## `raw_products`

| Column | Meaning |
|---|---|
| `product_id` | Stable product identifier |
| `product_name` | Display name |
| `category` | Product category |
| `unit_cost` | Internal unit cost for gross-profit calculations |

## Modeling rules to apply in the course

- Keep staging models close to source grain and meaning.
- Use `order_id`, `customer_id`, and `product_id` as relationship keys.
- Do not treat `pending` or `cancelled` orders as completed revenue.
- Verify that completed orders never have a negative final total.
