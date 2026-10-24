from pyspark.sql import functions as F
from common.spark_utils import tbl

FILES = {
    "orders_raw": "olist_orders_dataset.csv",
    "order_items_raw": "olist_order_items_dataset.csv",
    "sellers_raw": "olist_sellers_dataset.csv",
}


def run(spark, params):
    base = params["PRM_RAW_PATH"]
    for table, fname in FILES.items():
        df = (spark.read
              .option("header", True)
              .option("quote", '"')
              .option("escape", '"')
              .option("encoding", "UTF-8")
              .csv(f"{base}/{fname}"))          # all strings: bronze stays raw
        df = (df.withColumn("_ingestion_time", F.current_timestamp())
                .withColumn("_source_file", F.col("_metadata.file_path")))
        df.write.mode("overwrite").saveAsTable(tbl("bronze", table))
        print(f"bronze.{table}: {df.count()} rows")
