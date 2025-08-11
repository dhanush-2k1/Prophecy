from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emp.config.ConfigStore import *
from emp.functions import *

def remove_duplicates(spark: SparkSession, clean_dataframe: DataFrame) -> DataFrame:
    return clean_dataframe.distinct()
