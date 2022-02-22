"""
    The thrift Table object requires others objects as arguments.
    Use the builders for creating each of them.
    Some arguments are optional when creating a thrift object.
    Check each Builder constructor for more information.
"""

from hive_metastore_client import HiveMetastoreClient
from hive_metastore_client.builders import (
    ColumnBuilder,
    StorageDescriptorBuilder,
    ViewBuilder,
)

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

# You must create a list with the columns
columns = [
    ColumnBuilder("first_column", "string", "col comment").build(),
    ColumnBuilder("first_column", "string").build(),
]

query = """
    SELECT 
        first_column,
        second_column
    FROM 
        table_name
    WHERE
        first_column IS NOT NULL
"""

storage_descriptor = StorageDescriptorBuilder(columns=columns,).build()

view = ViewBuilder(
    view_name="orders",
    db_name="store",
    owner="owner name",
    storage_descriptor=storage_descriptor,
    view_expanded_text=query,
    view_original_text=query,
).build()

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_metastore_client:
    # Creating new view from table/view object
    hive_metastore_client.create_view(view)
