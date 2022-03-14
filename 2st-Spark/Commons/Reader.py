from typing import Any

from pyspark.sql import SparkSession


class Reader:
    @staticmethod
    def read_json(spark_session: SparkSession, path: str) -> Any:
        return spark_session.read.json(path, multiLine="true")
