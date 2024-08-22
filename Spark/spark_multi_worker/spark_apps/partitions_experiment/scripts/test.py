from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import BooleanType

import time
import pickle

@udf(returnType=BooleanType())
def prime_number_detector(num):

    import math

    num = int(num)
    if num in [0, 1]:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):

        if num % i == 0:
            return False
    
    return True


time_data = []
spark_session = SparkSession.builder.appName("Test").getOrCreate()

for i in range(4, 61, 4):
    
    data_df = spark_session.read.text('./apps/partitions_experiment/data/prime.txt')
    prime_nums = data_df[prime_number_detector(data_df['value'])]
    prime_nums = prime_nums.repartition(i)

    start_time = time.time()
    print(prime_nums.count())
    end_time = time.time()

    time_data.append(end_time - start_time)

    with open('./apps/partitions_experiment/data/Exe_time_2_2_3.txt', 'a+') as f:
        f.write(str(end_time - start_time) + '\n')

spark_session.stop()
