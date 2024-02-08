"""
    Use the builders for creating Database thrift object.
    Some arguments are optional when creating a thrift object.
    Check Builder constructor for more information.
"""

from hive_metastore_client_databricks.builders import DatabaseBuilder
from hive_metastore_client_databricks import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

# Creating database object using builder
database = DatabaseBuilder("database_name").build()

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Creating new database from thrift table object
    hive_client.create_database(database)
