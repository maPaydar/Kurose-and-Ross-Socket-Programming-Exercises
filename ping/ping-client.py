import time
import sheard.Client as Client

if __name__ == '__main__':
    client = Client()
    for i in range(1, 10):
        client.sendto(''.encode(), 'localhost', 10000)
        start = time.time()
        client.receive()
        end = time.time()
        print("RTT= {:.10f}ms".format((end - start) * 1000))