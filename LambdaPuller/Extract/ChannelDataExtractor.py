from Commons.APIkey import APIkey
from typing import Any
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class ChannelDataExtractor(DataExtractor):
    def request(self, channel_id, key) -> Any:
        request: Any = build('youtube', 'v3', developerKey=key).channels().list(
            part="statistics",
            id=channel_id
        )
        return request.execute()

    def extract(self, ChannelsID: dict) -> dict:
        api_key: APIkey = APIkey()
        key: Any = api_key.get_key()
        list_req: list = list()
        values_channel_id = list(ChannelsID.values())

        i: int = 0
        while i < len(values_channel_id):
            try:
                print("try: ", key)
                list_req.append(self.request(values_channel_id[i], key))
            except Exception:
                current_key: Any = key
                key = api_key.get_key(current_key, next_key="true")
                print("except: ", key)
                i = i - 1
            i = i + 1

        print("Data about channels pulled")

        return dict(zip(list(map(lambda c: c, ChannelsID)), list_req))
