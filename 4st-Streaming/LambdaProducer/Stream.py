import json
from typing import Any

import boto3


class Stream:
    def __init__(self, stream_name: str) -> None:
        self.stream_name = stream_name

    @staticmethod
    def connect() -> Any:
        return boto3.client('kinesis')

    def put_to_stream(self, data: Any, partition_key: str) -> None:
        client: Any = self.connect()
        client.put_record(
            StreamName=self.stream_name,
            Data=json.dumps(data),
            PartitionKey=partition_key)
