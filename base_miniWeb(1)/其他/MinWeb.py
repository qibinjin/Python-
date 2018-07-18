import socket
import re
"""
#GET / HTTP/1.1\r\n


response_line = 'HTTP 1.1 200 OK\r\n'
# response_body = 'Content-Type:text/html,application/xhtml+xml,application/xml;\r\n'
Connection = 'keep-alive\r\n'
Content_Type = 'text/html,application/xhtml+xml,application/xml;charset=UTF-8\r\n\r\n'
response_header = response_line + Connection + Content_Type
decode_response = response_header.encode('utf-8')
#--------------------------------------------------------------------------------------------------
Host = 'Host: localhost:8989\r\n'
User_Agent = 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0\r\n'
Accept = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
Accept_Language = 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\n'
Accept_Encoding= 'Accept-Encoding: gzip, deflate\r\n'
Cookie = 'Cookie: Pycharm-c9b2eeaf=872042e8-45df-4272-87e2-823d742e87e7\r\n'
Connection = 'Connection: keep-alive\r\n'
Upgrade_Insecure_Requests = 'Upgrade-Insecure-Requests: 1\r\n\r\n'


HOST=''
POST=8989
BUFF = 1024
ADDR=(HOST,POST)
Client_request_line = []
Client_request_header={}

Server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
Server_socket.bind(ADDR)
Server_socket.listen(128)

Client_socket,address = Server_socket.accept()
Client_date = Client_socket.recv(BUFF)
#-----------------处理响应头------------------------------------------------
#游览器请求报文处理
header_content = re.split('\\r\\n',Client_date.decode('utf-8'))
Client_request_line = header_content[0]
#获得GET请求资源路径
match_obj = re.search('/\S*',Client_request_line)
src = match_obj.group()
#对请求进行处理
for request_headers in header_content[1:-2]:
    dict_key = re.split(':',request_headers,1)
    Client_request_header.setdefault(dict_key[0],dict_key[1])

#------------------响应体---------------------------------------------------------------
result = b''
if src == '/' or src == '/index':
    print(src)
    # response_result = 'src/index.py'
    response_result = 'src/index.html'
else:
    response_result = 'src' + src
try:
    with open(response_result,'rb') as read_result:
        result += read_result.read()
except Exception as e:
    print('没有找到资源...')
    with open('src/error.html','rb') as error_result:
        result += error_result.read()
send_content = decode_response + result
Client_socket.send(send_content)

Client_socket.close()

"""

#处理请求报文
def Handle_header(self,client_date):
        # Client_request_header = {}
        # 游览器请求报文处理
        header_content = re.split('\\r\\n', client_date.decode('utf-8'))
        Client_request_line = header_content[0]
        print(Client_request_line)
        # 获得GET请求资源路径
        match_obj = re.search('/\S*', Client_request_line)
        src = match_obj.group()
        print(src)
        # 对请求进行处理
        # for request_headers in header_content[1:-2]:
        #     dict_key = re.split(':', request_headers, 1)
        #     Client_request_header.setdefault(dict_key[0], dict_key[1])

def response_date(self,src):
    if (src == r'/') or (src == r'/index') or (src == r'/index.html'):
        response_index = r'src/index.html'
        return response_index
    else:
        response_src = 'src' + src
        return response_src

@staticmethod
def read_result(response_reslut, client_socket):
        try:
            response_line = 'HTTP 1.1 200 OK\r\n'
            Connection = 'keep-alive\r\n'
            Server = 'Server:PWS1.0\r\n'
            Content_Type = 'text/html,application/xhtml+xml,application/xml,image/webp,image/apng;charset=UTF-8\r\n\r\n'
            content = b''
            with open(response_reslut, 'rb') as read_result:
                content += read_result.read(1024)
            OK = (response_line + Connection + Server + Content_Type).encode('utf-8') + content
            client_socket.send(OK)
        except Exception as e:
            print('没有找到资源...')
            error_response_line = 'HTTP 1.1 404 NOT FOUND \r\n'
            Connection = 'keep-alive\r\n'
            Server = 'Server:PWS1.0\r\n'
            Content_Type = 'text/html,application/xhtml+xml,application/xml,image/webp,image/apng;charset=UTF-8\r\n\r\n'
            result = b''
            with open('src/error.html', 'rb') as error_result:
                result += error_result.read(1024)
                ERROR = (error_response_line + Connection + Server + Content_Type).encode('utf-8') + result
            client_socket.send(OK)
        """
        # ------------------响应体-------------------------------------

        result = b''
        send_content =b''

            response_line = 'HTTP 1.1 200 OK\r\n'
            Connection = 'keep-alive\r\n'
            Content_Type = 'charset=UTF-8\r\n\r\n'
            response_header = response_line + Connection + Content_Type
            client_request = response_header.encode('utf-8')
            send_content = client_request + result
        except Exception as e:
            print('没有找到资源...')
            print(response_result)
            with open('src/error.html', 'rb') as error_result:
                result = error_result.read()

            error_response_line = 'HTTP 1.1 404 NOT FOUND \r\n'
            Connection = 'keep-alive\r\n'
            Content_Type = 'charset=UTF-8\r\n\r\n'
            response_header = error_response_line + Connection + Content_Type
            client_request = response_header.encode('utf-8')
            send_content = client_request + result
        client_socket.send(send_content)
    """


#将服务器封装成对象一个类
from socket import AF_INET,SOL_SOCKET,SO_REUSEADDR,SOCK_STREAM,socket
class MiniWeb(object):
    __Client_request_line = []

    def __init__(self,port,host='',fmaily=AF_INET,type=SOCK_STREAM):
        self.port = port
        self.host = host
        self.fmaily = fmaily
        self.type = type
        self.sock = socket(self.fmaily, self.type)
        self.sock.bind((self.host,self.port))
        self.sock.listen(128)

    #开始服务
    def start(self):
        while True:
            Client_socket, address = self.sock.accept()
            Client_date = Client_socket.recv(4096)

            # header_content = re.split('\\r\\n', Client_date.decode('utf-8'))
            # print(header_content)
            # Client_request_line = header_content[0]
            # print(Client_request_line)
            # 获得GET请求资源路径
            # match_obj = re.search('/\S*', Client_request_line)
            match_obj = re.search('/\S*', Client_date.decode('utf-8'))
            src = match_obj.group()


            result = b''
            if (src == r'/') or (src == r'/index') or (src == r'/index.html'):
                response_index = r'src/index.html'
                response_line = 'HTTP 1.1 200 OK\r\n'
                Connection = 'Keep-Alive\r\n'
                Server = 'Server:PWS1.0\r\n'
                Content_Type = 'text/html,application/xhtml+xml,application/xml,image/webp,image/apng;charset=UTF-8\r\n\r\n'
                try:
                    with open(response_index, 'rb') as read_result:
                        for line in read_result:
                            result += line
                    response = (response_line + Connection + Server + Content_Type).encode('utf-8') + result
                    Client_socket.send(response)
                except FileNotFoundError as e:
                    response_line = 'HTTP 1.1 404 NOT FOUND \r\n'
                    Connection = 'Keep-Alive\r\n'
                    Server = 'Server:PWS1.0\r\n'
                    Content_Type = 'text/html,application/xhtml+xml,application/xml,image/webp,image/apng;charset=UTF-8\r\n\r\n'

                    with open('src/error.html', 'rb') as error_result:
                        print('没有找到资源...')
                        for error_line in error_result:
                            result += error_result
                response = (response_line + Connection + Server + Content_Type).encode('utf-8') + result
                Client_socket.send(response)
            else:
                response_src = 'src' + src
                response_line = 'HTTP 1.1 200 OK\r\n'
                Connection = 'Keep-Alive\r\n'
                Server = 'Server:PWS1.0\r\n'
                Content_Type = 'text/html,application/xhtml+xml,application/xml,image/webp,image/apng;charset=UTF-8\r\n\r\n'
                try:
                    with open(response_src, 'rb') as read_result:
                        for line in read_result:
                            result += line
                except FileNotFoundError as e:
                    response_line = 'HTTP 1.1 404 NOT FOUND \r\n'
                    Connection = 'Keep-Alive\r\n'
                    Server = 'Server:PWS1.0\r\n'
                    Content_Type = 'text/html,application/xhtml+xml,application/xml,image/webp,image/apng;charset=UTF-8\r\n\r\n'

                    with open('src/error.html', 'rb') as error_result:
                        print('没有找到资源...')
                        for error_line in error_result:
                            result += error_line
                response = (response_line + Connection + Server + Content_Type).encode('utf-8') + result
                Client_socket.send(response)




import socket
import re
if __name__ == '__main__':
    HOST = 'www.baidu.com'
    POST = 80
    BUFF = 1024
    ADDR = (HOST, POST)
    response_line = 'POST /index.html HTTP /1.1\r\n'
    Host='Host:www.baidu.com\r\n'
    Connection = 'Keep-Alive\r\n'
    Content_Type = 'text/html,application/xhtml+xml,application/xml,image/webp,image/apng;charset=UTF-8\r\n'
    Cookie = 'BAIDUID=56049A8671A76131874396CBCD1030A8:FG=1; BIDUPSID=56049A8671A76131874396CBCD1030A8; PSTM=1524616797; ispeed_lsm=18; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=0; H_PS_PSSID=1421_26459_21095_18560_22074; BD_CK_SAM=1; PSINO=1; H_PS_645EC=7f62n33rbfM9%2BuITJ3OhaA%2B7AT1W1TEqwOyWXz1l2huQRJGVMl1j3TfF%2F2A'
    User_Agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36\r\n\r\n'

    request_content = (response_line + Host + Connection + Content_Type + Cookie + User_Agent).encode('utf-8')
    #创建TCP服务器Socket
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #释放端口占用
    # client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #请求服务器
    client_socket.connect(ADDR)
    client_socket.send(request_content)

    result = b''
    while True:
        recv_date = client_socket.recv(BUFF)
        if recv_date:
            result += recv_date
        else:
            break
    print(result.decode('utf-8'))


    #关闭套接字
    client_socket.close()






