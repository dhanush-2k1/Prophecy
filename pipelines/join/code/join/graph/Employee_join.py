from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from join.config.ConfigStore import *
from join.functions import *

def Employee_join(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("EmployeeID", StringType(), True), StructField("Name", StringType(), True), StructField("DeptID", IntegerType(), True), StructField("Salary", DecimalType(20, 2), True), StructField("Experience", DecimalType(20, 1), True), StructField("Bonus", DecimalType(20, 2), True), StructField("City", StringType(), True), StructField("Gender", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Employee_join.csv")
