import socket
import re
import gevent
from gevent import monkey
import sys
monkey.patch_all()  #识别耗时操作
"""

def handler_client_request(client_socket):
    # 获取客户端请求报文
    recv_date = client_socket.recv(BUFF)
    print(recv_date.decode('utf-8'))
    # ------------------------------------------------------------------------
    # 通过查找获取请求路径
    match_obj = re.search('/\S*', recv_date.decode('utf-8'))
    if not match_obj:  # 如果访问路径有误
        print('访问路径有误！')
        client_socket.close()
        return
    # 获取匹配结果
    src_path = match_obj.group()
    if (src_path == '/') or (src_path == '/index'):
        src_path = '/index.html'
        # 读取文件资源
        # ---------------------------------------------------------------------------
    try:
        with open('src' + src_path, 'rb') as read_result:
            file_date = read_result.read()
    except Exception as e:
        print('没有找到资源...')
        response_line = 'HTTP/1.1 404 NOT FOUND \r\n'
        Connection = 'Connection:Keep-Alive\r\n'
        Server = 'Server:PWS1.0\r\n'
        Content_Type = 'Content_Type:text/html,application/xhtml+xml,application/xml;charset=UTF-8\r\n\r\n'
        with open('src/error.html', 'rb') as error_result:
            error_date = error_result.read()
        Error = (response_line + Connection + Server + Content_Type).encode('utf-8') + error_date
        client_socket.send(Error)
    else:
        response_line = 'HTTP/1.1 200 OK\r\n'
        Connection = 'Connection:Keep-Alive\r\n'
        Server = 'Server:PWS1.0\r\n'
        Content_Type = 'Content_Type:text/html,application/xhtml+xml,application/xml;charset=UTF-8\r\n\r\n'
        response = (response_line + Connection + Server + Content_Type).encode('utf-8') + file_date
        client_socket.send(response)
    finally:
        client_socket.close()

def main():
    # 创建TCP服务器Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 释放端口占用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口号和主机IP
    server_socket.bind(ADDR)
    # 设置监听连接数
    server_socket.listen(128)
    while True:
        # 等待客户端的连接
        client_socket, address = server_socket.accept()
        # handler_client_request(client_socket)
        gevent.spawn(handler_client_request,client_socket)
"""
BUFF = 4096
#封装HTTP请求
class MinHttpWebServer(object):
    def __init__(self,port,host=''):
        # 创建TCP服务器Socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 释放端口占用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定端口号和主机IP
        server_socket.bind((host,port))
        # 设置监听连接数
        server_socket.listen(128)
        #设置对象属性
        self.server_socket = server_socket

    def run(self):
        while True:
            # 等待客户端的连接
            client_socket, address = self.server_socket.accept()
            # handler_client_request(client_socket)
            gevent.spawn(self.prosess_handler, client_socket)

    def prosess_handler(self,client_socket):
        # 获取客户端请求报文
        recv_date = client_socket.recv(BUFF)
        print(recv_date.decode('utf-8'))

        # 通过查找获取请求路径
        match_obj = re.search('/\S*', recv_date.decode('utf-8'))

        # 判断访问路径是否有误
        if not match_obj:
            print('访问路径有误！')
            client_socket.close()
            return

        # 获取匹配结果
        src_path = match_obj.group()
        if src_path == '/': src_path = '/index.html'

        if src_path.endswith('.html'):
        # src_path.endswith('.html')

            #当收到已.html结尾的请求,调用Application矿建来处理客户请求
            import Application
            request_path = {
                'PATH_INFO': src_path
            }
            print('服务器>', src_path)
            #接框架处理完后返回的数据
            response_body = Application.app(src_path,self.start_response)
            response_date = self.response_line + self.response_header + '\r\n' + response_body
            client_socket.send(response_date.encode('utf-8'))
            client_socket.close()
        else:
            try:
                with open('static' + src_path, 'rb') as read_result:
                    file_data = read_result.read()
            except Exception as e:
                print('没有找到资源...')
                response_line = 'HTTP/1.1 404 NOT FOUND \r\n'
                Connection = 'Connection:Keep-Alive\r\n'
                Server = 'Server:PWS1.0\r\n'

                with open('templates/error.html', 'rb') as error_result:
                    error_data = error_result.read()
                Error = (response_line + Connection + Server + '\r\n').encode('utf-8') + error_data
                client_socket.send(Error)
            else:
                response_line = 'HTTP/1.1 200 OK\r\n'
                Connection = 'Connection:Keep-Alive\r\n'
                Server = 'Server:PWS1.0\r\n'
                response = (response_line + Connection + Server + '\r\n').encode('utf-8') + file_data
                client_socket.send(response)
            finally:
                client_socket.close()


        # else:
        #     if (src_path == '/') or (src_path == '/index'):
        #         src_path = '/index.html'
        #     self.prosess_file(src_path, client_socket)

    def start_response(self,status,response_date):
        """接收   来自框架 相应状态码 和响应头 并且拼接保存"""
        self.response_line = 'HTTP/1.1 %s\r\n' % status
        for hander in response_date:
            self.response_header = '%s:%s\r\n' % hander


"""
    def prosess_file(self,src_path,client_socket):
        try:
            with open('templates' + src_path, 'rb') as read_result:
                file_date = read_result.read(4096)
        except Exception as e:
            print('没有找到资源...')
            response_line = 'HTTP/1.1 404 NOT FOUND \r\n'
            Connection = 'Connection:Keep-Alive\r\n'
            Server = 'Server:PWS1.0\r\n'
            Content_Type = 'Content_Type:text/html,application/xhtml+xml,application/xml;charset=UTF-8\r\n\r\n'
            with open('templates/error.html', 'rb') as error_result:
                error_date = error_result.read()
            Error = (response_line + Connection + Server + Content_Type).encode('utf-8') + error_date
            client_socket.send(Error)
        else:
            response_line = 'HTTP/1.1 200 OK\r\n'
            Connection = 'Connection:Keep-Alive\r\n'
            Server = 'Server:PWS1.0\r\n'
            Content_Type = 'Content_Type:text/html,application/xhtml+xml,application/xml;charset=UTF-8\r\n\r\n'
            response = (response_line + Connection + Server + Content_Type).encode('utf-8') + file_date
            client_socket.send(response)
        finally:
            client_socket.close()
"""

def main():
    if not len(sys.argv) == 2:
        print("参数错误格式为：<python3 xxx.py 0000>")
        return
    if not sys.argv[1].isdigit():
        print("参数错误格式为：<python3 xxx.py 0000>")
        return
    print(sys.argv)
    port = int(sys.argv[1])
    mhws = MinHttpWebServer(port)
    mhws.run()

if __name__ == '__main__':
    main()





