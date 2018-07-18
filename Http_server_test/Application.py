def index():
    with open('templates/test9.html', 'r', encoding='utf-8') as f:
        html_data = f.read()
    return html_data


def login():
    with open('templates/test8.html', 'r', encoding='utf-8') as f:
        html_data = f.read()
    return html_data


def logged(username, passwd):
    with open('data.txt', 'r') as f:
        for i in f.readlines():
            if i[:-1] == ('username=%s, passwd=%s' % (username, passwd)):
                break
        else:
            return '<script>setTimeout("window.history.back(-1)",3000);</script><h1>登录失败...3秒之后调到登录界面</h1>'
        return "<script>setTimeout(\"window.location.href='http://localhost:8080/'\",3000);</script><h1>登录成功...3秒之后调到主页</h1>"


def regist(username, passwd):
    with open('data.txt', 'a') as f:
        f.write('username=%s, passwd=%s\n' % (username, passwd))
    return '<h1>注册成功</h1>'


url_list = [
    ('/index.html', index),
    ('/test8.html', login),
    ('/login.html', logged),
    ('/regist.html', regist)
]


def app(env, start_response):
    for path, func in url_list:
        if env['METHOD'] == 'GET':
            if env['PATH_INFO'] == path:
                start_response('HTTP/1.1 200 OK\r\n',[('Server', 'PWS1.1'), ('Content-Type', 'text/html;charset=UTF-8')])
                return func()

        elif env['METHOD'] == 'POST':
            if env['PATH_INFO'] == path:
                data = env['FORM_DATA'].split('&')
                username = data[0].split('=')[1]
                passwd = data[1].split('=')[1]
                start_response('HTTP/1.1 200 OK\r\n',[('Server', 'PWS1.1'), ('Content-Type', 'text/html;charset=UTF-8')])
                return func(username, passwd)
    else:
        start_response('HTTP/1.1 404 Not Found\r\n',[('Server', 'PWS1.1'), ('Content-Type', 'text/html;charset=UTF-8')])
        return '<h1>您访问的网页不存在</h1>'

