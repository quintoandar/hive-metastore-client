from unittest import mock
from unittest.mock import Mock

from hive_metastore_client.hive_mestastore_client import HiveMetastoreClient


class TestHiveMetastoreClient:
    @mock.patch("hive_metastore_client.hive_mestastore_client.TSocket")
    @mock.patch("hive_metastore_client.hive_mestastore_client.TTransport")
    @mock.patch("hive_metastore_client.hive_mestastore_client.TBinaryProtocol")
    def test__init_protocol(
        self, mocked_tbinaryp, mocked_ttransport, mocked_tsocket, hive_metastore_client
    ):
        # arrange
        mocked_transport = Mock()
        mocked_ttransport.TBufferedTransport.return_value = mocked_transport

        expected_return = Mock()
        mocked_tbinaryp.TBinaryProtocol.return_value = expected_return

        # act
        returned_value = hive_metastore_client._init_protocol(
            host="111.222.333", port=1234
        )

        # assert
        assert expected_return == returned_value
        mocked_tbinaryp.TBinaryProtocol.assert_called_once_with(mocked_transport)

    def test_open(self, hive_metastore_client):
        # arrange
        mocked_transport = Mock()
        hive_metastore_client._oprot = mocked_transport

        # act
        returned_value = hive_metastore_client.open()

        # assert
        assert returned_value == hive_metastore_client
        hive_metastore_client._oprot.trans.open.assert_called_once_with()

    def test_close(self, hive_metastore_client):
        # arrange
        mocked_transport = Mock()
        hive_metastore_client._oprot = mocked_transport

        # act
        hive_metastore_client.close()

        # assert
        hive_metastore_client._oprot.trans.close.assert_called_once_with()

    @mock.patch.object(HiveMetastoreClient, "open")
    def test__enter__(self, mocked_open, hive_metastore_client):
        # act
        with hive_metastore_client:
            pass

        # assert
        mocked_open.assert_called_once_with()

    @mock.patch.object(HiveMetastoreClient, "close")
    def test__exit__(self, mocked_close, hive_metastore_client):
        # act
        with hive_metastore_client:
            pass

        # assert
        mocked_close.assert_called_once_with()
