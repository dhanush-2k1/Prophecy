from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from reparition.config.ConfigStore import *
from reparition.functions import *

def reduce_partitions(spark: SparkSession, Emp_join: DataFrame) -> DataFrame:
    return Emp_join.repartition(col("Dept_DeptID"))
