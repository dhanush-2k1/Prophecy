from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_sample_1.config.ConfigStore import *
from test_sample_1.functions import *

def department_lookup(spark: SparkSession, in0: DataFrame):
    keyColumns = ['''DeptID''']
    valueColumns = ['''Department''']
    createLookup("Dept_lookup", in0, spark, keyColumns, valueColumns)
