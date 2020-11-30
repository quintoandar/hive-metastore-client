from hive_metastore_client.builders.partition_builder import PartitionBuilder
from hive_metastore_client.builders.storage_descriptor_builder import StorageDescriptorBuilder
from hive_metastore_client.hive_mestastore_client import HiveMetastoreClient

HIVE_HOST = "<ADD_HIVE_HOST_HERE>"
HIVE_PORT = 9083

# You must create a list with the columns
columns = [
    ColumnBuilder("lastname", "string", "col comment").build(),
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

# partitions should be formatted in a list
partition_list = [
    PartitionBuilder("a").build(),
    PartitionBuilder("b").build()
]

with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_client:
    # adding partitions to specified table
    hive_client.add_partitions(partition_list)
