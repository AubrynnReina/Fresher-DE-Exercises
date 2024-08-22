from pyspark.sql import SparkSession


spark_session = SparkSession.builder.appName("Test").getOrCreate()
spark_context = spark_session.sparkContext
data_df = spark_context.textFile('./apps/partitions_experiment/data/prime_5tr.txt')

print('Number of lines: ', data_df.count())
print(f'Num of executors: {spark_context.getConf().get("spark.executor.instances")}')
