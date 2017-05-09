class Util:
    @staticmethod
    def get_object_from_http_request(request):
        return request.split("\\r\\n")[0].split(" ")[1][1:]

    @staticmethod
    def get_file_data(filename, mode):
        f = open(filename, mode)
        data = f.read()
        f.close()
        return data

    @staticmethod
    def get_simple_http_header(status, headers):
        response = ''
        if status == 'ok':
            response += 'HTTP/1.1 200 OK\r\n'
        else:
            response += 'HTTP/1.1 404 Not Found\r\n'
        for key in headers:
            response += key + ':' + headers[key] + '\r\n'
        response += '\r\n'
        return response.encode('ascii')

    @staticmethod
    def encode_string(string, mode):
        return string.encode(mode)

    @staticmethod
    def receive_all(sock):
        data = b''
        while True:
            part = sock.recv(4096)
            data += part
            if len(part) < 4096:
                break
        return data
