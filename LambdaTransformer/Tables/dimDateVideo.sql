CREATE EXTERNAL TABLE IF NOT EXISTS `{database}`.`dimDateVideo` (
 `date_id` string,
 `year` int,
 `month` int,
 `day` int,
 `week` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://{bucket}/Data/Video/DimDateVideo'
TBLPROPERTIES ('has_encrypted_data'='false')