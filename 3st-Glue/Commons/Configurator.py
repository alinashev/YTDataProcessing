class Configurator:
    def __init__(self, data_version, general_data_source, s3_general_agg_dir):
        self.data_version = data_version
        self.s3_general_agg_dir = s3_general_agg_dir
        self.general_data_source = general_data_source

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
            "query": """SELECT * FROM {temp_view_name} ORDER BY viewCount ASC LIMIT 3""",
            "dir": self.s3_general_agg_dir + "/hourly/leastviewchannel",
            "mode": "append"
        }

    def get_hourly_aggregation_two(self) -> dict:
        return {
            "query": """SELECT * FROM {temp_view_name} ORDER BY subscriberCount DESC LIMIT 3""",
            "dir": self.s3_general_agg_dir + "/hourly/mostsubscriberchannel",
            "mode": "append"
        }

    def get_hourly_aggregation_three(self) -> dict:
        return {
            "query": """SELECT * FROM {temp_view_name} ORDER BY commentCount DESC LIMIT 3""",
            "dir": self.s3_general_agg_dir + "/hourly/mostcommentvideo",
            "mode": "append"
        }

    def get_hourly_aggregation_four(self) -> dict:
        return {
            "query": """SELECT * FROM {temp_view_name} ORDER BY likeCount DESC LIMIT 3""",
            "dir": self.s3_general_agg_dir + "/hourly/mostlikevideo",
            "mode": "append"
        }

    def get_daily_aggregation_one(self) -> dict:
        return {
            "data_source": self.s3_general_agg_dir + "/hourly/mostcommentvideo",
            "query": """SELECT DISTINCT a.date, a.id, a.commentCount, b.year, b.month 
                        FROM(SELECT date, id, MAX(commentCount) as commentCount 
                        FROM {temp_view_name} GROUP BY date, id)
                        AS a LEFT JOIN(SELECT id, date, year, month 
                        FROM {temp_view_name}) AS b ON a.date = b.date""",
            "dir": self.s3_general_agg_dir + "/daily/mostcommentvideo",
            "mode": "overwrite"
        }

    def get_daily_aggregation_two(self) -> dict:
        return {
            "data_source": self.s3_general_agg_dir + "/hourly/mostlikevideo",
            "query": """SELECT DISTINCT a.date, a.id, a.likeCount, b.year, b.month
                        FROM(SELECT date, id, MAX(likeCount) as likeCount 
                        FROM {temp_view_name} GROUP BY date, id )
                        AS a LEFT JOIN(SELECT id, date, year, month 
                        FROM {temp_view_name}) AS b ON a.date = b.date""",
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
