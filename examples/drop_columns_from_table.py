from hive_metastore_client_databricks import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

# You must create a list with the columns' names to drop
columns = ["quantity"]

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Dropping columns from table
    hive_client.drop_columns_from_table(
        db_name="store", table_name="order", columns=columns
    )
