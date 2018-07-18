from socket import *
import threading
import os

class MyThread(threading.Thread):
    def __init__(self, myfunc, name='None'):
        threading.Thread.__init__(self)
        self.myfunc = myfunc
        # self.args = myarg
        self.name = name

    def run(self):
        self.myfunc()


tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

tcp_socket.bind(('', 8080))

tcp_socket.listen(5)


def main():
    while True:
        client_sock, ip_part = tcp_socket.accept()

        recvdata = client_sock.recv(1024).decode('utf-8')

        response_line = 'HTTP/1.1 200\r\n'
        response_head = 'Server: nginx/1.8.1\r\nDate: Sun, 03 Jun 2018 06:32:01 GMT\r\nConnection: keep-alive\r\n\r\n'
        response_data = b''
        with open('./index.html', 'rb') as f:
            while True:
                data = f.read()
                if data:
                    response_data += data
                else:
                    break
        send_data = (response_line + response_head).encode('utf-8') + response_data

        client_sock.send(send_data)

        print(recvdata)

        client_sock.close()


if __name__ == '__main__':

    # threads = []
    #
    # for i in range(5):
    #
    #     t = threading.Thread(target=main, args=())
    #     threads.append(t)
    #
    # for i in range(5):
    #     threads[i].start()
    # print(threading.active_count())
    # for i in range(5):
    #     threads[i].join()

    threads = []

    for i in range(5):
        t = MyThread(main)
        threads.append(t)

    for i in range(5):
        threads[i].start()
