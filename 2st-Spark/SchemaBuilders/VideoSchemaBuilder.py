from typing import Any
from pyspark.sql.types import StructType, StructField, StringType
from SchemaBuilders.SchemaBuilder import SchemaBuilder


class VideoSchemaBuilder(SchemaBuilder):

    def build(self, spark_session: Any) -> Any:
        emptyRDD: Any = spark_session.sparkContext.emptyRDD()
        video_df_schema: Any = StructType([
            StructField('id', StringType(), True),
            StructField('channelTitle', StringType(), True),
            StructField('channelId', StringType(), True),
            StructField('categoryId', StringType(), True),
            StructField('commentCount', StringType(), True),
            StructField('likeCount', StringType(), True),
            StructField('viewCount', StringType(), True)
        ])
        return spark_session.createDataFrame(emptyRDD, video_df_schema)
