import threading
from sheard.Log import Log


class ClientThread(threading.Thread):
    def __init__(self, connection, handler):
        threading.Thread.__init__(self)
        self.connection = connection
        self.handler = handler
        self.is_stopped = False

    def start(self):
        while not self.is_stopped:
            Log.i('Socket is online')
            self.handle(self.connection.recv(1024))
        Log.i('Socket connection closed')

    def stop(self):
        self.is_stopped = True
        self.connection.close()
        Log.d('Stop connection')

    def handle(self, data):
        self.handler.handle(self, data)
