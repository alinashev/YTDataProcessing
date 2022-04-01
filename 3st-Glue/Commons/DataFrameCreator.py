from typing import Any

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, lit

from Commons.DataVersion import DataVersion


class DataFrameCreator:
    def __init__(self, spark_session: SparkSession, data_source: str, data_version: DataVersion, param=None,
                 columns: list = None) -> None:
        self.data_source = data_source
        self.spark_session = spark_session
        self.data_version = data_version
        self.columns = columns
        self.param = param
        self.df = None

    def create(self) -> Any:
        if self.param == "raw":
            self.df = self.spark_session.read.json(
                self.data_source + "/*.json", multiLine="true").select(
                explode("info.items").alias("items")).select(self.columns)\
                .withColumn("time", lit(self.data_version.get_date() + "-" + self.data_version.get_hour())) \
                .withColumn("year", lit(self.data_version.get_year())) \
                .withColumn("month", lit(self.data_version.get_month())) \
                .withColumn("date", lit(self.data_version.get_date())) \
                .withColumn("hour", lit(self.data_version.get_hour())).dropna()
        else:
            self.df = self.spark_session.read.format("parquet").load(self.data_source)
        return self.df
