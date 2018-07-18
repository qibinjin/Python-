from gevent import monkey
import socket
import re
import gevent
import sys
import logging
monkey.patch_all()

# 让gevent能够识别耗时操作，让协程自动切换执行，失败的耗时操作由： recv, accept, time.sleep, 网络请求延时


# 封装的web服务器类
class HttpWebServer(object):
    def __init__(self, port, app):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置socket选项，立即释放端口
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        # 创建对象提供socket属性
        self.tcp_server_socket = tcp_server_socket
        self.line_headers = ''
        # 保存一个app引用到属性中
        self.app = app

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler('./log.txt', 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        fmt = logging.Formatter('%(asctime)s - %(filename)s + %(lineno)d - %(levelname)s : %(message)s')
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)

        logger.addHandler(fh)
        logger.addHandler(ch)

        self.logger = logger

    # 启动服务器
    def start(self):
        # 循环接收客户端的连接请求
        while True:
            service_client_socket, ip_port = self.tcp_server_socket.accept()
            self.logger.info('来自%s的连接' % str(ip_port))
            # handle_client_request(service_client_socket)
            # 开辟协程并执行对应的任务
            gevent.spawn(self.handle_client_request, service_client_socket)
            # t = threading.Thread(target= self.handle_client_request, args=(service_client_socket, ))
            # t.start()
            # t = multiprocessing.Process(target=self.handle_client_request, args=(service_client_socket,))
            # t.start()
            # 不需要加上join，主要原有是我们的进程不会退出
            # g1.join()

    # 处理客户端的请求
    def handle_client_request(self, service_client_socket):
        # 获取客户端的请求报文数据
        client_request_data = service_client_socket.recv(4096)

        # GET /index2.html HTTP/1.1xxxxxxx
        client_request_conent = client_request_data.decode("utf-8")
        # 通过正则查找请求的资源路径
        match_obj = re.search("/\S*", client_request_conent)

        if not match_obj:
            print("访问路径有误")
            service_client_socket.close()
            return

        # 获取匹配结果
        request_path = match_obj.group()
        self.logger.info('请求访问 %s' % request_path)

        if request_path == "/":
            # 如果用户没有指定资源路径那么默认访问的数据是首页的数据
            request_path = "/index.html"

        if request_path.endswith(".html"):
            # 当收到以.py结尾就是动态资源请求
            # import Application
            env = {
                "PATH_INFO": request_path
            }
            # 拼接响应报文  并且进行发送
            # 调用app 处理动态资源请求 返回值 就是 响应体
            response_body = self.app(env, self.start_response)
            # 按照响应头 + 相应体 拼接 发送 关闭
            response_data = self.line_headers + "\r\n" + response_body

            service_client_socket.send(response_data.encode('utf-8'))
            service_client_socket.close()

        else:
            # 读取指定文件数据
            # 使用rb的原因是浏览器也有可能请求的是图片
            try:
                with open("static" + request_path, "rb") as file:
                    # 读取文件数据
                    file_data = file.read()
            except Exception:
                # 准备响应报文数据
                # 响应行
                self.logger.error('发生错误，没有打开数据 %s' % request_path)
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 响应头
                response_header = "Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n"
                # 响应体 -> 打开一个404html数据把数据给浏览器
                response_body = "<h1>非常抱歉<br>您当前访问的网页已经不存在了</h1>".encode("utf-8")

                # 匹配响应报文数据
                response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                # 发送响应报文数据
                service_client_socket.send(response_data)
            else:
                # 准备响应报文数据
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 响应头
                response_header = "Server: PWS1.0\r\n"
                # 响应体
                response_body = file_data

                # 匹配响应报文数据
                response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                # 发送响应报文数据
                service_client_socket.send(response_data)
            finally:
                service_client_socket.close()

    def start_response(self, status, response_header_list):
        """接收 来自 框架 相应状态 和 响应头 并且拼接 保存"""
        self.line_headers = "HTTP/1.1 %s\r\n" % status
        for header in response_header_list:
            self.line_headers += "%s : %s\r\n" % header


# 主函数
def main():
    print(sys.argv)
    if len(sys.argv) != 3:
        print("启动命令如下: python3 xxx.py 9090 Application:app")
        return
    if not sys.argv[1].isdigit():
        print("启动命令如下: python3 xxx.py 9090 Application:app")
        return
    port = int(sys.argv[1])
    # print(port)

    # 获取 Application:app
    # print(sys.argv[2])
    module_name_app_name = sys.argv[2]
    data = module_name_app_name.split(":")
    if len(data) != 2:
        print("启动命令如下: python3 xxx.py 9090 Application:app")
        return
    # print("模块名 %s 函数名%s" % (data[0], data[1]))
    # 参数是模块的字符串 名称  返回值就是模块对象 的引用
    framework = __import__(data[0])

    # 获取到了模块对象 的属性 返回 属性的引用
    app = getattr(framework, data[1])

    server = HttpWebServer(port, app)
    server.start()


if __name__ == '__main__':
    main()
