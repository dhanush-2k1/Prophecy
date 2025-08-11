from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from join_2.config.ConfigStore import *
from join_2.functions import *

def reformat_employee_data(spark: SparkSession, Deduplicate_1: DataFrame) -> DataFrame:
    return Deduplicate_1.select(
        col("EmployeeID"), 
        col("Name"), 
        col("DeptID"), 
        (col("Salary") + col("Bonus")).alias("Salary"), 
        col("Experience")
    )
