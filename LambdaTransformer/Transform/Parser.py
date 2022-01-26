from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    @abstractmethod
    def parse(self, json_string: Any, collection: Any) -> Any:
        pass
