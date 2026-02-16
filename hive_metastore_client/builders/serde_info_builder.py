"""SerDeInfoBuilder."""

from typing import Dict, Optional

from hive_metastore_client.builders.abstract_builder import AbstractBuilder
from thrift_files.libraries.thrift_hive_metastore_client.ttypes import (  # type: ignore # noqa: E501
    SerDeInfo,
    SerdeType,
)


class SerDeInfoBuilder(AbstractBuilder):
    """Builds thrift table's Serialization-Deserialization info object."""

    def __init__(
        self,
        name: Optional[str] = None,
        serialization_lib: Optional[str] = None,
        parameters: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        serializer_class: Optional[str] = None,
        deserializer_class: Optional[str] = None,
        serde_type: Optional[SerdeType] = None,
    ) -> None:
        """
        Constructor.

        :param name: name of the serde. Table name by default
        :param serialization_lib: the class that implements the extractor & loader
        :param parameters: initialization parameters
        :param description: serde description
        :param serializer_class: serializer class for serde
        :param deserializer_class: deserializer class for serde
        :param serde_type: one of SerdeType values
        """
        self.name = name
        self.serialization_lib = serialization_lib
        self.parameters = {} if parameters is None else parameters
        self.description = description
        self.serializer_class = serializer_class
        self.deserializer_class = deserializer_class
        self.serde_type = serde_type

    def build(self) -> SerDeInfo:
        """Returns the thrift SerDeInfo object."""
        return SerDeInfo(
            name=self.name,
            serializationLib=self.serialization_lib,
            parameters=self.parameters,
            description=self.description,
            serializerClass=self.serializer_class,
            deserializerClass=self.deserializer_class,
            serdeType=self.serde_type,
        )
