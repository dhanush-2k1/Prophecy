from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emp.config.ConfigStore import *
from emp.functions import *

def clean_dataframe(spark: SparkSession, df: DataFrame) -> DataFrame:
    from pyspark.sql.functions import col, trim, regexp_replace, lower, upper, initcap
    from pyspark.sql.types import StringType, IntegerType, FloatType, DoubleType, LongType, ShortType
    # Step 2: Apply data cleansing operations
    # Start with the original columns
    transformed_columns = []

    # Check if column exists after null operations
    if "Emp_avg_sal" not in df.columns:
        print(
            "Warning: Column 'Emp_avg_sal' not found after null operation. Skipping transformations for this column."
        )
    else:
        # If the column is a string type, apply text-based operations
        if isinstance(df.schema["Emp_avg_sal"].dataType, StringType):
            transformed_columns = [regexp_replace(regexp_replace(trim(col("Emp_avg_sal")), r'\s+', ' '), r'\s+', '')\
                                     .alias("Emp_avg_sal")]
        elif isinstance(df.schema["Emp_avg_sal"].dataType, (IntegerType, FloatType, DoubleType, LongType, ShortType)):
            df = df.na.fill({"Emp_avg_sal" : 0})
            transformed_columns = [col("Emp_avg_sal")]
        else:
            transformed_columns = [col("Emp_avg_sal")]

    # Check if column exists after null operations
    if "Emp_avg_age" not in df.columns:
        print(
            "Warning: Column 'Emp_avg_age' not found after null operation. Skipping transformations for this column."
        )
    else:
        # If the column is a string type, apply text-based operations
        if isinstance(df.schema["Emp_avg_age"].dataType, StringType):
            # Add the transformed column to the list with alias
            transformed_columns.append(
                regexp_replace(regexp_replace(trim(col("Emp_avg_age")), r'\s+', ' '), r'\s+', '').alias("Emp_avg_age")
            )
        elif isinstance(df.schema["Emp_avg_age"].dataType, (IntegerType, FloatType, DoubleType, LongType, ShortType)):
            df = df.na.fill({"Emp_avg_age" : 0})
            transformed_columns.append(col("Emp_avg_age"))
        else:
            # If the column doesn't require transformation, add it as is
            transformed_columns.append(col("Emp_avg_age"))

    df = df.select(*[col(c) for c in df.columns if c not in ["Emp_avg_sal", "Emp_avg_age"]], *transformed_columns)

    return df
