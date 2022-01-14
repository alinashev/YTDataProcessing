from typing import Any

from Commons.APIkey import APIkey
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class VideoDataExtractor(DataExtractor):

    def request(self, channel_id, key):
        request: Any = build('youtube', 'v3', developerKey=key).search().list(
            part="snippet",
            channelId=channel_id,
            maxResults="50",
            order="rating"
        )
        return request.execute()

    def extract(self, ChannelsID: dict) -> dict:
        key = APIkey().get_key()
        list_req: list = list()
        values_channel_id = list(ChannelsID.values())

        i = 0
        while i < len(values_channel_id):
            try:
                list_req.append(self.request(values_channel_id[i], key))
            except Exception:
                key = APIkey().get_key(next_key="true")
                i = i - 1
            i = i + 1

        print("Data about video pulled")
        return dict(zip(list(map(lambda c: c, ChannelsID)), list_req))
