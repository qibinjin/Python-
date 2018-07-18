
def print_name():
    with open('templates/print_name.html', 'r') as f:
        html_data = f.read()

    return html_data

url_list = {
    (r'/index.html', print_name)
}
def app(env, start_response):

    for k,func in url_list:
        if env['PATH_INFO'] == k:
            start_response('HTTP/1.1 200 OK\r\n', [('Server', 'PWS1.0')])

            return func()
        else:
            start_response('HTTP/1.1 404 Not Found\r\n', [('Server', 'PWS1.0'), ('Content-Type', 'text/html; charset=utf8')])

            return '<b1>您请求的页面不存在</b1>'