from sheard.ProxyHandler import ProxyHandler
from sheard.TcpServer import TcpServer
from sheard.ClientThread import ClientThread

if __name__ == '__main__':
    server = TcpServer('localhost', 8080)
    server.listen(lambda connection: ClientThread(connection, ProxyHandler()).start())
