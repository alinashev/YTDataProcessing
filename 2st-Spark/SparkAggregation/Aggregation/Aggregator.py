from typing import Any

from pyspark.sql import SparkSession


class Aggregator:
    @staticmethod
    def aggregate(spark_session: SparkSession, data_frame: Any, query: str) -> Any:
        temp_view_name: str = "temp"
        data_frame.createTempView(temp_view_name)
        result_df: Any = spark_session.sql(query.format(temp_view_name=temp_view_name))
        spark_session.catalog.dropTempView(temp_view_name)
        return result_df
