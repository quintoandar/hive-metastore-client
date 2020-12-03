from hive_metastore_client.builders import PartitionBuilder
from hive_metastore_client.hive_mestastore_client import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

DATABASE_NAME = "database_name"
TABLE_NAME = "table_name"

# partitions should be provided as list
# values should be passed in the same hierarchical order of the partitions
partition_list = [
    PartitionBuilder(
        values=["2020", "12", "13"], db_name=DATABASE_NAME, table_name=TABLE_NAME,
    ).build(),
    PartitionBuilder(
        values=["2020", "12", "14"], db_name=DATABASE_NAME, table_name=TABLE_NAME,
    ).build(),
]

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Adding two set of partitions to specified table
    hive_client.add_partitions_to_table(DATABASE_NAME, TABLE_NAME, partition_list)
