from hive_metastore_client import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

DATABASE_NAME = "database_name"
TABLE_NAME = "table_name"

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Getting partition values as a list from specified table
    returned_value = hive_client.get_partition_values_from_table(
        DATABASE_NAME, TABLE_NAME
    )
