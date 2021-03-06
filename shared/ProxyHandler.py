import socket

from shared.Handler import Handler
from shared.Log import Log
from shared.Util import Util


class ProxyHandler(Handler):
    cache = {}

    def handle(self, client, data):
        try:
            object = Util.get_object_from_http_request(str(data.rstrip()))
            if object in ProxyHandler.cache:
                response = ProxyHandler.cache[object]
                Log.i('data %s was cached', object)
            else:
                Log.i('data %s not cached', object)
                response = self.send_to_web_server(data)
                ProxyHandler.cache[object] = response
            client.connection.sendall(response)
            client.connection.close()
        except Exception:
            pass
        client.stop()


def send_to_web_server(self, request):
    client_socket = socket.socket()
    client_socket.connect(('localhost', 10000))
    client_socket.send(request)
    data = Util.receive_all(client_socket)
    return data
