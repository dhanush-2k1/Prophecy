from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from script.config.ConfigStore import *
from script.functions import *
from prophecy.utils import *
from script.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Employee_join = Employee_join(spark)
    df_department_salary_totals = department_salary_totals(spark, df_Employee_join)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("script").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/script")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/script", config = Config)(pipeline)

if __name__ == "__main__":
    main()
