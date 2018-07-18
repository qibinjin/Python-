import time
#存放地址和对应的函数
route_path = []
#定义路由装饰器
def route(url):
    def warpper(func):
        route_path.append((url, func))
        def inner():
            pass
        return inner
    return warpper
#执行/页面逻辑
@route('/')
def home():
    return 'home'

#执行index页面逻辑
@route('/index.html')
def index():
    with open('templates/index.html','r') as index_file:
        html_date = index_file.read()
    return html_date

#执行center页面逻辑
@route('/center.html')
def content():
    with open('templates/center.html', 'r') as index_file:
        html_date = index_file.read()
    return html_date

#执行update页面逻辑
@route('/update.html')
def update():
    return 'update'

#执行error页面逻辑

def error():
    return '<h1>没有找到资源文件error</h1>'

#框架入口
def app(request_info,start_response):
    # print('访问资源路径:->',request_info['PATH_INFO'])
    # request_url = request_info['PATH_INFO']
    # if request_info['PATH_INFO'] == '/gettime.py':
    #     start_response('HTTP / 1.1 200 OK', [('Content-Type', 'text/html;charset=UTF-8')])
    #     return gettime()
    # if request_info['PATH_INFO'] == '/index.py':
    #     result_str = index(request_info['PATH_INFO'])
    #     start_response('HTTP / 1.1 200 OK', [('Content-Type', 'text/html;charset=UTF-8')])
    #     return result_str
    #读取路由对应的action函数
    #遍历本地路由列表中的地址和函数
    for url,func in route_path:
        # print('url->',url)
        # print('request_info->',request_info)

        #判断请求资源是否在路由中
        if url == request_info:
            start_response('HTTP / 1.1 200 OK', [('Content-Type', 'text/html;harset=UTF-8')])
            return func()
    #如果没有在返回错误页面
    else:
        start_response('HTTP / 1.1 404 NOT FOUND', [('Content-Type', 'text/html;charset=UTF-8')])
        return error()
