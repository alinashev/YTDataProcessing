from typing import Any


class Configurator:
    @staticmethod
    def get_file_name(channel_id: str, data_type: str = None) -> str:
        return "chd" + (channel_id + '.json') if data_type is 'channel' else "vd" + channel_id + '.json'

    @staticmethod
    def get_dir_name(data_version: Any, data_type: str = None) -> str:
        path: str = "Resources/" + data_version.get_date() + "/" + data_version.get_hour() + "/"
        return path + "channelData/" if data_type is "channel" else path + "videoData/"
