import time
import re
from pymysql import connect
from urllib.parse import unquote


def my_sql(sql, parameter=None):
    conn = connect(host='localhost', port=3306, user='root', password='mysql', db='stock_db', charset='utf8')
    cur = conn.cursor()
    try:
        cur.execute(sql, parameter)
        all_data = cur.fetchall()
        conn.commit()
    except Exception as e:
        conn.rollback()
        return 'Error' + str(e)
    else:
        return all_data
    finally:
        cur.close()
        conn.close()


def get_time(path_info):
    """在用户请求 /gettime.py的时候 应该执行当前函数"""
    return time.ctime()


def index(path_info):
    """在用户请求 /index.py的时候 执行当前函数"""
    # 读取模板文件
    with open("template/index.html", "r") as file:
        html_data = file.read()

    # TODO: 从数据库中查询出 股票数据  添加到模板网页中
    data_from_mysql = ""
    all_data = my_sql('select * from info')
    for line in all_data:
        line_str = '''<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td> <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s"></td>
        </tr>
        ''' % (line + (line[1],))
        data_from_mysql += line_str
    # 模板替换 模板变量{%content%} ---> 用户所需要的动态资源

    return re.sub(r"\{%content%\}", data_from_mysql, html_data)
    # return "response from index"


def center(path_info):
    with open('template/center.html', 'r') as file:
        data_html = file.read()

    data_from_mysql = ''
    sql = 'select info.code,info.short,info.chg,info.turnover,info.price,info.highs,focus.note_info \
        from info join focus on info.id = focus.info_id;'
    all_data = my_sql(sql)
    if all_data is str:
        return '数据库读取错误'

    for line in all_data:
        line_str = """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
            <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s"></td>
            </tr>""" % (line + (line[0],) + (line[0],))
        data_from_mysql += line_str

    return re.sub(r'\{%content%\}', data_from_mysql, data_html)


def add(path_info):
    sql = 'select * from focus where info_id=(select id from info where code=%s)'
    if my_sql(sql, path_info.group(1)):
        return '已经添加过了'
    sql = 'insert into focus(info_id) select id from info where code=%s'
    if my_sql(sql, path_info.group(1)) is str:
        return '删除失败'
    return '添加成功'


def delete(path_info):
    sql = 'delete from focus where info_id=(select id from info where code=%s)'
    if my_sql(sql, path_info.group(1)) is str:
        return '删除失败'
    return '删除成功'


def update(path_info):
    with open('template/update.html', 'r') as file:
        html_data = file.read()
    sql = 'select note_info from focus where info_id = (select id from info where code =%s);'
    html_data = re.sub(r'\{%code%\}', path_info.group(1), html_data)
    # my_sql 得到的返回是 (('利好',),) 因此需要[0][0] 取到字符串
    html_data = re.sub(r'\{%note_info%\}', my_sql(sql, path_info.group(1))[0][0], html_data)
    return html_data


def update_note_info(path_info):
    sql = 'update focus join info on focus.info_id=info.id set focus.note_info = %s  where info.code=%s;'
    if my_sql(sql, (unquote(path_info.group(2)), path_info.group(1))) is str:
        return '更新失败'
    return '更新成功'


# 路由列表 提前把所有路径和对应的函数代码  放到集合中 django框架添加路由的方式
route_list = [
    ('^/gettime.html$', get_time),
    ('^/index.html$', index),
    ('^/center.html$', center),
    ('^/add/(\d{6}).html', add),
    ('^/del/(\d{6}).html', delete),
    ('^/update/(\d{6}).html', update),
    ('^/update/(\d{6})/(.*).html', update_note_info)
]


def app(environ, start_response):
    """# 这是一个web框架/web应用程序  是被web服务器调用的"""
    # app是 框架提供给web服务器调用 作用: 处理动态资源请求
    # 参数1 包含了用户请求信息的 字典 快速查询
    # 掌握------- 用户请求的路径信息'PATH_INFO': '/index.html',

    # 处理动态资源请求
    # 获取用户信息   -----> 查询数据 --- 替换模板
    path_info = environ['PATH_INFO']
    # print("接收到用户的动态资源请求 %s" % path_info)

    # 遍历路由列表中的每一项  然后将用户请求路径和 每一项的路径进行比较
    # 如果有匹配的 就执行对应的函数
    for url, func in route_list:
        ret = re.match(url, path_info)
        if ret:
            start_response('200 OK', [('Content-Type', 'text/html')])
            return func(ret)
    else:
        # 参数2 是一个函数的引用  函数的作用: 通过调用该函数 将相应状态和头 传给服务器
        start_response('404 Not Found', [('Content-Type', 'text/html;charset=utf-8')])

        # app函数返回值就是响应体
        return '<h1>非常抱歉<br>您当前访问的网页已经不存在了</h1>'
