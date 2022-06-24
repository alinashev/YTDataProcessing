from typing import Any
from googleapiclient.discovery import build

from Commons.APIkey import APIkey


class DataExtractor:
    def __init__(self, param: str = None) -> None:
        self.api_key: APIkey = APIkey()
        self.param = param

    def request(self, key: str, item: str = None, nextPageToken: str = None) -> Any:
        request: Any = build('youtube', 'v3', developerKey=key).commentThreads()
        if self.param is "comments":
            request = request.list(part='snippet, replies', textFormat='plainText', maxResults='100', order='time',
                                   videoId=item)
        elif self.param is "commentNext":
            request = request.list(part='snippet, replies', textFormat='plainText', maxResults='100', order='time',
                                   videoId=item, pageToken=nextPageToken)
        return request.execute()

    def extract(self, item: list, nextPageToken: str = None) -> Any:
        key: Any = self.api_key.get_key()
        while True:
            try:
                return self.request(key, item, nextPageToken)
            except Exception:
                key = self.api_key.get_key(key, next_key=True)
                print("KEY: ", key)
                self.extract(item, nextPageToken)
