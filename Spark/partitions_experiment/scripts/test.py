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

for i in range(6, 13, 6):
    
    spark_session = SparkSession.builder.appName("Test").getOrCreate()

    data_df = spark_session.read.text('../data/prime.txt')
    prime_nums = data_df[prime_number_detector(data_df['value'])]

    start_time = time.time()
    print(prime_nums.count())
    end_time = time.time()

    time_data.append(end_time - start_time)

    spark_session.stop()

with open('../data/Exe_time_2_3_2.pkl', 'wb') as f:
    pickle.dump(time_data, f)