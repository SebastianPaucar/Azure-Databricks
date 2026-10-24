
```bash
D=/path/to/SQL-PySpark/datasets/EXTRACTED/brazilian-ecommerce
for f in olist_orders_dataset.csv olist_order_items_dataset.csv olist_sellers_dataset.csv; do
  databricks fs cp $D/$f dbfs:/Volumes/workspace/bronze/raw/
done
databricks fs ls dbfs:/Volumes/workspace/bronze/raw/
```
