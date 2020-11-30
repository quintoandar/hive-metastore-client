from hive_metastore_client.builders import (
    ColumnBuilder,
    SerDeInfoBuilder,
    StorageDescriptorBuilder,
    PartitionBuilder,
)
from hive_metastore_client.hive_mestastore_client import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

# You must create a list with the partition columns
columns = [
    ColumnBuilder("partition_column_1", "string", "col comment").build(),
    ColumnBuilder("partition_column_2", "string", "col comment").build(),
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

# partitions should be provided as list
partition_list = [
    PartitionBuilder(
        values=["partition_column_1_value_a", "partition_column_2_value_b"],
        db_name="database_name",
        table_name="table_name",
        create_time=10000,
        last_access_time=10000,
        sd=storage_descriptor,
    ).build(),
    PartitionBuilder(
        values=["partition_column_1_value_a", "partition_column_2_value_c"],
        db_name="database_name",
        table_name="table_name",
        create_time=10000,
        last_access_time=10000,
        sd=storage_descriptor,
    ).build(),
]

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # adding two set of partitions to specified table
    hive_client.add_partitions(partition_list)
