import googleapiclient

from typing import Any
from DataExtractor import DataExtractor
from Stream import Stream


class Executor:
    def execute(self, video) -> None:
        stream_name: str = "a-comments"
        partition_key: str = "comments"
        try:
            video_data: list = DataExtractor("comments").extract(video)
            self.send(stream_name, partition_key, video_data["items"])
            next_page_token = video_data['nextPageToken']
        except googleapiclient.errors.HttpError:
            print("Video has disabled comments")
        except KeyError:
            print("Key Error")

        while True:
            video_data: list = DataExtractor("commentNext").extract(video, next_page_token)
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
