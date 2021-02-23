from hive_metastore_client import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

DATABASE_NAME = "database_name"
TABLE_NAME = "table_name"

partition_list = [
    ["2020", "1", "28"],
    ["2020", "1", "29"],
    ["2020", "1", "30"],
    ["2020", "1", "31"],
]

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Dropping various partitions at once
    hive_client.bulk_drop_partitions(
        DATABASE_NAME, TABLE_NAME, partition_list, delete_data=False
    )
