from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_sample_1.config.ConfigStore import *
from test_sample_1.functions import *

def reformat_employee_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("EmployeeID"), 
        col("Name"), 
        lookup("Dept_lookup", col("DeptID")).getField("department").alias("Dept_Name"), 
        col("Salary"), 
        col("Experience")
    )
