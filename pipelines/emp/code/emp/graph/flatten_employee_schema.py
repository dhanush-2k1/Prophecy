from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emp.config.ConfigStore import *
from emp.functions import *

def flatten_employee_schema(spark: SparkSession, remove_duplicates: DataFrame) -> DataFrame:
    flt_col = remove_duplicates.columns
    selectCols = [col("Emp_Department") if "Emp_Department" in flt_col else col("Emp_Department"),                   col("Emp_avg_sal") if "Emp_avg_sal" in flt_col else col("Emp_avg_sal"),                   col("Emp_avg_age") if "Emp_avg_age" in flt_col else col("Emp_avg_age")]

    return remove_duplicates.select(*selectCols)
