from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from compare_columns.config.ConfigStore import *
from compare_columns.functions import *
from prophecy.utils import *
from compare_columns.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Employee_join = Employee_join(spark)
    df_Employee_join_1 = Employee_join_1(spark)
    df_column_comparison_summary = column_comparison_summary(spark, df_Employee_join, df_Employee_join_1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("compare_columns").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/compare_columns")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/compare_columns", config = Config)(pipeline)

if __name__ == "__main__":
    main()
