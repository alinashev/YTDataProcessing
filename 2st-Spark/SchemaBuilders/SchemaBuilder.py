from abc import abstractmethod
from typing import Any


class SchemaBuilder:
    @abstractmethod
    def build(self, spark_session: Any) -> Any:
        pass
