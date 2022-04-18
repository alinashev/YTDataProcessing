from typing import Any


class Configurator:
    def __init__(self, data_version, general_data_source=None, s3_general_agg_dir=None):
        self.data_version = data_version
        self.s3_general_agg_dir = s3_general_agg_dir
        self.general_data_source = general_data_source

    def get_file_name(self, channel_id: str, data_type: str = None) -> str:
        return "chd" + channel_id + ".json" if data_type is 'channel' else "vd" + channel_id + ".json"

    def get_dir_name(self, data_type: str = None) -> str:
        path: str = "Resources/" + self.data_version.get_date() + "/" + self.data_version.get_hour() + "/"
        return path + "channelData" if data_type is "channel" else path + "videoData"

    def get_channel_param(self) -> dict:
        return {
            "data_source": self.general_data_source + "/channelData",
            "data_type": "raw",
            "columns": ["items.id",
                        "items.statistics.subscriberCount",
                        "items.statistics.videoCount",
                        "items.statistics.viewCount"]
        }

    def get_video_param(self) -> dict:
        return {
            "data_source": self.general_data_source + "/videoData",
            "data_type": "raw",
            "columns": ["items.id",
                        "items.snippet.channelTitle",
                        "items.snippet.channelId",
                        "items.snippet.categoryId",
                        "items.statistics.commentCount",
                        "items.statistics.likeCount",
                        "items.statistics.viewCount"]
        }

    def get_hourly_aggregation_one(self) -> dict:
        return {
            "type": "hourly",
            "item": "viewCount",
            "ascending": True,
            "dir": self.s3_general_agg_dir + "/hourly/leastviewchannel",
            "mode": "append"
        }

    def get_hourly_aggregation_two(self) -> dict:
        return {
            "type": "hourly",
            "item": "subscriberCount",
            "ascending": False,
            "dir": self.s3_general_agg_dir + "/hourly/mostsubscriberchannel",
            "mode": "append"
        }

    def get_hourly_aggregation_three(self) -> dict:
        return {
            "type": "hourly",
            "item": "commentCount",
            "ascending": False,
            "dir": self.s3_general_agg_dir + "/hourly/mostcommentvideo",
            "mode": "append"
        }

    def get_hourly_aggregation_four(self) -> dict:
        return {
            "type": "hourly",
            "item": "likeCount",
            "ascending": False,
            "dir": self.s3_general_agg_dir + "/hourly/mostlikevideo",
            "mode": "append"
        }

    def get_daily_aggregation_one(self) -> dict:
        return {
            "data_source": self.s3_general_agg_dir + "/hourly/mostcommentvideo",
            "type": "daily",
            "item": "commentCount",
            "dir": self.s3_general_agg_dir + "/daily/mostcommentvideo",
            "mode": "overwrite"
        }

    def get_daily_aggregation_two(self) -> dict:
        return {
            "data_source": self.s3_general_agg_dir + "/hourly/mostlikevideo",
            "type": "daily",
            "item": "likeCount",
            "dir": self.s3_general_agg_dir + "/daily/mostlikevideo",
            "mode": "overwrite"
        }

    def get_all_configuration(self) -> list:
        return [
            {**self.get_channel_param(), **self.get_hourly_aggregation_one()},
            {**self.get_channel_param(), **self.get_hourly_aggregation_two()},
            {**self.get_video_param(), **self.get_hourly_aggregation_three()},
            {**self.get_video_param(), **self.get_hourly_aggregation_four()},
            self.get_daily_aggregation_one(),
            self.get_daily_aggregation_two()
        ]
