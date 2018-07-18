import socket
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(('ntlias-stu.boxuegu.com', 80))

data = '''GET / HTTP/1.1
Host: ntlias-stu.boxuegu.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

'''
recv_content = b''
tcp_client.send(data.encode('utf- 8'))
while True:
    recv_data = tcp_client.recv(1024)
    if recv_data:
        recv_content += recv_data
    else:
        break

print(recv_content.decode('utf-8').split('\r\n\r\n',1)[1])

