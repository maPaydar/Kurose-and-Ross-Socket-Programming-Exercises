import sys
import sheard.UdpServer as UdpServer

if __name__ == "__main__":
    server = UdpServer('localhost', 10000)
    server.start(server.send)
    sys.exit(0)