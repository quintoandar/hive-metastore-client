from copy import copy
from unittest import mock
from unittest.mock import Mock, ANY

import pytest
from pytest import raises
from thrift.transport.TTransport import TTransportException

from hive_metastore_client import HiveMetastoreClient
from hive_metastore_client.builders import TableBuilder
from thrift_files.libraries.thrift_hive_metastore_client.ttypes import (
    FieldSchema,
    NoSuchObjectException,
    AlreadyExistsException,
    PartitionValuesRequest,
)


class TestHiveMetastoreClient:
    @mock.patch("hive_metastore_client.hive_metastore_client.TSocket")
    @mock.patch("hive_metastore_client.hive_metastore_client.TTransport")
    @mock.patch("hive_metastore_client.hive_metastore_client.TBinaryProtocol")
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

    @mock.patch.object(HiveMetastoreClient, "get_table")
    @mock.patch.object(HiveMetastoreClient, "alter_table")
    def test_add_columns_to_table(
        self, mocked_alter_table, mocked_get_table, hive_metastore_client
    ):
        # arrange
        db_name = "db_name"
        table_name = "table_name"
        cols = [Mock(), Mock()]

        mocked_return_get_table = Mock()
        mocked_get_table.return_value = mocked_return_get_table

        # act
        hive_metastore_client.add_columns_to_table(
            db_name=db_name, table_name=table_name, columns=cols
        )

        # assert
        mocked_get_table.assert_called_once_with(dbname=db_name, tbl_name=table_name)
        mocked_alter_table.assert_called_once_with(
            dbname=db_name, tbl_name=table_name, new_tbl=mocked_return_get_table
        )

    @mock.patch.object(HiveMetastoreClient, "get_table")
    @mock.patch.object(HiveMetastoreClient, "alter_table")
    @mock.patch.object(HiveMetastoreClient, "setMetaConf")
    def test_drop_columns_from_table(
        self,
        mocked_set_meta_conf,
        mocked_alter_table,
        mocked_get_table,
        hive_metastore_client,
    ):
        # arrange
        db_name = "db_name"
        table_name = "table_name"
        cols = ["col1", "col2"]

        mocked_return_get_table = Mock()
        mocked_return_get_table.sd.cols = [
            FieldSchema(name="col1"),
            FieldSchema(name="col2"),
            FieldSchema(name="col3"),
        ]
        mocked_get_table.return_value = mocked_return_get_table
        expected_table_column = [FieldSchema(name="col3")]
        expected_mocked_table = mocked_return_get_table
        expected_mocked_table.sd.cols = expected_table_column

        # act
        hive_metastore_client.drop_columns_from_table(
            db_name=db_name, table_name=table_name, columns=cols
        )

        # assert
        mocked_set_meta_conf.assert_called_once_with(
            hive_metastore_client.COL_TYPE_INCOMPATIBILITY_DISALLOW_CONFIG, "false"
        )
        mocked_get_table.assert_called_once_with(dbname=db_name, tbl_name=table_name)
        mocked_alter_table.assert_called_once_with(
            dbname=db_name, tbl_name=table_name, new_tbl=expected_mocked_table
        )

    def test__validate_lists_length_with_diff_lens(self, hive_metastore_client):
        # arrange
        list_a = [1, 2, 3]
        list_b = [1]

        # act
        with pytest.raises(ValueError):
            hive_metastore_client._validate_lists_length(list_a, list_b)

    def test__validate_lists_length_with_same_len(self, hive_metastore_client):
        # arrange
        list_a = [1, 2, 3]
        list_b = [1, 4, 1000]

        # act
        hive_metastore_client._validate_lists_length(list_a, list_b)

    @mock.patch.object(HiveMetastoreClient, "get_table")
    @mock.patch.object(HiveMetastoreClient, "_format_partitions_location")
    @mock.patch.object(HiveMetastoreClient, "add_partition")
    def test_add_partitions_if_not_exists(
        self,
        mocked_add_partition,
        mocked__format_partitions,
        mocked_get_table,
        hive_metastore_client,
    ):
        # arrange
        db_name = "database_name"
        table_name = "table_name"

        mocked_table = Mock()
        mocked_get_table.return_value = mocked_table

        mocked_partition_list = [Mock()]
        partition_1 = "abc"
        formatted_partitions_location = [partition_1]
        mocked__format_partitions.return_value = formatted_partitions_location

        # act
        hive_metastore_client.add_partitions_if_not_exists(
            db_name=db_name, table_name=table_name, partition_list=mocked_partition_list
        )

        # assert
        mocked_get_table.assert_called_once_with(dbname=db_name, tbl_name=table_name)
        mocked__format_partitions.assert_called_once_with(
            partition_list=mocked_partition_list,
            table_storage_descriptor=mocked_table.sd,
            table_partition_keys=mocked_table.partitionKeys,
        )
        mocked_add_partition.assert_called_once_with(partition_1)

    @mock.patch.object(HiveMetastoreClient, "get_table")
    @mock.patch.object(HiveMetastoreClient, "_format_partitions_location")
    @mock.patch.object(HiveMetastoreClient, "add_partition")
    def test_add_partitions_if_not_exists_with_duplicated_partitions(
        self,
        mocked_add_partition,
        mocked__format_partitions,
        mocked_get_table,
        hive_metastore_client,
    ):
        # arrange
        db_name = "database_name"
        table_name = "table_name"

        mocked_table = Mock()
        mocked_get_table.return_value = mocked_table

        mocked_partition_list = [Mock()]
        partition_1 = "abc"
        partition_2 = "abcd"
        formatted_partitions_location = [partition_1, partition_2]
        mocked__format_partitions.return_value = formatted_partitions_location

        mocked_add_partition.side_effect = [True, AlreadyExistsException()]

        # act
        hive_metastore_client.add_partitions_if_not_exists(
            db_name=db_name, table_name=table_name, partition_list=mocked_partition_list
        )

        # assert
        mocked_get_table.assert_called_once_with(dbname=db_name, tbl_name=table_name)
        mocked__format_partitions.assert_called_once_with(
            partition_list=mocked_partition_list,
            table_storage_descriptor=mocked_table.sd,
            table_partition_keys=mocked_table.partitionKeys,
        )
        mocked_add_partition.assert_has_calls(
            [mock.call(partition_1), mock.call(partition_2)]
        )

    @mock.patch.object(HiveMetastoreClient, "get_table")
    @mock.patch.object(HiveMetastoreClient, "_format_partitions_location")
    @mock.patch.object(HiveMetastoreClient, "add_partition")
    def test_add_partitions_if_not_exists_with_invalid_partitions(
        self,
        mocked_add_partition,
        mocked__format_partitions,
        mocked_get_table,
        hive_metastore_client,
    ):
        # assert
        with raises(ValueError):
            # act
            hive_metastore_client.add_partitions_if_not_exists(
                db_name=ANY, table_name=ANY, partition_list=[]
            )
        mocked_get_table.assert_not_called()
        mocked__format_partitions.assert_not_called()
        mocked_add_partition.assert_not_called()

    @mock.patch.object(HiveMetastoreClient, "get_table")
    @mock.patch.object(HiveMetastoreClient, "_format_partitions_location")
    @mock.patch.object(HiveMetastoreClient, "add_partitions")
    def test_add_partitions_to_table(
        self,
        mocked_add_partitions,
        mocked__format_partitions,
        mocked_get_table,
        hive_metastore_client,
    ):
        # arrange
        db_name = "database_name"
        table_name = "table_name"

        mocked_table = Mock()
        mocked_get_table.return_value = mocked_table

        mocked_partition_list = [Mock()]
        formatted_partitions_location = ["abc"]
        mocked__format_partitions.return_value = formatted_partitions_location

        # act
        hive_metastore_client.add_partitions_to_table(
            db_name=db_name, table_name=table_name, partition_list=mocked_partition_list
        )

        # assert
        mocked_get_table.assert_called_once_with(dbname=db_name, tbl_name=table_name)
        mocked__format_partitions.assert_called_once_with(
            partition_list=mocked_partition_list,
            table_storage_descriptor=mocked_table.sd,
            table_partition_keys=mocked_table.partitionKeys,
        )
        mocked_add_partitions.assert_called_once_with(formatted_partitions_location)

    @mock.patch.object(HiveMetastoreClient, "get_table")
    @mock.patch.object(HiveMetastoreClient, "_format_partitions_location")
    @mock.patch.object(HiveMetastoreClient, "add_partitions")
    def test_add_partitions_to_table_with_duplicated_partitions(
        self,
        mocked_add_partitions,
        mocked__format_partitions,
        mocked_get_table,
        hive_metastore_client,
    ):
        # arrange
        db_name = "database_name"
        table_name = "table_name"

        mocked_table = Mock()
        mocked_get_table.return_value = mocked_table

        mocked_partition_list = [Mock()]
        formatted_partitions_location = ["abc"]
        mocked__format_partitions.return_value = formatted_partitions_location

        mocked_add_partitions.side_effect = AlreadyExistsException()

        # assert
        with raises(AlreadyExistsException):
            # act
            hive_metastore_client.add_partitions_to_table(
                db_name=db_name,
                table_name=table_name,
                partition_list=mocked_partition_list,
            )

        mocked_get_table.assert_called_once_with(dbname=db_name, tbl_name=table_name)
        mocked__format_partitions.assert_called_once_with(
            partition_list=mocked_partition_list,
            table_storage_descriptor=mocked_table.sd,
            table_partition_keys=mocked_table.partitionKeys,
        )
        mocked_add_partitions.assert_called_once_with(formatted_partitions_location)

    @mock.patch.object(HiveMetastoreClient, "get_table")
    @mock.patch.object(HiveMetastoreClient, "_format_partitions_location")
    @mock.patch.object(HiveMetastoreClient, "add_partitions")
    def test_add_partitions_to_table_with_empty_partition_list(
        self,
        mocked_add_partitions,
        mocked__format_partitions,
        mocked_get_table,
        hive_metastore_client,
    ):
        # assert
        with raises(ValueError):
            # act
            hive_metastore_client.add_partitions_to_table(
                db_name=ANY, table_name=ANY, partition_list=[]
            )
        mocked_get_table.assert_not_called()
        mocked__format_partitions.assert_not_called()
        mocked_add_partitions.assert_not_called()

    @mock.patch.object(HiveMetastoreClient, "_validate_lists_length")
    def test_format_partitions_location(
        self, mocked_validate_lists_length, hive_metastore_client
    ):
        # arrange
        mocked_partition = Mock()
        mocked_partition.sd = None
        mocked_partition.values = ["2000"]
        partition_list = [mocked_partition]
        mocked_table_storage_descriptor = Mock()
        mocked_table_storage_descriptor.location = "xyz"
        mocked_field_schema_1 = Mock()
        mocked_field_schema_1.name = "year"
        table_partition_keys = [mocked_field_schema_1]
        expected_location = "xyz/year=2000"

        # act
        returned_value = hive_metastore_client._format_partitions_location(
            partition_list, mocked_table_storage_descriptor, table_partition_keys
        )

        # assert
        assert mocked_validate_lists_length.call_count == 1
        assert returned_value[0].sd.location == expected_location

    @mock.patch.object(HiveMetastoreClient, "create_database")
    def test_create_database_if_not_exists_with_nonexistent_database(
        self, mocked_create_database, hive_metastore_client,
    ):
        # arrange
        mocked_database_obj = Mock()

        # act
        hive_metastore_client.create_database_if_not_exists(mocked_database_obj)

        # assert
        mocked_create_database.assert_called_once_with(mocked_database_obj)

    @mock.patch.object(HiveMetastoreClient, "create_database")
    def test_create_database_if_not_exists_with_existent_database(
        self, mocked_create_database, hive_metastore_client,
    ):
        # arrange
        mocked_database_obj = Mock()
        mocked_create_database.side_effect = AlreadyExistsException()

        # act
        hive_metastore_client.create_database_if_not_exists(mocked_database_obj)

        # assert
        mocked_create_database.assert_called_once_with(mocked_database_obj)

    @mock.patch.object(HiveMetastoreClient, "create_table")
    def test_create_external_table(self, mocked_create_table, hive_metastore_client):
        # arrange
        table = TableBuilder(
            table_name="table_name",
            db_name="database_name",
            owner="owner",
            storage_descriptor=Mock(),
            partition_keys=[],
        ).build()
        updated_table = copy(table)
        updated_table.parameters = {"EXTERNAL": "TRUE"}
        updated_table.tableType = "EXTERNAL_TABLE"

        # act
        hive_metastore_client.create_external_table(table)

        # assert
        mocked_create_table.assert_called_once_with(updated_table)

    @mock.patch.object(HiveMetastoreClient, "get_table", return_value=None)
    def test_get_partition_keys_objects_with_invalid_table(
        self, mocked_get_table, hive_metastore_client,
    ):
        # arrange
        table_name = "table_name"
        database_name = "database_name"

        # act
        returned_value = hive_metastore_client.get_partition_keys_objects(
            database_name, table_name
        )

        # assert
        assert returned_value == []
        mocked_get_table.assert_called_once_with(
            dbname=database_name, tbl_name=table_name
        )

    @mock.patch.object(HiveMetastoreClient, "get_table")
    def test_get_partition_keys_objects_with_not_partitioned_table(
        self, mocked_get_table, hive_metastore_client,
    ):
        # arrange
        table_name = "table_name"
        database_name = "database_name"
        mocked_table = Mock()
        # the default return from hive metastore for not partitioned tables is an empty list
        mocked_table.partitionKeys = []
        mocked_get_table.return_value = mocked_table

        # act
        returned_value = hive_metastore_client.get_partition_keys_objects(
            database_name, table_name
        )

        # assert
        assert returned_value == []
        mocked_get_table.assert_called_once_with(
            dbname=database_name, tbl_name=table_name
        )

    @mock.patch.object(HiveMetastoreClient, "get_table")
    def test_get_partition_keys_objects_with_partitioned_table(
        self, mocked_get_table, hive_metastore_client,
    ):
        # arrange
        table_name = "table_name"
        database_name = "database_name"
        mocked_table = Mock()
        mocked_partition_a = Mock()
        mocked_partition_b = Mock()
        mocked_table.partitionKeys = [mocked_partition_a, mocked_partition_b]
        mocked_get_table.return_value = mocked_table

        # act
        returned_value = hive_metastore_client.get_partition_keys_objects(
            database_name, table_name
        )

        # assert
        assert returned_value == [mocked_partition_a, mocked_partition_b]
        mocked_get_table.assert_called_once_with(
            dbname=database_name, tbl_name=table_name
        )

    @mock.patch.object(
        HiveMetastoreClient, "get_partition_keys_objects", return_value=[]
    )
    def test_get_partition_keys_names_with_invalid_or_not_partitioned_table(
        self, mocked_get_partition_keys_objects, hive_metastore_client,
    ):
        # arrange
        table_name = "table_name"
        database_name = "database_name"

        # act
        returned_value = hive_metastore_client.get_partition_keys_names(
            database_name, table_name
        )

        # assert
        assert returned_value == []
        mocked_get_partition_keys_objects.assert_called_once_with(
            db_name=database_name, table_name=table_name
        )

    @mock.patch.object(
        HiveMetastoreClient, "get_partition_keys_objects", return_value=[]
    )
    def test_get_partition_keys_names_with_partitioned_table(
        self, mocked_get_partition_keys_objects, hive_metastore_client,
    ):
        # arrange
        table_name = "table_name"
        database_name = "database_name"
        mocked_partition_a = Mock()
        mocked_partition_a.name = "mocked_partition_a"
        mocked_partition_b = Mock()
        mocked_partition_b.name = "mocked_partition_b"
        mocked_get_partition_keys_objects.return_value = [
            mocked_partition_a,
            mocked_partition_b,
        ]
        expected_return = ["mocked_partition_a", "mocked_partition_b"]

        # act
        returned_value = hive_metastore_client.get_partition_keys_names(
            database_name, table_name
        )

        # assert
        assert returned_value == expected_return
        mocked_get_partition_keys_objects.assert_called_once_with(
            db_name=database_name, table_name=table_name
        )

    @mock.patch.object(HiveMetastoreClient, "drop_partition", return_value=None)
    def test_bulk_drop_partitions(self, mock_drop_partition, hive_metastore_client):
        # arrange
        db_name = "db_name"
        table_name = "table_name"
        partition_list = [["1995", "9", "22"], ["2013", "2", "14"], ["2021", "1", "1"]]

        # act
        hive_metastore_client.bulk_drop_partitions(
            db_name, table_name, partition_list, mock.ANY
        )

        # assert
        assert mock_drop_partition.call_count == len(partition_list)

    @mock.patch.object(HiveMetastoreClient, "drop_partition", return_value=None)
    def test_bulk_drop_partitions_with_errors(
        self, mock_drop_partition, hive_metastore_client
    ):
        # arrange
        db_name = "db_name"
        table_name = "table_name"
        partition_list = [["1995", "9", "22"], ["2021", "1", "1"], ["2021", "1", "2"]]
        mock_drop_partition.side_effect = [
            None,
            NoSuchObjectException(),
            NoSuchObjectException(),
        ]

        # assert
        with raises(
            NoSuchObjectException,
            match=r"partitions_not_dropped=\[\['2021', '1', '1'\], \['2021', '1', '2'\]\]",
        ):
            # act
            hive_metastore_client.bulk_drop_partitions(
                db_name, table_name, partition_list, mock.ANY
            )

        assert mock_drop_partition.call_count == len(partition_list)

    @mock.patch.object(HiveMetastoreClient, "get_partition_values", return_value=[])
    @mock.patch.object(
        HiveMetastoreClient, "get_partition_keys_objects", return_value=[]
    )
    def test_get_partition_values_from_table_with_partitioned_table(
        self,
        mocked_get_partition_keys_objects,
        mocked_get_partition_values,
        hive_metastore_client,
    ):
        # arrange
        table_name = "table_name"
        database_name = "database_name"

        mocked_partition_a = Mock()
        mocked_partition_a.name = "partition_key_1"
        mocked_partition_b = Mock()
        mocked_partition_b.name = "partition_key_2"
        mocked_get_partition_keys_objects.return_value = [
            mocked_partition_a,
            mocked_partition_b,
        ]

        mocked_partition_values_response = Mock()
        mocked_partition_values = []

        mocked_partition_values_partition_a = Mock()
        mocked_partition_values_partition_a.row = ["partition_a"]
        mocked_partition_values.append(mocked_partition_values_partition_a)

        mocked_partition_values_partition_b = Mock()
        mocked_partition_values_partition_b.row = ["partition_b"]
        mocked_partition_values.append(mocked_partition_values_partition_b)

        mocked_partition_values_response.partitionValues = mocked_partition_values
        mocked_get_partition_values.return_value = mocked_partition_values_response
        expected_partition_values_request = PartitionValuesRequest(
            dbName=database_name,
            tblName=table_name,
            partitionKeys=mocked_get_partition_keys_objects.return_value,
        )
        expected_return = [["partition_a"], ["partition_b"]]

        # act
        returned_value = hive_metastore_client.get_partition_values_from_table(
            database_name, table_name
        )

        # assert
        assert returned_value == expected_return
        mocked_get_partition_keys_objects.assert_called_once_with(
            db_name=database_name, table_name=table_name
        )
        mocked_get_partition_values.assert_called_once_with(
            expected_partition_values_request
        )

    @mock.patch.object(HiveMetastoreClient, "get_partition_values")
    @mock.patch.object(HiveMetastoreClient, "get_partition_keys_objects")
    def test_get_partition_values_from_table_with_non_partitioned_table(
        self,
        mocked_get_partition_keys_objects,
        mocked_get_partition_values,
        hive_metastore_client,
    ):
        # arrange
        table_name = "table_name"
        database_name = "database_name"

        mocked_get_partition_keys_objects.return_value = []
        expected_partition_values_request = PartitionValuesRequest(
            dbName=database_name, tblName=table_name, partitionKeys=[],
        )

        mocked_get_partition_values.side_effect = [TTransportException()]
        expected_return = []

        # act
        returned_value = hive_metastore_client.get_partition_values_from_table(
            database_name, table_name
        )

        # assert
        assert returned_value == expected_return
        mocked_get_partition_keys_objects.assert_called_once_with(
            db_name=database_name, table_name=table_name
        )

    @mock.patch.object(
        HiveMetastoreClient, "get_partition_keys_objects", return_value=[]
    )
    def test_get_partition_keys_with_partitioned_table(
        self, mocked_get_partition_keys_objects, hive_metastore_client
    ):
        # arrange
        db_name = "<db_name>"
        table_name = "<table_name>"

        partition_1 = Mock()
        partition_1.name = "name_1"
        partition_1.type = "type_1"

        partition_2 = Mock()
        partition_2.name = "name_2"
        partition_2.type = "type_2"

        mocked_get_partition_keys_objects.return_value = [partition_1, partition_2]
        expected_value = [("name_1", "type_1"), ("name_2", "type_2")]
        # act
        returned_value = hive_metastore_client.get_partition_keys(db_name, table_name)

        # assert
        assert returned_value == expected_value
        mocked_get_partition_keys_objects.assert_called_once_with(
            db_name=db_name, table_name=table_name
        )

    @mock.patch.object(
        HiveMetastoreClient, "get_partition_keys_objects", return_value=[]
    )
    def test_get_partition_keys_with_non_partitioned_table(
        self, mocked_get_partition_keys_objects, hive_metastore_client
    ):
        # arrange
        db_name = "<db_name>"
        table_name = "<table_name>"

        mocked_get_partition_keys_objects.return_value = []
        expected_value = []
        # act
        returned_value = hive_metastore_client.get_partition_keys(db_name, table_name)

        # assert
        assert returned_value == expected_value
        mocked_get_partition_keys_objects.assert_called_once_with(
            db_name=db_name, table_name=table_name
        )

    @mock.patch.object(HiveMetastoreClient, "get_schema", return_value=None)
    def test_get_schema_with_non_empty_schema(
        self, mocked_get_schema, hive_metastore_client,
    ):
        # arrange
        table_name = "table_name"
        database_name = "database_name"

        mocked_field_schema_a = FieldSchema(name="col1")
        mocked_field_schema_b = FieldSchema(name="col12")
        mocked_get_schema.return_value = [mocked_field_schema_a, mocked_field_schema_b]

        # act
        returned_value = hive_metastore_client.get_field_schema(
            database_name, table_name
        )

        # assert
        assert returned_value == [mocked_field_schema_a, mocked_field_schema_b]
        mocked_get_schema.assert_called_once_with(
            dbname=database_name, tbl_name=table_name
        )
