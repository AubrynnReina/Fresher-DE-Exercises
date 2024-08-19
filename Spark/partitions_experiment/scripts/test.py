def prime_number_detector(num):

    import math

    if num in [0, 1]:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):

        if num % i == 0:
            return False
    
    return True


from pyspark.sql import SparkSession

spark_session = SparkSession.builder.appName("Test").getOrCreate()

data_df = spark_session.read.text('../data/prime.txt')
print(data_df.count())