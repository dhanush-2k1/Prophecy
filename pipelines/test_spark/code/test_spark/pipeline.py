from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test_spark.config.ConfigStore import *
from test_spark.functions import *
from prophecy.utils import *
from test_spark.graph import *

def pipeline(spark: SparkSession) -> None:
    df_employee = employee(spark)
    df_filter_high_salary = filter_high_salary(spark, df_employee)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("test_spark").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test_spark")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/test_spark", config = Config)(pipeline)

if __name__ == "__main__":
    main()
