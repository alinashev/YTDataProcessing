from typing import Any
from googleapiclient.discovery import build
from Commons.APIkey import APIkey


class DataExtractor:
    def __init__(self, param: str = None) -> None:
        self.api_key: APIkey = APIkey()
        self.param = param

    def request(self, items_id: str, key: str) -> Any:
        if self.param is "channel":
            request = build('youtube', 'v3', developerKey=key).channels().list(part="statistics", id=items_id)
        elif self.param is "video_id":
            request = build('youtube', 'v3', developerKey=key).search().list(part="snippet", channelId=items_id,
                                                                                  maxResults="50", order="rating")
        else:
            request = build('youtube', 'v3', developerKey=key).videos().list(part="id,snippet,statistics", id=items_id)
        return request.execute()

    def extract(self, items: list) -> list:
        key: Any = self.api_key.get_key()
        list_response: list = list()
        i = 0
        while i < len(items):
            try:
                list_response.append(self.request(items[i], key))
            except Exception:
                key = self.api_key.get_key(key, next_key=True)
                i = i - 1
            i = i + 1
        return list_response
