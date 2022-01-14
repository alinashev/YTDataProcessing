import os

from Commons.ChannelsID import ChannelsID
from Commons.ServiceSQS import ServiceSQS


def lambda_handler(event, context):
    service: ServiceSQS = ServiceSQS()
    channel_id: list = ChannelsID('channels.txt').get_channels_id()
    for channel in channel_id:
        service.send_message(channel, queue_name=os.environ.get("LambdaTriggerQueueName"))

    return "Successfully completed"
