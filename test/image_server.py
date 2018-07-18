from socket import *
import threading


class MyThread(threading.Thread):
    def __init__(self, my_func, name='None'):
        threading.Thread.__init__(self)
        self.my_func = my_func
        # self.args = my_arg
        self.name = name

    def run(self):
        self.my_func()

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
tcp_socket.bind(('', 8080))
tcp_socket.listen(5)


def main():
    while True:
        client_sock, ip_part = tcp_socket.accept()
        # file_name = client_sock.recv(1024).decode('utf-8')
        file_name, recvdata = eval(client_sock.recv(102400).decode('utf-8'))
        with open(file_name, 'wb') as f:
            f.write(recvdata)
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
        t = MyThread(main, name='%d' % i)
        threads.append(t)

    for i in range(5):
        threads[i].start()
