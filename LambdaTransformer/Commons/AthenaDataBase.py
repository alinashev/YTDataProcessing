from typing import Any
from pyathena import connect


class AthenaDataBase:
    def __init__(self):
        self.connection = None

    def connect(self,
                bucket,
                region_name='us-east-2') -> Any:

        s3_staging_dir = "s3://" + bucket + "/Athena/Result/"
        try:
            self.connection = connect(s3_staging_dir,
                                      region_name=region_name)
        except Exception as error:
            print(error)
        return self.connection
