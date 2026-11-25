# Data dictionary and metric definitions

- `delivery_days`: elapsed days from order purchase to actual customer delivery.
- `delay_days`: elapsed days from estimated delivery date to actual customer delivery; positive = late, negative = early.
- `late_delivery`: Boolean flag where `delay_days > 0`.
- `delivery_status`: Late, Early or On estimated date.
- `late_delivery_rate_pct`: late delivered orders / eligible delivered orders * 100.
- `review_score`: mean review score per order where multiple review records exist.
- `freight_total`: sum of item-level freight values for an order.

Delivery KPIs use delivered orders with non-null actual delivery timestamps. Seller scorecard metrics are seller-order level, not item-row level.
