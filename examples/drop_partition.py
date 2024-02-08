from hive_metastore_client_databricks.builders import PartitionBuilder
from hive_metastore_client_databricks import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

DATABASE_NAME = "database_name"
TABLE_NAME = "table_name"

# Partitions should be provided as list
# Values should be passed in the same hierarchical order of the partitions
partition_values = ["2020", "12", "13"]

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Dropping respective partition from metastore but keeping its data
    hive_client.drop_partition(
        DATABASE_NAME, TABLE_NAME, partition_values, deleteData=False
    )
