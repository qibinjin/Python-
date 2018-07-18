import threading
import socket
import re
import time


class Http_Server(object):
    def __init__(self, port):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('', port))

        tcp_server_socket.listen(10)
        self.tcp_server_socket = tcp_server_socket

    def start_server(self):
        while True:
            client_socket, ip_part = self.tcp_server_socket.accept()
            print(ip_part)
            t = threading.Thread(target=self.client_handler, args=(client_socket,))
            t.start()

    def client_handler(self, client_socket):
        recv_data = client_socket.recv(8192).decode('utf-8')

        print(recv_data)
        if recv_data:
            request_path = re.search(r'/\S*', recv_data).group()
            method = re.search(r'^\S*', recv_data).group()
            if method == 'POST':
                formdata = re.search(r'username=\S*', recv_data).group()
            else:
                formdata = None
            if request_path == '/': request_path = '/index.html'

            if request_path.endswith('.html'):
                env = {
                    'PATH_INFO': request_path,
                    'METHOD': method,
                    'FORM_DATA': formdata
                }
                import Application

                body = Application.app(env, self.start_response)
                client_socket.send((self.header + '\r\n' + body).encode('utf-8'))
            else:
                try:
                    with open('static' + request_path, 'rb') as f:
                        html_data = f.read()

                except Exception:
                    head = 'HTTP/1.1 404 Not Found\r\nServer: PWS1.1\r\nContent-Type:text/html; charset=utf8\r\n'
                    body = '您访问的页面不存在'
                    client_socket.send((head + '\r\n' + body).encode('utf-8'))
                else:
                    head = 'HTTP/1.1 200 Ok\r\nConnection: keep-alive\r\nServer: PWS1.1\r\n'
                    client_socket.send(head.encode('utf-8') + html_data)
                finally:
                    client_socket.close()

    def start_response(self, line, head):
        self.header = line
        for i in head:
            self.header += '%s: %s\r\n' % i


if __name__ == '__main__':
    http_server = Http_Server(8080)
    http_server.start_server()
