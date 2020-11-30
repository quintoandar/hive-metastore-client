from unittest import mock
from unittest.mock import Mock
from hive_metastore_client.builders.database_builder import DatabaseBuilder


class TestDatabaseBuilder:
    @mock.patch("hive_metastore_client.builders.database_builder.Database")
    def test_build(self, mocked_database):
        # arrange
        mocked_database_name = "database_name"

        mocked_obj = Mock()
        mocked_database.return_value = mocked_obj

        # act
        returned_value = DatabaseBuilder(name=mocked_database_name).build()

        # assert
        assert returned_value == mocked_obj
        mocked_database.assert_called_once_with(
            name=mocked_database_name,
            description=None,
            locationUri=None,
            parameters=None,
            privileges=None,
            ownerName=None,
            ownerType=None,
            catalogName=None,
        )
