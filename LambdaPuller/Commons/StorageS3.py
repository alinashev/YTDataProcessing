import boto3


class StorageS3:

    def __init__(self, bucket_name='a-channel-data-bucket-01-10') -> None:
        self.s3 = boto3.resource('s3')
        self.__bucket_name = bucket_name

    def upload(self, file_name, directory: str) -> None:
        self.s3.meta.client.upload_file(file_name, self.__bucket_name,
                                        '{directory}{name}'.format(
                                            directory=directory,
                                            name=file_name.replace("tmp/", ""))
                                        )
