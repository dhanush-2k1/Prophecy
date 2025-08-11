from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from distrubuted.config.ConfigStore import *
from distrubuted.functions import *

def Employee_join(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("EmployeeID", StringType(), True), StructField("Name", StringType(), True), StructField("DeptID", IntegerType(), True), StructField("Salary", DoubleType(), True), StructField("Experience", DecimalType(20, 1), True), StructField("Bonus", DoubleType(), True), StructField("City", StringType(), True), StructField("Gender", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Employee_join.csv")
