from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from distrubuted.config.ConfigStore import *
from distrubuted.functions import *
from prophecy.utils import *
from distrubuted.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Employee_join = Employee_join(spark)
    df_distribute_by_department_out0, df_distribute_by_department_out1 = distribute_by_department(
        spark, 
        df_Employee_join
    )
    d1(spark, df_distribute_by_department_out0)
    d2(spark, df_distribute_by_department_out1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("distrubuted").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/distrubuted")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/distrubuted", config = Config)(pipeline)

if __name__ == "__main__":
    main()
