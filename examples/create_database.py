from hive_metastore_client.builders.database_builder import DatabaseBuilder
from hive_metastore_client.hive_mestastore_client import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:

    database_builder = DatabaseBuilder("database_name")
    database = database_builder.build()

    hive_client.create_database(database)
