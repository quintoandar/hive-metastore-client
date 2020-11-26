from thrift_files.libraries.thrift_hive_metastore_client.ttypes import FieldSchema


class ColumnBuilder:
    def __init__(self, name, type, comment=None) -> None:
        self.name = name
        self.type = type
        self.comment = comment

    def build(self) -> FieldSchema:
        return FieldSchema(name=self.name, type=self.type, comment=self.comment)
