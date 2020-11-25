from hive_metastore_client.hive_mestastore_client import HiveMetastoreClient


class TestHiveMetastoreClient:
    def test_foo(self, hive_metastore_client):
        # temp test
        assert isinstance(hive_metastore_client, HiveMetastoreClient)
