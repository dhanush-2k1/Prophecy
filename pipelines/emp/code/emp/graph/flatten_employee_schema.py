from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emp.config.ConfigStore import *
from emp.functions import *

def flatten_employee_schema(spark: SparkSession, remove_duplicates: DataFrame) -> DataFrame:
    flt_col = remove_duplicates.columns
    selectCols = [col("DeptID") if "DeptID" in flt_col else col("DeptID"),                   col("Experience") if "Experience" in flt_col else col("Experience"),                   col("Emp_avg_sal") if "Emp_avg_sal" in flt_col else col("Emp_avg_sal")]

    return remove_duplicates.select(*selectCols)
