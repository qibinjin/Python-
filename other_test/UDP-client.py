from socket import *
HOST = '192.168.164.27'
PORT = 2425
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
# udpCliSock.bind(("",2425))
# while True:
data = '1:100:rrr:www:32:asdasdsad'
# if not data:
    # break
udpCliSock.sendto(data.encode('utf-8'),ADDR)
# data, ADDR = udpCliSock.recvfrom(BUFSIZ)
udpCliSock.close()