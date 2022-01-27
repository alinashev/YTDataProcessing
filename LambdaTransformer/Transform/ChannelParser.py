from typing import Any

from DWHEntities.Channel.DimChannel import DimChannel
from DWHEntities.Channel.DimTimeChannel import DimTimeChannel
from DWHEntities.Channel.FactChannel import FactChannel
from Transform.Parser import Parser


class ChannelParser(Parser):
    def __init__(self) -> None:
        self.fact_channel_obj_list: list = list()
        self.dim_channel_obj_list: list = list()

        self.dim_time_obj_list: list = list()

    def parse(self, json_string: Any, ChannelsID: Any) -> None:

        time: DimTimeChannel = DimTimeChannel()

        self.dim_time_obj_list.append(time)

        for channel_id in ChannelsID:
            self.dim_channel_obj_list.append(DimChannel(str(channel_id),
                                                        str(ChannelsID[channel_id])
                                                        )
                                             )

            viewCount: int = 0
            try:
                viewCount = int(json_string[channel_id]["items"][0]["statistics"]["viewCount"])
            except KeyError:
                print("viewCount: ", viewCount, "FILE_NAME: ", ChannelsID[channel_id], " CHANNEL_NAME: ", channel_id)
                viewCount = 0

            subscriberCount: int = 0
            try:
                subscriberCount = int(json_string[channel_id]["items"][0]["statistics"]["subscriberCount"])
            except KeyError:
                print("subscriberCount: ", subscriberCount, "FILE_NAME: ", ChannelsID[channel_id], " CHANNEL_NAME: ",
                      channel_id)
                subscriberCount = 0

            videoCount = 0
            try:
                videoCount = int(json_string[channel_id]["items"][0]["statistics"]["videoCount"])
            except KeyError:
                print("videoCount: ", videoCount, "FILE_NAME: ", ChannelsID[channel_id], " CHANNEL_NAME: ", channel_id)
                videoCount = 0

            self.fact_channel_obj_list.append(
                FactChannel(str(ChannelsID[channel_id]),
                            str(time.get_time_id()),
                            viewCount,
                            subscriberCount,
                            videoCount
                            )
            )

    def get_fact_channel_obj_list(self) -> list:
        return self.fact_channel_obj_list

    def get_dim_channel_obj_list(self) -> list:
        return self.dim_channel_obj_list

    def get_dim_time_obj_list(self) -> list:
        return self.dim_time_obj_list
