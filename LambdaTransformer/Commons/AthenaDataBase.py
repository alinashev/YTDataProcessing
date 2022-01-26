from typing import Any
from pyathena import connect


class AthenaDataBase:
    def __init__(self):
        self.connection = None

    def connect(self,
                s3_staging_dir,
                region_name='us-east-2') -> Any:
        try:
            self.connection = connect(s3_staging_dir,
                                      region_name=region_name)
        except Exception as error:
            print(error)
        return self.connection
