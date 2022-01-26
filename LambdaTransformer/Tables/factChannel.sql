CREATE EXTERNAL TABLE IF NOT EXISTS `{database}`.`factChannel` (
`channel_id` string,
 `date_id` string,
 `time_id` string,
 `view_count` bigint,
 `subscriber_count` bigint,
 `video_count` bigint
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://{bucket}/Data/Channel/FactChannel'
TBLPROPERTIES ('has_encrypted_data'='false')