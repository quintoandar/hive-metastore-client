"""Database Builder Class."""
from typing import Mapping

from hive_metastore_client.builders.abstract_builder import AbstractBuilder
from thrift_files.libraries.thrift_hive_metastore_client.ttypes import Database, PrincipalPrivilegeSet, PrincipalType  # type: ignore # noqa: E501


class DatabaseBuilder(AbstractBuilder):
    """Builder class for database object."""

    def __init__(
        self,
        name: str,
        description: str = None,
        location_uri: str = None,
        parameters: Mapping[str, str] = None,
        privileges: PrincipalPrivilegeSet = None,
        owner_name: str = None,
        owner_type: PrincipalType = None,
        catalog_name: str = None,
    ):
        self.name = name
        self.description = description
        self.location_uri = location_uri
        self.parameters = parameters
        self.privileges = privileges
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.catalog_name = catalog_name

    def build(self) -> Database:
        """
        Builds Database object given builder parameters.

        :return: Database object built
        """
        database = Database(
            name=self.name,
            description=self.description,
            locationUri=self.location_uri,
            parameters=self.parameters,
            privileges=self.privileges,
            ownerName=self.owner_name,
            ownerType=self.owner_type,
            catalogName=self.catalog_name,
        )
        return database
