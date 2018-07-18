from socket import *

udp_ser = socket(AF_INET, SOCK_DGRAM)

udp_ser.bind(('', 8080))

data = 'nihaoa'.encode('gbk')

udp_ser.sendto(data,('10.254.7.116', 5555))

udp_ser.recvfrom(1024,('10.254.7.116', 5555))

udp_ser.close()
