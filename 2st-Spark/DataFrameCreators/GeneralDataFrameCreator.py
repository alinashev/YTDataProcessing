from abc import abstractmethod
from typing import Any


class GeneralDataFrameCreator:
    @abstractmethod
    def create(self) -> Any:
        pass
