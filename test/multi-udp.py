import threading
from socket import *
MY_ADDR = ('', 5555)
DES_ADDR = ('192.168.164.32', 5555)
MAX = 5


class MyThread(threading.Thread):
    def run(self):
        self._target(*self._args, **self._kwargs)


def send_msg(udp_socket:socket):
    while True:
        data = input('please input words').encode('utf-8')  # data = '123\n'.encode('utf-8')
        udp_socket.sendto(data, DES_ADDR)


def recv_msg(udp_socket):
    while True:
        recv_data, ip_part = udp_socket.recvfrom(1024)
        if recv_data.decode('utf-8'):
            print(recv_data.decode('utf-8'))


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', 5555))

    threads = []
    for i in range(MAX):
        t = MyThread(target=recv_msg, args=(udp_socket,))
        threads.append(t)
    for i in range(MAX):
        threads[i].start()

    send_msg(udp_socket)


if __name__ == '__main__':
    main()
