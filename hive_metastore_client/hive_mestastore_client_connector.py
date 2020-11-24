"""Base class for handling the connection with the Thrift server."""
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport

from hive_metastore_client.clients.thrift_hive_metastore_client import ThriftClient


class HiveMetastoreClientConnector(ThriftClient):
    """Handles the connection with the Thrift server."""

    def __init__(self, host, port=9083):
        """
        Instantiates the client object for given host and port.

        :param host: thrive metastore host. I.g.: https://xpto.com
        :param port: hive metastore port. Default is 9083.
        """
        protocol = self._init_protocol(host, port)
        super().__init__(protocol)

    @staticmethod
    def _init_protocol(host, port):
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

    def open(self):
        """
        Opens the connection with the Thrift server.

        :return: HiveMetastoreClientConnector instance
        """
        self._oprot.trans.open()
        return self

    def close(self):
        """Closes the connection with the Thrift server."""
        self._oprot.trans.close()

    def __enter__(self):
        """Handles the conn opening whenever the with statement is used."""
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Handles the conn's closing after the code in with stmt is ended."""
        self.close()
