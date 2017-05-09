from shared.ProxyHandler import ProxyHandler
from shared.TcpServer import TcpServer
from shared.ClientThread import ClientThread

if __name__ == '__main__':
    server = TcpServer('localhost', 8080)
    server.listen(lambda connection: ClientThread(connection, ProxyHandler()).start())
