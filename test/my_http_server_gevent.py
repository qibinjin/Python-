import socket
import re
import gevent
from gevent import monkey
import sys

monkey.patch_all()


class HttpServer(object):
    def __init__(self, port):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server_socket.bind(('', port))
        tcp_server_socket.listen(128)
        self.tcp_server = tcp_server_socket

    def start(self):
        while True:
            tcp_client_socket, ip_part = self.tcp_server.accept()
            gevent.spawn(self.serve_client, tcp_client_socket)

    @staticmethod
    def serve_client(tcp_client_socket):

        data = tcp_client_socket.recv(4096).decode('utf-8')
        print(data)
        if not data:
            return
        try:
            request_path = re.search('/\S*', data).group()
        except AttributeError:
            print('Please use browser to view....')
            return
        if request_path == '/':
            request_path = '/index.html'
        response_line = 'HTTP/1.1 200 OK\r\n'
        response_head = 'Server: PWS/1.1\r\nContent-Type: text/html;charset=utf-8\r\n'
        response_body = b''
        try:
            with open('/home/python/Desktop/static' + request_path, 'rb') as f:
                while True:
                    data = f.read(1024)
                    if data:
                        response_body += data
                    else:
                        break
        except FileNotFoundError:
            response_line = 'HTTP/1.1 404 NOT Found\r\n'
            response_body = '<h1>Requesting page is not exist....</h1>\r\n'
            send_data = (response_line + response_head + '\r\n' + response_body).encode('utf-8')
            tcp_client_socket.send(send_data)
        else:
            if request_path[-3:] == 'jpg':
                response_head = 'Server: PWB/1.1\r\nContent-Type: image/jpeg;charset=utf-8\r\n'
            elif request_path[-2:] == 'js':
                response_head = 'Server: PWB/1.1\r\nContent-Type: application/javascript;charset=utf-8\r\n'
            send_data = (response_line + response_head + '\r\n').encode('utf-8') + response_body

            try:
                tcp_client_socket.sendall(send_data)
            except:
                print('数据发送失败。。。')
                return
                # tcp_client_socket.close()
        finally:
            tcp_client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please check your Enter you should input like python3 xxx port')
        sys.exit()
    if not sys.argv[1].isdigit():
        print('Please check your Enter you should input like python3 xxx port')
        sys.exit()
    http_server = HttpServer(int(sys.argv[1]))
    http_server.start()
