from pyspark.sql import SparkSession

from Commons.Configurator import Configurator
from Commons.DataVersion import DataVersion
from Executor import Executor


def main():
    spark_session: SparkSession = SparkSession.builder.appName("App").master("local[8]"). \
        config("spark.driver.memory", "1g"). \
        config("spark.executor.memory", "1g"). \
        config("spark.memory.offHeap.enabled", True). \
        config("spark.memory.offHeap.size", "8g"). \
        getOrCreate()

    data_version: DataVersion = DataVersion()

    executor: Executor = Executor(data_version, spark_session)
    configurator: Configurator = Configurator(data_version)
    aggregation_list: list = configurator.get_all_configuration()

    for i in aggregation_list:
        executor.execute(**i)


if __name__ == '__main__':
    main()
