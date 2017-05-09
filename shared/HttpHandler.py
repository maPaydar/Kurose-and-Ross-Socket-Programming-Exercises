from shared.Handler import Handler
from shared.Log import Log
from shared.Util import Util


class HttpHandler(Handler):
    def handle(self, client, data):
        try:
            object = Util.get_object_from_http_request(str(data.rstrip()))
            Log.d('Requested Object = %s', object)
            data = Util.get_file_data(object, 'rb')
            headers = Util.get_simple_http_header('ok', {'Content-Type': '*/*', 'Content-Length': str(len(data))})
            Log.d('Response Headers = %s', headers)
            Log.d('Response Data = %s', data)
            client.connection.send(headers)
            client.connection.sendall(data)
            Log.i('Send data to client')

        except FileNotFoundError:
            reply = "HTTP/1.1 404 Not Found\r\n"
            client.connection.send(reply.encode('ascii'))
        client.stop()
