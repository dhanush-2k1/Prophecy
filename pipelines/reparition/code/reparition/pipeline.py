from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from reparition.config.ConfigStore import *
from reparition.functions import *
from prophecy.utils import *
from reparition.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Emp_join = Emp_join(spark)
    df_reduce_partitions = reduce_partitions(spark, df_Emp_join)
    Test_Shrava(spark, df_reduce_partitions)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("reparition").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/reparition")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/reparition", config = Config)(pipeline)

if __name__ == "__main__":
    main()
