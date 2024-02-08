"""
    The thrift Table object requires others objects as arguments.
    Use the builders for creating each of them.
    Some arguments are optional when creating a thrift object.
    Check each Builder constructor for more information.

    Due to a bug in Hive Metastore server we need to enforce the parameter
     EXTERNAL=TRUE when creating an external table. You can either use the
     method `create_external_table` with the table object or declare the two
     table parameters before calling the method create_table.
"""

from hive_metastore_client_databricks import HiveMetastoreClient
from hive_metastore_client_databricks.builders import (
    ColumnBuilder,
    SerDeInfoBuilder,
    StorageDescriptorBuilder,
    TableBuilder,
)

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
    location="s3a://path/to/file",
    input_format="org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat",
    output_format="org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat",
    serde_info=serde_info,
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
    hive_metastore_client.create_external_table(table)
