from typing import Any


class JsonFormatter:

    def form(self, items:list, data: list, data_type=None) -> Any:
        return self.get_channel_json(items, data) if data_type is "channel" else self.get_video_json(items, data)

    @staticmethod
    def get_channel_json(channel: list, channel_data: list) -> dict:
        channel_id: dict = {"channelName": [*channel][0]}
        values: dict = {"info": channel_data}
        return dict({**channel_id, **values})

    @staticmethod
    def get_video_json(video_list: list, video_data: list) -> list:
        keys: list = list(map(lambda i: dict({"Id": i}), video_list))
        values: list = list(map(lambda i: dict({"info": i}), video_data))
        return list(map(lambda i, j: dict({**i, **j}), keys, values))
