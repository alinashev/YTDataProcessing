from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    @abstractmethod
    def parse(self, json_string: Any, ChannelsID: Any) -> list:
        pass