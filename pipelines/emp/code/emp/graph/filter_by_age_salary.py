from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emp.config.ConfigStore import *
from emp.functions import *

def filter_by_age_salary(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(((col("Age") > lit(25)) & (col("Salary") >= lit(500000))))
