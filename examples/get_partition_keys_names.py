from hive_metastore_client_databricks import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

DATABASE_NAME = "database_name"
TABLE_NAME = "table_name"

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Retrieving the partition keys names via table schema
    returned_value = hive_client.get_partition_keys_names(DATABASE_NAME, TABLE_NAME)
