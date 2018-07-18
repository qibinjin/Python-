from socket import *
import threading

class MyThread(threading.Thread):
    def __init__(self, myfunc, name = 'None'):
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

        send_data = 'hello world'.encode('utf-8')

        client_sock.send(send_data)

        recvdata = client_sock.recv(1024).decode('utf-8')

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


