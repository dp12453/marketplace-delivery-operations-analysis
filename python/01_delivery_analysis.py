import pandas as pd
from pathlib import Path
DATA = Path('../data/raw')
orders = pd.read_csv(DATA/'olist_orders_dataset.csv', parse_dates=['order_purchase_timestamp','order_delivered_customer_date','order_estimated_delivery_date'])
customers = pd.read_csv(DATA/'olist_customers_dataset.csv')
reviews = pd.read_csv(DATA/'olist_order_reviews_dataset.csv')
orders = orders.merge(customers[['customer_id','customer_state']], on='customer_id', how='left')
review = reviews.groupby('order_id', as_index=False).agg(review_score=('review_score','mean'))
orders = orders.merge(review, on='order_id', how='left')
d = orders.query("order_status == 'delivered'").dropna(subset=['order_delivered_customer_date']).copy()
d['delivery_days'] = (d.order_delivered_customer_date-d.order_purchase_timestamp).dt.total_seconds()/86400
d['delay_days'] = (d.order_delivered_customer_date-d.order_estimated_delivery_date).dt.total_seconds()/86400
d['late_delivery'] = d.delay_days > 0
print('Delivered orders:', d.order_id.nunique())
print('Late delivery rate:', round(d.late_delivery.mean()*100,2),'%')
print('Average delivery days:', round(d.delivery_days.mean(),2))
print(d.groupby('customer_state').agg(orders=('order_id','nunique'),late_rate=('late_delivery','mean')).sort_values('late_rate',ascending=False).head(10))
