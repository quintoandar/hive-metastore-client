"""
    The thrift Table object requires others objects as arguments.
    Use the builders for creating each of them.
    Some arguments are optional when creating a thrift object.
    Check each Builder constructor for more information.
"""

from hive_metastore_client.builders.column_builder import ColumnBuilder
from hive_metastore_client.builders.serde_info_builder import SerDeInfoBuilder
from hive_metastore_client.builders.storage_descriptor_builder import (
    StorageDescriptorBuilder,
)
from hive_metastore_client.builders.table_builder import TableBuilder
from hive_metastore_client import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

# You must create a list with the columns
columns = [
    ColumnBuilder("id", "string", "col comment").build(),
    ColumnBuilder("client_name", "string").build(),
    ColumnBuilder("amount", "string").build(),
    ColumnBuilder("year", "string").build(),
    ColumnBuilder("month", "string").build(),
    ColumnBuilder("day", "string").build(),
]

# If you table has partitions create a list with the partition columns
# This list is similar to the columns list, and the year, month and day
# columns are the same.
partition_keys = [
    ColumnBuilder("year", "string").build(),
    ColumnBuilder("month", "string").build(),
    ColumnBuilder("day", "string").build(),
]

serde_info = SerDeInfoBuilder(
    serialization_lib="org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
).build()

storage_descriptor = StorageDescriptorBuilder(
    columns=columns,
    location="path/to/file",
    input_format="org.apache.hadoop.mapred.TextInputFormat",
    output_format="org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
    serde_info=serde_info,
).build()

table_builder = TableBuilder(
    "table_name", "db_name", storage_descriptor, partition_keys=partition_keys
).build()

table = TableBuilder(
    table_name="orders",
    db_name="store",
    owner="owner name",
    storage_descriptor=storage_descriptor,
    partition_keys=partition_keys,
).build()

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_metastore_client:
    # Creating new table from thrift table object
    hive_metastore_client.create_table(table)
