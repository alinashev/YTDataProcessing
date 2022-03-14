from typing import Any
from pyspark.sql.types import StructType, StructField, StringType
from SchemaBuilders.SchemaBuilder import SchemaBuilder


class ChannelSchemaBuilder(SchemaBuilder):

    def build(self, spark_session: Any) -> Any:
        emptyRDD: Any = spark_session.sparkContext.emptyRDD()
        channel_df_schema: Any = StructType([
            StructField('id', StringType(), True),
            StructField('subscriberCount', StringType(), True),
            StructField('videoCount', StringType(), True),
            StructField('viewCount', StringType(), True),
            StructField('channelTitle', StringType(), True)
        ])
        return spark_session.createDataFrame(emptyRDD, channel_df_schema)
