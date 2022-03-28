from typing import Any

from Commons.DataVersion import DataVersion
from Commons.FileWriter import FileWriter
from Commons.JsonFormatter import JsonFormatter
from Commons.Configurator import Configurator
from Commons.StorageS3 import StorageS3
from DataExtractor import DataExtractor


class Executor:
    def __init__(self, data_version: DataVersion) -> None:
        self.data_version = data_version

    def execute(self, channel: dict, storage: StorageS3, data_type: str = None) -> None:
        if data_type is "channel":
            items: list = list(channel.values())
            data: list = DataExtractor("channel").extract(items)
        else:
            response: Any = DataExtractor("video_id").extract(list(channel.values()))[0]
            items: list = list(map(lambda i: i['id']['videoId'], response['items']))
            data: list = DataExtractor().extract(items)
        json: Any = JsonFormatter().form(items, data, data_type)
        writer: FileWriter = FileWriter('tmp/' + Configurator.get_file_name(list(channel.values())[0], data_type))
        writer.writing(json)
        storage.upload(writer.get_path(), Configurator.get_dir_name(self.data_version, data_type))
        print("UPLOAD")
