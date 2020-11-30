from unittest import mock
from unittest.mock import Mock

from hive_metastore_client.builders.serde_info_builder import SerDeInfoBuilder


class TestSerDeInfoBuilder:
    @mock.patch("hive_metastore_client.builders.serde_info_builder.SerDeInfo")
    def test_build(self, mocked_serde_info):
        # arrange
        mocked_name = "<name>"
        mocked_serialization_lib = "<serialization_lib>"
        mocked_parameters = {"a": "1", "b": "2"}
        mocked_description = "<description>"
        mocked_serializer_class = "<serializer_class>"
        mocked_deserializer_class = "<deserializer_class>"
        mocked_serde_type = Mock()

        mocked_obj = Mock()
        mocked_serde_info.return_value = mocked_obj
        # act
        returned_value = SerDeInfoBuilder(
            name=mocked_name,
            serialization_lib=mocked_serialization_lib,
            parameters=mocked_parameters,
            description=mocked_description,
            serializer_class=mocked_serializer_class,
            deserializer_class=mocked_deserializer_class,
            serde_type=mocked_serde_type,
        ).build()

        # assert
        assert returned_value == mocked_obj
        mocked_serde_info.assert_called_once_with(
            name=mocked_name,
            serializationLib=mocked_serialization_lib,
            parameters=mocked_parameters,
            description=mocked_description,
            serializerClass=mocked_serializer_class,
            deserializerClass=mocked_deserializer_class,
            serdeType=mocked_serde_type,
        )
