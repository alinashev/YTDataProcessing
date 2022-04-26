class Configurator:
    def __init__(self, data_version):
        self.data_version = data_version

    def get_channel_param(self) -> dict:
        return {
            "s3_folder": "Resources/" + self.data_version.get_date() + "/" + self.data_version.get_hour() + "/channelData",
            "data_source": "DATA/Ch",
            "data_type": "raw",
            "columns": ["items.id",
                        "items.statistics.subscriberCount",
                        "items.statistics.videoCount",
                        "items.statistics.viewCount"]
        }

    def get_video_param(self) -> dict:
        return {
            "s3_folder": "Resources/" + self.data_version.get_date() + "/" + \
                         self.data_version.get_hour() + "/categoryData",
            "data_source": "DATA/Vd",
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
            "query": "Aggregation/Queries/leastViewChannel.sql",
            "file": "l-view-" + self.data_version.get_hour() + ".parquet",
            "dir": "SparkAggregation/least-view-count-ch/" + self.data_version.get_date()
        }

    def get_hourly_aggregation_two(self) -> dict:
        return {
            "query": "Aggregation/Queries/mostSubscribedChannel.sql",
            "file": "m-subs-" + self.data_version.get_hour() + ".parquet",
            "dir": "SparkAggregation/most-subscribed-ch/" + self.data_version.get_date()
        }

    def get_hourly_aggregation_three(self) -> dict:
        return {
            "query": "Aggregation/Queries/mostCommentVideo.sql",
            "file": "m-comm-" + self.data_version.get_hour() + ".parquet",
            "dir": "SparkAggregation/most-comments-v/" + self.data_version.get_date()
        }

    def get_hourly_aggregation_four(self) -> dict:
        return {
            "query": "Aggregation/Queries/mostLikeVideo.sql",
            "file": "m-like-" + self.data_version.get_hour() + ".parquet",
            "dir": "SparkAggregation/most-liked-v/" + self.data_version.get_date()
        }

    def get_daily_aggregation_one(self) -> dict:
        return {
            "s3_folder": "SparkAggregation/most-comments-v/" + self.data_version.get_date(),
            "data_source": "DailyAggregation/most_comments",
            "query": "Aggregation/Queries/dailyMostCommentVideo.sql",
            "file": "daily-m-comm-" + self.data_version.get_hour() + ".parquet",
            "dir": "DailySparkAggregation/daily-most-comments-v/" + self.data_version.get_date()
        }

    def get_daily_aggregation_two(self) -> dict:
        return {
            "s3_folder": "SparkAggregation" + "/" + "most-liked-v" + "/" + self.data_version.get_date(),
            "data_source": "DailyAggregation/most_liked",
            "query": "Aggregation/Queries/dailyMostLikedVideo.sql",
            "file": "daily-m-like-" + self.data_version.get_hour() + ".parquet",
            "dir": "DailySparkAggregation/daily-most-liked-v/" + self.data_version.get_date()
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
