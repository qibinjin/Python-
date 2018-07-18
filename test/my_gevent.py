import gevent
from gevent import monkey
import urllib.request

monkey.patch_all()


def download(img_url, img_name):
    with open(img_name, 'wb') as f:
        while True:
            g = urllib.request.urlopen(img_url)
            data = g.read(1024)
            if data:
                f.write(data)
            else:
                print('download ok....')
                break


if __name__ == '__main__':
    url1 = '192.168.164.77/BoeOt/my.jpg'
    url2 = '192.168.164.77/BoeOt/my.jpg'
    url3 = '192.168.164.77/BoeOt/my.jpg'
    gevent.joinall([gevent.spawn(download, url1, '1.jpg'),
                    gevent.spawn(download, url2, '2.jpg'),
                    gevent.spawn(download, url3, '3.jpg')])
