from datetime import datetime
from decimal import Decimal
from gold.vintage_pyspark import vintage_pyspark, vintage_sql

def _data(spark):
    orders = spark.createDataFrame([
        ("o1", "delivered", datetime(2017, 1, 10), datetime(2017, 1, 20), True),
        ("o2", "delivered", datetime(2017, 2, 5),  datetime(2017, 2, 9),  False),
        ("o3", "delivered", datetime(2017, 2, 7),  datetime(2017, 2, 25), True),
    ], "order_id string, order_status string, purchase_ts timestamp, delivered_ts timestamp, is_late boolean")
    items = spark.createDataFrame([
        ("o1", 1, "s1", Decimal("100.00")),
        ("o2", 1, "s1", Decimal("50.00")),
        ("o3", 1, "s1", Decimal("30.00")),
    ], "order_id string, order_item_id int, seller_id string, price decimal(12,2)")
    return orders, items

def test_pyspark_vintage(spark):
    o, i = _data(spark)
    rows = {(r.mob): r for r in vintage_pyspark(o, i, "2017-12-31", 24).collect()}
    assert rows[0].late_amount == Decimal("100.00")
    assert rows[1].total_amount == Decimal("80.00")
    assert rows[1].late_amount == Decimal("30.00")

def test_sql_matches_pyspark(spark):
    o, i = _data(spark)
    o.createOrReplaceTempView("t_orders"); i.createOrReplaceTempView("t_items")
    a = vintage_sql(spark, "2017-12-31", 24, "t_orders", "t_items").collect()
    b = vintage_pyspark(o, i, "2017-12-31", 24).collect()
    assert sorted(map(tuple, a)) == sorted(map(tuple, b))
