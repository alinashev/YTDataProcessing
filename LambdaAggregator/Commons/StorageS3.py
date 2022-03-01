import boto3
import botocore


class StorageS3:
    def __init__(self, bucket_name='task-bucket-a') -> None:
        self.s3 = None
        self.bucket_name = bucket_name
        self.s3 = boto3.resource('s3')

    def download_file(self, obj_name, file_name) -> None:
        try:
            self.s3.Bucket(self.bucket_name).download_file(obj_name, file_name)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    def upload(self, file_name, directory: str) -> None:
        self.s3.meta.client.upload_file(file_name, self.bucket_name,
                                        '{directory}{name}'.format(
                                            directory=directory,
                                            name=file_name.replace("tmp/", ""))
                                        )
