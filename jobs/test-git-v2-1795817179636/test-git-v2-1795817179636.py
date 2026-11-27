import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = SparkSession.builder.getOrCreate()

# Script generated for node S3DataSource
S3DataSource_1795817282902 = spark.read.format("csv") \
    .option("inferschema", "true") \
    .option("multiLine", "true") \
    .option("header", "true") \
    .option("recursiveFileLookup", "true") \
    .option("sep", ",") \
    .load("s3://test-bucket")
