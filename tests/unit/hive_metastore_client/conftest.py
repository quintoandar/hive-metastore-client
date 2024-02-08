from unittest import mock

import pytest

from hive_metastore_client_databricks import HiveMetastoreClient


@pytest.fixture
@mock.patch.object(HiveMetastoreClient, "_init_protocol")
def hive_metastore_client(mocked__init_protocol) -> HiveMetastoreClient:
    return HiveMetastoreClient(host="__HOST__")
