CREATE EXTERNAL TABLE IF NOT EXISTS `{database}`.`mostSubscribedChannel` (
`time_id` string,
`add_date` date,
`hour` int,
`subscriber_count` bigint,
`channel_id` string,
`channel_name` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES ( 'serialization.format' = '1')
LOCATION 's3://{bucket}/AggregatedData/MostSubscribedChannels'
TBLPROPERTIES ('has_encrypted_data'='false')