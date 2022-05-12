import googleapiclient

from typing import Any
from DataExtractor import DataExtractor
from Stream import Stream


class Executor:
    def execute(self) -> None:
        stream_name: str = "a-test"
        partition_key: str = "comments"
        response: Any = DataExtractor("video").extract()
        items: list = list()

        for i in response['items']:
            try:
                items.append(i['id'])
            except KeyError:
                print("KeyError: ", i['id'])
                continue

        for item in items:
            try:
                video_data: list = DataExtractor("comments").extract(item)
                self.send(stream_name, partition_key, video_data["items"])
                next_page_token = video_data['nextPageToken']
            except googleapiclient.errors.HttpError:
                print("Video has disabled comments")
                continue
            except KeyError:
                print("Key Error")
                continue

            while True:
                video_data: list = DataExtractor("commentNext").extract(item, next_page_token)
                self.send(stream_name, partition_key, video_data["items"])
                try:
                    next_page_token = video_data['nextPageToken']
                except KeyError:
                    print("No next page")
                    break

    def send(self, stream_name: str, partition_key: str, data: list) -> None:
        stream = Stream(stream_name)
        for d in data:
            stream.put_to_stream(d, partition_key)
