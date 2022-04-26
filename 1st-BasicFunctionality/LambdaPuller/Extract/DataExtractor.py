from abc import ABC, abstractmethod
from typing import Any


class DataExtractor(ABC):

    @abstractmethod
    def extract(self, ChannelsID: dict) -> Any:
        pass
