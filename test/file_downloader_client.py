from socket import *


file_name = 'hm.txt'
tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(('192.168.164.58', 8080))
tcp_client.send(file_name.encode('utf-8'))

with open(file_name, 'wb') as f:
    while True:
        recv_data = tcp_client.recv(1024)
        if recv_data:
            f.write(recv_data)
        else:
            print('download ok')
            break

tcp_client.close()