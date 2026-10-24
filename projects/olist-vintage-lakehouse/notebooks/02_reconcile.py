import sys
from pyspark.sql import functions as F
from common.spark_utils import get_spark, tbl

COLS = ["cohort_month", "mob", "late_amount", "total_amount", "order_count", "late_order_count"]


def fingerprint(df):
    h = F.xxhash64(*[F.col(c).cast("string") for c in COLS]).cast("decimal(38,0)")
    r = df.agg(F.count("*").alias("rows"),
               F.sum("late_amount").alias("late_sum"),
               F.sum("total_amount").alias("total_sum"),
               F.sum(h).alias("hash")).first()
    return r.asDict()


def main(a="seller_vintage_long", b="seller_vintage_long_py"):
    spark = get_spark()
    fa, fb = fingerprint(spark.table(tbl("gold", a))), fingerprint(spark.table(tbl("gold", b)))
    print(a, fa); print(b, fb)
    ok = fa == fb
    print("RECONCILED" if ok else "MISMATCH")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
