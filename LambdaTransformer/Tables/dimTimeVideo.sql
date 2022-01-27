CREATE EXTERNAL TABLE IF NOT EXISTS `{database}`.`dimTimeVideo` (
 `time_id` string,
 `year` int,
 `month` int,
 `day` int,
 `hour` int,
 `week` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://{bucket}/Data/Video/DimTimeVideo'
TBLPROPERTIES ('has_encrypted_data'='false')