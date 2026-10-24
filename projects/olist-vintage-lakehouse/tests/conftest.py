import sys, pathlib
import pytest
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    s = (SparkSession.builder.master("local[1]")
         .config("spark.sql.shuffle.partitions", "2")
         .config("spark.sql.session.timeZone", "UTC").getOrCreate())
    yield s
    s.stop()
