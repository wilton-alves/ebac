import os
from pyspark.sql import SparkSession

variables = [
    'JAVA_HOME',
    'SPARK_HOME',
    'SPARK_DIST_CLASSPATH',
    'PYSPARK_PYTHON',
    'PYSPARK_DRIVER_PYTHON',
]

print('Variáveis de ambiente:')
for var in variables:
    value = os.environ.get(var, 'Não definida')
    print(f'{var}: {value}')

spark = SparkSession.builder.getOrCreate()
print(f'Versão do Spark: {spark.version}')