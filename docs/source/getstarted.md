# Getting Started

Hive Metastore Client depends on **Python 3.7+**.

[Python Package Index](https://pypi.org/project/hive-metastore-client/) hosts reference to a pip-installable module of this library, using it is as straightforward as including it on your project's requirements.

```bash
pip install hive-metastore-client
```

Or after listing `hive-metastore-client` in your `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Discovering Hive Metastore Client

Click on the following links to open the [examples](https://github.com/quintoandar/hive-metastore-client/tree/main/examples):

**[#1 Create a database](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/create_database.py)**

**[#2 Create a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/create_table.py)**

**[#3 Create an external table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/create_external_table.py)**

**[#4 Add columns to a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/add_columns_to_table.py)**

**[#5 Add partitions to a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/add_partitions.py)**

**[#6 Get partition keys objects from a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/get_partition_keys_objects.py)**

**[#7 Get partition keys (names & types) from a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/get_partition_keys.py)**

**[#8 Get partition keys (names only) from a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/get_partition_keys_names.py)**

**[#9 Bulk drop partitions values from a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/bulk_drop_partitions.py)**

**[#10 Get partition values from a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/get_partition_values_from_table.py)**

## Available methods

You can see all the Hive Metastore server available methods by looking at the 
interface:
[`thrift_files.libraries.thrift_hive_metastore_client.ThriftHiveMetastore.Iface`](https://github.com/quintoandar/hive-metastore-client/blob/main/thrift_files/libraries/thrift_hive_metastore_client/ThriftHiveMetastore.py).

Beyond the default methods, this library also implements the methods below in
the [`HiveMetastoreClient`](https://github.com/quintoandar/hive-metastore-client/blob/main/hive_metastore_client/hive_metastore_client.py) class:

- [`add_columns_to_table`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.add_columns_to_table)
- [`drop_columns_from_table`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.drop_columns_from_table)
- [`add_partitions_if_not_exists`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.add_partitions_if_not_exists)
- [`create_database_if_not_exists`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.create_database_if_not_exists)
- [`create_external_table`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.create_external_table)
- [`get_partition_keys_objects`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.get_partition_keys_objects)
- [`get_partition_keys`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.get_partition_keys)
- [`get_partition_keys_names`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.get_partition_keys_names)
- [`bulk_drop_partitions`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.bulk_drop_partitions)
- [`get_partition_values_from_table`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.get_partition_values_from_table)
