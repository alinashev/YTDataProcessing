from Commons.Aggregator import Aggregator
from Commons.DataFrameCreator import DataFrameCreator


class Executor:
    def __init__(self, data_version, spark_session) -> None:
        self.data_version = data_version
        self.spark_session = spark_session

    def execute(self, data_source, query, dir, mode, data_type=None, columns=None) -> None:
        df = DataFrameCreator(self.spark_session, data_source, self.data_version, data_type, columns).create()
        aggregated_df = Aggregator.aggregate(self.spark_session, df, query)
        aggregated_df.write.mode(mode).parquet(dir)
