from Channel import Channel


def lambda_handler(event, context):
    tasks = list()
    channel_dict: dict = Channel('channels.txt').get_channels_id()
    for i in channel_dict:
        tasks.append({i: channel_dict[i]})

    return {
        'statuscode': 200,
        'body': {'taskList': tasks}
    }
