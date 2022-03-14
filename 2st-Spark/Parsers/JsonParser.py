from abc import abstractmethod
from typing import Any


class JsonParser:
    @abstractmethod
    def parse(self, json: Any, schema: Any) -> Any:
        pass
