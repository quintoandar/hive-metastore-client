# Discovering Hive Mestastore Client

Refer to the examples in this directory for discovering how to use this lib 
and to communicate with you Hive metastore server.

It is necessary to use the client instance with the `with` statement, this 
guarantees that the connection will automatically open and closed for you.
I.g.:
```python
hive_metastore_client = HiveMetastoreClient(HIVE_HOST, HIVE_PORT)
with hive_metastore_client as conn:

    database = DatabaseBuilder(name='new_db').build()
    conn.create_database(database) 
```

This lib encapsulate some the Thrift code's dependency into Builders.
You must utilize them for building the thrift entities objects before calling the client methods.