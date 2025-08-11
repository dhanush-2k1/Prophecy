from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from join.config.ConfigStore import *
from join.functions import *

def Department_Join(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("DeptID", IntegerType(), True), StructField("Department", StringType(), True), StructField("DeptHead", StringType(), True), StructField("Location", StringType(), True), StructField("Budget", DecimalType(20, 2), True), StructField("EmployeeCount", IntegerType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/department_join.csv")
