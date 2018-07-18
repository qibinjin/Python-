import socket
import time
HOST = ''
PORT = 5555
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcp_ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_ser.bind(ADDR)


flag = False
while True:
    tcp_ser.listen(128)
    print('等待连接中')

    client_sock, client_addr = tcp_ser.accept()
    print('已连接,连接来自 %s:%s' % client_addr)
    if flag:
        client_sock.sendto(data, client_addr)
    else:
        client_sock.sendto('欢迎进入聊天室'.encode('utf-8'), client_addr)
    data = client_sock.recv(BUFSIZE)

    if data.decode('utf-8') == 'q\r\n':
        break
    print(data.decode('utf-8'))
    client_sock.close()
    flag = True