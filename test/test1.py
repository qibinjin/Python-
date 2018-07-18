from socket import *
import threading

import time
MAX = 5
tcp_serv_socket = socket(AF_INET, SOCK_STREAM)
tcp_serv_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

tcp_serv_socket.bind(('', 8080))
tcp_serv_socket.listen(MAX)

def main():
    while True:
        client_socket, ip_part = tcp_serv_socket.accept()

        data = client_socket.recv(1024).decode('utf-8')
        print(data)

        client_socket.send('88'.encode('utf-8'))

        client_socket.close()


# def main1():
#     client_socket, ip_part = tcp_serv_socket.accept()
#
#     data = client_socket.recv(1024).decode('utf-8')
#     print(data)
#
#     client_socket.send('88'.encode('utf-8'))
#
#     client_socket.close()
threads = []

for i in range(MAX):
    t = threading.Thread(target=main, args=())
    threads.append(t)
for i in range(MAX):
    threads[i].start()
    print(threading.active_count())

# for i in range(MAX):
#     threads[i].join()
