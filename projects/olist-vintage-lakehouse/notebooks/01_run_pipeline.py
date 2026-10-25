# Databricks notebook source
import os, sys

dbutils.widgets.text("ambiente", "dev")
dbutils.widgets.text("fechaproceso", "")
dbutils.widgets.text("catalog", "workspace")
dbutils.widgets.text("raw_path", "/Volumes/workspace/bronze/raw")

os.environ["CATALOG"] = dbutils.widgets.get("catalog")
os.environ["OLIST_RAW_PATH"] = dbutils.widgets.get("raw_path")

# notebook lives in <bundle>/files/notebooks; src is a sibling folder
#nb_dir = os.path.dirname(dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get())
#sys.path.insert(0, "/Workspace" + os.path.dirname(nb_dir) + "/src")

# packages now come from the installed wheel!

from common.spark_utils import get_spark, ensure_schemas
from common.config import seed_process_config, get_params, PROCESS
from common.audit import run_with_audit
from bronze import ingest_olist
from silver import build_silver
from gold import vintage_pyspark

fecha = dbutils.widgets.get("fechaproceso")
spark = get_spark()
ensure_schemas(spark)
seed_process_config(spark)
params = get_params(spark)

def job():
    ingest_olist.run(spark, params)
    build_silver.run(spark, params)
    vintage_pyspark.run(spark, params, fecha, impl="sql")
    vintage_pyspark.run(spark, params, fecha, impl="py")

run_with_audit(spark, job, PROCESS, fecha)
