from typing import Any

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, lit

from Commons.DataVersion import DataVersion
from DataFrameCreators.GeneralDataFrameCreator import GeneralDataFrameCreator


class ChannelDataFrameCreator(GeneralDataFrameCreator):

    def __init__(self, spark_session: SparkSession, data_source: str, data_version: DataVersion):
        self.df = None
        self.data_source = data_source
        self.spark_session = spark_session
        self.data_version = data_version

    def create(self) -> Any:
        self.df = self.spark_session.read.json(
            self.data_source, multiLine="true").select(
            explode("info.items").alias("items")).select("items.id",
                                                         "items.statistics.subscriberCount",
                                                         "items.statistics.videoCount",
                                                         "items.statistics.viewCount"
                                                         ) \
            .withColumn("add_time", lit(self.data_version.get_date() + "-" + self.data_version.get_hour())) \
            .withColumn("add_date", lit(self.data_version.get_date())) \
            .withColumn("add_hour", lit(self.data_version.get_hour())).dropna()
        return self.df
