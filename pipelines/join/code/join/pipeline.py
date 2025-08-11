from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from join.config.ConfigStore import *
from join.functions import *
from prophecy.utils import *
from join.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Employee_join = Employee_join(spark)
    df_bulk_rename_columns = bulk_rename_columns(spark, df_Employee_join)
    df_Department_Join = Department_Join(spark)
    df_bulk_rename_columns_1 = bulk_rename_columns_1(spark, df_Department_Join)
    df_Source_0_Source_1 = Source_0_Source_1(spark, df_bulk_rename_columns, df_bulk_rename_columns_1)
    Emp_join(spark, df_Source_0_Source_1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("join").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/join")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/join", config = Config)(pipeline)

if __name__ == "__main__":
    main()
