from socket import *
import threading

HOST = '192.168.164.58'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)
def main():
    while True:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        with open('D:/Code/Python-/fly_fight/res/img-plane_7.jpg', 'rb') as f:
            data = f.read()
            file_data =('img-plane_%s.jpg' % threading.currentThread().name, data)
            tcpCliSock.send(repr(file_data).encode('utf-8'))
        tcpCliSock.close()
        break

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=main,name=i)
        threads.append(t)

    for i in range(5):
        threads[i].start()
