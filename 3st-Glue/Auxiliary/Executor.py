from Auxiliary.Aggregator import Aggregator
from Auxiliary.DataFrameCreator import DataFrameCreator


class Executor:
    def __init__(self, data_version, spark_session) -> None:
        self.data_version = data_version
        self.spark_session = spark_session

    def execute(self, data_source, dir, mode, type, item, ascending=None, data_type=None, columns=None) -> None:
        df = DataFrameCreator(self.spark_session, data_source, self.data_version, data_type, columns).create()
        aggregated_df = Aggregator.aggregate(df, type, item, ascending)
        aggregated_df.write.mode(mode).partitionBy("date").parquet(dir)
