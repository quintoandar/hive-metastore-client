from hive_metastore_client.hive_mestastore_client_connector import (
    HiveMetastoreClientConnector,
)


class HiveMetastoreClient(HiveMetastoreClientConnector):
    """
    The Hive metastore client
    """

    # Example
    # def get_tables(self, a, b):
    #     a = something(a, b)
    #     super().get_tables(a)
