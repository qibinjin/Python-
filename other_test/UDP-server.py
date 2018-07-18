from  socket import *
from time import ctime

HOST = '192.168.164.58'
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)


while True:
    print('waiting for message...')
    data = ''
    udpSerSock.sendto(data.encode('utf-8'), ADDR)
    print('...received from and returned to :', ADDR)
udpSerSock.close()