from Commons.ChannelsID import ChannelsID


def lambda_handler(event, context):
    tasks = list()
    channel_dict: list = ChannelsID('channels.txt').get_channels_id()
    for i in channel_dict:
        tasks.append({i: channel_dict[i]})

    return {
        'body': {'taskList': tasks}
    }
