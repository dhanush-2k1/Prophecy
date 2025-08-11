from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emp.config.ConfigStore import *
from emp.functions import *

def department_salary_age_avg(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("DeptID"))

    return df1.agg(round(avg(col("Salary")), 2).alias("avg_sal"), round(avg(col("Experience"))).alias("Experience"))
