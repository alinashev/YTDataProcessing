from typing import Any
from googleapiclient.discovery import build

from APIkey import APIkey


class DataExtractor:
    def __init__(self, param: str = None) -> None:
        self.api_key: APIkey = APIkey()
        self.param = param

    def request(self, key: str, item: str = None, nextPageToken: str = None) -> Any:
        request: Any = build('youtube', 'v3', developerKey=key)
        if self.param is "video":
            request = request.videos().list(part="id, statistics, snippet", chart="mostPopular", regionCode="ua")
        else:
            request = request.commentThreads()
            if self.param is "comments":
                request = request.list(part='snippet, replies', textFormat='plainText', maxResults='100', order='time',
                                       videoId=item)
            elif self.param is "commentNext":
                request = request.list(part='snippet, replies', textFormat='plainText', maxResults='100', order='time',
                                       videoId=item, pageToken=nextPageToken)
        return request.execute()

    def extract(self, item: list = None, nextPageToken: str = None) -> Any:
        items = list()
        if item is None:
            items = [1]
        else:
            items.append(item)

        key: Any = self.api_key.get_key()
        list_response: list = list()
        i = 0
        while i < len(items):
            try:
                list_response.append(self.request(key, items[i], nextPageToken))
            except Exception:
                key = self.api_key.get_key(key, next_key=True)
                print("KEY: ", key)
                i = i - 1
            i = i + 1
        return list_response[0]
