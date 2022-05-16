from typing import Any
from googleapiclient.discovery import build

from Commons.APIkey import APIkey


class Extractor:
    def __init__(self) -> None:
        self.api_key: APIkey = APIkey()

    def request(self, key: str) -> Any:
        request: Any = build('youtube', 'v3', developerKey=key)
        request = request.videos().list(part="id, statistics, snippet", chart="mostPopular", regionCode="ua")
        return request.execute()

    def extract(self) -> Any:
        key: Any = self.api_key.get_key()
        while True:
            try:
                return self.request(key)
            except Exception:
                key = self.api_key.get_key(key, next_key=True)
                print("KEY: ", key)
                self.extract()
