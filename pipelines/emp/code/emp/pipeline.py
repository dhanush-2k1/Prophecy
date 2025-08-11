from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from emp.config.ConfigStore import *
from emp.functions import *
from prophecy.utils import *
from emp.graph import *

def pipeline(spark: SparkSession) -> None:
    df_emp = emp(spark)
    df_filter_by_age_salary = filter_by_age_salary(spark, df_emp)
    df_department_salary_age_avg = department_salary_age_avg(spark, df_filter_by_age_salary)
    df_sort_by_avg_salary_desc = sort_by_avg_salary_desc(spark, df_department_salary_age_avg)
    df_bulk_rename_columns = bulk_rename_columns(spark, df_sort_by_avg_salary_desc)
    df_clean_dataframe = clean_dataframe(spark, df_bulk_rename_columns)
    df_remove_duplicates = remove_duplicates(spark, df_clean_dataframe)
    df_flatten_employee_schema = flatten_employee_schema(spark, df_remove_duplicates)
    tagrget_output(spark, df_flatten_employee_schema)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("emp").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/emp")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/emp", config = Config)(pipeline)

if __name__ == "__main__":
    main()
