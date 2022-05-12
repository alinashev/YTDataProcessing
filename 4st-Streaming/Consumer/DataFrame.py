import json
from typing import Any
from pyspark.sql.functions import lit
from Aggregator import Aggregator


class DataFrame:
    def transform(self, rdd, spark, data_version, agg_params) -> None:
        if not rdd.isEmpty():
            schema: list = ['comment_id', 'comment_text', 'length', 'like', 'reply']
            df: Any = spark.createDataFrame(rdd, schema=schema) \
                .withColumn('date', lit(data_version.get_date())) \
                .withColumn('hour', lit(data_version.get_hour())) \
                .withColumn('time_chunk', lit(int(data_version.get_minute()) // 5))
            for i in agg_params:
                param = i.get("param")
                out_dir = i.get("out_dir")
                Aggregator.aggregate(df, param, out_dir)

    def collect(self, json_str) -> str:
        comment_id: dict = {"comment_id": json_str["snippet"]["topLevelComment"]["id"]}
        video_id: dict = {"video_id": json_str["snippet"]["videoId"]}
        text: dict = {"comment_text": json_str["snippet"]["topLevelComment"]["snippet"]["textOriginal"]}
        like_count: dict = {"like_count": json_str["snippet"]["topLevelComment"]["snippet"]["likeCount"]}
        replay: dict = {"totalReplayCount": json_str["snippet"]["totalReplyCount"]}

        data: dict = {**comment_id, **video_id, **text, **like_count, **replay}
        return str(json.dumps(data))
