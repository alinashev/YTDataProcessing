import os
from datetime import datetime
from Commons.FileWriter import FileWriter
from Commons.StorageS3 import StorageS3
from Extract.ChannelDataExtractor import ChannelDataExtractor
from Extract.VideoCategoryExtractor import VideoCategoryExtractor
from Extract.VideoDataExtractor import VideoDataExtractor
from LambdaPuller.Commons.ServiceSQS import ServiceSQS
from Transform.VideoIDParser import VideoIDParser


def lambda_handler(event, context):
    channel = (event['Records'][0]['body'])
    future_message = channel

    folder_name = str(datetime.now().date()) + "/" + \
                  str(datetime.now().hour) + "h"

    name = channel.split()[0]
    id = channel.split()[1]

    channel_id: dict = {name: id}

    channel_file_name = "chd" + str(id + '.json')
    video_file_name = "vd" + str(id + '.json')
    category_file_name = "ctd" + str(id + '.json')

    file_writer_channels: FileWriter = FileWriter('/tmp/' + channel_file_name)
    file_writer_videos: FileWriter = FileWriter('/tmp/' + video_file_name)
    file_writer_category: FileWriter = FileWriter('/tmp/' + category_file_name)

    extractor_channels: ChannelDataExtractor = ChannelDataExtractor()
    extractor_videos: VideoDataExtractor = VideoDataExtractor()
    video_category_extractor: VideoCategoryExtractor = VideoCategoryExtractor()

    storage: StorageS3 = StorageS3(os.environ.get("BucketName"))

    channel_data = extractor_channels.extract(channel_id)
    video_data = extractor_videos.extract(channel_id)

    video_id: list = VideoIDParser().parse(video_data, channel_id)
    category_data = video_category_extractor.extract(video_id)

    file_writer_channels.writing(channel_data)
    file_writer_videos.writing(video_data)
    file_writer_category.writing(category_data)

    storage.upload(file_writer_channels.get_path(), "Resources/" + folder_name + "/" + "channelData")
    storage.upload(file_writer_videos.get_path(), "Resources/" + folder_name + "/" + "videoData")
    storage.upload(file_writer_category.get_path(), "Resources/" + folder_name + "/" + "categoryData")

    service: ServiceSQS = ServiceSQS()
    service.send_message(future_message, queue_name=os.environ.get("TransformerTriggerQueueName"))
    return "Successfully completed"
