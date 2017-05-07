from sheard.Handler import Handler
from sheard.Log import Log
from sheard.Util import Util


class HttpHandler(Handler):
    def handle(self, client, data):
        try:
            object = Util.get_object_from_http_request(str(data.rstrip()))
            Log.d('Requested Object = %s', object)
            data = Util.get_file_data(object, 'rb')
            headers = Util.get_simple_http_header('ok', {'Content-Type': '*/*', 'Content-Length': str(len(data))})
            Log.d('Response Headers = %s', headers)
            client.connection.send(headers)
            Log.d('Response Data = %s', data)
            client.connection.sendall(data)
            Log.i('Send data to client')

        except FileNotFoundError:
            reply = "HTTP/1.1 404 Not Found\r\n"
            client.connection.send(reply.encode('ascii'))
        client.stop()
