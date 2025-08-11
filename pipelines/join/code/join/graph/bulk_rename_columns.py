from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from join.config.ConfigStore import *
from join.functions import *

def bulk_rename_columns(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from prophecy.utils.transpiler.dataframe_fcns import evaluate_expression

    return evaluate_expression(
        in0,
        userExpression = "concat('Emp_', column_name)",
        selectedColumnNames = ["EmployeeID", "Name", "DeptID", "Salary", "Experience", "Bonus", "City", "Gender"],
        sparkSession = spark
    )
