import os
from pyspark.sql import SparkSession


def get_spark(app="olist-vintage"):
    builder = SparkSession.builder.appName(app)
    local = not os.environ.get("CATALOG", "").strip()
    if local:
        builder = builder.config("spark.sql.catalogImplementation", "hive")
    spark = builder.getOrCreate()
    if local:
        spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")
    spark.conf.set("spark.sql.session.timeZone", "UTC")
    return spark


def tbl(layer, name):
    """Table name; uses Unity Catalog three-part names when CATALOG is set."""
    catalog = os.environ.get("CATALOG", "").strip()
    return f"{catalog}.{layer}.{name}" if catalog else f"{layer}.{name}"


def ensure_schemas(spark, layers=("bronze", "silver", "gold", "ops")):
    catalog = os.environ.get("CATALOG", "").strip()
    for layer in layers:
        full = f"{catalog}.{layer}" if catalog else layer
        spark.sql(f"CREATE SCHEMA IF NOT EXISTS {full}")


def table_exists(spark, name):
    return spark.catalog.tableExists(name)
