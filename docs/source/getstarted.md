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

**[#3 Add columns to a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/add_columns_to_table.py)**

**[#4 Add partitions to a table](https://github.com/quintoandar/hive-metastore-client/blob/main/examples/add_partitions.py)**

## Available methods

You can see all the Hive Metastore server available methods by looking at the 
interface:
[`thrift_files.libraries.thrift_hive_metastore_client.ThriftHiveMetastore.Iface`](https://github.com/quintoandar/hive-metastore-client/blob/main/thrift_files/libraries/thrift_hive_metastore_client/ThriftHiveMetastore.py).

Beyond the default methods, this library also implements the methods below in
the [`HiveMetastoreClient`](https://github.com/quintoandar/hive-metastore-client/blob/main/hive_metastore_client/hive_metastore_client.py) class:

- [`add_columns_to_table`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.add_columns_to_table)
- [`drop_columns_from_table`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.drop_columns_from_table)
- [`add_partitions_if_not_exists`](https://hive-metastore-client.readthedocs.io/en/latest/hive_metastore_client.html#hive_metastore_client.hive_metastore_client.HiveMetastoreClient.add_columns_to_table)