from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from join_2.config.ConfigStore import *
from join_2.functions import *
from prophecy.utils import *
from join_2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Employee_join = Employee_join(spark)
    df_dynamic_column_selection = dynamic_column_selection(spark, df_Employee_join)
    df_reformat_employee_data = reformat_employee_data(spark, df_dynamic_column_selection)
    Test_Shravan(spark, df_reformat_employee_data)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("join_2").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/join_2")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/join_2", config = Config)(pipeline)

if __name__ == "__main__":
    main()
