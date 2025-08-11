from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from script.config.ConfigStore import *
from script.functions import *

def department_salary_totals(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0.groupBy('DeptId').agg(sum('salary').alias('sum_sal'), round(avg('salary'), 2).alias('avg_sal'))

    return out0
