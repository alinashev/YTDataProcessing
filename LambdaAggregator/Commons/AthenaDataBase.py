from typing import Any
from pyathena import connect
from pyathena.pandas.cursor import PandasCursor


class AthenaDataBase:
    def __init__(self, bucket, s3_staging_dir, region_name) -> None:
        self.connection = None
        self.bucket = bucket
        self.s3_staging_dir = s3_staging_dir
        self.region_name = region_name

    def connect(self) -> Any:
        try:
            self.connection = connect(self.s3_staging_dir,
                                      self.region_name,
                                      cursor_class=PandasCursor)
        except Exception as error:
            print(error)
        return self.connection
