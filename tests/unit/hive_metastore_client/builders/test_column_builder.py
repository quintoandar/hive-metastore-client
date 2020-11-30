from unittest import mock
from unittest.mock import Mock

from hive_metastore_client.builders.column_builder import ColumnBuilder


class TestColumnBuilder:
    @mock.patch("hive_metastore_client.builders.column_builder.FieldSchema")
    def test_build(self, mocked_field_schema):
        # arrange
        mocked_name = "a"
        mocked_type = "b"
        mocked_comment = "c"

        mocked_obj = Mock()
        mocked_field_schema.return_value = mocked_obj
        # act
        returned_value = ColumnBuilder(
            name=mocked_name, type=mocked_type, comment=mocked_comment
        ).build()

        # assert
        assert returned_value == mocked_obj
        mocked_field_schema.assert_called_once_with(
            name=mocked_name, type=mocked_type, comment=mocked_comment
        )
