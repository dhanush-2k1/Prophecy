from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_spark.config.ConfigStore import *
from test_spark.functions import *

def employee(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("ID", IntegerType(), True), StructField("First_Name", StringType(), True), StructField("Last_Name", StringType(), True), StructField("Age", IntegerType(), True), StructField("City", StringType(), True), StructField("Occupation", StringType(), True), StructField("Phone", DoubleType(), True), StructField("Email", StringType(), True), StructField("Salary", DecimalType(20, 2), True), StructField("Department", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/prophecy/employee.csv")
