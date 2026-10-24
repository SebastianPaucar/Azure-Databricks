import time
from datetime import datetime, date
from pyspark.sql import functions as F
from common.spark_utils import tbl, table_exists

SCHEMA = (
    "process string, layer string, fecha_proceso date, load_type string, "
    "status string, error string, start_ts timestamp, end_ts timestamp"
)


def run_with_audit(spark, func, process, fechaproceso, layer="all",
                   max_retries=3, backoff_base=2):
    name = tbl("ops", "run_log")
    fecha = date.fromisoformat(fechaproceso)

    load_type = "Rutina"
    if table_exists(spark, name):
        prior = (spark.table(name)
                 .filter((F.col("process") == process) & (F.col("fecha_proceso") == F.lit(fecha)))
                 .count())
        load_type = "Reproceso" if prior > 0 else "Rutina"

    start = datetime.now()
    error = None
    try:
        func()
        status = "Correcto"
    except Exception as e:
        status, error = "Error", f"{type(e).__name__}: {e}"
        print(f"ERROR: {error}")
    end = datetime.now()

    row = [(process, layer, fecha, load_type, status, error, start, end)]
    df = spark.createDataFrame(row, SCHEMA)

    for attempt in range(1, max_retries + 1):
        try:
            df.write.mode("append").saveAsTable(name)
            print(f"run_log written (attempt {attempt}) status={status}")
            break
        except Exception as e:
            if attempt == max_retries:
                raise
            wait = backoff_base ** attempt
            print(f"run_log retry {attempt}/{max_retries} in {wait}s: {e}")
            time.sleep(wait)

    if status == "Error":
        raise RuntimeError(error)
