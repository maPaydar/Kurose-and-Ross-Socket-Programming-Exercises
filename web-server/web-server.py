from shared.ClientThread import ClientThread
from shared.HttpHandler import HttpHandler
from shared.TcpServer import TcpServer

if __name__ == '__main__':
    server = TcpServer()
    server.listen(lambda connection: ClientThread(connection, HttpHandler()).start())
