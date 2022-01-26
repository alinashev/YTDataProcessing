CREATE EXTERNAL TABLE IF NOT EXISTS `{database}`.`factVideo` (
 `video_id` string,
 `date_id` string,
 `time_id` string,
 `view_count` bigint,
 `like_count` bigint,
 `comment_count` bigint
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://{bucket}/Data/Video/FactVideo'
TBLPROPERTIES ('has_encrypted_data'='false')