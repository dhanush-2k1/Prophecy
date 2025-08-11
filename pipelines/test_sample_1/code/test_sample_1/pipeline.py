from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test_sample_1.config.ConfigStore import *
from test_sample_1.functions import *
from prophecy.utils import *
from test_sample_1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Department_Join = Department_Join(spark)
    department_lookup(spark, df_Department_Join)
    df_Employee_join = Employee_join(spark)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("test_sample_1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test_sample_1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/test_sample_1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
