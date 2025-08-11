from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from reparition.config.ConfigStore import *
from reparition.functions import *

def Test_Shrava(spark: SparkSession, Repartition_1: DataFrame):
    Repartition_1.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/Downloads/")
