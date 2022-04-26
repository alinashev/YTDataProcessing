import boto3 as boto3
import botocore as botocore
import os
from typing import Any


class StorageS3:
    def __init__(self, bucket_name: Any = 'a-data-bucket-1') -> None:
        self.bucket_name: str = bucket_name
        self.s3 = boto3.resource('s3')

    def download_file(self, obj_name: str, file_name: str) -> None:
        try:
            self.s3.Bucket(self.bucket_name).download_file(obj_name, file_name)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    def download_folder(self, s3_folder: str, local_dir: str) -> None:
        bucket: Any = self.s3.Bucket(self.bucket_name)
        for obj in bucket.objects.filter(Prefix=s3_folder):
            if local_dir is None:
                path: Any = obj.key
            else:
                path: Any = os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            if obj.key[-1] == '/':
                continue
            self.download_file(obj.key, path)

    def upload(self, directory: str, file: str) -> None:
        self.s3.meta.client.upload_file(file, self.bucket_name,
                                        '{directory}/{name}'.format(
                                            directory=directory,
                                            name=file)
                                        )
