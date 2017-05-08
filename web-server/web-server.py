from sheard.ClientThread import ClientThread
from sheard.HttpHandler import HttpHandler
from sheard.TcpServer import TcpServer

if __name__ == '__main__':
    server = TcpServer()
    server.listen(lambda connection: ClientThread(connection, HttpHandler()).start())
