from typing import Any

from pyspark.sql.functions import col, max


class Aggregator:
    @staticmethod
    def aggregate(data_frame: Any, type: str, item: str, ascending: bool) -> Any:
        if type is "hourly":
            return data_frame.orderBy(item, ascending=ascending).limit(3)
        else:
            return data_frame.join(
                data_frame.groupBy(col("date"), col("id")).agg(max(col(item)).alias("likeCount")),
                on=["date", "id"], how='leftsemi').select("date", "id", item, "year", "month")
