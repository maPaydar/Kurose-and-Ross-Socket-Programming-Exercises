from sheard.HttpHandler import HttpHandler
from sheard.TcpServer import TcpServer
from sheard.ClientThread import ClientThread

if __name__ == '__main__':
    server = TcpServer()
    server.listen(lambda connection: ClientThread(connection, HttpHandler()).start())
