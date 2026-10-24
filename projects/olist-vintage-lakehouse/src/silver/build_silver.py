from pyspark.sql import functions as F
from common.spark_utils import tbl


def build_orders(df):
    return (df.select(
                "order_id", "customer_id",
                F.col("order_status"),
                F.to_timestamp("order_purchase_timestamp").alias("purchase_ts"),
                F.to_timestamp("order_delivered_customer_date").alias("delivered_ts"),
                F.to_timestamp("order_estimated_delivery_date").alias("estimated_ts"))
            .dropDuplicates(["order_id"])
            .withColumn("days_late",
                        F.when(F.col("delivered_ts").isNotNull(),
                               F.datediff(F.col("delivered_ts"), F.col("estimated_ts"))))
            .withColumn("is_late",
                        F.when(F.col("delivered_ts").isNotNull(),
                               F.col("delivered_ts") > F.col("estimated_ts"))))


def build_order_items(df):
    return df.select(
        "order_id",
        F.col("order_item_id").cast("int").alias("order_item_id"),
        "product_id", "seller_id",
        F.col("price").cast("decimal(12,2)").alias("price"),
        F.col("freight_value").cast("decimal(12,2)").alias("freight_value"),
    ).dropDuplicates(["order_id", "order_item_id"])


def build_sellers(df):
    return df.select("seller_id",
                     F.col("seller_zip_code_prefix").alias("zip_prefix"),
                     F.col("seller_city").alias("city"),
                     F.col("seller_state").alias("state")).dropDuplicates(["seller_id"])


def run(spark, params):
    spark.table(tbl("bronze", "orders_raw")).transform(build_orders) \
        .write.mode("overwrite").saveAsTable(tbl("silver", "orders"))
    spark.table(tbl("bronze", "order_items_raw")).transform(build_order_items) \
        .write.mode("overwrite").saveAsTable(tbl("silver", "order_items"))
    spark.table(tbl("bronze", "sellers_raw")).transform(build_sellers) \
        .write.mode("overwrite").saveAsTable(tbl("silver", "sellers"))
