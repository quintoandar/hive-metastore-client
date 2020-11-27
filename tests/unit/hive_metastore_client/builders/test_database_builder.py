from hive_metastore_client.builders.database_builder import DatabaseBuilder
from thrift_files.libraries.thrift_hive_metastore_client.ttypes import Database


class TestDatabaseBuilder:
    def test_build_with_name(self):
        database_builder = DatabaseBuilder(name="database_name")
        database = Database(name="database_name")

        assert database == database_builder.build()

    def test_build_with_description(self):
        database_builder = DatabaseBuilder(
            name="database_name", description="description"
        )
        database = Database(name="database_name", description="description")

        assert database == database_builder.build()
