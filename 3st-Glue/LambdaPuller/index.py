import os

from Commons.DataVersion import DataVersion
from Service.StorageS3 import StorageS3
from Executor import Executor


def lambda_handler(event, context):
    name = list(event.keys())[0]
    id = event[name]

    channel: dict = {name: id}
    data_version: DataVersion = DataVersion()
    storage: StorageS3 = StorageS3(os.environ.get("BucketName"))

    executor: Executor = Executor(data_version)
    try:
        executor.execute(channel, storage, "channel")
        executor.execute(channel, storage, "video")
    except IndexError:
        return {
            'statuscode': 403
        }

    return {
        'statuscode': 200
    }
