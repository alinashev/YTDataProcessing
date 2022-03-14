from abc import abstractmethod
from typing import Any

from pyspark.sql import SparkSession


class GeneralDataFrameCreator:
    @abstractmethod
    def create(self, spark_session: SparkSession, schema: Any, folder_name: str) -> Any:
        pass
