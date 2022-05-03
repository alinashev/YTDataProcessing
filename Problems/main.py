from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream


app_name = "app"
sc = SparkContext()
ssc = StreamingContext(sc, 1)

stream_name = "a-test"
endpoint = "https://kinesis.us-east-2.amazonaws.com"
region = "us-east-2"

kinesis_stream = KinesisUtils.createStream(ssc=ssc, kinesisAppName=app_name, streamName=stream_name,
                                           endpointUrl=endpoint, regionName=region,
                                           initialPositionInStream=str(InitialPositionInStream.TRIM_HORIZON),
                                           checkpointInterval=2)
