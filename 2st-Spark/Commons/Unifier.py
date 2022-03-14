import functools
from typing import Any


class Unifier:
    @staticmethod
    def union_data_frame(data_frame: Any) -> Any:
        return functools.reduce(lambda df1, df2: df1.union(
            df2.select(df1.columns)), data_frame)
