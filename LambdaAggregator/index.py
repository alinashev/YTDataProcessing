import json
from Commons.AthenaDataBase import AthenaDataBase
from Commons.Aggregator import Aggregator
from Commons.DataVersion import DataVersion
from Commons.TableCreator import TableCreator
from Commons.ParquetFormat import ParquetFormat
from Commons.StorageS3 import StorageS3


def lambda_handler(event, context):
    bucket = "a-data-bucket-1"
    s3_staging_dir = "s3://" + bucket + "/Athena/Result/"
    region_name = 'us-east-2'
    dataBase = "a-database"

    version: DataVersion = DataVersion()

    athena: AthenaDataBase = AthenaDataBase(bucket, s3_staging_dir, region_name)
    aggregator: Aggregator = Aggregator(athena.connect())
    tableCreator: TableCreator = TableCreator(athena.connect())
    storage: StorageS3 = StorageS3(bucket_name=bucket)

    df_least_view_count_ch = aggregator.execute(open("Query/aggregationLeastViewCountsInChannels.sql",
                                                     'r').read().format(database=dataBase, add_date=version.get_date(),
                                                                        hour=version.get_hour()))

    df_most_comments_v = aggregator.execute(open(
        "Query/aggregationMostCommentsVideo.sql", 'r').read().format(database=dataBase, add_date=version.get_date(),
                                                                     hour=version.get_hour()))

    df_most_liked_v = aggregator.execute(open(
        "Query/aggregationMostLikedVideo.sql", 'r').read().format(database=dataBase, add_date=version.get_date(),
                                                                  hour=version.get_hour()))

    df_most_subscribed_ch = aggregator.execute(open(
        "Query/aggregationMostSubscribedChannel.sql", 'r').read().format(database=dataBase, add_date=version.get_date(),
                                                                         hour=version.get_hour()))

    ParquetFormat.write(df_least_view_count_ch, "/tmp/" + "least-view-count-ch" + ".parquet")
    ParquetFormat.write(df_most_comments_v, "/tmp/" + "most-comments-v" + ".parquet")
    ParquetFormat.write(df_most_liked_v, "/tmp/" + "most-liked-v" + ".parquet")
    ParquetFormat.write(df_most_subscribed_ch, "/tmp/" + "most-subscribed-ch" + ".parquet")

    storage.upload("/tmp/" + "least-view-count-ch" + ".parquet",
                   "AggregatedData/LeastViewCountsInChannels/" + version.get_date() + "/" + version.get_hour())
    storage.upload("/tmp/" + "most-comments-v" + ".parquet",
                   "AggregatedData/MostCommentsVideo/" + version.get_date() + "/" + version.get_hour())
    storage.upload("/tmp/" + "most-liked-v" + ".parquet",
                   "AggregatedData/MostLikedVideo/" + version.get_date() + "/" + version.get_hour())
    storage.upload("/tmp/" + "most-subscribed-ch" + ".parquet",
                   "AggregatedData/MostSubscribedChannels/" + version.get_date() + "/" + version.get_hour())

    tableCreator.create(open("Tables/tableLeastViewCountsInChannels.sql", 'r').
                        read().format(database=dataBase, bucket=bucket))
    tableCreator.create(open("Tables/tableMostCommentsVideo.sql", 'r').
                        read().format(database=dataBase, bucket=bucket))
    tableCreator.create(open("Tables/tableMostLikedVideo.sql", 'r').
                        read().format(database=dataBase, bucket=bucket))
    tableCreator.create(open("Tables/tableMostSubscribedChannel.sql", 'r').
                        read().format(database=dataBase, bucket=bucket))

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully completed!')
    }
