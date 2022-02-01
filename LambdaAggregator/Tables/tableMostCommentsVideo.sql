CREATE EXTERNAL TABLE IF NOT EXISTS `{database}`.`mostCommentsVideo` (
	`time_id` string,
	`comment_count` bigint,
	`video_id` string,
	`title` string
) ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES ('serialization.format' = '1')
LOCATION 's3://{bucket}/AggregatedData/MostCommentsVideo'
TBLPROPERTIES ('has_encrypted_data' = 'false')