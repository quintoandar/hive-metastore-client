from unittest import mock
from unittest.mock import Mock

from hive_metastore_client_databricks.builders.table_builder import TableBuilder


class TestTableBuilder:
    @mock.patch("hive_metastore_client_databricks.builders.table_builder.Table")
    def test_build(self, mocked_table):
        # arrange
        mocked_table_name = ""
        mocked_db_name = ""
        mocked_owner = ""
        mocked_create_time = 123456
        mocked_last_access_time = 1234567
        mocked_retention = 1234568
        mocked_storage_descriptor = Mock()
        mocked_partition_keys = [Mock()]
        mocked_parameters = {"a": "b"}
        mocked_view_original_text = ""
        mocked_view_expanded_text = ""
        mocked_table_type = ""
        mocked_privileges = Mock()
        mocked_temporary = True
        mocked_rewrite_enabled = True
        mocked_creation_metadata = Mock()
        mocked_cat_name = ""
        mocked_owner_type = Mock()

        mocked_obj = Mock()
        mocked_table.return_value = mocked_obj

        # act
        returned_value = TableBuilder(
            table_name=mocked_table_name,
            db_name=mocked_db_name,
            owner=mocked_owner,
            create_time=mocked_create_time,
            last_access_time=mocked_last_access_time,
            retention=mocked_retention,
            storage_descriptor=mocked_storage_descriptor,
            partition_keys=mocked_partition_keys,
            parameters=mocked_parameters,
            view_original_text=mocked_view_original_text,
            view_expanded_text=mocked_view_expanded_text,
            table_type=mocked_table_type,
            privileges=mocked_privileges,
            temporary=mocked_temporary,
            rewrite_enabled=mocked_rewrite_enabled,
            creation_metadata=mocked_creation_metadata,
            cat_name=mocked_cat_name,
            owner_type=mocked_owner_type,
        ).build()

        # assert
        assert returned_value == mocked_obj
        mocked_table.assert_called_once_with(
            tableName=mocked_table_name,
            dbName=mocked_db_name,
            owner=mocked_owner,
            createTime=mocked_create_time,
            lastAccessTime=mocked_last_access_time,
            retention=mocked_retention,
            sd=mocked_storage_descriptor,
            partitionKeys=mocked_partition_keys,
            parameters=mocked_parameters,
            viewOriginalText=mocked_view_original_text,
            viewExpandedText=mocked_view_expanded_text,
            tableType=mocked_table_type,
            privileges=mocked_privileges,
            temporary=mocked_temporary,
            rewriteEnabled=mocked_rewrite_enabled,
            creationMetadata=mocked_creation_metadata,
            catName=mocked_cat_name,
            ownerType=mocked_owner_type,
        )
