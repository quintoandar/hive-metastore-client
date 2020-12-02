# Discovering Hive Mestastore Client

Refer to the examples in this directory for discovering how to use this lib 
and to communicate with you Hive metastore server.

It is necessary to use the client instance with the `with` statement, this 
guarantees that the connection will be automatically opened and closed for you.
I.g.:
```python
with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_metastore_client:

    database = DatabaseBuilder(name='new_db').build()
    hive_metastore_client.create_database(database) 
```

This lib encapsulate some the Thrift code's dependency into Builders.
You must utilize them for building the thrift entities objects before calling the client methods.