"""
    Use the builders for creating Column thrift object.
    Some arguments are optional when creating a thrift object.
    Check Builder constructor for more information.
"""

from hive_metastore_client_databricks.builders import ColumnBuilder
from hive_metastore_client_databricks import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

# You must create a list with the columns
columns = [
    ColumnBuilder(name="quantity", type="int", comment="item's quantity").build()
]

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # Adding columns to the table
    hive_client.add_columns_to_table(
        db_name="store", table_name="order", columns=columns
    )
