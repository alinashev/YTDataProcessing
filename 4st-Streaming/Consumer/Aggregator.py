from pyspark.sql import DataFrame


class Aggregator:
    @staticmethod
    def aggregate(df, param, out_dir) -> None:
        new_df: DataFrame = df.orderBy(param, ascending=False).limit(1)
        new_df.show()
        new_df.write.mode('append').partitionBy('date', 'hour', 'time_chunk').parquet(out_dir)
