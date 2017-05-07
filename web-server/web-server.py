from sheard.ClientThread import ClientThread
from sheard.TcpServer import TcpServer
from .HttpHandler import HttpHandler

if __name__ == '__main__':
    server = TcpServer()
    server.listen(lambda connection: ClientThread(connection, HttpHandler()).start())
