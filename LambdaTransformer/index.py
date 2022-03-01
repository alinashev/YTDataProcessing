import os
from Commons.DataVersion import DataVersion
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Load.Loader import Loader
from Load.ParquetFormat import ParquetFormat
from Transform.ChannelParser import ChannelParser
from Transform.VideoIDParser import VideoIDParser
from Transform.VideoParser import VideoParser


def lambda_handler(event, context):
    version = DataVersion()

    ch_name = list(event.keys())[0]
    ch_id = event[ch_name]

    channel_id: dict = {ch_name: ch_id}

    storage: StorageS3 = StorageS3(bucket_name=os.environ.get("BucketName"))

    chd_file_name: str = "chd" + ch_id + ".json"
    vd_file_name: str = "vd" + ch_id + ".json"
    ctd_file_name: str = "ctd" + ch_id + ".json"

    storage.download_file(
        "Resources/" + version.get_date() + "/" + version.get_hour() + "/channelData/" + chd_file_name,
        '/tmp/' + chd_file_name)

    storage.download_file(
        "Resources/" + version.get_date() + "/" + version.get_hour() + "/videoData/" + vd_file_name,
        '/tmp/' + vd_file_name)

    storage.download_file(
        "Resources/" + version.get_date() + "/" + version.get_hour() + "/categoryData/" + ctd_file_name,
        '/tmp/' + ctd_file_name)

    chd_reader: ReaderJSON = ReaderJSON('/tmp/' + chd_file_name)
    vd_reader: ReaderJSON = ReaderJSON('/tmp/' + vd_file_name)
    ctd_reder: ReaderJSON = ReaderJSON('/tmp/' + ctd_file_name)

    chd_json: dict = chd_reader.get_json()
    vd_json: dict = vd_reader.get_json()
    ctd_json: dict = ctd_reder.get_json()

    chd_parser: ChannelParser = ChannelParser()
    vd_id_parser: VideoIDParser = VideoIDParser()
    ctd_parser: VideoParser = VideoParser()

    chd_parser.parse(chd_json, channel_id)
    video_id_list = vd_id_parser.parse(vd_json, channel_id)
    ctd_parser.parse(ctd_json, video_id_list)

    ParquetFormat.load(chd_parser.get_fact_channel_obj_list(), '/tmp/' + "FC-" + ch_id + ".parquet")
    ParquetFormat.load(chd_parser.get_dim_channel_obj_list(), '/tmp/' + "DC-" + ch_id + ".parquet")
    ParquetFormat.load(chd_parser.get_dim_time_obj_list(), '/tmp/' + "DTC-" + ch_id + ".parquet")

    ParquetFormat.load(ctd_parser.get_fact_video_obj_list(), '/tmp/' + "FV-" + ch_id + ".parquet")
    ParquetFormat.load(ctd_parser.get_dim_video_obj_list(), '/tmp/' + "DV-" + ch_id + ".parquet")
    ParquetFormat.load(ctd_parser.get_dim_time_obj_list(), '/tmp/' + "DTV-" + ch_id + ".parquet")

    storage.upload('/tmp/' + "FC-" + ch_id + ".parquet",
                   "Data/Channel/FactChannel/" + version.get_date() + "/" + version.get_hour())
    storage.upload('/tmp/' + "DC-" + ch_id + ".parquet",
                   "Data/Channel/DimChannel/" + version.get_date() + "/" + version.get_hour())
    storage.upload('/tmp/' + "DTC-" + ch_id + ".parquet",
                   "Data/Channel/DimTimeChannel/" + version.get_date() + "/" + version.get_hour())

    storage.upload('/tmp/' + "FV-" + ch_id + ".parquet",
                   "Data/Video/FactVideo/" + version.get_date() + "/" + version.get_hour())
    storage.upload('/tmp/' + "DV-" + ch_id + ".parquet",
                   "Data/Video/DimVideo/" + version.get_date() + "/" + version.get_hour())
    storage.upload('/tmp/' + "DTV-" + ch_id + ".parquet",
                   "Data/Video/DimTimeVideo/" + version.get_date() + "/" + version.get_hour())

    Loader.load("Tables/factChannel.sql")
    Loader.load("Tables/dimChannel.sql")
    Loader.load("Tables/dimTimeChannel.sql")

    Loader.load("Tables/factVideo.sql")
    Loader.load("Tables/dimVideo.sql")
    Loader.load("Tables/dimTimeVideo.sql")

    return {
        'statuscode': 200
    }