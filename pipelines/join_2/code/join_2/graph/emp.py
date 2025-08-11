from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from join_2.config.ConfigStore import *
from join_2.functions import *

def emp(spark: SparkSession, reformat_employee_data: DataFrame):
    reformat_employee_data.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("error")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/prophecy/employee.csv")
