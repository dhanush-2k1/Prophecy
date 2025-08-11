from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from distrubuted.config.ConfigStore import *
from distrubuted.functions import *

def distribute_by_department(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    df1 = in0.filter((col("DeptID") == lit(101)))
    df2 = in0.filter((col("DeptID") == lit(102)))

    return df1, df2
