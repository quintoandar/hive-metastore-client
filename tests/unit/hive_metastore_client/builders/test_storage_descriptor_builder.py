from unittest import mock
from unittest.mock import Mock

from hive_metastore_client.builders.storage_descriptor_builder import (
    StorageDescriptorBuilder,
)


class TestStorageDescriptorBuilder:
    @mock.patch(
        "hive_metastore_client.builders.storage_descriptor_builder.StorageDescriptor"
    )
    def test_build(self, mocked_storage_descriptor):
        # arrange
        mocked_columns = [Mock()]
        mocked_location = "<location>"
        mocked_input_format = "<input_format>"
        mocked_output_format = "<output_format>"
        mocked_compressed = True
        mocked_num_buckets = 1
        mocked_serde_info = Mock()
        mocked_bucket_cols = ["<bucket_cols>"]
        mocked_sort_cols = [Mock()]
        mocked_parameters = {"a": "1"}
        mocked_skewed_info = Mock()
        mocked_stored_as_sub_directories = False

        mocked_obj = Mock()
        mocked_storage_descriptor.return_value = mocked_obj

        # act
        returned_value = StorageDescriptorBuilder(
            columns=mocked_columns,
            location=mocked_location,
            input_format=mocked_input_format,
            output_format=mocked_output_format,
            compressed=mocked_compressed,
            num_buckets=mocked_num_buckets,
            serde_info=mocked_serde_info,
            bucket_cols=mocked_bucket_cols,
            sort_cols=mocked_sort_cols,
            parameters=mocked_parameters,
            skewed_info=mocked_skewed_info,
            stored_as_sub_directories=mocked_stored_as_sub_directories,
        ).build()

        # assert
        assert returned_value == mocked_obj
        mocked_storage_descriptor.assert_called_once_with(
            cols=mocked_columns,
            location=mocked_location,
            inputFormat=mocked_input_format,
            outputFormat=mocked_output_format,
            compressed=mocked_compressed,
            numBuckets=mocked_num_buckets,
            serdeInfo=mocked_serde_info,
            bucketCols=mocked_bucket_cols,
            sortCols=mocked_sort_cols,
            parameters=mocked_parameters,
            skewedInfo=mocked_skewed_info,
            storedAsSubDirectories=mocked_stored_as_sub_directories,
        )
