from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
tcp_socket.bind(('', 8080))
tcp_socket.listen(5)
client_socket, ip_part = tcp_socket.accept()
file_name = client_socket.recv(1024).decode('utf-8')

with open(file_name, 'rb') as f:
    while True:
        data = f.read(1024)
        if data:
            client_socket.send(data)
        else:
            print('file download OK')
            break


# tcp_socket.close()
