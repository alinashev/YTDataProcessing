from Commons.APIkey import APIkey
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class VideoCategoryExtractor(DataExtractor):

    def __init__(self):
        self.list_video_id = list()

    def request(self, video_id, key) -> None:
        request = build('youtube', 'v3', developerKey=key).videos().list(
            part="id,snippet,statistics",
            id=video_id.get_video_id(),
        )
        return request.execute()

    def extract(self, video_id_list) -> dict:
        key = APIkey().get_key()
        list_response: list = list()

        i = 0
        while i < len(video_id_list):
            try:
                list_response.append(self.request(video_id_list[i], key))
                self.list_video_id.append(video_id_list[i].get_video_id())
            except Exception:
                key = APIkey().get_key(next_key="true")
                i = i - 1
            i = i + 1
        print('Data from youtube received')
        return dict(zip(self.list_video_id, list_response))

    def get_video_id_list(self) -> list:
        return self.list_video_id
