from typing import Any
from pyspark.sql.functions import explode, lit
from pyspark.sql.utils import AnalysisException
from Parsers.JsonParser import JsonParser


class ChannelJsonParser(JsonParser):

    def parse(self, json: Any, schema: Any = None) -> Any:
        json: Any = json.drop('None')
        channel_name: str = str(json.columns[0])
        try:
            channel_data_frame: Any = json.select(explode(channel_name + ".items").alias("items")
                                                  ).select("items.id",
                                                           "items.statistics.subscriberCount",
                                                           "items.statistics.videoCount",
                                                           "items.statistics.viewCount")
        except AnalysisException:
            raise
        channel_data_frame = channel_data_frame.withColumn("channelTitle", lit(channel_name))
        return channel_data_frame
