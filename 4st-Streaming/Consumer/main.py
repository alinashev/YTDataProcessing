import json

from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.dstream import TransformedDStream
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream

from Configurator import Configurator
from DataFrame import DataFrame
from DataVersion import DataVersion


def main():
    configurator: Configurator = Configurator()
    data_frame: DataFrame = DataFrame()
    data_version: DataVersion = DataVersion()

    aggregation_list: list = configurator.get_all_aggregate_params()

    spark = SparkSession.builder.appName("app").getOrCreate()
    sc = spark.sparkContext
    ssc = StreamingContext(sc, 300)

    kinesis: TransformedDStream = KinesisUtils.createStream(ssc=ssc,
                                                            kinesisAppName='CommentAggregator',
                                                            streamName='a-comments',
                                                            endpointUrl='https://kinesis.us-east-2.amazonaws.com',
                                                            regionName='us-east-2',
                                                            initialPositionInStream=InitialPositionInStream.LATEST,
                                                            checkpointInterval=5)

    lines: TransformedDStream = kinesis.map(lambda x: json.loads(x[:]))
    processed: TransformedDStream = lines.map(lambda x: json.loads(data_frame.collect(x)))
    try:
        transformed: TransformedDStream = processed.map(
            lambda x: (x['comment_id'], x['comment_text'], int(len(x['comment_text'])),
                       x['like_count'], x['totalReplayCount']))
        transformed.foreachRDD(lambda x: data_frame.transform(x, spark, data_version, aggregation_list))
    except KeyError:
        print("Key Error")

    ssc.start()
    ssc.awaitTermination()
