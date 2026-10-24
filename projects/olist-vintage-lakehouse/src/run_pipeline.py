import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))   # make src/ importable

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ambiente", default="dev")
    ap.add_argument("--fechaproceso", required=True)      # YYYY-MM-DD
    ap.add_argument("--layers", default="bronze,silver,gold")
    ap.add_argument("--catalog", default="")
    ap.add_argument("--raw-path", default="")
    a = ap.parse_args()

    if a.catalog:
        os.environ["CATALOG"] = a.catalog
    if a.raw_path:
        os.environ["OLIST_RAW_PATH"] = a.raw_path

    # imports after env is set, so config/spark_utils see it
    from common.spark_utils import get_spark, ensure_schemas
    from common.config import seed_process_config, get_params, PROCESS
    from common.audit import run_with_audit
    from bronze import ingest_olist
    from silver import build_silver
    from gold import vintage_pyspark


    spark = get_spark()
    ensure_schemas(spark)
    seed_process_config(spark)
    params = get_params(spark)
    layers = a.layers.split(",")

    def job():
        if "bronze" in layers:
            ingest_olist.run(spark, params)
        if "silver" in layers:
            build_silver.run(spark, params)
        if "gold" in layers:
            vintage_pyspark.run(spark, params, a.fechaproceso, impl="sql")
            vintage_pyspark.run(spark, params, a.fechaproceso, impl="py")

    run_with_audit(spark, job, PROCESS, a.fechaproceso)


if __name__ == "__main__":
    main()
