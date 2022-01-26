import os
from typing import Any
from Commons.AthenaDataBase import AthenaDataBase


class Loader:
    @staticmethod
    def load(file) -> None:
        try:
            data_base: AthenaDataBase = AthenaDataBase()
            connect: Any = data_base.connect(os.environ.get("DatabaseName"))
            cursor: Any = connect.cursor()

            sql_file = open(file, 'r')
            cursor.execute(sql_file.read().format(database=os.environ.get("DatabaseName"),
                                                  bucket=os.environ.get("BucketName")))
        except Exception as error:
            print(error)
