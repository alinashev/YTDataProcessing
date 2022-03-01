from typing import Any

import pandas
from pandas import DataFrame


class ParquetFormat:
    @staticmethod
    def load(entity: Any, file_name: str) -> None:
        data_frame: DataFrame = pandas.DataFrame([e.to_dict() for e in entity])
        data_frame.to_parquet(file_name, engine='pyarrow')

    @staticmethod
    def read(file_name) -> DataFrame:
        return pandas.read_parquet(file_name)