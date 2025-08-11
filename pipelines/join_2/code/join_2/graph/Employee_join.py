from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from join_2.config.ConfigStore import *
from join_2.functions import *

def Employee_join(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("EmployeeID", StringType(), True), StructField("Name", StringType(), True), StructField("DeptID", StringType(), True), StructField("Salary", StringType(), True), StructField("Experience", StringType(), True), StructField("Bonus", StringType(), True), StructField("City", StringType(), True), StructField("Gender", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Employee_join.csv")
