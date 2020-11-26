from thrift_files.libraries.thrift_hive_metastore_client.ttypes import Table


class TableBuilder:
    def __init__(
        self,
        table_name,
        db_name,
        storage_descriptor,
        owner=None,
        create_time=None,
        last_access_time=None,
        retention=None,
        partition_keys=None,
        parameters=None,
        view_original_text=None,
        view_expanded_text=None,
        table_type=None,
        privileges=None,
        temporary=False,
        rewrite_enabled=None,
    ) -> None:
        self.table_name = table_name
        self.db_name = db_name
        self.owner = owner
        self.create_time = create_time
        self.last_access_time = last_access_time
        self.retention = retention
        self.storage_descriptor = storage_descriptor
        self.partition_keys = partition_keys
        self.parameters = parameters
        self.view_original_text = view_original_text
        self.view_expanded_text = view_expanded_text
        self.table_type = table_type
        self.privileges = privileges
        self.temporary = temporary
        self.rewrite_enabled = rewrite_enabled


    def build(self) -> Table:
        return Table(
            tableName=self.table_name,
            dbName=self.db_name,
            owner=self.owner,
            createTime=self.create_time,
            lastAccessTime=self.last_access_time,
            retention=self.retention,
            sd=self.storage_descriptor,
            partitionKeys=self.partition_keys,
            parameters=self.parameters,
            viewOriginalText=self.view_original_text,
            viewExpandedText=self.view_expanded_text,
            tableType=self.table_type,
            privileges=self.privileges,
            temporary=self.temporary,
            rewriteEnabled=self.rewrite_enabled,
        )
