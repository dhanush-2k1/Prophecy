from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emp.config.ConfigStore import *
from emp.functions import *

def emp(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("EmployeeID", StringType(), True), StructField("Name", StringType(), True), StructField("DeptID", StringType(), True), StructField("Salary", DoubleType(), True), StructField("Experience", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/prophecy/employee.csv")
