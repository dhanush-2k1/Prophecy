from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emp.config.ConfigStore import *
from emp.functions import *

def sort_by_avg_salary_desc(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("avg_sal").desc_nulls_first())
