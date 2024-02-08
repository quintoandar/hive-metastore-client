from unittest import mock
from unittest.mock import Mock

from hive_metastore_client_databricks.builders import PartitionBuilder


class TestPartitionBuilder:
    @mock.patch("hive_metastore_client_databricks.builders.partition_builder.Partition")
    def test_build(self, mocked_partition):
        # arrange
        values = ["1", "2"]
        db_name = "database_name"
        table_name = "table_name"
        create_time = 10000
        last_access_time = 10000
        mocked_sd = Mock()
        parameters = {"key": "value"}
        mocked_privileges = Mock()
        cat_name = "catalog_name"

        mocked_obj = Mock()
        mocked_partition.return_value = mocked_obj

        # act
        returned_value = PartitionBuilder(
            values=values,
            db_name=db_name,
            table_name=table_name,
            create_time=create_time,
            last_access_time=last_access_time,
            sd=mocked_sd,
            parameters=parameters,
            privileges=mocked_privileges,
            cat_name=cat_name,
        ).build()

        # assert
        assert returned_value == mocked_obj
        mocked_partition.assert_called_once_with(
            values=values,
            dbName=db_name,
            tableName=table_name,
            createTime=create_time,
            lastAccessTime=last_access_time,
            sd=mocked_sd,
            parameters=parameters,
            privileges=mocked_privileges,
            catName=cat_name,
        )
