from Aggregation.Aggregator import Aggregator
from Commons.StorageS3 import StorageS3
from DataFrameCreator import DataFrameCreator


class Executor:
    def __init__(self, data_version, spark_session) -> None:
        self.data_version = data_version
        self.spark_session = spark_session
        self.storage = StorageS3()

    def execute(self, s3_folder, data_source, query, file, dir, data_type=None, columns=None) -> None:
        self.storage.download_folder(s3_folder, data_source)
        df = DataFrameCreator(self.spark_session, data_source, self.data_version, data_type, columns).create()
        aggregated_df = Aggregator.aggregate(self.spark_session, df, open(query, 'r').read())
        aggregated_df.toPandas().to_parquet(file, engine='pyarrow')
        self.storage.upload(dir, file)
