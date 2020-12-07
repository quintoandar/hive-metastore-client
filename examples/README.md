# Discovering Hive Mestastore Client

Refer to the examples in this directory for discovering how to use this lib 
and to communicate with you Hive metastore server.

It is necessary to use the client instance with the `with` statement, this 
guarantees that the connection will be automatically opened and closed for you.
I.g.:
```python
from hive_metastore_client import HiveMetastoreClient
from hive_metastore_client.builders import DatabaseBuilder

database = DatabaseBuilder(name='new_db').build()
with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_metastore_client:
    hive_metastore_client.create_database(database) 
```

This lib encapsulate some the Thrift code's dependency into Builders.
You must utilize them for building the thrift entities objects before calling the client methods.
