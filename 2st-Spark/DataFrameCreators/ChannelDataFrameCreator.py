import os
from typing import Any
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
from Commons.Reader import Reader
from Commons.Unifier import Unifier
from DataFrameCreators.GeneralDataFrameCreator import GeneralDataFrameCreator
from Parsers.ChannelJsonParser import ChannelJsonParser


class ChannelDataFrameCreator(GeneralDataFrameCreator):

    def create(self, spark_session: SparkSession, schema: Any, folder_name: str) -> Any:
        general_channel_data_frame: Any = schema
        try:
            for filename in os.listdir(folder_name):
                try:
                    channel_json: ChannelJsonParser = ChannelJsonParser()
                    single_channel_data_frame: Any = channel_json.parse(
                        Reader.read_json(spark_session, os.path.join(folder_name, filename)),
                        schema)
                except AnalysisException:
                    print("AnalysisException: " + filename)
                    continue
                general_channel_data_frame = Unifier.union_data_frame(
                    [general_channel_data_frame, single_channel_data_frame])
            return general_channel_data_frame
        except FileNotFoundError:
            print("The folder does not exist.")
        return general_channel_data_frame
