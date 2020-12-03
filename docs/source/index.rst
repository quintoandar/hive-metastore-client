Hive Metastore Client
=====================
Made with |:heart:| by the **Data Engineering** team from `QuintoAndar <https://github.com/quintoandar/>`_.

A client for connecting and running DMLs on Hive Metastore using Thrift protocol.

An example of how to use the library for running DML commands in hive metastore:

.. code-block:: python

    from hive_metastore_client.builders.database_builder import DatabaseBuilder
    from hive_metastore_client.hive_mestastore_client import HiveMetastoreClient

    database = DatabaseBuilder(name='new_db').build()
    with HiveMetastoreClient(HIVE_HOST, HIVE_PORT) as hive_metastore_client:
        hive_metastore_client.create_database(database)

To learn more use cases in practice, see [Hive Metastore Client's examples](https://github.com/quintoandar/hive-metastore-client/blob/main/examples)


Navigation
^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   getstarted
   modules
