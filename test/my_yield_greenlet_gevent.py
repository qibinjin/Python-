import time
from greenlet import greenlet
import gevent
from gevent import monkey

monkey.patch_all()

def work1():
    for i in range(10):
        print('work1')
        # gr2.switch()
        time.sleep(0.5)
        # g2.switch()

        # yield


def work2():
    for i in range(10):
        print('work2')
        # gr1.switch()
        time.sleep(0.5)
        # g1.switch()

        # yield


if __name__ == '__main__':
    # for i in range(10):
    #     next(work1())
    #     next(work2())
    # gr1 = greenlet(work1)
    # gr2 = greenlet(work2)
    # gr1.switch()
    # g1 = gevent.spawn(work1)
    # g2 = gevent.spawn(work2)
    # g1.join()
    # g2.join()
    gevent.joinall([gevent.spawn(work1),
                    gevent.spawn(work2)])
