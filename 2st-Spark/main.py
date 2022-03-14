from pyspark.sql import SparkSession
from Commons.DataVersion import DataVersion
from DataFrameCreators.ChannelDataFrameCreator import ChannelDataFrameCreator
from DataFrameCreators.VideoDataFrameCreator import VideoDataFrameCreator
from Commons.StorageS3 import StorageS3
from SchemaBuilders.ChannelSchemaBuilder import ChannelSchemaBuilder
from SchemaBuilders.VideoSchemaBuilder import VideoSchemaBuilder


def main():
    spark_session: SparkSession = SparkSession.builder.appName("App").master("local[*]"). \
        config("spark.driver.memory", "1g").getOrCreate()

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

    video_schema: VideoSchemaBuilder = VideoSchemaBuilder().build(spark_session)
    video_df: VideoDataFrameCreator = VideoDataFrameCreator()
    video_df.create(spark_session, video_schema, video_data_folder_name).groupBy("categoryId").count().show()

    channel_schema: ChannelSchemaBuilder = ChannelSchemaBuilder().build(spark_session)
    channel_df: ChannelDataFrameCreator = ChannelDataFrameCreator()
    channel_df.create(spark_session, channel_schema, channel_data_folder_name).show()


if __name__ == '__main__':
    main()
