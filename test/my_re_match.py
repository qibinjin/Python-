import re

url = 'qwewqwdaq@163.com'

data = re.match(r'[A-Za-z]{1}\w{7,11}@(163|126)\.(net|com)', url)
re.match('t?', 't')
re.match('t*', 'ttttt')
re.match('t+', 'tttt')
re.match('t{2,10}', 'ttttt')

re.match('^[0-9].*[A-Z]$', '1asdqweA')
re.match('^[a-z].*\D$', 'qwer12343tre_')
re.match('^\W.*[a-z]$', '*rewerwre()#re1')
print(data.group())
# data = re.match('\d{11}$', '123456789123123')

desc = '<html><h1>www.itcast.com</h1></html>'
data = re.match('<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', desc)
print(data.group())


def func(my_obj):
    ret = int(my_obj.group()) * 2
    return str(ret)


data = re.sub('\d+', func, 'asddas10,qweqwe20,qwe 30')
print(data)
words = '''<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>'''
result = re.sub('</?\w*>|&nbsp;|\s','',words)
print(result)