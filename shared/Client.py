import socket

from shared.Log import Log


class Client:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        else:
            self.sock = sock
        Log.i('Client created')

    def connect(self, host, port):
        self.host = host
        self.port = port
        self.sock.connect((host, port))
        Log.i('Client connected to server %s:%d', host, port)

    def send(self, msg):
        self.MSGLEN = len(msg)
        totalsent = 0
        while totalsent < self.MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def sendto(self, msg, host, port):
        self.sock.sendto(msg, (host, port))

    def receive(self):
        chunk = self.sock.recvfrom(1024)
        return chunk

