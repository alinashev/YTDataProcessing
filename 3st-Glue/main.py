import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from Commons.Configurator import Configurator
from Commons.DataVersion import DataVersion
from Commons.Executor import Executor


args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

data_version: DataVersion = DataVersion()

general_data_source: str = "s3://a-data-bucket-1/Resources/" + data_version.get_date() + "/" + data_version.get_hour()
general_agg_dir: str = "s3://a-data-bucket-1/GlueAggregated"

executor: Executor = Executor(data_version, spark)
configurator: Configurator = Configurator(data_version, general_data_source, general_agg_dir)
aggregation_list: list = configurator.get_all_configuration()

for i in aggregation_list:
    executor.execute(**i)

job.commit()
