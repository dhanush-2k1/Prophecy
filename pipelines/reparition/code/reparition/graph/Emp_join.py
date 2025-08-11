from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from reparition.config.ConfigStore import *
from reparition.functions import *

def Emp_join(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Emp_EmployeeID", StringType(), True), StructField("Emp_Name", StringType(), True), StructField("Emp_DeptID", IntegerType(), True), StructField("Emp_Salary", DoubleType(), True), StructField("Emp_Experience", DecimalType(20, 1), True), StructField("Emp_Bonus", DecimalType(20, 10), True), StructField("Emp_City", StringType(), True), StructField("Emp_Gender", StringType(), True), StructField("Dept_DeptID", IntegerType(), True), StructField("Dept_Department", StringType(), True), StructField("Dept_DeptHead", StringType(), True), StructField("Dept_Location", StringType(), True), StructField("Dept_Budget", DecimalType(20, 2), True), StructField("Dept_EmployeeCount", IntegerType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Downloads/")
