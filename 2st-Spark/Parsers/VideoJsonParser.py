from typing import Any
from pyspark.sql.functions import explode
from pyspark.sql.utils import AnalysisException
from Parsers.JsonParser import JsonParser
from Commons.Unifier import Unifier


class VideoJsonParser(JsonParser):

    def parse(self, json: Any, schema: Any) -> Any:
        data_frame: Any = schema
        json: Any = json.drop('None')
        video_name_list: list = json.columns

        try:
            for video_name in video_name_list:
                video_data_frame: Any = json.select(explode(video_name + ".items").alias("items")
                                                    ).select("items.id",
                                                             "items.snippet.channelTitle",
                                                             "items.snippet.channelId",
                                                             "items.snippet.categoryId",
                                                             "items.statistics.commentCount",
                                                             "items.statistics.likeCount",
                                                             "items.statistics.viewCount"
                                                             )
                data_frame = Unifier.union_data_frame([data_frame, video_data_frame])
        except AnalysisException:
            raise
        return data_frame
