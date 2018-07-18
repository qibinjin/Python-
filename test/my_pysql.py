import pymysql
import re

conn = pymysql.connect(host='localhost', port=3306, user='root',
                       password='mysql', db='jing_dong', charset='utf8')
cursor = conn.cursor()

cursor.execute('CREATE TABLE  if not exists person(\
                id int unsigned PRIMARY KEY auto_increment,\
                name VARCHAR(64), \
                mail VARCHAR (64),\
                qq VARCHAR (64),\
                phone VARCHAR(64),\
                birth VARCHAR (64));')

with open('/home/python/Desktop/sample.txt', 'r') as f:
    while True:
        data = f.readline()
        if data:
            data = data[:-1]
            # data = re.sub(r'\\', r'\\\\', data)
            ret = data.split('\t')
            # print(ret)

            sql = "insert into person values(0,%s,%s,%s,%s,%s);"
            # print(sql)
            cursor.execute(sql, ret)
        else:
            break
# print(cursor.fetchall())
conn.commit()
cursor.close()
conn.close()
