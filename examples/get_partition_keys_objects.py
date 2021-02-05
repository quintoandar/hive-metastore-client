from hive_metastore_client import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

DATABASE_NAME = "database_name"
TABLE_NAME = "table_name"

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Retrieving the partition keys via table schema
    hive_client.get_partition_keys_objects(DATABASE_NAME, TABLE_NAME)
