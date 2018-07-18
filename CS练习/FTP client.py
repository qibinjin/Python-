import os, socket, ftplib
#导入必备模块

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'
#地址信息,路径,文件名


def main():
    try:
        f = ftplib.FTP(HOST)# 尝试连接地址
    except (socket.error, socket.gaierror) as e:
        print('ERROR:cannot reach "%s"' % HOST)
        return

    print('connected to host "%s"' % HOST)

    try:
        f.login() #尝试作为anonymous登陆
    except ftplib.error_perm:
        print('ERROR: cannot login anoymously')
        f.quit()
        return
    print('Logged in as "anonymous"')

    try:
        f.cwd(DIRN) #改变路径 CD >>'pub/mozilla.org/webtools'
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('Changed to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE,
                     open(FILE, 'wb').write()) #尝试下载文件到本地
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('Downloaded "%s" to CWD' % FILE)

        f.quit()


if __name__ == '__main__':
    main()
my_dict = dict()
my_dict[1.0] = 1
my_dict[1] = 2
for k in my_dict:
    print(type(k))
    print(k)



