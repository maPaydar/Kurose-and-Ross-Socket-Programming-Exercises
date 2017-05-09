import socket

from sheard.Log import Log


class UdpServer:
    def __init__(self, host='localhost', port=10000):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        Log.i("Server ready on %s:%d", self.host, self.port)

    def start(self, on_received):
        while True:
            data, client_address = self.sock.recvfrom(1024)
            Log.i("receive data from client")
            on_received(data, client_address)

    def send(self, data, address):
        self.sock.sendto(data, address)
