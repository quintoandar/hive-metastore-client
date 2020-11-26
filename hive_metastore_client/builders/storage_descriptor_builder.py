from hive_metastore_client.builders.serde_info_builder import SerDeInfoBuilder
from thrift_files.libraries.thrift_hive_metastore_client.ttypes import (
    StorageDescriptor,
    FieldSchema,
)


class StorageDescriptorBuilder:
    def __init__(
        self,
        columns,
        location,
        input_format,
        output_format,
        serde_info=None,
        compressed=None,
        num_buckets=None,
        bucket_cols=None,
        sort_cols=None,
        parameters=None,
        skewed_info=None,
        stored_as_sub_directories=None,
    ) -> None:
        self.columns = columns
        self.location = location
        self.input_format = input_format
        self.output_format = output_format
        self.compressed = compressed
        self.num_buckets = num_buckets
        self.serde_info = serde_info or SerDeInfoBuilder().build()  # DEFAULT IS Parquet
        self.bucket_cols = bucket_cols
        self.sort_cols = sort_cols
        self.parameters = parameters
        self.skewed_info = skewed_info
        self.stored_as_sub_directories = stored_as_sub_directories

    def build(self) -> StorageDescriptor:

        return StorageDescriptor(
            cols=self.columns,
            location=self.location,
            inputFormat=self.input_format,
            outputFormat=self.output_format,
            compressed=self.compressed,
            numBuckets=self.num_buckets,
            serdeInfo=self.serde_info,
            bucketCols=self.bucket_cols,
            sortCols=self.sort_cols,
            parameters=self.parameters,
            skewedInfo=self.skewed_info,
            storedAsSubDirectories=self.stored_as_sub_directories,
        )
