import os

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream


os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kinesis-asl_2.12:3.2.1 pyspark-shell'
app_name = "app"
sc = SparkContext("local[*]")
ssc = StreamingContext(sc, 1)

stream_name = "a-test"
endpoint = "https://kinesis.us-east-2.amazonaws.com"
region = "us-east-2"

kinesis_stream = KinesisUtils.createStream(ssc=ssc,
                                           kinesisAppName=app_name,
                                           streamName=stream_name,
                                           endpointUrl=endpoint,
                                           regionName=region,
                                           initialPositionInStream=InitialPositionInStream.TRIM_HORIZON,
                                           checkpointInterval=2)
