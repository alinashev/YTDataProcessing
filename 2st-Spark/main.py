from pyspark.sql import SparkSession
from Aggregation.Aggregator import Aggregator
from Commons.DataVersion import DataVersion
from Commons.StorageS3 import StorageS3
from DataFrameCreators.ChannelDataFrameCreator import ChannelDataFrameCreator
from DataFrameCreators.VideoDataFrameCreator import VideoDataFrameCreator


def main():
    spark_session: SparkSession = SparkSession.builder.appName("App").master("local[8]"). \
        config("spark.driver.memory", "1g"). \
        config("spark.executor.memory", "1g"). \
        config("spark.memory.offHeap.enabled", True). \
        config("spark.memory.offHeap.size", "8g"). \
        getOrCreate()

    data_version: DataVersion = DataVersion()
    storage: StorageS3 = StorageS3()

    video_data_folder_name: str = "DATA/Vd"
    channel_data_folder_name: str = "DATA/Ch"

    video_data_s3_folder: str = "Resources" + "/" + data_version.get_date() + "/" + \
                                data_version.get_hour() + "/" + "categoryData"

    channel_data_s3_folder: str = "Resources" + "/" + data_version.get_date() + "/" + \
                                  data_version.get_hour() + "/" + "channelData"

    storage.download_folder(video_data_s3_folder, video_data_folder_name)
    storage.download_folder(channel_data_s3_folder, channel_data_folder_name)

    video_data_source = video_data_folder_name + "/*.json"
    video_df = VideoDataFrameCreator(spark_session, video_data_source, data_version).create()

    channel_data_source = channel_data_folder_name + "/*.json"
    channel_df = ChannelDataFrameCreator(spark_session, channel_data_source, data_version).create()

    most_comments_v_agg_dir = "SparkAggregation" + "/" + "most-comments-v" + "/" + data_version.get_date()
    most_liked_v_agg_file_dir = "SparkAggregation" + "/" + "most-liked-v" + "/" + data_version.get_date()
    least_view_count_ch_dir = "SparkAggregation" + "/" + "least-view-count-ch" + "/" + data_version.get_date()
    most_subscribed_ch_dir = "SparkAggregation" + "/" + "most-subscribed-ch" + "/" + data_version.get_date()

    most_comments_v_agg_file = "m-comm-" + data_version.get_hour() + ".parquet"
    most_liked_v_agg_file = "m-like-" + data_version.get_hour() + ".parquet"
    least_view_count_ch_file = "l-view-" + data_version.get_hour() + ".parquet"
    most_subscribed_ch_file = "m-subs-" + data_version.get_hour() + ".parquet"

    most_comments_v_df = Aggregator.aggregate(spark_session, video_df,
                                              open("Aggregation/Queries/mostCommentVideo.sql", 'r').read())
    most_liked_v_df = Aggregator.aggregate(spark_session, video_df,
                                           open("Aggregation/Queries/mostLikeVideo.sql", 'r').read())

    least_view_ch_df = Aggregator.aggregate(spark_session, channel_df,
                                            open("Aggregation/Queries/leastViewChannel.sql", 'r').read())
    most_subscribed_ch_df = Aggregator.aggregate(spark_session, channel_df,
                                                 open("Aggregation/Queries/mostSubscribedChannel.sql", 'r').read())

    most_comments_v_df.toPandas().to_parquet(most_comments_v_agg_file, engine='pyarrow')
    most_liked_v_df.toPandas().to_parquet(most_liked_v_agg_file, engine='pyarrow')
    least_view_ch_df.toPandas().to_parquet(least_view_count_ch_file, engine='pyarrow')
    most_subscribed_ch_df.toPandas().to_parquet(most_subscribed_ch_file, engine='pyarrow')

    storage.upload(most_comments_v_agg_dir, most_comments_v_agg_file)
    storage.upload(most_liked_v_agg_file_dir, most_liked_v_agg_file)
    storage.upload(least_view_count_ch_dir, least_view_count_ch_file)
    storage.upload(most_subscribed_ch_dir, most_subscribed_ch_file)

    data_for_daily_most_comment = "DailyAggregation/most_comments"
    data_for_daily_most_liked = "DailyAggregation/most_liked"

    storage.download_folder(most_comments_v_agg_dir, data_for_daily_most_comment)
    storage.download_folder(most_liked_v_agg_file_dir, data_for_daily_most_liked)

    daily_most_comments_v_agg_dir = "DailySparkAggregation" + "/" + "daily-most-comments-v" + "/" +\
                                    data_version.get_date()
    daily_most_liked_v_agg_file_dir = "DailySparkAggregation" + "/" + "daily-most-liked-v" + "/" +\
                                      data_version.get_date()

    daily_most_comments_v_agg_file = "daily-m-comm-" + data_version.get_hour() + ".parquet"
    daily_most_liked_v_agg_file = "daily-m-like-" + data_version.get_hour() + ".parquet"

    daily_m_comments_df = spark_session.read.format("parquet").load("DailyAggregation/most_comments")
    daily_most_comments_v_df = Aggregator.aggregate(spark_session, daily_m_comments_df,
                                                    open("Aggregation/Queries/dailyMostCommentVideo.sql", 'r').read())

    daily_most_comments_v_df.toPandas().to_parquet(daily_most_comments_v_agg_file, engine='pyarrow')
    storage.upload(daily_most_comments_v_agg_dir, daily_most_comments_v_agg_file)

    daily_m_liked_df = spark_session.read.format("parquet").load("DailyAggregation/most_liked")
    daily_most_liked_v_df = Aggregator.aggregate(spark_session, daily_m_liked_df,
                                                 open("Aggregation/Queries/dailyMostLikedVideo.sql", 'r').read())

    daily_most_liked_v_df.toPandas().to_parquet(daily_most_liked_v_agg_file, engine='pyarrow')
    storage.upload(daily_most_liked_v_agg_file_dir, daily_most_liked_v_agg_file)


if __name__ == '__main__':
    main()
