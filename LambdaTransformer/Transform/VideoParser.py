from typing import Any

from DWHEntities.Video.DimDateVideo import DimDateVideo
from DWHEntities.Video.DimTimeVideo import DimTimeVideo
from DWHEntities.Video.DimVideo import DimVideo
from DWHEntities.Video.FactVideo import FactVideo
from Transform.Parser import Parser


class VideoParser(Parser):
    def __init__(self) -> None:
        self.fact_video_obj_list: list = list()
        self.dim_video_obj_list: list = list()
        self.dim_date_obj_list: list = list()
        self.dim_time_obj_list: list = list()

    def parse(self, json_string: Any, video_obj_list: Any) -> None:

        date: DimDateVideo = DimDateVideo()
        time: DimTimeVideo = DimTimeVideo()

        self.dim_date_obj_list.append(date)
        self.dim_time_obj_list.append(time)

        i = 0
        while i < len(video_obj_list):
            obj = video_obj_list[i]
            try:
                res_description: str = str(
                    json_string[obj.get_video_id()]['items'][0]['snippet']['localized']['description'])
            except:
                res_description = None

            try:
                res_view_count: int = int(json_string[obj.get_video_id()]['items'][0]['statistics']['viewCount'])
            except:
                res_view_count = 0

            try:
                res_like_count: int = int(json_string[obj.get_video_id()]['items'][0]['statistics']['likeCount'])
            except:
                res_like_count = 0

            try:
                res_category_id: str = str(json_string[obj.get_video_id()]['items'][0]['snippet']['categoryId'])
            except:
                res_category_id = None

            try:
                res_title: str = str(json_string[obj.get_video_id()]['items'][0]['snippet']['localized']['title'])
            except:
                res_title = None

            try:
                res_comment_count: int = int(json_string[obj.get_video_id()]['items'][0]['statistics']['commentCount'])
            except:
                res_comment_count = 0

            self.dim_video_obj_list.append(
                DimVideo(str(obj.get_video_id()),
                         str(obj.get_channel_id()),
                         str(obj.get_channel_name()),
                         res_title,
                         res_description,
                         res_category_id
                         ))

            self.fact_video_obj_list.append(
                FactVideo(
                    str(obj.get_video_id()),
                    str(date.get_date_id()),
                    str(time.get_time_id()),
                    res_view_count,
                    res_like_count,
                    res_comment_count
                )
            )
            i = i + 1

    def get_fact_video_obj_list(self) -> list:
        return self.fact_video_obj_list

    def get_dim_video_obj_list(self) -> list:
        return self.dim_video_obj_list

    def get_dim_date_obj_list(self) -> list:
        return self.dim_date_obj_list

    def get_dim_time_obj_list(self) -> list:
        return self.dim_time_obj_list
