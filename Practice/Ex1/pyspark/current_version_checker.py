import sys

import findspark # Help with finding pyspark
findspark.init()

import pyspark

print('Python version:', sys.version.split(' ')[0])
print('PySpark version:', pyspark.__version__)