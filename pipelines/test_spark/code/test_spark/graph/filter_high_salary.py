from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_spark.config.ConfigStore import *
from test_spark.functions import *

def filter_high_salary(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("Salary") >= lit(50000)))
