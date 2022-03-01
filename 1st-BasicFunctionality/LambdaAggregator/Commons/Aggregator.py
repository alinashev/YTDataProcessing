from typing import Any


class Aggregator:
    def __init__(self, connect) -> None:
        self.connect = connect

    def execute(self, query) -> Any:
        try:
            cursor: Any = self.connect.cursor()
            return cursor.execute(query).as_pandas()

        except Exception as error:
            print(error)