from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from join.config.ConfigStore import *
from join.functions import *

def Source_0_Source_1(spark: SparkSession, Source_0: DataFrame, Source_1: DataFrame, ) -> DataFrame:
    return Source_0\
        .alias("Source_0")\
        .join(Source_1.alias("Source_1"), (col("Source_0.Emp_DeptID") == col("Source_1.Dept_DeptID")), "inner")
