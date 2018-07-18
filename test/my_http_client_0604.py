import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen(128)

    while True:
        tcp_client, ip = tcp_server_socket.accept()
        print(tcp_client.recv(1024))
        response_line = 'HTTP/1.1 200 ok\r\n'
        response_head = 'Server: PWB/1.1\r\nContent-Type: text/html;charset=utf-8\r\n'
        response_body = 'Hello World!!!'
        response_content = response_line + response_head + '\r\n' + response_body
        tcp_client.send(response_content.encode('utf-8'))
        tcp_client.close()