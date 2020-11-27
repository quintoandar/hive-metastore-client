"""Base class for handling the connection with the Thrift server."""
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport

from thrift_files.libraries.thrift_hive_metastore_client.ThriftHiveMetastore import (  # type: ignore # noqa: E501
    Client as ThriftClient,
)


class HiveMetastoreClient(ThriftClient):
    """Handles the connection with the Thrift server."""

    def __init__(self, host: str, port: int = 9083) -> None:
        """
        Instantiates the client object for given host and port.

        :param host: thrive metastore host. I.g.: https://xpto.com
        :param port: hive metastore port. Default is 9083.
        """
        protocol = self._init_protocol(host, port)
        super().__init__(protocol)

    @staticmethod
    def _init_protocol(host: str, port: int) -> TBinaryProtocol:
        """
        Instantiates the binary protocol object.

        This object contains the implementation of the Thrift protocol driver.

        :param host: thrive metastore host. I.g.: https://xpto.com
        :param port: the hive metastore port
        :return: the Thrift protocol driver
        :rtype: thrift.protocol.TBinaryProtocol.TBinaryProtocol
        """
        transport = TSocket.TSocket(host, int(port))
        transport = TTransport.TBufferedTransport(transport)

        return TBinaryProtocol.TBinaryProtocol(transport)

    def open(self) -> "HiveMetastoreClient":
        """
        Opens the connection with the Thrift server.

        :return: HiveMetastoreClientConnector instance
        """
        self._oprot.trans.open()
        return self

    def close(self) -> None:
        """Closes the connection with the Thrift server."""
        self._oprot.trans.close()

    def __enter__(self) -> "HiveMetastoreClient":
        """Handles the conn opening whenever the 'with' block statement is used."""
        self.open()
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        """Handles the conn closing after the code inside 'with' block is ended."""
        self.close()
