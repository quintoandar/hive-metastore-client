"""Hive Metastore Client main class."""
from hive_metastore_client.clients.hive_mestastore_client_connector import (
    HiveMetastoreClientConnector,
)


class HiveMetastoreClient(HiveMetastoreClientConnector):
    """User main interface with the metastore server methods."""

    # Example
    # def get_tables(self, a, b):
    #     a = something(a, b)
    #     super().get_tables(a)
