from unittest import mock

import pytest

from hive_metastore_client.hive_mestastore_client import HiveMetastoreClient
from hive_metastore_client.hive_mestastore_client_connector import (
    HiveMetastoreClientConnector,
)


@pytest.fixture
@mock.patch.object(HiveMetastoreClientConnector, "_init_protocol")
def hive_metastore_client(mocked__init_protocol) -> HiveMetastoreClient:
    return HiveMetastoreClient(host="__HOST__")
