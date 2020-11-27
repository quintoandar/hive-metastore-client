"""TableBuilder."""
from typing import List, Dict

from thrift_files.libraries.thrift_hive_metastore_client.ttypes import (  # type: ignore # noqa: E501
    Table,
    FieldSchema,
    PrincipalPrivilegeSet,
    CreationMetadata,
    PrincipalType,
    StorageDescriptor,
)


class TableBuilder:
    """Builds thrift Table object."""

    def __init__(
        self,
        table_name: str,
        db_name: str,
        storage_descriptor: StorageDescriptor,
        owner: str = None,
        create_time: int = None,
        last_access_time: int = None,
        retention: int = None,
        partition_keys: List[FieldSchema] = None,
        parameters: Dict[str, str] = None,
        view_original_text: str = None,
        view_expanded_text: str = None,
        table_type: str = None,
        privileges: PrincipalPrivilegeSet = None,
        temporary: bool = False,
        rewrite_enabled: bool = None,
        creation_metadata: CreationMetadata = None,
        cat_name: str = None,
        owner_type: PrincipalType = PrincipalType.USER,
    ) -> None:
        """
        Constructor.

        :param table_name: name of the table
        :param db_name: database name ('default')
        :param storage_descriptor:
        :param owner: owner of this table
        :param create_time: creation time of the table
        :param last_access_time: last access time (usually this will be filled
        from HDFS and shouldn't be relied on)
        :param retention: retention time
        :param partition_keys: partition keys of the table. only primitive
        types are supported
        :param parameters: to store comments or any other user level parameters
        :param view_original_text: original view text, null for non-view
        :param view_expanded_text: expanded view text, null for non-view
        :param table_type: table type enum, e.g. EXTERNAL_TABLE
        :param privileges: (no information in thrift mapping)
        :param temporary: (no information in thrift mapping)
        :param rewrite_enabled: rewrite enabled or not
        :param creation_metadata: only for MVs, it stores table names used and
        txn list at MV creation
        :param cat_name: Name of the catalog the table is in
        :param owner_type: owner type of this table (default to USER for
        backward compatibility)
        """
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
        self.creation_metadata = creation_metadata
        self.cat_name = cat_name
        self.owner_type = owner_type

    def build(self) -> Table:
        """Returns the thrift Table object."""
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
            creationMetadata=self.creation_metadata,
            catName=self.cat_name,
            ownerType=self.owner_type,
        )
