from typing import Any

from DWHEntities.Channel.DimChannel import DimChannel
from DWHEntities.Channel.DimDateChannel import DimDateChannel
from DWHEntities.Channel.DimTimeChannel import DimTimeChannel
from DWHEntities.Channel.FactChannel import FactChannel
from Transform.Parser import Parser


class ChannelParser(Parser):
    def __init__(self) -> None:
        self.fact_channel_obj_list: list = list()
        self.dim_channel_obj_list: list = list()

        self.dim_date_obj_list: list = list()
        self.dim_time_obj_list: list = list()

    def parse(self, json_string: Any, ChannelsID: Any) -> None:

        date: DimDateChannel = DimDateChannel()
        time: DimTimeChannel = DimTimeChannel()

        self.dim_date_obj_list.append(date)
        self.dim_time_obj_list.append(time)

        for channel_id in ChannelsID:
            self.dim_channel_obj_list.append(DimChannel(str(channel_id),
                                                        str(ChannelsID[channel_id])
                                                        )
                                             )

            try:
                subscriberCount: int = int(json_string[channel_id]["items"][0]["statistics"]["subscriberCount"])
            except KeyError:
                subscriberCount = subscriberCount

            self.fact_channel_obj_list.append(
                FactChannel(str(ChannelsID[channel_id]),
                            str(date.get_date_id()),
                            str(time.get_time_id()),
                            int(json_string[channel_id]["items"][0]["statistics"]["viewCount"]),
                            subscriberCount,
                            int(json_string[channel_id]["items"][0]["statistics"]["videoCount"])
                            )
            )

    def get_fact_channel_obj_list(self) -> list:
        return self.fact_channel_obj_list

    def get_dim_channel_obj_list(self) -> list:
        return self.dim_channel_obj_list

    def get_dim_date_obj_list(self) -> list:
        return self.dim_date_obj_list

    def get_dim_time_obj_list(self) -> list:
        return self.dim_time_obj_list
