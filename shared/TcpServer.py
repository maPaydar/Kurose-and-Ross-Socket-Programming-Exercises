from shared.Log import Log
import socket

class TcpServer:
    def __init__(self, address='localhost', port=10000):
        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.address, self.port))
        self.sock.listen(5)
        Log.i('Tcp Server running on %s:%d', self.address, self.port)

    def listen(self, handle_client):
        Log.i('Tcp server is listening...')
        while True:
            socket = self.sock.accept()[0]
            Log.i('Socket %s connected', socket)
            handle_client(socket)