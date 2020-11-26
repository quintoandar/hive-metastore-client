from thrift_files.libraries.thrift_hive_metastore_client.ttypes import SerDeInfo


class SerDeInfoBuilder:
    DEFAULT_SER_LIB = "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"

    def __init__(
        self,
        name=None,
        serialization_lib=None,
        parameters=None,
        description=None,
        serializer_class=None,
        deserializer_class=None,
        serde_type=None,
    ) -> None:
        self.name = name
        self.serialization_lib = serialization_lib or self.DEFAULT_SER_LIB
        self.parameters = parameters
        self.description = description
        self.serializer_class = serializer_class
        self.deserializer_class = deserializer_class
        self.serde_type = serde_type

    def build(self) -> SerDeInfo:
        return SerDeInfo(
            name=self.name,
            serializationLib=self.serialization_lib,
            parameters=self.parameters,
            description=self.description,
            serializerClass=self.serializer_class,
            deserializerClass=self.deserializer_class,
            serdeType=self.serde_type,
        )
