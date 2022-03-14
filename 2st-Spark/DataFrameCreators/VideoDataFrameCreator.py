import os
from typing import Any
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
from DataFrameCreators.GeneralDataFrameCreator import GeneralDataFrameCreator
from Parsers.VideoJsonParser import VideoJsonParser
from Commons.Reader import Reader
from Commons.Unifier import Unifier


class VideoDataFrameCreator(GeneralDataFrameCreator):

    def create(self, spark_session: SparkSession, schema: Any, folder_name: str) -> Any:
        general_video_data_frame: Any = schema
        try:
            for filename in os.listdir(folder_name):
                try:
                    video_json: VideoJsonParser = VideoJsonParser()
                    single_video_data_frame: Any = video_json.parse(
                        Reader.read_json(spark_session, os.path.join(folder_name, filename)),
                        schema)
                except AnalysisException:
                    print("AnalysisException: " + filename)
                    continue
                general_video_data_frame = Unifier.union_data_frame(
                    [general_video_data_frame, single_video_data_frame])
            return general_video_data_frame
        except FileNotFoundError:
            print("The folder does not exist.")
        return general_video_data_frame
