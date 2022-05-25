import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

import datetime
from awsglue import DynamicFrame
from pyspark.sql.functions import lit, length

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

aggregation_params = ["length", "likeCount", "totalReplyCount"]
s3_path = "s3://a-data-bucket-1/StreamingOutput/"

dataframe_AmazonKinesis_node = glueContext.create_data_frame.from_options(
    connection_type="kinesis",
    connection_options={
        "typeOfData": "kinesis",
        "streamARN": "arn:aws:kinesis:us-east-2:062261762656:stream/a-comments",
        "classification": "json",
        "startingPosition": "earliest",
        "inferSchema": "true",
    },
    transformation_ctx="dataframe_AmazonKinesis",
)


def aggregate(df, param, out_dir) -> None:
    df = df.orderBy(param, ascending=False).limit(1)
    df.write.mode("append").partitionBy('date', 'hour', 'time_chunk').parquet(s3_path + out_dir + "/")


def process_batch(data_frame, batchId) -> None:
    if data_frame.count() > 0:
        now = datetime.datetime.now()
        AmazonKinesis_DynamicFrame = DynamicFrame.fromDF(data_frame, glueContext, "from_data_frame")
        df = AmazonKinesis_DynamicFrame.toDF()
        df = df.select("id",
                       "snippet.videoId",
                       "snippet.topLevelComment.snippet.textDisplay",
                       "snippet.topLevelComment.snippet.likeCount",
                       "snippet.totalReplyCount").withColumn('date', lit(str(now.date()))) \
            .withColumn('hour', lit(str(now.hour))) \
            .withColumn('time_chunk', lit(int(now.minute) // 5)) \
            .withColumn("length", length("textDisplay"))

        for param in aggregation_params:
            aggregate(df, param, param)


glueContext.forEachBatch(
    frame=dataframe_AmazonKinesis_node,
    batch_function=process_batch,
    options={
        "windowSize": "300 seconds",
        "checkpointLocation": args["TempDir"] + "/" + args["JOB_NAME"] + "/checkpoint/",
    },
)
job.commit()
