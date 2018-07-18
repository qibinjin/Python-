
from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('',2425))
while True:
    data = '1:100:admin:HOST:32:nijoih'
    udp_socket.sendto(data.encode('utf-8'), ('192.168.164.108', 2425))
# data, ip_part = udp_socket.recvfrom(1024)
# data, ip_part = udp_socket.recvfrom(1024)
print(data.decode('utf-8'))