from hive_metastore_client.hive_metastore.ThriftHiveMetastore import Client as ThriftClient
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol


class HiveMetastoreClientConnector(ThriftClient):
    """
    The Hive Metastore Client bla
    """

    def __init__(self, host, port=9083):
        """
        Instantiates the client object for given host and port

        :param host: thrive metastore host. I.g.: https://xpto.com
        :param port: hive metastore port. Default is 9083.
        """
        protocol = self._init_protocol(host, port)
        super().__init__(protocol)

    @staticmethod
    def _init_protocol(host, port):
        """
        Instantiates the binary protocol object with the implementation
        of the Thrift protocol driver.

        :param host: thrive metastore host. I.g.: https://xpto.com
        :param port: the hive metastore port
        :return: the Thrift protocol driver
        :rtype: thrift.protocol.TBinaryProtocol.TBinaryProtocol
        """
        transport = TSocket.TSocket(host, int(port))
        transport = TTransport.TBufferedTransport(transport)

        return TBinaryProtocol.TBinaryProtocol(transport)

    def open(self):
        self._oprot.trans.open()
        return self

    def close(self):
        self._oprot.trans.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
