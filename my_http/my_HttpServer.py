import gevent, socket, re
from gevent import monkey

monkey.patch_all()


class HttpServer(object):
    def __init__(self, port, app):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        tcp_server_socket.bind(('', port))
        tcp_server_socket.listen()

        self.tcp_server_socket = tcp_server_socket

        self.app = app

    def start_server(self):
        while True:
            client_socket, ip_part = self.tcp_server_socket.accept()

            gevent.spawn(self.client_handler, client_socket)

    def client_handler(self, client_socket):
        recv_data = client_socket.recv(4096).decode('utf-8').split('\r\n', 1)[0]
        request_path = ''
        print(recv_data)
        if recv_data:
            request_path = re.search(r'/\S*', recv_data).group()
            print(request_path)
        if request_path == '/':
            request_path = '/index.html'

        if request_path.endswith('.html'):
            env = {
                'PATH_INFO': request_path
            }

            response_body = self.app(env, self.start_response)
            client_socket.send((self.response_header + '\r\n' + response_body).encode('utf-8'))

        else:
            try:
                with open('static' + request_path, 'rb') as file:
                    html_data = file.read()

            except Exception:
                response_line = 'HTTP/1.1 404 Not Found\r\n'
                response_head = 'Server: PWS1.0\r\nContent-Type: text/html; charset=utf8\r\n'
                response_body = '<b1>您请求的页面不存在</b1>'

                client_socket.send((response_line + response_head + '\r\n' + response_body).encode('utf-8'))
            else:
                response_line = 'HTTP/1.1 200 OK\r\n'
                response_head = 'Server: PWS1.0\r\n'
                client_socket.send((response_line + response_head + '\r\n').encode('utf-8') + html_data)
            finally:
                client_socket.close()

    def start_response(self, response_line, response_head):

        self.response_header = response_line
        for v in response_head:
            self.response_header += '%s: %s\r\n' % v


if __name__ == '__main__':
    import Application
    a = HttpServer(8080, Application.app)
    a.start_server()
