from pyspark.sql import functions as F
from common.spark_utils import tbl, table_exists
import os

DEFAULTS = {
    "PRM_RAW_PATH": os.environ.get(
        "OLIST_RAW_PATH",
        os.path.expanduser("~/GIT/SQL-PySpark/datasets/EXTRACTED/brazilian-ecommerce")),
    "PRM_MAX_MOB": "24",
}

PROCESS = "OLIST_VINTAGE"


def seed_process_config(spark, process=PROCESS, params=None):
    """Create ops.process_config and insert missing defaults (idempotent)."""
    params = {**DEFAULTS, **(params or {})}
    name = tbl("ops", "process_config")
    rows = [(process, k, v) for k, v in params.items()]
    new = spark.createDataFrame(rows, "process string, param string, value string")
    if not table_exists(spark, name):
        new.write.saveAsTable(name)
        return
    existing = spark.table(name).filter(F.col("process") == process).select("param")
    missing = new.join(existing, "param", "left_anti").select("process", "param", "value")
    missing.write.mode("append").saveAsTable(name)


def get_params(spark, process=PROCESS):
    df = spark.table(tbl("ops", "process_config")).filter(F.col("process") == process)
    params = {r["param"]: r["value"] for r in df.collect()}
    if not params:
        raise RuntimeError(f"No parameters found for process '{process}'")
    return params
